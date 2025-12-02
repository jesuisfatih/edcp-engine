# Source: https://shopify.dev/docs/api/admin-graphql/latest/connections/OrderConnection#queries-with-this-connection

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

GraphQL Admin API

Choose a version:

unstable 2026-01 release candidate2025-10 latest2025-07 2025-04 2025-01

2025-10latest

  * [Overview](/docs/api/admin-graphql/2025-10)
  * [Client libraries](/docs/api/admin-graphql/2025-10#client-libraries)
  * [Authentication](/docs/api/admin-graphql/2025-10#authentication)
  * [Endpoints and queries](/docs/api/admin-graphql/2025-10#endpoints-and-queries)
  * [Rate limits](/docs/api/admin-graphql/2025-10#rate-limits)
  * [Status and error codes](/docs/api/admin-graphql/2025-10#status-and-error-codes)

* * *

  * Access

  * Analytics

  * Apps

  * B2B

  * Billing

  * Bulk operations

  * Cart

  * Checkout branding

  * Common objects

  * Customers

  * Discounts and marketing

  * Events

  * Inventory

  * Localizations

  * Metafields

  * Metaobjects

  * Online store

  * Orders

  * Privacy

  * Products and collections

  * Retail

  * Shipping and fulfillment

  * Shopify Markets

  * Shopify Payments

  * Store properties

  * Webhooks

  * * * *

  * GraphQL Types

[Full index](/docs/api/admin-graphql/2025-10/full-index)

Choose a version:

unstable 2026-01 release candidate2025-10 latest2025-07 2025-04 2025-01

2025-10latest

[Anchor to OrderConnection](/docs/api/admin-
graphql/latest/connections/OrderConnection#top)

# OrderConnection

connection

Copy page MD

An auto-generated type for paginating through multiple Orders.

##

[Anchor to Fields with this connection](/docs/api/admin-
graphql/latest/connections/OrderConnection#fields-with-this-connection)Fields
with this connection

[Anchor to Company.orders](/docs/api/admin-
graphql/latest/connections/OrderConnection#reference-
Company.orders)[Company.orders](/docs/api/admin-
graphql/latest/objects/Company#field-Company.fields.orders)

•OBJECT

    

Represents information about a company which is also a customer of the shop.

[Anchor to CompanyContact.orders](/docs/api/admin-
graphql/latest/connections/OrderConnection#reference-
CompanyContact.orders)[CompanyContact.orders](/docs/api/admin-
graphql/latest/objects/CompanyContact#field-CompanyContact.fields.orders)

•OBJECT

    

A person that acts on behalf of company associated to [a
customer](https://shopify.dev/api/admin-graphql/latest/objects/customer).

[Anchor to CompanyLocation.orders](/docs/api/admin-
graphql/latest/connections/OrderConnection#reference-
CompanyLocation.orders)[CompanyLocation.orders](/docs/api/admin-
graphql/latest/objects/CompanyLocation#field-CompanyLocation.fields.orders)

•OBJECT

    

A location or branch of a [company that's a
customer](https://shopify.dev/api/admin-graphql/latest/objects/company) of the
shop. Configuration of B2B relationship, for example prices lists and checkout
settings, may be done for a location.

[Anchor to Customer.orders](/docs/api/admin-
graphql/latest/connections/OrderConnection#reference-
Customer.orders)[Customer.orders](/docs/api/admin-
graphql/latest/objects/Customer#field-Customer.fields.orders)

•OBJECT

    

Represents information about a customer of the shop, such as the customer's
contact details, their order history, and whether they've agreed to receive
marketing material by email.

**Caution:** Only use this data if it's required for your app's functionality.
Shopify will restrict [access to scopes](https://shopify.dev/api/usage/access-
scopes) for apps that don't have a legitimate use for the associated data.

[Anchor to CustomerMergePreviewDefaultFields.orders](/docs/api/admin-
graphql/latest/connections/OrderConnection#reference-
CustomerMergePreviewDefaultFields.orders)[CustomerMergePreviewDefaultFields.orders](/docs/api/admin-
graphql/latest/objects/CustomerMergePreviewDefaultFields#field-
CustomerMergePreviewDefaultFields.fields.orders)

•OBJECT

    

The fields that will be kept as part of a customer merge preview.

[Anchor to SubscriptionBillingCycleEditedContract.orders](/docs/api/admin-
graphql/latest/connections/OrderConnection#reference-
SubscriptionBillingCycleEditedContract.orders)[SubscriptionBillingCycleEditedContract.orders](/docs/api/admin-
graphql/latest/objects/SubscriptionBillingCycleEditedContract#field-
SubscriptionBillingCycleEditedContract.fields.orders)

•OBJECT

    

Represents a subscription contract with billing cycles.

[Anchor to SubscriptionContract.orders](/docs/api/admin-
graphql/latest/connections/OrderConnection#reference-
SubscriptionContract.orders)[SubscriptionContract.orders](/docs/api/admin-
graphql/latest/objects/SubscriptionContract#field-
SubscriptionContract.fields.orders)

•OBJECT

    

Represents a Subscription Contract.

[Anchor to SubscriptionContractBase.orders](/docs/api/admin-
graphql/latest/connections/OrderConnection#reference-
SubscriptionContractBase.orders)[SubscriptionContractBase.orders](/docs/api/admin-
graphql/latest/interfaces/SubscriptionContractBase#fields-orders)

•INTERFACE

    

Represents subscription contract common fields.

[Anchor to Shop.orders](/docs/api/admin-
graphql/latest/connections/OrderConnection#reference-
Shop.orders)[Shop.orders](/docs/api/admin-graphql/latest/objects/Shop#field-
Shop.fields.orders)

•OBJECT

Deprecated

    

* * *

Was this section helpful?

YesNo

##

[Anchor to Queries with this connection](/docs/api/admin-
graphql/latest/connections/OrderConnection#queries-with-this-
connection)Queries with this connection

[Anchor to orders](/docs/api/admin-
graphql/latest/connections/OrderConnection#query-
orders)[orders](/docs/api/admin-graphql/latest/queries/orders)

•query

    

Returns a list of [orders](https://shopify.dev/api/admin-
graphql/latest/objects/Order) placed in the store, including data such as
order status, customer, and line item details. Use the `orders` query to build
reports, analyze sales performance, or automate fulfillment workflows. The
`orders` query supports
[pagination](https://shopify.dev/docs/api/usage/pagination-graphql),
[sorting](https://shopify.dev/docs/api/admin-
graphql/latest/queries/orders#arguments-sortKey), and
[filtering](https://shopify.dev/docs/api/admin-
graphql/latest/queries/orders#arguments-query).

Show fields

* * *

Was this section helpful?

YesNo

##

[Anchor to Possible returns](/docs/api/admin-
graphql/latest/connections/OrderConnection#possible-returns)Possible returns

[Anchor to edges](/docs/api/admin-
graphql/latest/connections/OrderConnection#returns-edges)edges

•[[OrderEdge!]!](/docs/api/admin-graphql/latest/objects/OrderEdge)

non-null

    

The connection between the node and its parent. Each edge contains a minimum
of the edge's cursor and the node.

Show fields

[Anchor to nodes](/docs/api/admin-
graphql/latest/connections/OrderConnection#returns-nodes)nodes

•[[Order!]!](/docs/api/admin-graphql/latest/objects/Order)

non-null

    

A list of nodes that are contained in OrderEdge. You can fetch data about an
individual node, or you can follow the edges to fetch data about a collection
of related nodes. At each node, you specify the fields that you want to
retrieve.

Show fields

[Anchor to pageInfo](/docs/api/admin-
graphql/latest/connections/OrderConnection#returns-pageInfo)pageInfo

•[PageInfo!](/docs/api/admin-graphql/latest/objects/PageInfo)

non-null

    

An object that’s used to retrieve [cursor
information](https://shopify.dev/api/usage/pagination-graphql) about the
current page.

Show fields

* * *

Was this section helpful?

YesNo

## Map

### Fields with this connection

  * {}[Company.orders](/docs/api/admin-graphql/latest/objects/Company#field-Company.fields.orders)
  * {}[CompanyContact.orders](/docs/api/admin-graphql/latest/objects/CompanyContact#field-CompanyContact.fields.orders)
  * {}[CompanyLocation.orders](/docs/api/admin-graphql/latest/objects/CompanyLocation#field-CompanyLocation.fields.orders)
  * {}[Customer.orders](/docs/api/admin-graphql/latest/objects/Customer#field-Customer.fields.orders)
  * {}[CustomerMergePreviewDefaultFields.orders](/docs/api/admin-graphql/latest/objects/CustomerMergePreviewDefaultFields#field-CustomerMergePreviewDefaultFields.fields.orders)
  * {}[SubscriptionBillingCycleEditedContract.orders](/docs/api/admin-graphql/latest/objects/SubscriptionBillingCycleEditedContract#field-SubscriptionBillingCycleEditedContract.fields.orders)
  * {}[SubscriptionContract.orders](/docs/api/admin-graphql/latest/objects/SubscriptionContract#field-SubscriptionContract.fields.orders)
  * ||-[SubscriptionContractBase.orders](/docs/api/admin-graphql/latest/interfaces/SubscriptionContractBase#fields-orders)

Show deprecations

### Queries with this connection

  * <?>[orders](/docs/api/admin-graphql/latest/queries/orders)

### Possible returns

  * <->[OrderConnection.edges](/docs/api/admin-graphql/latest/connections/OrderConnection#returns-edges)
  * <->[OrderConnection.nodes](/docs/api/admin-graphql/latest/connections/OrderConnection#returns-nodes)
  * <->[OrderConnection.pageInfo](/docs/api/admin-graphql/latest/connections/OrderConnection#returns-pageInfo)

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

