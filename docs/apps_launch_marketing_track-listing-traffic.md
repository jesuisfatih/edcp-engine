# Source: https://shopify.dev/docs/apps/launch/marketing/track-listing-traffic

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

  * [Set up Google Analytics for your app listing](/docs/apps/launch/marketing/track-listing-traffic#set-up-google-analytics-for-your-app-listing)
  * [Set up Facebook Pixel for your app listing](/docs/apps/launch/marketing/track-listing-traffic#set-up-facebook-pixel-for-your-app-listing)
  * [URL parameters](/docs/apps/launch/marketing/track-listing-traffic#url-parameters)

# Track your listing traffic

Copy page MD

You can get more information about how merchants are finding your app listing
in the Shopify App Store by tracking your listing traffic with Google
Analytics or Facebook Pixel. [Optimize your
listing](/docs/apps/launch/marketing#improving-your-app-listing) for both
merchants and the Shopify App Store search engine, by gaining a better
understanding of how merchants currently discover your app.

Note

Both [full and limited visibilty](/docs/apps/launch/distribution/visibility)
apps can add Google Analytics or Facebook Pixel tracking, but limited visible
apps won't show up in Shopify App Store search results or category pages.

* * *

##

[Anchor to Set up Google Analytics for your app
listing](/docs/apps/launch/marketing/track-listing-traffic#set-up-google-
analytics-for-your-app-listing)Set up Google Analytics for your app listing

  1. Log in to your [Partner Dashboard](https://partners.shopify.com/organizations).
  2. Click **Apps**.
  3. Click the name of your app.
  4. Click **Distribution**.
  5. Click **Create listing** or **Manage listing** , and then click the listing that you want to edit.
  6. In the **Tracking information** section, next to **Google analytics code (optional)** , enter your GA4 measurement ID.
  7. Click **Save**.

###

[Anchor to Migrating from Universal Analytics to Google Analytics
4](/docs/apps/launch/marketing/track-listing-traffic#migrating-from-universal-
analytics-to-google-analytics-4)Migrating from Universal Analytics to Google
Analytics 4

Google Universal Analytics is being sunset in July 2023. If you previously
used Universal Analytics for your app listing and you want to migrate to
Google Analytics 4, then follow the process to set up Google Analytics, but
replace your UA tracking ID with your new GA4 tracking ID.

Depending on how you use Universal Analytics, you might need to perform the
following additional steps:

  * If you use Universal Analytics audiences, then you need to [migrate audiences to GA4](https://support.google.com/analytics/answer/11184423).
  * If you use Universal Analytics to track Google Ad conversions on your app listing, then you need to [migrate conversion tracking to GA4](https://support.google.com/analytics/answer/11184423).

###

[Anchor to Full-funnel app install
attributions](/docs/apps/launch/marketing/track-listing-traffic#full-funnel-
app-install-attributions)Full-funnel app install attributions

To provide full details of the app installation funnel, the Shopify App Store
uses [Google Analytics 4's Measurement
Protocol](https://developers.google.com/analytics/devguides/collection/protocol/ga4)
for server-side events (like app installation). To receive these events, an
app listing must be on Google Analytics 4 and have entered an API secret
generated in the Google Analytics UI.

The following events are sent to Google Analytics and display in the Real-time
view. However, event parameters might take up to 24 hours to propagate and
need to be added as an [Event-scoped Custom
Dimension](https://support.google.com/analytics/answer/10075209?hl=en#zippy=%2Ccreate-
an-event-scoped-custom-dimension%2Ccreate-a-custom-metric%2Canalyze-an-event-
scoped-custom-dimension).

Events sent to Google AnalyticsEvent name| Parameters| Description  
---|---|---  
`shopify_app_install`|

  * `api_key`
  * `shop_id`
  * `shop_name`
  * `shop_url`

| Sent when a merchant finishes installing an app.  
`shopify_app_ad_click`|

  * `api_key`
  * `surface_type`
  * `surface_detail`

| Sent when a merchant visits an app listing from a Shopify App Store ad
click.  
  
To generate an API secret:

  1. Log into your [Google Analytics](https://analytics.google.com/analytics/web/#/).
  2. Click on the **Admin** icon in the bottom left corner.
  3. Click on **Data Streams** under Property settings.
  4. Select the measurement stream which corresponds to the **Measurement ID** which you have added to your app listing.
  5. Click on **Measurement Protocol API secrets** and click **Create** to generate a new API Secret.

To add the API secret to your app listing:

  1. Log in to your [Partner Dashboard](https://partners.shopify.com/organizations).
  2. Click **Apps**.
  3. Click the name of your app.
  4. Click **Distribution**.
  5. Click **Create listing** or **Manage listing** , and then click the listing that you want to edit.
  6. In the **Tracking information** section, next to **Google analytics code (optional)** , ensure you have upgraded to Google Analyitics 4.
  7. Enter your API Secret.
  8. Click **Save**.

###

[Anchor to Google e-commerce events](/docs/apps/launch/marketing/track-
listing-traffic#google-e-commerce-events)Google e-commerce events

To enhance tracking for e-commerce related interactions, the following events
have been implemented:

E-commerce events sent to Google AnalyticsEvent name| Parameters| Description  
---|---|---  
[`view_item`](https://developers.google.com/analytics/devguides/collection/ga4/reference/events?sjid=2649380085872637034-NC&client_type=gtag#view_item)|

  * `currency`
  * `value`
  * `items`
  * `item_id`
  * `item_name`
  * `price`
  * `quantity`

| Sent when a merchant views an app's details page  
[`add_to_cart`](https://developers.google.com/analytics/devguides/collection/ga4/reference/events?sjid=2649380085872637034-NC&client_type=gtag#add_to_cart)|

  * `currency`
  * `value`
  * `items`
  * `item_id`
  * `item_name`
  * `price`
  * `quantity`

| Sent when a merchant clicks the **Install** button  
  
###

[Anchor to Other events](/docs/apps/launch/marketing/track-listing-
traffic#other-events)Other events

You might want to track the following additional Shopify-specific events in
Google Analytics. These events are triggered client-side from the Shopify App
Store.

Event sent to Google AnalyticsEvent name| Parameters| Description  
---|---|---  
`Add App button`|

  * `event_category`: Always returns `Shopify App Store`.
  * `event_label`: The app's handle.

| Sent when a app user clicks **Install** on an App Listing page.  
`Open app button`|

  * `event_category`: Always returns `Shopify App Store`.
  * `event_label`: The app's handle.

| Sent when a app user clicks **Open** on an App Listing page.  
  
* * *

##

[Anchor to Set up Facebook Pixel for your app
listing](/docs/apps/launch/marketing/track-listing-traffic#set-up-facebook-
pixel-for-your-app-listing)Set up Facebook Pixel for your app listing

  1. Log in to your [Partner Dashboard](https://partners.shopify.com/organizations).
  2. Click **Apps**.
  3. Click the name of your app.
  4. Click **Distribution**.
  5. Click **Create listing** or **Manage listing** , and then click the listing that you want to edit.
  6. In the **E. Tracking** section, next to **3\. Facebook Pixel (optional)** , enter your Facebook Pixel tracking ID.
  7. Click **Save**.

###

[Anchor to Meta Pixel events](/docs/apps/launch/marketing/track-listing-
traffic#meta-pixel-events)Meta Pixel events

To enhance tracking for e-commerce related interactions, the following events
have been implemented:

E-commerce events sent to

[Meta Pixel](https://developers.facebook.com/docs/meta-pixel/reference/)Event
name| Parameters| Description  
---|---|---  
`ViewContent`|

  * `content_ids`
  * `content_name`
  * `currency`
  * `value`

| Sent when a merchant views an app's details page  
  
###

[Anchor to Meta Pixel full-funnel app install
attributions](/docs/apps/launch/marketing/track-listing-traffic#meta-pixel-
full-funnel-app-install-attributions)Meta Pixel full-funnel app install
attributions

The Shopify App Store uses [Meta's Conversions
API](https://developers.facebook.com/docs/marketing-api/conversions-api) to
track server-side events like app installations and provide full installation
funnel details. To receive these events, your app listing needs a configured
Facebook Pixel and an access token from Facebook Events Manager.

Events are sent to Meta Pixel and appear in Events Manager. Event parameters
may take up to 24 hours to fully appear in Facebook's attribution reporting.

Events sent to Meta PixelEvent name| Parameters| Description  
---|---|---  
`AddToCart`|

  * `content_ids`
  * `content_name`
  * `currency`
  * `value`

| Sent when a merchant clicks the **Install** button  
`Purchase`|

  * `shop_name`
  * `shop_url`
  * `value`
  * `currency`
  * `content_ids`
  * `content_type`

| Sent when a merchant finishes installing an app  
  
To generate an access token:

  1. Log into your [Facebook Events Manager](https://business.facebook.com/events_manager2/).
  2. Select your pixel from the data sources.
  3. Click on **Settings**.
  4. Scroll down to **Conversions API**.
  5. Click **Generate Access Token**.
  6. Copy the generated token. It will only be shown once.

To add the access token to your app listing:

  1. Log in to your [Partner Dashboard](https://partners.shopify.com/organizations).
  2. Click **Apps**.
  3. Click the name of your app.
  4. Click **Distribution**.
  5. Click **Create listing** or **Manage listing** , and then click the listing that you want to edit.
  6. In the **Tracking information** section, next to **Facebook Pixel (optional)** , enter your pixel ID.
  7. Enter your access token in the **Facebook Pixel Access Token** field.
  8. Click **Save**.

* * *

##

[Anchor to URL parameters](/docs/apps/launch/marketing/track-listing-
traffic#url-parameters)URL parameters

After you've set up Google Analytics or Facebook Pixel for your app listing,
Shopify passes additional URL parameters when a merchant visits your app
listing from the Shopify App Store. You can see parameters such as the
following in your Google Analytics or Facebook Pixel dashboard:

![The additional parameters shown in the Google Analytics or Facebook Pixel
dashboard](https://cdn.shopify.com/shopifycloud/shopify-
dev/production/assets/assets/images/api/being-successful-in-the-app-store/ga-
parameters-DgoVsLAh.png)

These are noteworthy parameters which can appear in the URL and their meaning:

Parameter| Description| Possible values  
---|---|---  
locale| The language that the merchant has selected in the Shopify App Store.|

  * `zh-CN`: Chinese (Simplified)
  * `zh-TW`: Chinese (Traditional)
  * `cs`: Czech
  * `da`: Danish
  * `nl`: Dutch
  * `fi`: Finnish
  * `fr`: French
  * `de`: German
  * `hi`: Hindi
  * `it`: Italian
  * `ja`: Japanese
  * `ko`: Korean
  * `nb`: Norwegian (Bokmal)
  * `pl`: Polish
  * `pt-PT`: Portuguese
  * `pt-BR`: Portuguese (Brazilian)
  * `es`: Spanish
  * `sv`: Swedish
  * `th`: Thai
  * `tr`: Turkish

  
surface_type| The type of page the merchant came from to get to your app
listing.|

  * `home`: The home page of the Shopify App Store.
  * `search`: The organic search result on the Shopify App Store.
  * `search_ad`: The paid search result on the Shopify App Store.
  * `category`: One of the category pages on the Shopify App Store.
  * `collection`: One of the collection pages on the Shopify App Store.
  * `story`: One of the story pages on the Shopify App Store.
  * `partners`: One of the partner pages on the Shopify App Store.
  * `app_details`: One of the app listing pages on the Shopify App Store.
  * `app_group`: One of the app extension pages on the Shopify App Store.

  
surface_detail| Details about the page that the merchant came from.|

  * For `home`, this is the descriptive handle of the section of the home page where the merchant found your app.
  * For `search`, this is the merchant's search query.
  * For `category`, this includes the titles of the category and the subcategories, joined by a hyphen.
  * For `collection`, this is the title of the collection where the merchant found your app.
  * For `story`, this is the descriptive handle of the section of the story page where the merchant found your app.
  * For `app-details`, this is the unique handle of the app listing page where the merchant found your app.

  
surface_inter_position| The section on the page where the merchant found your
app.|

  * For `home`, this is the section of the Shopify App Store home page where the merchant found your app. The sections are numbered from the top, starting with 1.
  * For `search`, this is the page of search results where the merchant found your app.
  * For `category`, this is the page of category results where the merchant found your app.
  * For `collection`, this is the page of collection results where the merchant found your app.
  * For `story`, this is the section of the story page where the merchant found your app. The sections are numbered from the top, starting with 1.
  * For `app-details`, this is the section of the app listing page where the merchant found your app. The sections are numbered from the top, starting with 1.

  
surface_intra_position| The position within the section of the page where the
merchant found your app. The positions are numbered left to right, top to
bottom, starting with 1.|

  * For `home`, this is the position of your app within the section.
  * For `search`, this is the position of your app on the results page.
  * For `category`, this is the position of your app on the category page.
  * For `collection`, this is the position of your app on the collection page.
  * For `story`, this is the position of your app within the section.
  * For `partners`, this is the position of your app on the partner page.
  * For `app-details`, this is the position of your app within the section.

  
  
* * *

Was this page helpful?

YesNo

  * [Set up Google Analytics for your app listing](/docs/apps/launch/marketing/track-listing-traffic#set-up-google-analytics-for-your-app-listing)
  * [Set up Facebook Pixel for your app listing](/docs/apps/launch/marketing/track-listing-traffic#set-up-facebook-pixel-for-your-app-listing)
  * [URL parameters](/docs/apps/launch/marketing/track-listing-traffic#url-parameters)

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

