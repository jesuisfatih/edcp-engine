# Source: https://shopify.dev/docs/api/admin-graphql/latest/objects/UrlRedirect

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

[Anchor to UrlRedirect](/docs/api/admin-
graphql/latest/objects/UrlRedirect#top)

# UrlRedirect

object

Copy page MD

Requires `read_online_store_navigation` access scope.

The URL redirect for the online store.

##

[Anchor to Fields](/docs/api/admin-
graphql/latest/objects/UrlRedirect#fields)Fields

[Anchor to id](/docs/api/admin-graphql/latest/objects/UrlRedirect#field-
UrlRedirect.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

The ID of the URL redirect.

[Anchor to path](/docs/api/admin-graphql/latest/objects/UrlRedirect#field-
UrlRedirect.fields.path)path

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The old path to be redirected from. When the user visits this path, they will
be redirected to the target location.

[Anchor to target](/docs/api/admin-graphql/latest/objects/UrlRedirect#field-
UrlRedirect.fields.target)target

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The target location where the user will be redirected to.

* * *

Was this section helpful?

YesNo

## Map

### Fields and connections with this object

  * <->[UrlRedirectConnection.nodes](/docs/api/admin-graphql/latest/connections/UrlRedirectConnection#returns-nodes)
  * {}[UrlRedirectEdge.node](/docs/api/admin-graphql/latest/objects/UrlRedirectEdge#field-UrlRedirectEdge.fields.node)

* * *

##

[Anchor to Queries](/docs/api/admin-
graphql/latest/objects/UrlRedirect#queries)Queries

[Anchor to urlRedirect](/docs/api/admin-
graphql/latest/objects/UrlRedirect#query-
urlRedirect)[urlRedirect](/docs/api/admin-graphql/latest/queries/urlRedirect)

•query

    

Returns a `UrlRedirect` resource by ID.

Show fields

[Anchor to urlRedirects](/docs/api/admin-
graphql/latest/objects/UrlRedirect#query-
urlRedirects)[urlRedirects](/docs/api/admin-
graphql/latest/queries/urlRedirects)

•query

    

A list of redirects for a shop.

Show fields

* * *

Was this section helpful?

YesNo

## <?>UrlRedirect Queries

### Queried by

  * <?>[urlRedirect](/docs/api/admin-graphql/latest/queries/urlRedirect)
  * <?>[urlRedirects](/docs/api/admin-graphql/latest/queries/urlRedirects)

* * *

##

[Anchor to Mutations](/docs/api/admin-
graphql/latest/objects/UrlRedirect#mutations)Mutations

[Anchor to urlRedirectCreate](/docs/api/admin-
graphql/latest/objects/UrlRedirect#mutation-
urlRedirectCreate)[urlRedirectCreate](/docs/api/admin-
graphql/latest/mutations/urlRedirectCreate)

•mutation

    

Creates a [`UrlRedirect`](https://shopify.dev/api/admin-
graphql/latest/objects/UrlRedirect) object.

Show payload

[Anchor to urlRedirectUpdate](/docs/api/admin-
graphql/latest/objects/UrlRedirect#mutation-
urlRedirectUpdate)[urlRedirectUpdate](/docs/api/admin-
graphql/latest/mutations/urlRedirectUpdate)

•mutation

    

Updates a URL redirect.

Show payload

* * *

Was this section helpful?

YesNo

## <~> UrlRedirect Mutations

### Mutated by

  * <~>[urlRedirectCreate](/docs/api/admin-graphql/latest/mutations/urlRedirectCreate)
  * <~>[urlRedirectUpdate](/docs/api/admin-graphql/latest/mutations/urlRedirectUpdate)

* * *

##

[Anchor to Interfaces](/docs/api/admin-
graphql/latest/objects/UrlRedirect#interfaces)Interfaces

[Anchor to Node](/docs/api/admin-graphql/latest/objects/UrlRedirect#interface-
Node)[Node](/docs/api/admin-graphql/latest/interfaces/Node)

•interface

* * *

Was this section helpful?

YesNo

## ||-UrlRedirect Implements

### Implements

  * ||-[Node](/docs/api/admin-graphql/latest/interfaces/Node)

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

