# Source: https://shopify.dev/docs/apps/launch/billing/refund-app-charges#next-steps

Skip to main content

[![Docs page](https://cdn.shopify.com/shopifycloud/shopify-
dev/production/assets/dev-docs-logo-2-light-D4UI1jxY.svg)![Docs
page](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/dev-
docs-logo-2-dark-BQ-Bk9XA.svg)](/docs)

  * [Apps](/docs/apps/build)
  * [Storefronts](/docs/storefronts)
  * [Agents](/docs/agents)
  * References
  * •
  * Assistant

  * search + assistant
  *   * [Help](/support)
  * •
[Log in](http://dev.shopify.com/dashboard)

Apps

  * [Build](/docs/apps/build)
  * [Design](/docs/apps/design)
  * [Launch](/docs/apps/launch)

Collapse sidebar

  * ### Quality assurance

    * [Going live](/docs/apps/launch)
    * [Checklist of requirements](/docs/apps/launch/app-requirements-checklist)
    * Built for Shopify

    * [Privacy requirements](/docs/apps/launch/privacy-requirements)
    * [Work with protected customer data](/docs/apps/launch/protected-customer-data)
  * ### Pricing strategy

    * [About billing for your app](/docs/apps/launch/billing)
    * [Managed pricing](/docs/apps/launch/billing/managed-pricing)
    * [Redirect to plan selection](/docs/apps/launch/billing/redirect-plan-selection-page)
    * [Offer free trials](/docs/apps/launch/billing/offer-free-trials)
    * Subscription billing

    * [Support one-time purchases](/docs/apps/launch/billing/support-one-time-purchases)
    * [Award app credits](/docs/apps/launch/billing/award-app-credits)
    * [Refund app charges](/docs/apps/launch/billing/refund-app-charges)
    * [View charges and earnings](/docs/apps/launch/billing/view-charges-earnings)
  * ### Deployment

    * [About deployment](/docs/apps/launch/deployment)
    * [Deploy to Google Cloud Run](/docs/apps/launch/deployment/deploy-to-google-cloud-run)
    * [Deploy to a hosting service](/docs/apps/launch/deployment/deploy-to-hosting-service)
    * [About app versions](/docs/apps/launch/deployment/app-versions)
    * [Deploy and release app versions](/docs/apps/launch/deployment/deploy-app-versions)
    * [Deploy app components in a CD pipeline](/docs/apps/launch/deployment/deploy-in-ci-cd-pipeline)
  * ### Reaching customers

    * [About app distribution](/docs/apps/launch/distribution)
    * [Select a distribution method](/docs/apps/launch/distribution/select-distribution-method)
    * [Support your customers](/docs/apps/launch/distribution/support-your-customers)
    * [Sunsetting your app](/docs/apps/launch/distribution/sunsetting-your-app)
    * [Go-to-market success](/docs/apps/launch/distribution/go-to-market-success)
    * [Track app usage](/docs/apps/launch/distribution/track-app-usage)
    * [App listing visibility](/docs/apps/launch/distribution/visibility)
    * [App revenue share](/docs/apps/launch/distribution/revenue-share)
  * ### Shopify app store review

    * [About the Shopify App Store](/docs/apps/launch/app-store-review)
    * [About the app review process](/docs/apps/launch/app-store-review/review-process)
    * [Submit your app for review](/docs/apps/launch/app-store-review/submit-app-for-review)
    * [Pass app review](/docs/apps/launch/app-store-review/pass-app-review)
    * [App listing categories](/docs/apps/launch/app-store-review/app-listing-categories)
    * [Policy violations](/docs/apps/launch/app-store-review/policy-violations)
    * [About app audits](/docs/apps/launch/app-store-review/app-audits)
  * ### Shopify App Store ads

    * [About Shopify App Store ads](/docs/apps/launch/marketing/advertising)
    * [Create ads](/docs/apps/launch/marketing/advertising/create-ads)
    * [Manage ads](/docs/apps/launch/marketing/advertising/manage-ads)
    * [Check ad performance](/docs/apps/launch/marketing/advertising/check-ad-performance)
    * [Ad billing](/docs/apps/launch/marketing/advertising/ad-billing)
    * [Ad permissions](/docs/apps/launch/marketing/advertising/permissions)
    * [Ads FAQ](/docs/apps/launch/marketing/advertising/faq)
  * ### Marketing your app

    * [About marketing your app](/docs/apps/launch/marketing)
    * [Write a press release](/docs/apps/launch/marketing/write-press-release)
    * [Shopify brand assets](/docs/apps/launch/marketing/shopify-brand-assets)
    * [Track your listing traffic](/docs/apps/launch/marketing/track-listing-traffic)
    * [Manage app reviews](/docs/apps/launch/marketing/manage-app-reviews)

Full index

ExpandOn this page

  * [How it works](/docs/apps/launch/billing/refund-app-charges#how-it-works)
  * [Required permissions](/docs/apps/launch/billing/refund-app-charges#required-permissions)
  * [Limitations](/docs/apps/launch/billing/refund-app-charges#limitations)
  * [Issue a refund for an app charge](/docs/apps/launch/billing/refund-app-charges#issue-a-refund-for-an-app-charge)
  * [Next steps](/docs/apps/launch/billing/refund-app-charges#next-steps)

# Refund app charges

Copy page MD

From the [app charge overview](/docs/apps/launch/billing/view-charges-
earnings#app-charge-overview-page) page for a particular app charge, you can
issue a full or partial refund to the merchant.

* * *

##

[Anchor to How it works](/docs/apps/launch/billing/refund-app-charges#how-it-
works)How it works

When you issue a refund to a merchant for an app or theme, Shopify refunds you
only for any commission collected. The processing fee charged on the app or
theme sale is not refunded. [Learn how to view your Shopify fee
invoices](https://help.shopify.com/partners/getting-started/getting-paid#fee-
and-commission-invoices).

You can issue multiple refunds for the same charge when a partial refund is
completed, as long as there's a remaining balance on the charge. When there's
no remaining balance, the button to issue the refund isn't available.

* * *

##

[Anchor to Required permissions](/docs/apps/launch/billing/refund-app-
charges#required-permissions)Required permissions

Store owners can issue refunds by default. Staff members require the `Manage
refunds` and `Manage app` permissions. [Learn more about managing staff member
permissions](https://help.shopify.com/partners/dashboard/account-access).

* * *

##

[Anchor to Limitations](/docs/apps/launch/billing/refund-app-
charges#limitations)Limitations

The following are limitations associated with issuing refunds:

  * You can only refund charges that the merchant has paid for. If an app charge hasn't been paid, then you can [credit the charge](/docs/apps/launch/billing/award-app-credits) to remove it from the merchant's bill.

  * Apps can't issue refunds for charges that are higher than $1000.00 USD. To process a refund that meets this criterion, contact [Shopify Support](https://partners.shopify.com/current/support/).

  * Apps can't issue refunds for invoices that are older than 12 months. To process a refund that meets this criterion, contact [Shopify Support](https://partners.shopify.com/current/support/).

  * If a merchant paid for their invoice with an Automated Clearing House (ACH) bank transfer, then apps can only refund charges on invoices that are less than 90 days old.

* * *

##

[Anchor to Issue a refund for an app charge](/docs/apps/launch/billing/refund-
app-charges#issue-a-refund-for-an-app-charge)Issue a refund for an app charge

You can issue a full or partial refund for an app charge through the [Partner
Dashboard](https://www.shopify.com/partners).

Note

Merchants don't receive an automatic notification of the refund status, so you
must follow up with the merchant and ask them to check their invoice to make
sure that the refund went through.

  1. Log in to your [Partner Dashboard](https://www.shopify.com/partners).
  2. In the Partner Dashboard search bar, enter the name of the store with the app charges that you want to check.
  3. In the search results, click the name of the store.
  4. Next to the app charge that you want to check, click the link in the **Details** column.
  5. Click the arrow to open the charge, and then click **Issue refund**.
  6. In the **Refund amount** field, enter the amount that you want to refund. You can refund the full amount or a partial amount.
  7. Click **Refund**.

After the refund is complete, the charge details are updated to include the
refund.

* * *

##

[Anchor to Next steps](/docs/apps/launch/billing/refund-app-charges#next-
steps)Next steps

[![](/images/icons/48/hearts.png)![](/images/icons/48/hearts-dark.png)Best
practicesLearn best practices for app billing.Best practicesLearn best
practices for app billing.](/docs/apps/launch/billing)

[Best practices  
  
Learn best practices for app billing.](/docs/apps/launch/billing)

* * *

Was this page helpful?

YesNo

  * [How it works](/docs/apps/launch/billing/refund-app-charges#how-it-works)
  * [Required permissions](/docs/apps/launch/billing/refund-app-charges#required-permissions)
  * [Limitations](/docs/apps/launch/billing/refund-app-charges#limitations)
  * [Issue a refund for an app charge](/docs/apps/launch/billing/refund-app-charges#issue-a-refund-for-an-app-charge)
  * [Next steps](/docs/apps/launch/billing/refund-app-charges#next-steps)

### Updates

  * [Developer changelog](/changelog)
  * [Shopify Editions](https://www.shopify.com/editions)

### Business growth

  * [Shopify Partners Program](https://www.shopify.com/partners?shpxid=222dd762-CA08-48FF-E4D4-FF926B8FFCAD)
  * [Shopify App Store](https://apps.shopify.com/?shpxid=222dd762-CA08-48FF-E4D4-FF926B8FFCAD)
  * [Shopify Academy](https://www.shopifyacademy.com/page/catalog#role_developer?utm_source=web_dotdev&utm_medium=footer_businessgrowth)

### Legal

  * [Terms of service](https://www.shopify.com/legal/terms?shpxid=222dd762-CA08-48FF-E4D4-FF926B8FFCAD)
  * [API terms of use](https://www.shopify.com/legal/api-terms?shpxid=222dd762-CA08-48FF-E4D4-FF926B8FFCAD)
  * [Privacy policy](https://www.shopify.com/legal/privacy?shpxid=222dd762-CA08-48FF-E4D4-FF926B8FFCAD)
  * [Partners Program Agreement](https://www.shopify.com/partners/terms?shpxid=222dd762-CA08-48FF-E4D4-FF926B8FFCAD)

### Shopify

  * [About Shopify](https://www.shopify.com/about?shpxid=222dd762-CA08-48FF-E4D4-FF926B8FFCAD)
  * [Shopify Plus](https://www.shopify.com/plus?shpxid=222dd762-CA08-48FF-E4D4-FF926B8FFCAD)
  * [Careers](https://www.shopify.com/careers?shpxid=222dd762-CA08-48FF-E4D4-FF926B8FFCAD)
  * [Investors](https://investors.shopify.com/home/default.aspx?shpxid=222dd762-CA08-48FF-E4D4-FF926B8FFCAD)
  * [Press and media](https://shopify.com/news?shpxid=7db0d4e4-24E8-4087-58FA-7EE470CA745A)

