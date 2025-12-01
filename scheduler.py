import threading
import time
from datetime import datetime, timedelta
from ss_api_client import SSActivewearClient
from shopify_client import ShopifyClient
from sync_manager import SyncManager
import json

class AutoSyncScheduler:
    """Scheduler for automatic product and inventory updates"""
    
    def __init__(self):
        self.enabled = False
        self.interval_hours = 12
        self.last_run = None
        self.next_run = None
        self.running = False
        self.thread = None
        self.config = None
        self.sync_options = None
        self.auto_sync_options = {}  # Store auto sync specific options
        self.require_approval = True
        self.pending_approval = False
    
    def start(self, config: dict, sync_options: dict, require_approval: bool = True):
        """Start automatic sync scheduler"""
        self.config = config
        self.sync_options = sync_options
        self.require_approval = require_approval
        self.enabled = True
        self.last_run = None
        self.next_run = datetime.now() + timedelta(hours=self.interval_hours)
        
        if self.thread is None or not self.thread.is_alive():
            self.thread = threading.Thread(target=self._scheduler_loop, daemon=True)
            self.thread.start()
    
    def stop(self):
        """Stop automatic sync scheduler"""
        self.enabled = False
        self.pending_approval = False
    
    def approve_pending_sync(self):
        """Approve pending sync"""
        if self.pending_approval:
            self.pending_approval = False
            self._run_sync()
            return True
        return False
    
    def get_status(self) -> dict:
        """Get scheduler status"""
        return {
            'enabled': self.enabled,
            'interval_hours': self.interval_hours,
            'last_run': self.last_run.isoformat() if self.last_run else None,
            'next_run': self.next_run.isoformat() if self.next_run else None,
            'running': self.running,
            'pending_approval': self.pending_approval,
            'require_approval': self.require_approval,
            'auto_sync_options': self.auto_sync_options or {}
        }
    
    def _scheduler_loop(self):
        """Main scheduler loop"""
        while self.enabled:
            try:
                now = datetime.now()
                
                # Check if it's time to run
                if self.next_run and now >= self.next_run:
                    if self.require_approval:
                        # Wait for approval
                        self.pending_approval = True
                        # Wait up to 1 hour for approval
                        approval_timeout = now + timedelta(hours=1)
                        while self.pending_approval and now < approval_timeout:
                            time.sleep(60)  # Check every minute
                            now = datetime.now()
                        
                        if self.pending_approval:
                            # Approval timeout, skip this run
                            self.pending_approval = False
                            self.next_run = datetime.now() + timedelta(hours=self.interval_hours)
                            continue
                    else:
                        # Run immediately
                        self._run_sync()
                
                # Sleep for 1 minute before checking again
                time.sleep(60)
                
            except Exception as e:
                print(f"Scheduler error: {e}")
                time.sleep(60)
    
    def _run_sync(self):
        """Run synchronization"""
        if self.running or not self.config:
            return
        
        self.running = True
        try:
            ss_client = SSActivewearClient(
                self.config.get('ss_account_number'),
                self.config.get('ss_api_key')
            )
            shopify_client = ShopifyClient(
                self.config.get('shopify_domain'),
                self.config.get('shopify_token')
            )
            
            # Use auto_sync_options if available, otherwise use sync_options with defaults
            if self.auto_sync_options:
                auto_sync_options = self.sync_options.copy()
                auto_sync_options.update(self.auto_sync_options)
            else:
                # Default: only update existing products
                auto_sync_options = self.sync_options.copy()
                auto_sync_options['create_new'] = False
                auto_sync_options['update_existing'] = True
            
            sync_manager = SyncManager(ss_client, shopify_client, auto_sync_options)
            sync_manager.start_sync()
            
            # Wait for sync to complete
            while sync_manager.status == 'running':
                time.sleep(5)
            
            self.last_run = datetime.now()
            self.next_run = datetime.now() + timedelta(hours=self.interval_hours)
            
        except Exception as e:
            print(f"Auto-sync error: {e}")
        finally:
            self.running = False

# Global scheduler instance
scheduler = AutoSyncScheduler()

