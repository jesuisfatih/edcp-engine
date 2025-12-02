# Source: https://shopify.dev/docs/apps/launch/deployment/app-versions

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

  * [Deployment workflow](/docs/apps/launch/deployment/app-versions#deployment-workflow)
  * [How app versions are created](/docs/apps/launch/deployment/app-versions#how-app-versions-are-created)

# About app versions

Copy page MD

After you set up your [app configuration](/docs/apps/build/cli-for-apps/app-
configuration) or create one or more [app extensions](/docs/apps/build/app-
extensions), you can deploy these components together and release a new app
version to users. An app version is a snapshot of your app configuration and
all extensions.

* * *

##

[Anchor to Deployment workflow](/docs/apps/launch/deployment/app-
versions#deployment-workflow)Deployment workflow

Your app configuration and all extensions are versioned together as a single
[app version](/docs/apps/launch/deployment/app-versions).

When you run the [`deploy` command](/docs/api/shopify-cli/app/app-deploy)
using [Shopify CLI](/docs/api/shopify-cli), an app version is created and
released. You can revert to a previous app version at any time. You can also
create an app version from the Dev Dashboard.

Releasing an app version replaces the current active version that's served to
stores that have your app installed. It might take several minutes for app
users to be upgraded to the new version.

Tip

If you want to deploy app configuration and extensions to Shopify regularly,
then you can [integrate Shopify CLI into your CI/CD
pipeline](/docs/apps/launch/deployment/deploy-in-ci-cd-pipeline) to
programmatically deploy your app components using the [`deploy`
command](/docs/api/shopify-cli/app/app-deploy).

* * *

##

[Anchor to How app versions are created](/docs/apps/launch/deployment/app-
versions#how-app-versions-are-created)How app versions are created

The contents of your app version are different depending where you create it.

For details about creating and managing app versions, refer to [Deploy and
release app versions](/docs/apps/launch/deployment/deploy-app-versions).

Tool| App version contents  
---|---  
Shopify CLI| An app version created using Shopify CLI contains the following:

  * The app configuration from the local [configuration file](/docs/apps/build/cli-for-apps/app-configuration).
  * The local version of the app's extensions. If you have an extension in your deployed app, but the extension code doesn't exist locally, then the extension isn't included in the version.

  
Dev Dashboard: App version create page| An app version created from the
version create page in the Dev Dashboard contains the configuration on that
page, as well as any extensions that are present on the current active version
of the app.  
  
* * *

Was this page helpful?

YesNo

  * [Deployment workflow](/docs/apps/launch/deployment/app-versions#deployment-workflow)
  * [How app versions are created](/docs/apps/launch/deployment/app-versions#how-app-versions-are-created)

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

