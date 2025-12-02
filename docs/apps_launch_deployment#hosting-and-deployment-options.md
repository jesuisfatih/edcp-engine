# Source: https://shopify.dev/docs/apps/launch/deployment#hosting-and-deployment-options

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

  * [General requirements for deployment](/docs/apps/launch/deployment#general-requirements-for-deployment)
  * [How it works](/docs/apps/launch/deployment#how-it-works)
  * [Deploying to production](/docs/apps/launch/deployment#deploying-to-production)
  * [Hosting and deployment options](/docs/apps/launch/deployment#hosting-and-deployment-options)
  * [App versions](/docs/apps/launch/deployment#app-versions)
  * [Next steps](/docs/apps/launch/deployment#next-steps)

# About deployment

Copy page MD

This guide explains how to make your Shopify app available to merchants.
You'll learn about hosting options and deployment requirements, whether you're
building with [Shopify React Router](/docs/apps/build/build) or another
framework.

* * *

##

[Anchor to General requirements for
deployment](/docs/apps/launch/deployment#general-requirements-for-
deployment)General requirements for deployment

Before deploying your app:

  * Review your [app's launch requirements](/docs/apps/launch/app-requirements-checklist) and [learn about the launch process](/docs/apps/launch)
  * [Test your app functionality](/docs/apps/build/cli-for-apps/manage-app-config-files#test-your-app-functionality) in a development environment
  * Make sure your local `shopify.app.toml` configuration file is accurate

Note

The [Shopify React Router template](/docs/apps/build/build) automatically
handles key deployment requirements such as authentication, session
management, webhook handling, and environment configuration.

* * *

##

[Anchor to How it works](/docs/apps/launch/deployment#how-it-works)How it
works

When you deploy a Shopify app, you're making your code available to merchants.
This involves:

  * Moving your code from your local development environment to a hosting service
  * Connecting your hosted app to Shopify through [Shopify CLI](/docs/apps/build/cli-for-apps) or the [Dev Dashboard](https://dev.shopify.com/dashboard/)
  * Managing app extensions and configurations through app versions

Your hosting service manages the app's runtime environment and handles
incoming requests through authenticated connections.

* * *

##

[Anchor to Deploying to production](/docs/apps/launch/deployment#deploying-to-
production)Deploying to production

If you're planning on deploying your app for use in production, then consider
creating a separate app. The app might use the same repository and code base
that you use for development and testing, but has its own record and
configuration in the Dev Dashboard.

Note

When deploying a Shopify app, we need to be able to reliably determine which
extensions have been added, updated, and removed from your app. This means
that we need to map extension code to our records of your extensions on
Shopify.

To achieve this, [app extensions](/docs/apps/build/app-extensions) are
idenitified by extension user identifiers (UIDs) that are set in the
`shopify.extension.toml` file. Extension UIDs are unique, source-defined, and
app-scoped, so they can be shared across production, staging, and development
apps.

By default, UIDs are automatically added when you create a new extension using
`shopify app extension generate`, or when you run `shopify app deploy`. UIDs
are deterministic based on the extension handle, so they will always be the
same for extensions with the same app handle value.

Note

[App extensions](/docs/apps/build/app-extensions) are all managed with the
Shopify CLI. If you want to make any changes to app extensions, you must
deploy new versions from the Shopify CLI.

* * *

##

[Anchor to Hosting and deployment
options](/docs/apps/launch/deployment#hosting-and-deployment-options)Hosting
and deployment options

The following are common providers for hosting your Shopify app:

[![](/images/icons/48/googlecloudrun.png)![](/images/icons/48/googlecloudrun-
dark.png)Deploy to Google Cloud RunLearn how to deploy your Shopify app to
Google Cloud Run.Deploy to Google Cloud RunLearn how to deploy your Shopify
app to Google Cloud Run.](/docs/apps/launch/deployment/deploy-to-google-cloud-
run)

[Deploy to Google Cloud Run  
  
Learn how to deploy your Shopify app to Google Cloud
Run.](/docs/apps/launch/deployment/deploy-to-google-cloud-run)

[![](/images/icons/48/flyio.png)![](/images/icons/48/flyio-dark.png)Deploy to
Fly.ioLearn how to deploy your Shopify app to Fly.io.Deploy to Fly.ioLearn how
to deploy your Shopify app to Fly.io.](https://fly.io/shopify)

[Deploy to Fly.io  
  
Learn how to deploy your Shopify app to Fly.io.](https://fly.io/shopify)

[![](/images/icons/48/render.png)![](/images/icons/48/render-dark.png)Deploy
to RenderLearn how to deploy your Shopify app to Render.Deploy to RenderLearn
how to deploy your Shopify app to Render.](https://docs.render.com/deploy-
shopify-app)

[Deploy to Render  
  
Learn how to deploy your Shopify app to
Render.](https://docs.render.com/deploy-shopify-app)

###

[Anchor to Manual deployment](/docs/apps/launch/deployment#manual-
deployment)Manual deployment

If you're comfortable with app hosting and deployment, or if you have specific
infrastructure requirements, then you can deploy to a preferred hosting
service that can run JavaScript apps:

[![](/images/icons/48/tutorial.png)![](/images/icons/48/tutorial-
dark.png)Manual deployment guideChoose this option if you need complete
control over your hosting environment or have specific infrastructure
requirements.Manual deployment guideChoose this option if you need complete
control over your hosting environment or have specific infrastructure
requirements.](/docs/apps/launch/deployment/deploy-to-hosting-service)

[Manual deployment guide  
  
Choose this option if you need complete control over your hosting environment
or have specific infrastructure
requirements.](/docs/apps/launch/deployment/deploy-to-hosting-service)

* * *

##

[Anchor to App versions](/docs/apps/launch/deployment#app-versions)App
versions

After setting up your [app configuration](/docs/apps/build/cli-for-apps/app-
configuration) or creating [app extensions](/docs/apps/build/app-extensions),
you can deploy these components together and release a new app version to
users.

[![](/images/icons/48/app.png)![](/images/icons/48/app-dark.png)App versions
overviewLearn about the deployment model for app configuration and
extensions.App versions overviewLearn about the deployment model for app
configuration and extensions.](/docs/apps/launch/deployment/app-versions)

[App versions overview  
  
Learn about the deployment model for app configuration and
extensions.](/docs/apps/launch/deployment/app-versions)

[![](/images/icons/48/pickaxe-3.png)![](/images/icons/48/pickaxe-3-dark.png)Deploy
and release app versionsLearn how to deploy app configuration and extensions
to Shopify.Deploy and release app versionsLearn how to deploy app
configuration and extensions to Shopify.](/docs/apps/launch/deployment/deploy-
app-versions)

[Deploy and release app versions  
  
Learn how to deploy app configuration and extensions to
Shopify.](/docs/apps/launch/deployment/deploy-app-versions)

[![](/images/icons/48/tutorial.png)![](/images/icons/48/tutorial-
dark.png)Deploy in a CD pipelineLearn how to deploy in a CI/CD pipeline.Deploy
in a CD pipelineLearn how to deploy in a CI/CD
pipeline.](/docs/apps/launch/deployment/deploy-in-ci-cd-pipeline)

[Deploy in a CD pipeline  
  
Learn how to deploy in a CI/CD pipeline.](/docs/apps/launch/deployment/deploy-
in-ci-cd-pipeline)

* * *

##

[Anchor to Next steps](/docs/apps/launch/deployment#next-steps)Next steps

After you have deployed your app, it's time to [review distribution
options](/docs/apps/launch/distribution/select-distribution-method).

* * *

Was this page helpful?

YesNo

  * [General requirements for deployment](/docs/apps/launch/deployment#general-requirements-for-deployment)
  * [How it works](/docs/apps/launch/deployment#how-it-works)
  * [Deploying to production](/docs/apps/launch/deployment#deploying-to-production)
  * [Hosting and deployment options](/docs/apps/launch/deployment#hosting-and-deployment-options)
  * [App versions](/docs/apps/launch/deployment#app-versions)
  * [Next steps](/docs/apps/launch/deployment#next-steps)

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

