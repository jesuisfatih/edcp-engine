# Source: https://shopify.dev/docs/api/customer/latest/connections/DraftOrderConnection

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

[Anchor to
DraftOrderConnection](/docs/api/customer/latest/connections/DraftOrderConnection#top)

# DraftOrderConnection

connection

Copy page MD

An auto-generated type for paginating through multiple DraftOrders.

##

[Anchor to Fields with this
connection](/docs/api/customer/latest/connections/DraftOrderConnection#fields-
with-this-connection)Fields with this connection

[Anchor to
Company.draftOrders](/docs/api/customer/latest/connections/DraftOrderConnection#reference-
Company.draftOrders)[Company.draftOrders](/docs/api/customer/latest/objects/Company#field-
Company.fields.draftOrders)

•OBJECT

    

Represents a company's information.

[Anchor to
CompanyContact.draftOrders](/docs/api/customer/latest/connections/DraftOrderConnection#reference-
CompanyContact.draftOrders)[CompanyContact.draftOrders](/docs/api/customer/latest/objects/CompanyContact#field-
CompanyContact.fields.draftOrders)

•OBJECT

    

Represents the customer's contact information.

[Anchor to
CompanyLocation.draftOrders](/docs/api/customer/latest/connections/DraftOrderConnection#reference-
CompanyLocation.draftOrders)[CompanyLocation.draftOrders](/docs/api/customer/latest/objects/CompanyLocation#field-
CompanyLocation.fields.draftOrders)

•OBJECT

    

Represents a company's business location.

[Anchor to
Customer.draftOrders](/docs/api/customer/latest/connections/DraftOrderConnection#reference-
Customer.draftOrders)[Customer.draftOrders](/docs/api/customer/latest/objects/Customer#field-
Customer.fields.draftOrders)

•OBJECT

    

Represents the personal information of a customer. Apps using the Customer
Account API must meet the protected customer data
[requirements](https://shopify.dev/docs/apps/launch/protected-customer-data).

* * *

Was this section helpful?

YesNo

##

[Anchor to Possible
returns](/docs/api/customer/latest/connections/DraftOrderConnection#possible-
returns)Possible returns

[Anchor to
edges](/docs/api/customer/latest/connections/DraftOrderConnection#returns-
edges)edges

•[[DraftOrderEdge!]!](/docs/api/customer/latest/objects/DraftOrderEdge)

non-null[Pre-auth accessible](/docs/apps/build/customer-accounts/order-status-
page#customer-account-api)

    

The connection between the node and its parent. Each edge contains a minimum
of the edge's cursor and the node.

Show fields

[Anchor to
nodes](/docs/api/customer/latest/connections/DraftOrderConnection#returns-
nodes)nodes

•[[DraftOrder!]!](/docs/api/customer/latest/objects/DraftOrder)

non-null[Pre-auth accessible](/docs/apps/build/customer-accounts/order-status-
page#customer-account-api)

    

A list of nodes that are contained in DraftOrderEdge. You can fetch data about
an individual node, or you can follow the edges to fetch data about a
collection of related nodes. At each node, you specify the fields that you
want to retrieve.

Show fields

[Anchor to
pageInfo](/docs/api/customer/latest/connections/DraftOrderConnection#returns-
pageInfo)pageInfo

•[PageInfo!](/docs/api/customer/latest/objects/PageInfo)

non-null[Pre-auth accessible](/docs/apps/build/customer-accounts/order-status-
page#customer-account-api)

    

An object that’s used to retrieve [cursor
information](https://shopify.dev/api/usage/pagination-graphql) about the
current page.

Show fields

* * *

Was this section helpful?

YesNo

## Map

### Fields with this connection

  * {}[Company.draftOrders](/docs/api/customer/latest/objects/Company#field-Company.fields.draftOrders)
  * {}[CompanyContact.draftOrders](/docs/api/customer/latest/objects/CompanyContact#field-CompanyContact.fields.draftOrders)
  * {}[CompanyLocation.draftOrders](/docs/api/customer/latest/objects/CompanyLocation#field-CompanyLocation.fields.draftOrders)
  * {}[Customer.draftOrders](/docs/api/customer/latest/objects/Customer#field-Customer.fields.draftOrders)

### Possible returns

  * <->[DraftOrderConnection.edges](/docs/api/customer/latest/connections/DraftOrderConnection#returns-edges)
  * <->[DraftOrderConnection.nodes](/docs/api/customer/latest/connections/DraftOrderConnection#returns-nodes)
  * <->[DraftOrderConnection.pageInfo](/docs/api/customer/latest/connections/DraftOrderConnection#returns-pageInfo)

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

