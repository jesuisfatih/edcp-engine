# Source: https://shopify.dev/docs/api/admin-graphql/latest/objects/shoppaypaymentrequestlineitem

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

[Anchor to ShopPayPaymentRequestLineItem](/docs/api/admin-
graphql/latest/objects/shoppaypaymentrequestlineitem#top)

# ShopPayPaymentRequestLineItem

object

Copy page MD

Represents a line item for a Shop Pay payment request.

##

[Anchor to Fields](/docs/api/admin-
graphql/latest/objects/shoppaypaymentrequestlineitem#fields)Fields

[Anchor to finalItemPrice](/docs/api/admin-
graphql/latest/objects/shoppaypaymentrequestlineitem#field-
ShopPayPaymentRequestLineItem.fields.finalItemPrice)finalItemPrice

•[MoneyV2!](/docs/api/admin-graphql/latest/objects/MoneyV2)

non-null

    

The final item price for the line item.

Show fields

[Anchor to finalLinePrice](/docs/api/admin-
graphql/latest/objects/shoppaypaymentrequestlineitem#field-
ShopPayPaymentRequestLineItem.fields.finalLinePrice)finalLinePrice

•[MoneyV2!](/docs/api/admin-graphql/latest/objects/MoneyV2)

non-null

    

The final line price for the line item.

Show fields

[Anchor to image](/docs/api/admin-
graphql/latest/objects/shoppaypaymentrequestlineitem#field-
ShopPayPaymentRequestLineItem.fields.image)image

•[ShopPayPaymentRequestImage](/docs/api/admin-
graphql/latest/objects/ShopPayPaymentRequestImage)

    

The image of the line item.

Show fields

[Anchor to itemDiscounts](/docs/api/admin-
graphql/latest/objects/shoppaypaymentrequestlineitem#field-
ShopPayPaymentRequestLineItem.fields.itemDiscounts)itemDiscounts

•[[ShopPayPaymentRequestDiscount!]](/docs/api/admin-
graphql/latest/objects/ShopPayPaymentRequestDiscount)

    

The item discounts for the line item.

Show fields

[Anchor to label](/docs/api/admin-
graphql/latest/objects/shoppaypaymentrequestlineitem#field-
ShopPayPaymentRequestLineItem.fields.label)label

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The label of the line item.

[Anchor to lineDiscounts](/docs/api/admin-
graphql/latest/objects/shoppaypaymentrequestlineitem#field-
ShopPayPaymentRequestLineItem.fields.lineDiscounts)lineDiscounts

•[[ShopPayPaymentRequestDiscount!]](/docs/api/admin-
graphql/latest/objects/ShopPayPaymentRequestDiscount)

    

The line discounts for the line item.

Show fields

[Anchor to originalItemPrice](/docs/api/admin-
graphql/latest/objects/shoppaypaymentrequestlineitem#field-
ShopPayPaymentRequestLineItem.fields.originalItemPrice)originalItemPrice

•[MoneyV2](/docs/api/admin-graphql/latest/objects/MoneyV2)

    

The original item price for the line item.

Show fields

[Anchor to originalLinePrice](/docs/api/admin-
graphql/latest/objects/shoppaypaymentrequestlineitem#field-
ShopPayPaymentRequestLineItem.fields.originalLinePrice)originalLinePrice

•[MoneyV2](/docs/api/admin-graphql/latest/objects/MoneyV2)

    

The original line price for the line item.

Show fields

[Anchor to quantity](/docs/api/admin-
graphql/latest/objects/shoppaypaymentrequestlineitem#field-
ShopPayPaymentRequestLineItem.fields.quantity)quantity

•[Int!](/docs/api/admin-graphql/latest/scalars/Int)

non-null

    

The quantity of the line item.

[Anchor to requiresShipping](/docs/api/admin-
graphql/latest/objects/shoppaypaymentrequestlineitem#field-
ShopPayPaymentRequestLineItem.fields.requiresShipping)requiresShipping

•[Boolean](/docs/api/admin-graphql/latest/scalars/Boolean)

    

Whether the line item requires shipping.

[Anchor to sku](/docs/api/admin-
graphql/latest/objects/shoppaypaymentrequestlineitem#field-
ShopPayPaymentRequestLineItem.fields.sku)sku

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The SKU of the line item.

* * *

Was this section helpful?

YesNo

## Map

### Fields with this object

  * {}[ShopPayPaymentRequest.lineItems](/docs/api/admin-graphql/latest/objects/ShopPayPaymentRequest#field-ShopPayPaymentRequest.fields.lineItems)

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

