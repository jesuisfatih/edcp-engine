# Source: https://shopify.dev/docs/apps/launch/protected-customer-data#example-api-requests-for-protected-customer-data

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

  * [Request access to protected customer data](/docs/apps/launch/protected-customer-data#request-access-to-protected-customer-data)
  * [Using protected customer data](/docs/apps/launch/protected-customer-data#using-protected-customer-data)
  * [Requirements](/docs/apps/launch/protected-customer-data#requirements)
  * [Data protection review](/docs/apps/launch/protected-customer-data#data-protection-review)

# Work with protected customer data

Copy page MD

Privacy and data protection are critical foundations for ecommerce and are
important to merchants and their customers. The protected customer data
requirements focus on data minimization, transparency, and security so that
you can better support a merchant's path towards compliance with privacy and
data protection rules.

When your app uses the [Admin API](/docs/api/admin-graphql) or the [Customer
Account API](/docs/api/customer), the review process for your public,
published app might require action as described in the following table:

Level| Data use| Partner actions  
---|---|---  
0| No customer data| No action required  
1| Customer data **excluding** name, address, phone, and email fields|

  * Request access to protected customer data in the Partner Dashboard
  * Implement level 1 protected customer data requirements

  
2| Customer data **including** name, address, phone, or email fields|

  * Request access to protected customer data and fields in the Partner Dashboard
  * Implement level 1 and level 2 protected customer data requirements
  * Participate in data protection reviews

  
  
Shopify will approve your app to use protected customer data if the requested
data is the minimum amount required by your app to provide the merchant with
the app functionality. If you're approved to access the data that you
requested, then code updates aren't required. If you aren't approved to access
the data that you requested, then you might need to update your app to handle
errors or redacted data. For more information, refer to the example API
requests for protected customer data.

While we encourage all apps to meet protected customer data requirements,
access to the different levels can vary based on app types. See below:

Level| Public app| Custom app| Admin created custom app  
---|---|---|---  
1| Requires review| Always available| Always available  
2| Requires review| Always available| [Varies by
plan](https://help.shopify.com/en/manual/apps/app-types/custom-apps#custom-
level2-pii-app)  
  
To access customer data in development, select the data and fields you're
using in the Partner Dashboard. You don't need to submit a request for review
for apps that are installed only on development stores.

Important

Partners are legally bound by the terms and conditions of the [Shopify Partner
Program Agreement](https://www.shopify.com/partners/terms) and the [Shopify
API License and Terms of Use](https://www.shopify.com/legal/api-terms),
regardless of the API version that they're using. Protected customer data
requirements aren't intended to replace the terms and conditions that you
agree to as a Shopify Partner.

* * *

##

[Anchor to Request access to protected customer
data](/docs/apps/launch/protected-customer-data#request-access-to-protected-
customer-data)Request access to protected customer data

Public apps request access to protected customer data and protected customer
fields through the Partner Dashboard.

Protected customer data includes any data that directly relates to a customer
or prospective customer, as represented in the API types and resources. Types
and resources that don't refer to a single customer, such as the
[product](/docs/api/admin-graphql/latest/queries/product) query, aren't
included.

In addition to requesting access to protected customer data, you'll need to
request access to the following protected customer fields individually because
they directly identify customers:

  * Name: first and last names
  * Address: address line 1, address line 2, geolocation, and zip codes in both billing and shipping addresses
  * Email
  * Phone

If your access is approved, these fields will appear in the protected customer
API types and resources.

To request access:

  1. From the Partner Dashboard, go to [**Apps**](https://partners.shopify.com/current/apps), and then select your app.

  2. In the sidebar, click **API access requests**.

  3. Find **Protected customer data access** and click **Request access**.

  4. Select **Protected customer data** , provide your reasons for using it, and click **Save**.

  5. If your app needs access to protected customer fields, then select the relevant fields, provide your reasons for using them, and click **Save**.

  6. Complete your **Data protection details** , making sure that your app meets the protected customer data requirements.

  7. [Submit your app for review](/docs/apps/launch/app-store-review/submit-app-for-review).

If your app is for testing or installed only on a development store, you can
access customer data in development after Step 5. You don't need to submit for
review.

You'll receive updates about the status of your review by email and through
your Partner Dashboard.

###

[Anchor to Protected customer data API types and
resources](/docs/apps/launch/protected-customer-data#protected-customer-data-
api-types-and-resources)Protected customer data API types and resources

The [GraphQL Admin API](/docs/api/admin-graphql) and [Customer Account
API](/docs/api/customer) reference documentation defines what types, objects,
and fields represent protected customer data.

The following table summarizes the API types that are considered protected
customer data.

API resource/type| Protected customer data  
---|---  
Customers ([GraphQL Admin API](/docs/api/admin-
graphql/latest/objects/Customer), [Customer Account
API](/docs/api/customer/latest/objects/Customer))| Data that defines facts
about a single customer, including name, addresses, email, and phone number.  
Shipping rates ([GraphQL Admin API](/docs/api/admin-
graphql/latest/objects/ShippingRate))| Shipping rates that related to a single
order, which relates to a single customer.  
[Webhooks](/docs/api/webhooks), Metafields ([GraphQL Admin
API](/docs/api/admin-graphql/latest/objects/Metafield), [Customer Account
API](/docs/api/customer/latest/objects/Metafield))| Events and metafields that
relate to a single customer or order.  
Orders ([GraphQL Admin API](/docs/api/admin-graphql/latest/objects/Order),
[Customer Account API](/docs/api/customer/latest/objects/Order))| Orders,
draft orders, abandoned checkouts, refunds, transactions, and other data that
relate to a single customer.  
Checkout ([Storefront API](/docs/api/storefront/latest/objects/Checkout))|
Checkout and payments that relate to orders by a single customer.  
Shipping and fulfillment ([GraphQL Admin API](/docs/api/admin-
graphql/latest/objects/FulfillmentOrder), [Customer Account
API](/docs/api/customer/latest/objects/Fulfillment))| Shipping and fulfillment
data that relate to orders by a single customer.  
Online store ([Storefront API](/docs/api/storefront/latest/objects/Comment))|
Comments on a store that contain data about the commenter.  
Gift cards ([GraphQL Admin API](/docs/api/admin-
graphql/latest/objects/GiftCard))| Gift cards that are used by a single
customer.  
  
* * *

##

[Anchor to Using protected customer data](/docs/apps/launch/protected-
customer-data#using-protected-customer-data)Using protected customer data

After your app is approved to access protected customer data, API requests and
webhooks that contain protected resources will return the data requested.
Responses will include only approved fields, and unapproved fields will be
redacted.

GraphQL requests to unapproved types will return an HTTP `200 Ok` response
with an error message in the `errors` hash.

###

[Anchor to Example API requests for protected customer
data](/docs/apps/launch/protected-customer-data#example-api-requests-for-
protected-customer-data)Example API requests for protected customer data

The following examples show API requests and responses for an app that is
approved to access protected customer data and the `email` and `name` fields.
In this scenario, the `phone` and `address` fields are redacted from the
GraphQL replies. The reply also includes an `errors` message with an
explanation of redacted fields.

####

[Anchor to GraphQL Admin API request with approved
fields](/docs/apps/launch/protected-customer-data#graphql-admin-api-request-
with-approved-fields)GraphQL Admin API request with approved fields

## POST /admin/api/{api_version}/graphql.json

## GraphQL Query

Copy

9

1

2

3

4

5

6

7

{

customer(id: "gid://shopify/Customer/957611081784") {

email

firstName

lastName

}

}

## JSON Response

Copy

99

1

2

3

4

5

6

7

8

9

10

HTTP/1.1 200 OK

{

"data": {

"customer": {

"email": "testcustomer@example.com",

"firstName": "Sally",

"lastName": "Testopherson",

}

}

}

####

[Anchor to GraphQL Admin API request with unapproved
fields](/docs/apps/launch/protected-customer-data#graphql-admin-api-request-
with-unapproved-fields)GraphQL Admin API request with unapproved fields

## POST /admin/api/{api_version}/graphql.json

## GraphQL Query

Copy

9

1

2

3

4

5

6

{

customer(id: "gid://shopify/Customer/957611081784") {

email

phone

}

}

## JSON Response

Copy

99

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

18

19

HTTP/1.1 200 OK

{

"data": {

"customer": {

"email": "testcustomer@example.com",

"phone": null,

}

},

"errors": [

{

"message": "This app is not approved to access the Customer object. See
https://partners.shopify.com/123/apps/456/customer_data for more details.",

"locations": ...,

"path": [

"customer",

"phone"

]

}

]

}

####

[Anchor to Customer Account API request with approved
fields](/docs/apps/launch/protected-customer-data#customer-account-api-
request-with-approved-fields)Customer Account API request with approved fields

## POST /customer/api/{api_version}/graphql.json

## GraphQL Query

Copy

9

1

2

3

4

5

6

7

8

9

{

customer {

firstName

lastName

emailAddress {

emailAddress

}

}

}

## JSON Response

Copy

99

1

2

3

4

5

6

7

8

9

10

11

12

HTTP/1.1 200 OK

{

"data": {

"customer": {

"firstName": "Sally",

"lastName": "Testopherson",

"emailAddress": {

"emailAddress": "testcustomer@example.com"

},

}

}

}

####

[Anchor to Customer Account API request with unapproved
fields](/docs/apps/launch/protected-customer-data#customer-account-api-
request-with-unapproved-fields)Customer Account API request with unapproved
fields

## POST /customer/api/unstable/graphql.json

## Query

Copy

9

1

2

3

4

5

6

7

8

9

{

customer {

firstName

lastName

phoneNumber {

phoneNumber

}

}

}

## JSON Response

Copy

99

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

18

HTTP/1.1 200 OK

{

"data": {

"customer": {

"firstName": "Sally",

"lastName": "Testopherson",

"phoneNumber": {

"phoneNumber": null

},

}

},

"errors": [

{

"message":"This app is not approved to use the phoneNumber field. See
https://partners.shopify.com/123/apps/456/customer_data for more details.",

"locations": ...,

"path":["customer","phoneNumber","phoneNumber"]

}

}

* * *

##

[Anchor to Requirements](/docs/apps/launch/protected-customer-
data#requirements)Requirements

To help apps safely process protected customer data, you must implement the
following requirements in your development practices and in your apps. These
requirements reflect the minimum acceptable handling of protected customer
data and help apps support merchants with increasingly strict privacy and
security requirements. You might need to consult with a privacy or legal
professional for help applying these requirements to your business.

If you're using only protected customer data, then you must meet the level 1
requirements.

If you're using protected customer data including name, address, phone, or
email fields, then you must meet all of the level 1 and 2 requirements.

**Level 1 requirements** :

  1. **Process only the minimum personal data required to provide app functionality to merchants.**

Processing personal data comes with legal and regulatory requirements to
secure, monitor, manage, and communicate about the data. Using the minimum
data required helps minimize the time and effort spent complying with these
requirements, and limits the potential damage of a data breach or unauthorized
access.

  2. **Inform merchants what personal data you process and your reason for processing it.**

Transparency with merchants about what personal data is processed and why
helps merchants manage what processing occurs on their behalf. This
information is often included in your privacy policy or data protection
agreement.

  3. **Limit your processing of personal data to the stated purposes.**

Processing must be limited to the stated purposes to ensure that merchants and
customers are correctly informed about how their data is used.

  4. **Where applicable, respect and apply customer consent decisions.**

Customer consent is a critical mechanism for customers to participate in their
data processing and might be required depending on the type of processing your
app performs.

  5. **Where applicable, respect and apply customer decisions to opt out of any data sharing such as a ‘data sale’ or similar concept under applicable laws or regulations.**

Merchants must comply with applicable laws and regulations around sharing of
personal data and this requirement helps ensure you are prepared to support
them.

  6. **If you use personal data for automated decision-making and those decisions might have legal or significant effects, then you must allow customers to opt out.**

Automated decision-making can include personal data processing such as
profiling, analyzing, predicting, or scoring algorithms. Automated decisions
with legal or significant effects are those that have a material impact on
people's lives and it's important to give customers the option to have their
data manually processed.

  7. **Make privacy and data protection agreements with your merchants.**

Data protection agreements or privacy policies represent an agreement about
personal data processing and are an important tool for formal and safe data
privacy practices. They often include details such as data transfer
mechanisms, scope of data processed, legal roles and responsibilities,
retention, and definition of terms.

  8. **Apply retention periods to make sure that personal data isn’t kept for longer than needed.**

Personal data must not be kept longer than necessary for the stated processing
purposes. Retaining personal data longer than necessary increases the security
risk of unauthorized access or inappropriate processing.

  9. **Encrypt data at rest and in transit.**

Encrypting data when stored and as it transits various networks helps to
prevent bad actors from gaining access to it even if they have access to the
application. It also reduces the consequences of unintentionally disclosing
the data set to the general public.

**Level 2 requirements** :

  9. **Encrypt your data backups.**

Data backups can contain personal data and should be treated with the same
level of concern and consideration as production data in order to prevent
unauthorized access.

  10. **Keep test and production data separate.**

Strict separation of environments prevents personal data from production from
leaking into less secure environments where it could become exposed.

  11. **Have a data loss prevention strategy.**

A data loss prevention strategy is a combination of technical controls,
policies, and standards that protect an organization from the possibility of a
bad actor extracting data for nefarious purposes.

  12. **Limit staff access to protected customer data.**

Limiting staff access to protected customer data minimizes the risk that data
will be improperly accessed, exfiltrated, or processed.

  13. **Require strong passwords for staff accounts.**

Strong password requirements often include minimum length and a mixture of
numbers, letters, and special characters.

  14. **Keep an access log to protected customer data.**

Keeping logs and reviewing them frequently allows an organization to not only
keep an audit trail of activity related to data access, but also assess
whether their security controls are working effectively.

  15. **Implement a security incident response policy.**

A security incident response policy helps organizations respond appropriately
to security incidents and/or data breaches. These policies often include
incident severity scales, roles and responsibilities, escalation paths,
evidence collection, and required actions.

* * *

##

[Anchor to Data protection review](/docs/apps/launch/protected-customer-
data#data-protection-review)Data protection review

To help you meet the protected customer data requirements, we might ask for a
detailed review of your practices. During this review, you'll need to provide
evidence that your app and your practices meet the protected customer data
requirements. If we select your app for a data protection review, then we'll
contact you with instructions on how to proceed. Data protection reviews can
occur after you've implemented the protected customer data requirements.

While any app might be selected, data protection reviews will likely focus on
apps that have:

  * High number of merchant installs
  * High volume of customer records
  * More protected customer fields approved
  * Long retention of personal data

* * *

Was this page helpful?

YesNo

  * [Request access to protected customer data](/docs/apps/launch/protected-customer-data#request-access-to-protected-customer-data)
  * [Using protected customer data](/docs/apps/launch/protected-customer-data#using-protected-customer-data)
  * [Requirements](/docs/apps/launch/protected-customer-data#requirements)
  * [Data protection review](/docs/apps/launch/protected-customer-data#data-protection-review)

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

