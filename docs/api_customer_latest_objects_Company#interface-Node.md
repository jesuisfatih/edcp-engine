# Source: https://shopify.dev/docs/api/customer/latest/objects/Company#interface-Node

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

Collapse sidebar

Customer Account API

Choose a version:

unstable 2026-01 release candidate2025-10 latest2025-07 2025-04 2025-01

2025-10latest

  * [Overview](/docs/api/customer/2025-10)
  * [Authentication](/docs/api/customer/2025-10#authentication)
  * [Endpoints and queries](/docs/api/customer/2025-10#endpoints-and-queries)
  * [Directives](/docs/api/customer/2025-10#directives)
  * [Rate limits](/docs/api/customer/2025-10#rate-limits)
  * [Status and error codes](/docs/api/customer/2025-10#status-and-error-codes)

* * *

  * Common objects

  * * * *

  * GraphQL Types

[Full index](/docs/api/customer/2025-10/full-index)

Choose a version:

unstable 2026-01 release candidate2025-10 latest2025-07 2025-04 2025-01

2025-10latest

[Anchor to Company](/docs/api/customer/latest/objects/Company#top)

# Company

object

Copy page MD

Represents a company's information.

##

[Anchor to Fields](/docs/api/customer/latest/objects/Company#fields)Fields

[Anchor to draftOrders](/docs/api/customer/latest/objects/Company#field-
Company.fields.draftOrders)draftOrders

•[DraftOrderConnection!](/docs/api/customer/latest/connections/DraftOrderConnection)

non-null

    

The list of company draft orders.

Show fields

[Anchor to externalId](/docs/api/customer/latest/objects/Company#field-
Company.fields.externalId)externalId

•[String](/docs/api/customer/latest/scalars/String)

[Pre-auth accessible](/docs/apps/build/customer-accounts/order-status-
page#customer-account-api)

    

A unique externally-supplied ID for the company.

[Anchor to id](/docs/api/customer/latest/objects/Company#field-
Company.fields.id)id

•[ID!](/docs/api/customer/latest/scalars/ID)

non-null[Pre-auth accessible](/docs/apps/build/customer-accounts/order-status-
page#customer-account-api)

    

A globally-unique ID.

[Anchor to locations](/docs/api/customer/latest/objects/Company#field-
Company.fields.locations)locations

•[CompanyLocationConnection!](/docs/api/customer/latest/connections/CompanyLocationConnection)

non-null

    

The list of locations that the business of the business contact belongs to.

Show fields

[Anchor to metafield](/docs/api/customer/latest/objects/Company#field-
Company.fields.metafield)metafield

•[Metafield](/docs/api/customer/latest/objects/Metafield)

[Pre-auth accessible](/docs/apps/build/customer-accounts/order-status-
page#customer-account-api)

    

A metafield found by namespace and key.

Show fields

[Anchor to metafields](/docs/api/customer/latest/objects/Company#field-
Company.fields.metafields)metafields

•[[Metafield]!](/docs/api/customer/latest/objects/Metafield)

non-null[Pre-auth accessible](/docs/apps/build/customer-accounts/order-status-
page#customer-account-api)

    

The metafields associated with the resource matching the supplied list of
namespaces and keys.

Show fields

[Anchor to name](/docs/api/customer/latest/objects/Company#field-
Company.fields.name)name

•[String!](/docs/api/customer/latest/scalars/String)

non-null[Pre-auth accessible](/docs/apps/build/customer-accounts/order-status-
page#customer-account-api)

    

The name of the company.

[Anchor to orders](/docs/api/customer/latest/objects/Company#field-
Company.fields.orders)orders

•[OrderConnection!](/docs/api/customer/latest/connections/OrderConnection)

non-null

    

The list of customer orders under the company.

Show fields

* * *

Was this section helpful?

YesNo

## Map

### Fields with this object

  * {}[CompanyContact.company](/docs/api/customer/latest/objects/CompanyContact#field-CompanyContact.fields.company)
  * {}[PurchasingCompany.company](/docs/api/customer/latest/objects/PurchasingCompany#field-PurchasingCompany.fields.company)

* * *

##

[Anchor to Queries](/docs/api/customer/latest/objects/Company#queries)Queries

[Anchor to company](/docs/api/customer/latest/objects/Company#query-
company)[company](/docs/api/customer/latest/queries/company)

•query

    

The information of the customer's company. Apps using the Customer Account API
must meet the protected customer data
[requirements](https://shopify.dev/docs/apps/launch/protected-customer-data).

Show fields

* * *

Was this section helpful?

YesNo

## <?>Company Queries

### Queried by

  * <?>[company](/docs/api/customer/latest/queries/company)

* * *

##

[Anchor to
Interfaces](/docs/api/customer/latest/objects/Company#interfaces)Interfaces

[Anchor to HasMetafields](/docs/api/customer/latest/objects/Company#interface-
HasMetafields)[HasMetafields](/docs/api/customer/latest/interfaces/HasMetafields)

•interface

[Anchor to Node](/docs/api/customer/latest/objects/Company#interface-
Node)[Node](/docs/api/customer/latest/interfaces/Node)

•interface

* * *

Was this section helpful?

YesNo

## ||-Company Implements

### Implements

  * ||-[HasMetafields](/docs/api/customer/latest/interfaces/HasMetafields)
  * ||-[Node](/docs/api/customer/latest/interfaces/Node)

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

