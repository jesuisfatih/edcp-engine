# Source: https://shopify.dev/docs/api/admin-graphql/latest/interfaces/Node#possible-types-AppPurchaseOneTime.fields.test

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

[Anchor to Node](/docs/api/admin-graphql/latest/interfaces/Node#top)

# Node

interface

Copy page MD

An object with an ID field to support global identification, in accordance
with the [Relay
specification](https://relay.dev/graphql/objectidentification.htm#sec-Node-
Interface). This interface is used by the
[node](https://shopify.dev/api/admin-graphql/unstable/queries/node) and
[nodes](https://shopify.dev/api/admin-graphql/unstable/queries/nodes) queries.

##

[Anchor to Fields](/docs/api/admin-
graphql/latest/interfaces/Node#fields)Fields

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#fields-id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

* * *

Was this section helpful?

YesNo

##

[Anchor to Types implemented in](/docs/api/admin-
graphql/latest/interfaces/Node#types-implemented-in)Types implemented in

[Anchor to AbandonedCheckout](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
AbandonedCheckout)[AbandonedCheckout](/docs/api/admin-
graphql/latest/objects/AbandonedCheckout)

•OBJECT

    

A checkout that was abandoned by the customer.

Show fields

[Anchor to abandonedCheckoutUrl](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
AbandonedCheckout.fields.abandonedCheckoutUrl)abandonedCheckoutUrl

•[URL!](/docs/api/admin-graphql/latest/scalars/URL)

non-null

    

The URL for the buyer to recover their checkout.

[Anchor to billingAddress](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
AbandonedCheckout.fields.billingAddress)billingAddress

•[MailingAddress](/docs/api/admin-graphql/latest/objects/MailingAddress)

    

The billing address provided by the buyer. Null if the user did not provide a
billing address.

Show fields

[Anchor to completedAt](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
AbandonedCheckout.fields.completedAt)completedAt

•[DateTime](/docs/api/admin-graphql/latest/scalars/DateTime)

    

The date and time when the buyer completed the checkout. Null if the checkout
has not been completed.

[Anchor to createdAt](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-AbandonedCheckout.fields.createdAt)createdAt

•[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime)

non-null

    

The date and time when the checkout was created.

[Anchor to customAttributes](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
AbandonedCheckout.fields.customAttributes)customAttributes

•[[Attribute!]!](/docs/api/admin-graphql/latest/objects/Attribute)

non-null

    

A list of extra information that has been added to the checkout.

Show fields

[Anchor to customer](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-AbandonedCheckout.fields.customer)customer

•[Customer](/docs/api/admin-graphql/latest/objects/Customer)

    

The customer who created this checkout. May be null if the checkout was
created from a draft order or via an app.

Show fields

[Anchor to defaultCursor](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
AbandonedCheckout.fields.defaultCursor)defaultCursor

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

A default [cursor](https://shopify.dev/api/usage/pagination-graphql) that
returns the single next record, sorted ascending by ID.

[Anchor to discountCodes](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
AbandonedCheckout.fields.discountCodes)discountCodes

•[[String!]!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The discount codes entered by the buyer at checkout.

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
AbandonedCheckout.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to lineItems](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-AbandonedCheckout.fields.lineItems)lineItems

•[AbandonedCheckoutLineItemConnection!](/docs/api/admin-
graphql/latest/connections/AbandonedCheckoutLineItemConnection)

non-null

    

A list of the line items in this checkout.

Show fields

[Anchor to name](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-AbandonedCheckout.fields.name)name

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

Unique merchant-facing identifier for the checkout.

[Anchor to note](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-AbandonedCheckout.fields.note)note

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

A merchant-facing note added to the checkout. Not visible to the buyer.

[Anchor to shippingAddress](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
AbandonedCheckout.fields.shippingAddress)shippingAddress

•[MailingAddress](/docs/api/admin-graphql/latest/objects/MailingAddress)

    

The shipping address to where the line items will be shipped. Null if the user
did not provide a shipping address.

Show fields

[Anchor to subtotalPriceSet](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
AbandonedCheckout.fields.subtotalPriceSet)subtotalPriceSet

•[MoneyBag!](/docs/api/admin-graphql/latest/objects/MoneyBag)

non-null

    

The sum of all items in the checkout, including discounts but excluding
shipping, taxes and tips.

Show fields

[Anchor to taxesIncluded](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
AbandonedCheckout.fields.taxesIncluded)taxesIncluded

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether taxes are included in line item and shipping line prices.

[Anchor to taxLines](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-AbandonedCheckout.fields.taxLines)taxLines

•[[TaxLine!]!](/docs/api/admin-graphql/latest/objects/TaxLine)

non-null

    

Individual taxes charged on the checkout.

Show fields

[Anchor to totalDiscountSet](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
AbandonedCheckout.fields.totalDiscountSet)totalDiscountSet

•[MoneyBag!](/docs/api/admin-graphql/latest/objects/MoneyBag)

non-null

    

The total amount of discounts to be applied.

Show fields

[Anchor to totalDutiesSet](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
AbandonedCheckout.fields.totalDutiesSet)totalDutiesSet

•[MoneyBag](/docs/api/admin-graphql/latest/objects/MoneyBag)

    

The total duties applied to the checkout.

Show fields

[Anchor to totalLineItemsPriceSet](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
AbandonedCheckout.fields.totalLineItemsPriceSet)totalLineItemsPriceSet

•[MoneyBag!](/docs/api/admin-graphql/latest/objects/MoneyBag)

non-null

    

The sum of the prices of all line items in the checkout.

Show fields

[Anchor to totalPriceSet](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
AbandonedCheckout.fields.totalPriceSet)totalPriceSet

•[MoneyBag!](/docs/api/admin-graphql/latest/objects/MoneyBag)

non-null

    

The sum of all items in the checkout, including discounts, shipping, taxes,
and tips.

Show fields

[Anchor to totalTaxSet](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
AbandonedCheckout.fields.totalTaxSet)totalTaxSet

•[MoneyBag](/docs/api/admin-graphql/latest/objects/MoneyBag)

    

The total tax applied to the checkout.

Show fields

[Anchor to updatedAt](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-AbandonedCheckout.fields.updatedAt)updatedAt

•[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime)

non-null

    

The date and time when the checkout was most recently updated.

[Anchor to lineItemsQuantity](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
AbandonedCheckout.fields.lineItemsQuantity)lineItemsQuantity

•[Int!](/docs/api/admin-graphql/latest/scalars/Int)

non-nullDeprecated

    

[Anchor to AbandonedCheckoutLineItem](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
AbandonedCheckoutLineItem)[AbandonedCheckoutLineItem](/docs/api/admin-
graphql/latest/objects/AbandonedCheckoutLineItem)

•OBJECT

    

A single line item in an abandoned checkout.

Show fields

[Anchor to components](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
AbandonedCheckoutLineItem.fields.components)components

•[[AbandonedCheckoutLineItemComponent!]](/docs/api/admin-
graphql/latest/objects/AbandonedCheckoutLineItemComponent)

    

A list of line item components for this line item.

Show fields

[Anchor to customAttributes](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
AbandonedCheckoutLineItem.fields.customAttributes)customAttributes

•[[Attribute!]!](/docs/api/admin-graphql/latest/objects/Attribute)

non-null

    

A list of extra information that has been added to the line item.

Show fields

[Anchor to discountAllocations](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
AbandonedCheckoutLineItem.fields.discountAllocations)discountAllocations

•[DiscountAllocationConnection!](/docs/api/admin-
graphql/latest/connections/DiscountAllocationConnection)

non-null

    

Discount allocations that have been applied on the line item.

Show fields

[Anchor to discountedTotalPriceSet](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
AbandonedCheckoutLineItem.fields.discountedTotalPriceSet)discountedTotalPriceSet

•[MoneyBag!](/docs/api/admin-graphql/latest/objects/MoneyBag)

non-null

    

Final total price for the entire quantity of this line item, including
discounts.

Show fields

[Anchor to discountedTotalPriceWithCodeDiscount](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
AbandonedCheckoutLineItem.fields.discountedTotalPriceWithCodeDiscount)discountedTotalPriceWithCodeDiscount

•[MoneyBag!](/docs/api/admin-graphql/latest/objects/MoneyBag)

non-null

    

The total price for the entire quantity of this line item, after all discounts
are applied, at both the line item and code-based line item level.

Show fields

[Anchor to discountedUnitPriceSet](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
AbandonedCheckoutLineItem.fields.discountedUnitPriceSet)discountedUnitPriceSet

•[MoneyBag!](/docs/api/admin-graphql/latest/objects/MoneyBag)

non-null

    

The price of a single variant unit after discounts are applied at the line
item level, in shop and presentment currencies.

Show fields

[Anchor to discountedUnitPriceWithCodeDiscount](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
AbandonedCheckoutLineItem.fields.discountedUnitPriceWithCodeDiscount)discountedUnitPriceWithCodeDiscount

•[MoneyBag!](/docs/api/admin-graphql/latest/objects/MoneyBag)

non-null

    

The price of a single variant unit after all discounts are applied, at both
the line item and code-based line item level.

Show fields

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
AbandonedCheckoutLineItem.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to image](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-AbandonedCheckoutLineItem.fields.image)image

•[Image](/docs/api/admin-graphql/latest/objects/Image)

    

The image associated with the line item's variant or product. NULL if the line
item has no product, or if neither the variant nor the product have an image.

Show fields

[Anchor to originalTotalPriceSet](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
AbandonedCheckoutLineItem.fields.originalTotalPriceSet)originalTotalPriceSet

•[MoneyBag!](/docs/api/admin-graphql/latest/objects/MoneyBag)

non-null

    

Original total price for the entire quantity of this line item, before
discounts.

Show fields

[Anchor to originalUnitPriceSet](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
AbandonedCheckoutLineItem.fields.originalUnitPriceSet)originalUnitPriceSet

•[MoneyBag!](/docs/api/admin-graphql/latest/objects/MoneyBag)

non-null

    

Original price for a single unit of this line item, before discounts.

Show fields

[Anchor to parentRelationship](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
AbandonedCheckoutLineItem.fields.parentRelationship)parentRelationship

•[AbandonedCheckoutLineItemParentRelationship](/docs/api/admin-
graphql/latest/objects/AbandonedCheckoutLineItemParentRelationship)

    

The parent relationship for this line item.

Show fields

[Anchor to product](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-AbandonedCheckoutLineItem.fields.product)product

•[Product](/docs/api/admin-graphql/latest/objects/Product)

    

Product for this line item. NULL for custom line items and products that were
deleted after checkout began.

Show fields

[Anchor to quantity](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-AbandonedCheckoutLineItem.fields.quantity)quantity

•[Int!](/docs/api/admin-graphql/latest/scalars/Int)

non-null

    

The quantity of the line item.

[Anchor to sku](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
AbandonedCheckoutLineItem.fields.sku)sku

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

SKU for the inventory item associated with the variant, if any.

[Anchor to title](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-AbandonedCheckoutLineItem.fields.title)title

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

Title of the line item. Defaults to the product's title.

[Anchor to variant](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-AbandonedCheckoutLineItem.fields.variant)variant

•[ProductVariant](/docs/api/admin-graphql/latest/objects/ProductVariant)

    

Product variant for this line item. NULL for custom line items and variants
that were deleted after checkout began.

Show fields

[Anchor to variantTitle](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
AbandonedCheckoutLineItem.fields.variantTitle)variantTitle

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

Title of the variant for this line item. NULL for custom line items and
products that don't have distinct variants.

[Anchor to Abandonment](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Abandonment)[Abandonment](/docs/api/admin-graphql/latest/objects/Abandonment)

•OBJECT

    

A browse, cart, or checkout that was abandoned by a customer.

Show fields

[Anchor to abandonedCheckoutPayload](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Abandonment.fields.abandonedCheckoutPayload)abandonedCheckoutPayload

•[AbandonedCheckout](/docs/api/admin-graphql/latest/objects/AbandonedCheckout)

    

The abandonment payload for the abandoned checkout.

Show fields

[Anchor to abandonmentType](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Abandonment.fields.abandonmentType)abandonmentType

•[AbandonmentAbandonmentType!](/docs/api/admin-
graphql/latest/enums/AbandonmentAbandonmentType)

non-null

    

The abandonment type.

Show enum values

[Anchor to app](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
Abandonment.fields.app)app

•[App!](/docs/api/admin-graphql/latest/objects/App)

non-null

    

The app associated with an abandoned checkout.

Show fields

[Anchor to cartUrl](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Abandonment.fields.cartUrl)cartUrl

•[URL](/docs/api/admin-graphql/latest/scalars/URL)

    

Permalink to the cart page.

[Anchor to createdAt](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Abandonment.fields.createdAt)createdAt

•[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime)

non-null

    

The date and time when the abandonment was created.

[Anchor to customer](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Abandonment.fields.customer)customer

•[Customer!](/docs/api/admin-graphql/latest/objects/Customer)

non-null

    

The customer who abandoned this event.

Show fields

[Anchor to customerHasNoDraftOrderSinceAbandonment](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Abandonment.fields.customerHasNoDraftOrderSinceAbandonment)customerHasNoDraftOrderSinceAbandonment

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether the customer has a draft order since this abandonment has been
abandoned.

[Anchor to customerHasNoOrderSinceAbandonment](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Abandonment.fields.customerHasNoOrderSinceAbandonment)customerHasNoOrderSinceAbandonment

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether the customer has completed an order since this checkout has been
abandoned.

[Anchor to daysSinceLastAbandonmentEmail](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Abandonment.fields.daysSinceLastAbandonmentEmail)daysSinceLastAbandonmentEmail

•[Int!](/docs/api/admin-graphql/latest/scalars/Int)

non-null

    

The number of days since the last abandonment email was sent to the customer.

[Anchor to emailSentAt](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Abandonment.fields.emailSentAt)emailSentAt

•[DateTime](/docs/api/admin-graphql/latest/scalars/DateTime)

    

When the email was sent, if that's the case.

[Anchor to emailState](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Abandonment.fields.emailState)emailState

•[AbandonmentEmailState](/docs/api/admin-
graphql/latest/enums/AbandonmentEmailState)

    

The email state (e.g., sent or not sent).

Show enum values

[Anchor to hoursSinceLastAbandonedCheckout](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Abandonment.fields.hoursSinceLastAbandonedCheckout)hoursSinceLastAbandonedCheckout

•[Float](/docs/api/admin-graphql/latest/scalars/Float)

    

The number of hours since the customer has last abandoned a checkout.

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
Abandonment.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to inventoryAvailable](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Abandonment.fields.inventoryAvailable)inventoryAvailable

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether the products in abandonment are available.

[Anchor to isFromCustomStorefront](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Abandonment.fields.isFromCustomStorefront)isFromCustomStorefront

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether the abandonment event comes from a custom storefront channel.

[Anchor to isFromOnlineStore](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Abandonment.fields.isFromOnlineStore)isFromOnlineStore

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether the abandonment event comes from the Online Store sales channel.

[Anchor to isFromShopApp](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Abandonment.fields.isFromShopApp)isFromShopApp

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether the abandonment event comes from the Shop app sales channel.

[Anchor to isFromShopPay](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Abandonment.fields.isFromShopPay)isFromShopPay

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether the abandonment event comes from Shop Pay.

[Anchor to isMostSignificantAbandonment](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Abandonment.fields.isMostSignificantAbandonment)isMostSignificantAbandonment

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether the customer didn't complete another most significant step since this
abandonment.

[Anchor to lastBrowseAbandonmentDate](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Abandonment.fields.lastBrowseAbandonmentDate)lastBrowseAbandonmentDate

•[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime)

non-null

    

The date for the latest browse abandonment.

[Anchor to lastCartAbandonmentDate](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Abandonment.fields.lastCartAbandonmentDate)lastCartAbandonmentDate

•[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime)

non-null

    

The date for the latest cart abandonment.

[Anchor to lastCheckoutAbandonmentDate](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Abandonment.fields.lastCheckoutAbandonmentDate)lastCheckoutAbandonmentDate

•[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime)

non-null

    

The date for the latest checkout abandonment.

[Anchor to mostRecentStep](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Abandonment.fields.mostRecentStep)mostRecentStep

•[AbandonmentAbandonmentType!](/docs/api/admin-
graphql/latest/enums/AbandonmentAbandonmentType)

non-null

    

The most recent step type.

Show enum values

[Anchor to productsAddedToCart](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Abandonment.fields.productsAddedToCart)productsAddedToCart

•[CustomerVisitProductInfoConnection!](/docs/api/admin-
graphql/latest/connections/CustomerVisitProductInfoConnection)

non-null

    

The products added to the cart during the customer abandoned visit.

Show fields

[Anchor to productsViewed](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Abandonment.fields.productsViewed)productsViewed

•[CustomerVisitProductInfoConnection!](/docs/api/admin-
graphql/latest/connections/CustomerVisitProductInfoConnection)

non-null

    

The products viewed during the customer abandoned visit.

Show fields

[Anchor to visitStartedAt](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Abandonment.fields.visitStartedAt)visitStartedAt

•[DateTime](/docs/api/admin-graphql/latest/scalars/DateTime)

    

The date and time when the visit started.

[Anchor to AddAllProductsOperation](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
AddAllProductsOperation)[AddAllProductsOperation](/docs/api/admin-
graphql/latest/objects/AddAllProductsOperation)

•OBJECT

    

Represents an operation publishing all products to a publication.

Show fields

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
AddAllProductsOperation.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to processedRowCount](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
AddAllProductsOperation.fields.processedRowCount)processedRowCount

•[Int](/docs/api/admin-graphql/latest/scalars/Int)

    

The count of processed rows, summing imported, failed, and skipped rows.

[Anchor to rowCount](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-AddAllProductsOperation.fields.rowCount)rowCount

•[RowCount](/docs/api/admin-graphql/latest/objects/RowCount)

    

Represents a rows objects within this background operation.

Show fields

[Anchor to status](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-AddAllProductsOperation.fields.status)status

•[ResourceOperationStatus!](/docs/api/admin-
graphql/latest/enums/ResourceOperationStatus)

non-null

    

The status of this operation.

Show enum values

[Anchor to AdditionalFee](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
AdditionalFee)[AdditionalFee](/docs/api/admin-
graphql/latest/objects/AdditionalFee)

•OBJECT

    

The additional fees that have been applied to the order.

Show fields

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
AdditionalFee.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to name](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-AdditionalFee.fields.name)name

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The name of the additional fee.

[Anchor to price](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-AdditionalFee.fields.price)price

•[MoneyBag!](/docs/api/admin-graphql/latest/objects/MoneyBag)

non-null

    

The price of the additional fee.

Show fields

[Anchor to taxLines](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-AdditionalFee.fields.taxLines)taxLines

•[[TaxLine!]!](/docs/api/admin-graphql/latest/objects/TaxLine)

non-null

    

A list of taxes charged on the additional fee.

Show fields

[Anchor to App](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
App)[App](/docs/api/admin-graphql/latest/objects/App)

•OBJECT

    

A Shopify application.

Show fields

[Anchor to apiKey](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-App.fields.apiKey)apiKey

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

A unique application API identifier.

[Anchor to appStoreAppUrl](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
App.fields.appStoreAppUrl)appStoreAppUrl

•[URL](/docs/api/admin-graphql/latest/scalars/URL)

    

App store page URL of the app.

[Anchor to appStoreDeveloperUrl](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
App.fields.appStoreDeveloperUrl)appStoreDeveloperUrl

•[URL](/docs/api/admin-graphql/latest/scalars/URL)

    

App store page URL of the developer who created the app.

[Anchor to availableAccessScopes](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
App.fields.availableAccessScopes)availableAccessScopes

•[[AccessScope!]!](/docs/api/admin-graphql/latest/objects/AccessScope)

non-null

    

All requestable access scopes available to the app.

Show fields

[Anchor to banner](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-App.fields.banner)banner

•[Image!](/docs/api/admin-graphql/latest/objects/Image)

non-null

    

Banner image for the app.

Show fields

[Anchor to description](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
App.fields.description)description

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

Description of the app.

[Anchor to developerName](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
App.fields.developerName)developerName

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The name of the app developer.

[Anchor to developerType](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
App.fields.developerType)developerType

•[AppDeveloperType!](/docs/api/admin-graphql/latest/enums/AppDeveloperType)

non-null

    

The type of app developer.

Show enum values

[Anchor to embedded](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-App.fields.embedded)embedded

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether the app uses the Embedded App SDK.

[Anchor to failedRequirements](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
App.fields.failedRequirements)failedRequirements

•[[FailedRequirement!]!](/docs/api/admin-
graphql/latest/objects/FailedRequirement)

non-null

    

Requirements that must be met before the app can be installed.

Show fields

[Anchor to features](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-App.fields.features)features

•[[String!]!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

A list of app features that are shown in the Shopify App Store listing.

[Anchor to feedback](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-App.fields.feedback)feedback

•[AppFeedback](/docs/api/admin-graphql/latest/objects/AppFeedback)

    

Feedback from this app about the store.

Show fields

[Anchor to handle](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-App.fields.handle)handle

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

Handle of the app.

[Anchor to icon](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-App.fields.icon)icon

•[Image!](/docs/api/admin-graphql/latest/objects/Image)

non-null

    

Icon that represents the app.

Show fields

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
App.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to installation](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
App.fields.installation)installation

•[AppInstallation](/docs/api/admin-graphql/latest/objects/AppInstallation)

    

Corresponding AppInstallation for this shop and App. Returns null if the App
is not installed.

Show fields

[Anchor to installUrl](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-App.fields.installUrl)installUrl

•[URL](/docs/api/admin-graphql/latest/scalars/URL)

    

Webpage where you can install the app, if app requires explicit user
permission.

[Anchor to isPostPurchaseAppInUse](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
App.fields.isPostPurchaseAppInUse)isPostPurchaseAppInUse

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether the app is the [post purchase](https://shopify.dev/apps/checkout/post-
purchase) app in use.

[Anchor to optionalAccessScopes](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
App.fields.optionalAccessScopes)optionalAccessScopes

•[[AccessScope!]!](/docs/api/admin-graphql/latest/objects/AccessScope)

non-null

    

The optional scopes requested by the app. Lists the optional access scopes the
app has declared in its configuration. These scopes are optionally requested
by the app after installation.

Show fields

[Anchor to previouslyInstalled](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
App.fields.previouslyInstalled)previouslyInstalled

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether the app was previously installed on the current shop.

[Anchor to pricingDetails](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
App.fields.pricingDetails)pricingDetails

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

Detailed information about the app pricing.

[Anchor to pricingDetailsSummary](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
App.fields.pricingDetailsSummary)pricingDetailsSummary

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

Summary of the app pricing details.

[Anchor to privacyPolicyUrl](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
App.fields.privacyPolicyUrl)privacyPolicyUrl

•[URL](/docs/api/admin-graphql/latest/scalars/URL)

    

Link to app privacy policy.

[Anchor to publicCategory](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
App.fields.publicCategory)publicCategory

•[AppPublicCategory!](/docs/api/admin-graphql/latest/enums/AppPublicCategory)

non-null

    

The public category for the app.

Show enum values

[Anchor to published](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-App.fields.published)published

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether the app is published to the Shopify App Store.

[Anchor to requestedAccessScopes](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
App.fields.requestedAccessScopes)requestedAccessScopes

•[[AccessScope!]!](/docs/api/admin-graphql/latest/objects/AccessScope)

non-null

    

The access scopes requested by the app. Lists the access scopes the app has
declared in its configuration. Merchant must grant approval to these scopes
for the app to be installed.

Show fields

[Anchor to screenshots](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
App.fields.screenshots)screenshots

•[[Image!]!](/docs/api/admin-graphql/latest/objects/Image)

non-null

    

Screenshots of the app.

Show fields

[Anchor to shopifyDeveloped](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
App.fields.shopifyDeveloped)shopifyDeveloped

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether the app was developed by Shopify.

[Anchor to title](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-App.fields.title)title

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

Name of the app.

[Anchor to uninstallMessage](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
App.fields.uninstallMessage)uninstallMessage

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

Message that appears when the app is uninstalled. For example: By removing
this app, you will no longer be able to publish products to MySocialSite or
view this app in your Shopify admin. You can re-enable this channel at any
time.

[Anchor to webhookApiVersion](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
App.fields.webhookApiVersion)webhookApiVersion

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The webhook API version for the app.

[Anchor to developerUrl](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
App.fields.developerUrl)developerUrl

•[URL!](/docs/api/admin-graphql/latest/scalars/URL)

non-nullDeprecated

    

[Anchor to launchUrl](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-App.fields.launchUrl)launchUrl

•[URL!](/docs/api/admin-graphql/latest/scalars/URL)

non-nullDeprecated

    

[Anchor to navigationItems](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
App.fields.navigationItems)navigationItems

•[[NavigationItem!]!](/docs/api/admin-graphql/latest/objects/NavigationItem)

non-nullDeprecated

    

Show fields

[Anchor to uninstallUrl](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
App.fields.uninstallUrl)uninstallUrl

•[URL](/docs/api/admin-graphql/latest/scalars/URL)

Deprecated

    

[Anchor to AppCatalog](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
AppCatalog)[AppCatalog](/docs/api/admin-graphql/latest/objects/AppCatalog)

•OBJECT

    

A catalog that defines the publication associated with an app.

Show fields

[Anchor to apps](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-AppCatalog.fields.apps)apps

•[AppConnection!](/docs/api/admin-graphql/latest/connections/AppConnection)

non-null

    

The apps associated with the catalog.

Show fields

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
AppCatalog.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to operations](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
AppCatalog.fields.operations)operations

•[[ResourceOperation!]!](/docs/api/admin-
graphql/latest/interfaces/ResourceOperation)

non-null

    

Most recent catalog operations.

Show fields

[Anchor to priceList](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-AppCatalog.fields.priceList)priceList

•[PriceList](/docs/api/admin-graphql/latest/objects/PriceList)

    

The price list associated with the catalog.

Show fields

[Anchor to publication](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
AppCatalog.fields.publication)publication

•[Publication](/docs/api/admin-graphql/latest/objects/Publication)

    

A group of products and collections that's published to a catalog.

Show fields

[Anchor to status](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-AppCatalog.fields.status)status

•[CatalogStatus!](/docs/api/admin-graphql/latest/enums/CatalogStatus)

non-null

    

The status of the catalog.

Show enum values

[Anchor to title](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-AppCatalog.fields.title)title

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The name of the catalog.

[Anchor to AppCredit](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-AppCredit)[AppCredit](/docs/api/admin-graphql/latest/objects/AppCredit)

•OBJECT

    

Represents monetary credits that merchants can apply toward future app
purchases, subscriptions, or usage-based billing within their Shopify store.
App credits provide a flexible way to offer refunds, promotional credits, or
compensation without processing external payments.

For example, if a merchant experiences service downtime, an app might issue
credits equivalent to the affected billing period. These credits can apply to
future charges, reducing the merchant's next invoice or extending their
subscription period.

Use the `AppCredit` object to:

  * Issue refunds for service interruptions or billing disputes
  * Provide promotional credits for new merchant onboarding
  * Compensate merchants for app-related issues or downtime
  * Create loyalty rewards or referral bonuses within your billing system
  * Track credit balances and application history for accounting purposes

For comprehensive billing strategies and credit management patterns, see the
[subscription billing
guide](https://shopify.dev/docs/apps/launch/billing/subscription-billing).

Show fields

[Anchor to amount](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-AppCredit.fields.amount)amount

•[MoneyV2!](/docs/api/admin-graphql/latest/objects/MoneyV2)

non-null

    

The amount that can be used towards future app purchases in Shopify.

Show fields

[Anchor to createdAt](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-AppCredit.fields.createdAt)createdAt

•[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime)

non-null

    

The date and time when the app credit was created.

[Anchor to description](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
AppCredit.fields.description)description

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The description of the app credit.

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
AppCredit.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to test](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-AppCredit.fields.test)test

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether the app credit is a test transaction.

[Anchor to AppInstallation](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
AppInstallation)[AppInstallation](/docs/api/admin-
graphql/latest/objects/AppInstallation)

•OBJECT

    

Represents an installed application on a shop.

Show fields

[Anchor to accessScopes](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
AppInstallation.fields.accessScopes)accessScopes

•[[AccessScope!]!](/docs/api/admin-graphql/latest/objects/AccessScope)

non-null

    

The access scopes granted to the application by a merchant during
installation.

Show fields

[Anchor to activeSubscriptions](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
AppInstallation.fields.activeSubscriptions)activeSubscriptions

•[[AppSubscription!]!](/docs/api/admin-graphql/latest/objects/AppSubscription)

non-null

    

The active application subscriptions billed to the shop on a recurring basis.

Show fields

[Anchor to allSubscriptions](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
AppInstallation.fields.allSubscriptions)allSubscriptions

•[AppSubscriptionConnection!](/docs/api/admin-
graphql/latest/connections/AppSubscriptionConnection)

non-null

    

All subscriptions created for a shop.

Show fields

[Anchor to app](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
AppInstallation.fields.app)app

•[App!](/docs/api/admin-graphql/latest/objects/App)

non-null

    

Application which is installed.

Show fields

[Anchor to credits](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-AppInstallation.fields.credits)credits

•[AppCreditConnection!](/docs/api/admin-
graphql/latest/connections/AppCreditConnection)

non-null

    

Credits that can be used towards future app purchases.

Show fields

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
AppInstallation.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to launchUrl](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-AppInstallation.fields.launchUrl)launchUrl

•[URL!](/docs/api/admin-graphql/latest/scalars/URL)

non-null

    

The URL to launch the application.

[Anchor to metafield](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-AppInstallation.fields.metafield)metafield

•[Metafield](/docs/api/admin-graphql/latest/objects/Metafield)

    

A [custom field](https://shopify.dev/docs/apps/build/custom-data), including
its `namespace` and `key`, that's associated with a Shopify resource for the
purposes of adding and storing additional information.

Show fields

[Anchor to metafields](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
AppInstallation.fields.metafields)metafields

•[MetafieldConnection!](/docs/api/admin-
graphql/latest/connections/MetafieldConnection)

non-null

    

A list of [custom fields](https://shopify.dev/docs/apps/build/custom-data)
that a merchant associates with a Shopify resource.

Show fields

[Anchor to oneTimePurchases](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
AppInstallation.fields.oneTimePurchases)oneTimePurchases

•[AppPurchaseOneTimeConnection!](/docs/api/admin-
graphql/latest/connections/AppPurchaseOneTimeConnection)

non-null

    

One-time purchases to a shop.

Show fields

[Anchor to publication](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
AppInstallation.fields.publication)publication

•[Publication](/docs/api/admin-graphql/latest/objects/Publication)

    

The publication associated with the installed application.

Show fields

[Anchor to revenueAttributionRecords](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
AppInstallation.fields.revenueAttributionRecords)revenueAttributionRecords

•[AppRevenueAttributionRecordConnection!](/docs/api/admin-
graphql/latest/connections/AppRevenueAttributionRecordConnection)

non-null

    

The records that track the externally-captured revenue for the app. The
records are used for revenue attribution purposes.

Show fields

[Anchor to uninstallUrl](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
AppInstallation.fields.uninstallUrl)uninstallUrl

•[URL](/docs/api/admin-graphql/latest/scalars/URL)

    

The URL to uninstall the application.

[Anchor to channel](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-AppInstallation.fields.channel)channel

•[Channel](/docs/api/admin-graphql/latest/objects/Channel)

Deprecated

    

Show fields

[Anchor to subscriptions](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
AppInstallation.fields.subscriptions)subscriptions

•[[AppSubscription!]!](/docs/api/admin-graphql/latest/objects/AppSubscription)

non-nullDeprecated

    

Show fields

[Anchor to AppPurchaseOneTime](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
AppPurchaseOneTime)[AppPurchaseOneTime](/docs/api/admin-
graphql/latest/objects/AppPurchaseOneTime)

•OBJECT

    

Represents a one-time purchase of app services or features by a merchant,
tracking the transaction details and status throughout the billing lifecycle.
This object captures essential information about non-recurring charges,
including price and merchant acceptance status.

One-time purchases are particularly valuable for apps offering premium
features, professional services, or digital products that don't require
ongoing subscriptions. For instance, a photography app might sell premium
filters as one-time purchases, while a marketing app could charge for
individual campaign setups or advanced analytics reports.

Use the `AppPurchaseOneTime` object to:

  * Track the status of individual feature purchases and service charges
  * Track payment status for premium content or digital products
  * Access purchase details to enable or disable features based on payment status

The purchase status indicates whether the charge is pending merchant approval,
has been accepted and processed, or was declined. This status tracking is
crucial for apps that need to conditionally enable features based on
successful payment completion.

Purchase records include creation timestamps, pricing details, and test flags
to distinguish between production charges and development testing. The test
flag ensures that development and staging environments don't generate actual
charges while maintaining realistic billing flow testing.

For detailed implementation patterns and billing best practices, see the [one-
time-charges page](https://shopify.dev/docs/apps/launch/billing/one-time-
charges).

Show fields

[Anchor to createdAt](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-AppPurchaseOneTime.fields.createdAt)createdAt

•[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime)

non-null

    

The date and time when the app purchase occurred.

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
AppPurchaseOneTime.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to name](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-AppPurchaseOneTime.fields.name)name

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The name of the app purchase.

[Anchor to price](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-AppPurchaseOneTime.fields.price)price

•[MoneyV2!](/docs/api/admin-graphql/latest/objects/MoneyV2)

non-null

    

The amount to be charged to the store for the app purchase.

Show fields

[Anchor to status](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-AppPurchaseOneTime.fields.status)status

•[AppPurchaseStatus!](/docs/api/admin-graphql/latest/enums/AppPurchaseStatus)

non-null

    

The status of the app purchase.

Show enum values

[Anchor to test](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-AppPurchaseOneTime.fields.test)test

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether the app purchase is a test transaction.

[Anchor to AppRevenueAttributionRecord](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
AppRevenueAttributionRecord)[AppRevenueAttributionRecord](/docs/api/admin-
graphql/latest/objects/AppRevenueAttributionRecord)

•OBJECT

    

Tracks revenue that was captured outside of Shopify's billing system but needs
to be attributed to the app for comprehensive revenue reporting and partner
analytics. This object enables accurate revenue tracking when apps process
payments through external systems while maintaining visibility into total app
performance.

External revenue attribution is essential for apps that offer multiple payment
channels or process certain transactions outside Shopify's billing
infrastructure. For example, an enterprise app might process large custom
contracts through external payment processors, or a marketplace app could
handle direct merchant-to-merchant transactions that still generate app
commissions.

Use the `AppRevenueAttributionRecord` object to:

  * Report revenue from external payment processors and billing systems
  * Track commission-based earnings from marketplace or referral activities
  * Maintain comprehensive revenue analytics across multiple payment channels
  * Ensure accurate partner revenue sharing and commission calculations
  * Generate complete financial reports that include all app-generated revenue streams
  * Support compliance requirements for external revenue documentation

Each attribution record includes the captured amount, external transaction
timestamp, and idempotency keys to prevent duplicate reporting. The record
type field categorizes different revenue streams, enabling detailed analytics
and reporting segmentation.

Revenue attribution records are particularly important for apps participating
in Shopify's partner program, as they ensure accurate revenue sharing
calculations and comprehensive performance metrics. The captured timestamp
reflects when the external payment was processed, not when the attribution
record was created in Shopify.

For detailed revenue attribution values, see the [AppRevenueAttributionType
enum](https://shopify.dev/docs/api/admin-
graphql/latest/enums/AppRevenueAttributionType).

Show fields

[Anchor to amount](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-AppRevenueAttributionRecord.fields.amount)amount

•[MoneyV2!](/docs/api/admin-graphql/latest/objects/MoneyV2)

non-null

    

The financial amount captured in this attribution.

Show fields

[Anchor to capturedAt](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
AppRevenueAttributionRecord.fields.capturedAt)capturedAt

•[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime)

non-null

    

The timestamp when the financial amount was captured.

[Anchor to createdAt](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-AppRevenueAttributionRecord.fields.createdAt)createdAt

•[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime)

non-null

    

The timestamp at which this revenue attribution was issued.

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
AppRevenueAttributionRecord.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to idempotencyKey](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
AppRevenueAttributionRecord.fields.idempotencyKey)idempotencyKey

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The unique value submitted during the creation of the app revenue attribution
record. For more information, refer to [Idempotent
requests](https://shopify.dev/api/usage/idempotent-requests).

[Anchor to test](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-AppRevenueAttributionRecord.fields.test)test

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Indicates whether this is a test submission.

[Anchor to type](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-AppRevenueAttributionRecord.fields.type)type

•[AppRevenueAttributionType!](/docs/api/admin-
graphql/latest/enums/AppRevenueAttributionType)

non-null

    

The type of revenue attribution.

Show enum values

[Anchor to AppSubscription](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
AppSubscription)[AppSubscription](/docs/api/admin-
graphql/latest/objects/AppSubscription)

•OBJECT

    

Provides users access to services and/or features for a duration of time.

Show fields

[Anchor to createdAt](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-AppSubscription.fields.createdAt)createdAt

•[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime)

non-null

    

The date and time when the app subscription was created.

[Anchor to currentPeriodEnd](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
AppSubscription.fields.currentPeriodEnd)currentPeriodEnd

•[DateTime](/docs/api/admin-graphql/latest/scalars/DateTime)

    

The date and time when the current app subscription period ends. Returns
`null` if the subscription isn't active.

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
AppSubscription.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to lineItems](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-AppSubscription.fields.lineItems)lineItems

•[[AppSubscriptionLineItem!]!](/docs/api/admin-
graphql/latest/objects/AppSubscriptionLineItem)

non-null

    

The plans attached to the app subscription.

Show fields

[Anchor to name](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-AppSubscription.fields.name)name

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The name of the app subscription.

[Anchor to returnUrl](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-AppSubscription.fields.returnUrl)returnUrl

•[URL!](/docs/api/admin-graphql/latest/scalars/URL)

non-null

    

The URL that the merchant is redirected to after approving the app
subscription.

[Anchor to status](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-AppSubscription.fields.status)status

•[AppSubscriptionStatus!](/docs/api/admin-
graphql/latest/enums/AppSubscriptionStatus)

non-null

    

The status of the app subscription.

Show enum values

[Anchor to test](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-AppSubscription.fields.test)test

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Specifies whether the app subscription is a test transaction.

[Anchor to trialDays](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-AppSubscription.fields.trialDays)trialDays

•[Int!](/docs/api/admin-graphql/latest/scalars/Int)

non-null

    

The number of free trial days, starting at the subscription's creation date,
by which billing is delayed.

[Anchor to AppUsageRecord](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
AppUsageRecord)[AppUsageRecord](/docs/api/admin-
graphql/latest/objects/AppUsageRecord)

•OBJECT

    

Store usage for app subscriptions with usage pricing.

Show fields

[Anchor to createdAt](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-AppUsageRecord.fields.createdAt)createdAt

•[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime)

non-null

    

The date and time when the usage record was created.

[Anchor to description](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
AppUsageRecord.fields.description)description

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The description of the app usage record.

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
AppUsageRecord.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to idempotencyKey](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
AppUsageRecord.fields.idempotencyKey)idempotencyKey

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

A unique key generated by the client to avoid duplicate charges.

[Anchor to price](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-AppUsageRecord.fields.price)price

•[MoneyV2!](/docs/api/admin-graphql/latest/objects/MoneyV2)

non-null

    

The price of the usage record.

Show fields

[Anchor to subscriptionLineItem](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
AppUsageRecord.fields.subscriptionLineItem)subscriptionLineItem

•[AppSubscriptionLineItem!](/docs/api/admin-
graphql/latest/objects/AppSubscriptionLineItem)

non-null

    

Defines the usage pricing plan the merchant is subscribed to.

Show fields

[Anchor to Article](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Article)[Article](/docs/api/admin-graphql/latest/objects/Article)

•OBJECT

    

An article in the blogging system.

Show fields

[Anchor to author](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Article.fields.author)author

•[ArticleAuthor](/docs/api/admin-graphql/latest/objects/ArticleAuthor)

    

The name of the author of the article.

Show fields

[Anchor to blog](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Article.fields.blog)blog

•[Blog!](/docs/api/admin-graphql/latest/objects/Blog)

non-null

    

The blog containing the article.

Show fields

[Anchor to body](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Article.fields.body)body

•[HTML!](/docs/api/admin-graphql/latest/scalars/HTML)

non-null

    

The text of the article's body, complete with HTML markup.

[Anchor to comments](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Article.fields.comments)comments

•[CommentConnection!](/docs/api/admin-
graphql/latest/connections/CommentConnection)

non-null

    

List of the article's comments.

Show fields

[Anchor to commentsCount](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Article.fields.commentsCount)commentsCount

•[Count](/docs/api/admin-graphql/latest/objects/Count)

    

Count of comments. Limited to a maximum of 10000 by default.

Show fields

[Anchor to createdAt](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Article.fields.createdAt)createdAt

•[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime)

non-null

    

The date and time (ISO 8601 format) when the article was created.

[Anchor to defaultCursor](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Article.fields.defaultCursor)defaultCursor

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

A default [cursor](https://shopify.dev/api/usage/pagination-graphql) that
returns the single next record, sorted ascending by ID.

[Anchor to events](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Article.fields.events)events

•[EventConnection!](/docs/api/admin-
graphql/latest/connections/EventConnection)

non-null

    

The paginated list of events associated with the host subject.

Show fields

[Anchor to handle](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Article.fields.handle)handle

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

A unique, human-friendly string for the article that's automatically generated
from the article's title. The handle is used in the article's URL.

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
Article.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to image](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Article.fields.image)image

•[Image](/docs/api/admin-graphql/latest/objects/Image)

    

The image associated with the article.

Show fields

[Anchor to isPublished](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Article.fields.isPublished)isPublished

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether or not the article is visible.

[Anchor to metafield](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Article.fields.metafield)metafield

•[Metafield](/docs/api/admin-graphql/latest/objects/Metafield)

    

A [custom field](https://shopify.dev/docs/apps/build/custom-data), including
its `namespace` and `key`, that's associated with a Shopify resource for the
purposes of adding and storing additional information.

Show fields

[Anchor to metafields](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Article.fields.metafields)metafields

•[MetafieldConnection!](/docs/api/admin-
graphql/latest/connections/MetafieldConnection)

non-null

    

A list of [custom fields](https://shopify.dev/docs/apps/build/custom-data)
that a merchant associates with a Shopify resource.

Show fields

[Anchor to publishedAt](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Article.fields.publishedAt)publishedAt

•[DateTime](/docs/api/admin-graphql/latest/scalars/DateTime)

    

The date and time (ISO 8601 format) when the article became or will become
visible. Returns null when the article isn't visible.

[Anchor to summary](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Article.fields.summary)summary

•[HTML](/docs/api/admin-graphql/latest/scalars/HTML)

    

A summary of the article, which can include HTML markup. The summary is used
by the online store theme to display the article on other pages, such as the
home page or the main blog page.

[Anchor to tags](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Article.fields.tags)tags

•[[String!]!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

A comma-separated list of tags. Tags are additional short descriptors
formatted as a string of comma-separated values.

[Anchor to templateSuffix](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Article.fields.templateSuffix)templateSuffix

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The name of the template an article is using if it's using an alternate
template. If an article is using the default `article.liquid` template, then
the value returned is `null`.

[Anchor to title](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Article.fields.title)title

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The title of the article.

[Anchor to translations](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Article.fields.translations)translations

•[[Translation!]!](/docs/api/admin-graphql/latest/objects/Translation)

non-null

    

The published translations associated with the resource.

Show fields

[Anchor to updatedAt](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Article.fields.updatedAt)updatedAt

•[DateTime](/docs/api/admin-graphql/latest/scalars/DateTime)

    

The date and time (ISO 8601 format) when the article was last updated.

[Anchor to metafieldDefinitions](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Article.fields.metafieldDefinitions)metafieldDefinitions

•[MetafieldDefinitionConnection!](/docs/api/admin-
graphql/latest/connections/MetafieldDefinitionConnection)

non-nullDeprecated

    

Show fields

[Anchor to BasicEvent](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
BasicEvent)[BasicEvent](/docs/api/admin-graphql/latest/objects/BasicEvent)

•OBJECT

    

Basic events chronicle resource activities such as the creation of an article,
the fulfillment of an order, or the addition of a product.

### General events

Action| Description  
---|---  
`create`| The item was created.  
`destroy`| The item was destroyed.  
`published`| The item was published.  
`unpublished`| The item was unpublished.  
`update`| The item was updated.  
  
### Order events

Order events can be divided into the following categories:

  * _Authorization_ : Includes whether the authorization succeeded, failed, or is pending.
  * _Capture_ : Includes whether the capture succeeded, failed, or is pending.
  * _Email_ : Includes confirmation or cancellation of the order, as well as shipping.
  * _Fulfillment_ : Includes whether the fulfillment succeeded, failed, or is pending. Also includes cancellation, restocking, and fulfillment updates.
  * _Order_ : Includess the placement, confirmation, closing, re-opening, and cancellation of the order.
  * _Refund_ : Includes whether the refund succeeded, failed, or is pending.
  * _Sale_ : Includes whether the sale succeeded, failed, or is pending.
  * _Void_ : Includes whether the void succeeded, failed, or is pending.

Action| Message| Description  
---|---|---  
`authorization_failure`| The customer, unsuccessfully, tried to authorize:
`{money_amount}`.| Authorization failed. The funds cannot be captured.  
`authorization_pending`| Authorization for `{money_amount}` is pending.|
Authorization pending.  
`authorization_success`| The customer successfully authorized us to capture:
`{money_amount}`.| Authorization was successful and the funds are available
for capture.  
`cancelled`| Order was cancelled by `{shop_staff_name}`.| The order was
cancelled.  
`capture_failure`| We failed to capture: `{money_amount}`.| The capture
failed. The funds cannot be transferred to the shop.  
`capture_pending`| Capture for `{money_amount}` is pending.| The capture is in
process. The funds are not yet available to the shop.  
`capture_success`| We successfully captured: `{money_amount}`| The capture was
successful and the funds are now available to the shop.  
`closed`| Order was closed.| The order was closed.  
`confirmed`| Received a new order: `{order_number}` by `{customer_name}`.| The
order was confirmed.  
`fulfillment_cancelled`| We cancelled `{number_of_line_items}` from being
fulfilled by the third party fulfillment service.| Fulfillment for one or more
of the line_items failed.  
`fulfillment_pending`| We submitted `{number_of_line_items}` to the third
party service.| One or more of the line_items has been assigned to a third
party service for fulfillment.  
`fulfillment_success`| We successfully fulfilled line_items.| Fulfillment was
successful for one or more line_items.  
`mail_sent`| `{message_type}` email was sent to the customer.| An email was
sent to the customer.  
`placed`| Order was placed.| An order was placed by the customer.  
`re_opened`| Order was re-opened.| An order was re-opened.  
`refund_failure`| We failed to refund `{money_amount}`.| The refund failed.
The funds are still with the shop.  
`refund_pending`| Refund of `{money_amount}` is still pending.| The refund is
in process. The funds are still with shop.  
`refund_success`| We successfully refunded `{money_amount}`.| The refund was
successful. The funds have been transferred to the customer.  
`restock_line_items`| We restocked `{number_of_line_items}`.| One or more of
the order's line items have been restocked.  
`sale_failure`| The customer failed to pay `{money_amount}`.| The sale failed.
The funds are not available to the shop.  
`sale_pending`| The `{money_amount}` is pending.| The sale is in process. The
funds are not yet available to the shop.  
`sale_success`| We successfully captured `{money_amount}`.| The sale was
successful. The funds are now with the shop.  
`update`| `{order_number}` was updated.| The order was updated.  
`void_failure`| We failed to void the authorization.| Voiding the
authorization failed. The authorization is still valid.  
`void_pending`| Authorization void is pending.| Voiding the authorization is
in process. The authorization is still valid.  
`void_success`| We successfully voided the authorization.| Voiding the
authorization was successful. The authorization is no longer valid.  
  
Show fields

[Anchor to action](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-BasicEvent.fields.action)action

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The action that occured.

[Anchor to additionalContent](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
BasicEvent.fields.additionalContent)additionalContent

•[JSON](/docs/api/admin-graphql/latest/scalars/JSON)

    

Provides additional content for collapsible timeline events.

[Anchor to additionalData](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
BasicEvent.fields.additionalData)additionalData

•[JSON](/docs/api/admin-graphql/latest/scalars/JSON)

    

Provides additional data for event consumers.

[Anchor to appTitle](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-BasicEvent.fields.appTitle)appTitle

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The name of the app that created the event.

[Anchor to arguments](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-BasicEvent.fields.arguments)arguments

•[JSON](/docs/api/admin-graphql/latest/scalars/JSON)

    

Refers to a certain event and its resources.

[Anchor to attributeToApp](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
BasicEvent.fields.attributeToApp)attributeToApp

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether the event was created by an app.

[Anchor to attributeToUser](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
BasicEvent.fields.attributeToUser)attributeToUser

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether the event was caused by an admin user.

[Anchor to author](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-BasicEvent.fields.author)author

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The entity which performed the action that generated the event.

[Anchor to createdAt](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-BasicEvent.fields.createdAt)createdAt

•[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime)

non-null

    

The date and time when the event was created.

[Anchor to criticalAlert](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
BasicEvent.fields.criticalAlert)criticalAlert

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether the event is critical.

[Anchor to hasAdditionalContent](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
BasicEvent.fields.hasAdditionalContent)hasAdditionalContent

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether this event has additional content.

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
BasicEvent.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to message](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-BasicEvent.fields.message)message

•[FormattedString!](/docs/api/admin-graphql/latest/scalars/FormattedString)

non-null

    

Human readable text that describes the event.

[Anchor to secondaryMessage](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
BasicEvent.fields.secondaryMessage)secondaryMessage

•[FormattedString](/docs/api/admin-graphql/latest/scalars/FormattedString)

    

Human readable text that supports the event message.

[Anchor to subject](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-BasicEvent.fields.subject)subject

•[HasEvents](/docs/api/admin-graphql/latest/interfaces/HasEvents)

    

The resource that generated the event. To see a list of possible types, refer
to [HasEvents](https://shopify.dev/docs/api/admin-
graphql/unstable/interfaces/HasEvents#implemented-in).

Show fields

[Anchor to subjectId](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-BasicEvent.fields.subjectId)subjectId

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

The ID of the resource that generated the event.

[Anchor to subjectType](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
BasicEvent.fields.subjectType)subjectType

•[EventSubjectType!](/docs/api/admin-graphql/latest/enums/EventSubjectType)

non-null

    

The type of the resource that generated the event.

Show enum values

[Anchor to Blog](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Blog)[Blog](/docs/api/admin-graphql/latest/objects/Blog)

•OBJECT

    

Shopify stores come with a built-in blogging engine, allowing a shop to have
one or more blogs. Blogs are meant to be used as a type of magazine or
newsletter for the shop, with content that changes over time.

Show fields

[Anchor to articles](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Blog.fields.articles)articles

•[ArticleConnection!](/docs/api/admin-
graphql/latest/connections/ArticleConnection)

non-null

    

List of the blog's articles.

Show fields

[Anchor to articlesCount](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Blog.fields.articlesCount)articlesCount

•[Count](/docs/api/admin-graphql/latest/objects/Count)

    

Count of articles. Limited to a maximum of 10000 by default.

Show fields

[Anchor to commentPolicy](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Blog.fields.commentPolicy)commentPolicy

•[CommentPolicy!](/docs/api/admin-graphql/latest/enums/CommentPolicy)

non-null

    

Indicates whether readers can post comments to the blog and if comments are
moderated or not.

Show enum values

[Anchor to createdAt](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Blog.fields.createdAt)createdAt

•[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime)

non-null

    

The date and time when the blog was created.

[Anchor to events](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Blog.fields.events)events

•[EventConnection!](/docs/api/admin-
graphql/latest/connections/EventConnection)

non-null

    

The paginated list of events associated with the host subject.

Show fields

[Anchor to feed](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Blog.fields.feed)feed

•[BlogFeed](/docs/api/admin-graphql/latest/objects/BlogFeed)

    

FeedBurner provider details. Any blogs that aren't already integrated with
FeedBurner can't use the service.

Show fields

[Anchor to handle](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Blog.fields.handle)handle

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

A unique, human-friendly string for the blog. If no handle is specified, a
handle will be generated automatically from the blog title. The handle is
customizable and is used by the Liquid templating language to refer to the
blog.

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
Blog.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to metafield](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Blog.fields.metafield)metafield

•[Metafield](/docs/api/admin-graphql/latest/objects/Metafield)

    

A [custom field](https://shopify.dev/docs/apps/build/custom-data), including
its `namespace` and `key`, that's associated with a Shopify resource for the
purposes of adding and storing additional information.

Show fields

[Anchor to metafields](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Blog.fields.metafields)metafields

•[MetafieldConnection!](/docs/api/admin-
graphql/latest/connections/MetafieldConnection)

non-null

    

A list of [custom fields](https://shopify.dev/docs/apps/build/custom-data)
that a merchant associates with a Shopify resource.

Show fields

[Anchor to tags](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Blog.fields.tags)tags

•[[String!]!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

A list of tags associated with the 200 most recent blog articles.

[Anchor to templateSuffix](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Blog.fields.templateSuffix)templateSuffix

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The name of the template a blog is using if it's using an alternate template.
Returns `null` if a blog is using the default blog.liquid template.

[Anchor to title](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Blog.fields.title)title

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The title of the blog.

[Anchor to translations](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Blog.fields.translations)translations

•[[Translation!]!](/docs/api/admin-graphql/latest/objects/Translation)

non-null

    

The published translations associated with the resource.

Show fields

[Anchor to updatedAt](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Blog.fields.updatedAt)updatedAt

•[DateTime](/docs/api/admin-graphql/latest/scalars/DateTime)

    

The date and time when the blog was update.

[Anchor to metafieldDefinitions](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Blog.fields.metafieldDefinitions)metafieldDefinitions

•[MetafieldDefinitionConnection!](/docs/api/admin-
graphql/latest/connections/MetafieldDefinitionConnection)

non-nullDeprecated

    

Show fields

[Anchor to BulkOperation](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
BulkOperation)[BulkOperation](/docs/api/admin-
graphql/latest/objects/BulkOperation)

•OBJECT

    

An asynchronous long-running operation to fetch data in bulk or to bulk import
data.

Bulk operations are created using the `bulkOperationRunQuery` or
`bulkOperationRunMutation` mutation. After they are created, clients should
poll the `status` field for updates. When `COMPLETED`, the `url` field
contains a link to the data in [JSONL](http://jsonlines.org/) format.

Refer to the [bulk operations guide](https://shopify.dev/api/usage/bulk-
operations/imports) for more details.

Show fields

[Anchor to completedAt](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
BulkOperation.fields.completedAt)completedAt

•[DateTime](/docs/api/admin-graphql/latest/scalars/DateTime)

    

When the bulk operation was successfully completed.

[Anchor to createdAt](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-BulkOperation.fields.createdAt)createdAt

•[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime)

non-null

    

When the bulk operation was created.

[Anchor to errorCode](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-BulkOperation.fields.errorCode)errorCode

•[BulkOperationErrorCode](/docs/api/admin-
graphql/latest/enums/BulkOperationErrorCode)

    

Error code for failed operations.

Show enum values

[Anchor to fileSize](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-BulkOperation.fields.fileSize)fileSize

•[UnsignedInt64](/docs/api/admin-graphql/latest/scalars/UnsignedInt64)

    

File size in bytes of the file in the `url` field.

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
BulkOperation.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to objectCount](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
BulkOperation.fields.objectCount)objectCount

•[UnsignedInt64!](/docs/api/admin-graphql/latest/scalars/UnsignedInt64)

non-null

    

A running count of all the objects processed. For example, when fetching all
the products and their variants, this field counts both products and variants.
This field can be used to track operation progress.

[Anchor to partialDataUrl](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
BulkOperation.fields.partialDataUrl)partialDataUrl

•[URL](/docs/api/admin-graphql/latest/scalars/URL)

    

The URL that points to the partial or incomplete response data (in
[JSONL](http://jsonlines.org/) format) that was returned by a failed
operation. The URL expires 7 days after the operation fails. Returns `null`
when there's no data available.

[Anchor to query](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-BulkOperation.fields.query)query

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

GraphQL query document specified in `bulkOperationRunQuery`.

[Anchor to rootObjectCount](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
BulkOperation.fields.rootObjectCount)rootObjectCount

•[UnsignedInt64!](/docs/api/admin-graphql/latest/scalars/UnsignedInt64)

non-null

    

A running count of all the objects that are processed at the root of the
query. For example, when fetching all the products and their variants, this
field only counts products. This field can be used to track operation
progress.

[Anchor to status](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-BulkOperation.fields.status)status

•[BulkOperationStatus!](/docs/api/admin-
graphql/latest/enums/BulkOperationStatus)

non-null

    

Status of the bulk operation.

Show enum values

[Anchor to type](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-BulkOperation.fields.type)type

•[BulkOperationType!](/docs/api/admin-graphql/latest/enums/BulkOperationType)

non-null

    

The bulk operation's type.

Show enum values

[Anchor to url](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
BulkOperation.fields.url)url

•[URL](/docs/api/admin-graphql/latest/scalars/URL)

    

The URL that points to the response data in [JSONL](http://jsonlines.org/)
format. The URL expires 7 days after the operation completes.

[Anchor to BusinessEntity](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
BusinessEntity)[BusinessEntity](/docs/api/admin-
graphql/latest/objects/BusinessEntity)

•OBJECT

    

Represents a merchant's Business Entity.

Show fields

[Anchor to address](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-BusinessEntity.fields.address)address

•[BusinessEntityAddress!](/docs/api/admin-
graphql/latest/objects/BusinessEntityAddress)

non-null

    

The address of the merchant's Business Entity.

Show fields

[Anchor to archived](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-BusinessEntity.fields.archived)archived

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether the Business Entity is archived from the shop.

[Anchor to companyName](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
BusinessEntity.fields.companyName)companyName

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The name of the company associated with the merchant's Business Entity.

[Anchor to displayName](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
BusinessEntity.fields.displayName)displayName

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The display name of the merchant's Business Entity.

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
BusinessEntity.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to primary](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-BusinessEntity.fields.primary)primary

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether it's the merchant's primary Business Entity.

[Anchor to shopifyPaymentsAccount](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
BusinessEntity.fields.shopifyPaymentsAccount)shopifyPaymentsAccount

•[ShopifyPaymentsAccount](/docs/api/admin-
graphql/latest/objects/ShopifyPaymentsAccount)

    

Shopify Payments account information, including balances and payouts.

Show fields

[Anchor to CalculatedOrder](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
CalculatedOrder)[CalculatedOrder](/docs/api/admin-
graphql/latest/objects/CalculatedOrder)

•OBJECT

    

An order with edits applied but not saved.

Show fields

[Anchor to addedDiscountApplications](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
CalculatedOrder.fields.addedDiscountApplications)addedDiscountApplications

•[CalculatedDiscountApplicationConnection!](/docs/api/admin-
graphql/latest/connections/CalculatedDiscountApplicationConnection)

non-null

    

Returns only the new discount applications being added to the order in the
current edit.

Show fields

[Anchor to addedLineItems](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
CalculatedOrder.fields.addedLineItems)addedLineItems

•[CalculatedLineItemConnection!](/docs/api/admin-
graphql/latest/connections/CalculatedLineItemConnection)

non-null

    

Returns only the new line items being added to the order during the current
edit.

Show fields

[Anchor to cartDiscountAmountSet](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
CalculatedOrder.fields.cartDiscountAmountSet)cartDiscountAmountSet

•[MoneyBag](/docs/api/admin-graphql/latest/objects/MoneyBag)

    

Amount of the order-level discount (doesn't contain any line item discounts)
in shop and presentment currencies.

Show fields

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
CalculatedOrder.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to lineItems](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-CalculatedOrder.fields.lineItems)lineItems

•[CalculatedLineItemConnection!](/docs/api/admin-
graphql/latest/connections/CalculatedLineItemConnection)

non-null

    

Returns all items on the order that existed before starting the edit. Will
include any changes that have been made. Will not include line items added
during the current edit.

Show fields

[Anchor to notificationPreviewHtml](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
CalculatedOrder.fields.notificationPreviewHtml)notificationPreviewHtml

•[HTML](/docs/api/admin-graphql/latest/scalars/HTML)

    

The HTML of the customer notification for the order edit.

[Anchor to notificationPreviewTitle](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
CalculatedOrder.fields.notificationPreviewTitle)notificationPreviewTitle

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The customer notification title.

[Anchor to originalOrder](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
CalculatedOrder.fields.originalOrder)originalOrder

•[Order!](/docs/api/admin-graphql/latest/objects/Order)

non-null

    

The order without any changes applied.

Show fields

[Anchor to shippingLines](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
CalculatedOrder.fields.shippingLines)shippingLines

•[[CalculatedShippingLine!]!](/docs/api/admin-
graphql/latest/objects/CalculatedShippingLine)

non-null

    

Returns the shipping lines on the order that existed before starting the edit.
Will include any changes that have been made as well as shipping lines added
during the current edit. Returns only the first 250 shipping lines.

Show fields

[Anchor to stagedChanges](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
CalculatedOrder.fields.stagedChanges)stagedChanges

•[OrderStagedChangeConnection!](/docs/api/admin-
graphql/latest/connections/OrderStagedChangeConnection)

non-null

    

List of changes made to the order during the current edit.

Show fields

[Anchor to subtotalLineItemsQuantity](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
CalculatedOrder.fields.subtotalLineItemsQuantity)subtotalLineItemsQuantity

•[Int!](/docs/api/admin-graphql/latest/scalars/Int)

non-null

    

The sum of the quantities for the line items that contribute to the order's
subtotal.

[Anchor to subtotalPriceSet](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
CalculatedOrder.fields.subtotalPriceSet)subtotalPriceSet

•[MoneyBag](/docs/api/admin-graphql/latest/objects/MoneyBag)

    

The subtotal of the line items, in shop and presentment currencies, after all
the discounts are applied. The subtotal doesn't include shipping. The subtotal
includes taxes for taxes-included orders and excludes taxes for taxes-excluded
orders.

Show fields

[Anchor to taxLines](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-CalculatedOrder.fields.taxLines)taxLines

•[[TaxLine!]!](/docs/api/admin-graphql/latest/objects/TaxLine)

non-null

    

Taxes charged for the line item.

Show fields

[Anchor to totalOutstandingSet](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
CalculatedOrder.fields.totalOutstandingSet)totalOutstandingSet

•[MoneyBag!](/docs/api/admin-graphql/latest/objects/MoneyBag)

non-null

    

Total price of the order less the total amount received from the customer in
shop and presentment currencies.

Show fields

[Anchor to totalPriceSet](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
CalculatedOrder.fields.totalPriceSet)totalPriceSet

•[MoneyBag!](/docs/api/admin-graphql/latest/objects/MoneyBag)

non-null

    

Total amount of the order (includes taxes and discounts) in shop and
presentment currencies.

Show fields

[Anchor to committed](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-CalculatedOrder.fields.committed)committed

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-nullDeprecated

    

[Anchor to CartTransform](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
CartTransform)[CartTransform](/docs/api/admin-
graphql/latest/objects/CartTransform)

•OBJECT

    

A deployed cart transformation function that actively modifies how products
appear and behave in customer carts. Cart transforms enable sophisticated
merchandising strategies by programmatically merging, expanding, or updating
cart line items based on custom business logic.

Use the `CartTransform` object to:

  * Monitor active bundling and cart modification logic
  * Track transform function deployment status and configuration
  * Manage error handling behavior for cart processing failures
  * Coordinate multiple transforms when running complex merchandising strategies
  * Analyze transform performance and customer interaction patterns

Each cart transform links to a specific [Shopify
Function](https://shopify.dev/docs/apps/build/functions) that contains the
actual cart modification logic. The `blockOnFailure` setting determines
whether cart processing should halt when the transform encounters errors, or
whether it should allow customers to proceed with unmodified carts. This
flexibility ensures merchants can balance feature richness with checkout
reliability.

Transform functions operate during cart updates, product additions, and
checkout initiation, providing multiple touchpoints to enhance the shopping
experience. They integrate seamlessly with existing cart APIs while extending
functionality beyond standard product catalog capabilities.

The function ID connects to your deployed function code, while the
configuration settings control how the transform behaves in different
scenarios. Multiple transforms can work together, processing cart
modifications in sequence to support complex merchandising workflows.

Learn more about [customized bundles](https://shopify.dev/docs/apps/selling-
strategies/bundles/add-a-customized-bundle), and about the [Cart Transform
Function API](https://shopify.dev/docs/api/functions/latest/cart-transform).

Show fields

[Anchor to blockOnFailure](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
CartTransform.fields.blockOnFailure)blockOnFailure

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether a run failure will block cart and checkout operations.

[Anchor to functionId](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
CartTransform.fields.functionId)functionId

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The ID for the Cart Transform function.

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
CartTransform.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to metafield](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-CartTransform.fields.metafield)metafield

•[Metafield](/docs/api/admin-graphql/latest/objects/Metafield)

    

A [custom field](https://shopify.dev/docs/apps/build/custom-data), including
its `namespace` and `key`, that's associated with a Shopify resource for the
purposes of adding and storing additional information.

Show fields

[Anchor to metafields](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
CartTransform.fields.metafields)metafields

•[MetafieldConnection!](/docs/api/admin-
graphql/latest/connections/MetafieldConnection)

non-null

    

A list of [custom fields](https://shopify.dev/docs/apps/build/custom-data)
that a merchant associates with a Shopify resource.

Show fields

[Anchor to CashTrackingAdjustment](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
CashTrackingAdjustment)[CashTrackingAdjustment](/docs/api/admin-
graphql/latest/objects/CashTrackingAdjustment)

•OBJECT

    

Tracks an adjustment to the cash in a cash tracking session for a point of
sale device over the course of a shift.

Show fields

[Anchor to cash](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-CashTrackingAdjustment.fields.cash)cash

•[MoneyV2!](/docs/api/admin-graphql/latest/objects/MoneyV2)

non-null

    

The amount of cash being added or removed.

Show fields

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
CashTrackingAdjustment.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to note](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-CashTrackingAdjustment.fields.note)note

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The note entered when the adjustment was made.

[Anchor to staffMember](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
CashTrackingAdjustment.fields.staffMember)staffMember

•[StaffMember!](/docs/api/admin-graphql/latest/objects/StaffMember)

non-null

    

The staff member who made the adjustment.

Show fields

[Anchor to time](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-CashTrackingAdjustment.fields.time)time

•[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime)

non-null

    

The time when the adjustment was made.

[Anchor to CashTrackingSession](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
CashTrackingSession)[CashTrackingSession](/docs/api/admin-
graphql/latest/objects/CashTrackingSession)

•OBJECT

    

Tracks the balance in a cash drawer for a point of sale device over the course
of a shift.

Show fields

[Anchor to adjustments](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
CashTrackingSession.fields.adjustments)adjustments

•[CashTrackingAdjustmentConnection!](/docs/api/admin-
graphql/latest/connections/CashTrackingAdjustmentConnection)

non-null

    

The adjustments made to the cash drawer during this session.

Show fields

[Anchor to cashTrackingEnabled](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
CashTrackingSession.fields.cashTrackingEnabled)cashTrackingEnabled

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether this session is tracking cash payments.

[Anchor to cashTransactions](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
CashTrackingSession.fields.cashTransactions)cashTransactions

•[OrderTransactionConnection!](/docs/api/admin-
graphql/latest/connections/OrderTransactionConnection)

non-null

    

The cash transactions made during this session.

Show fields

[Anchor to closingBalance](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
CashTrackingSession.fields.closingBalance)closingBalance

•[MoneyV2](/docs/api/admin-graphql/latest/objects/MoneyV2)

    

The counted cash balance when the session was closed.

Show fields

[Anchor to closingNote](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
CashTrackingSession.fields.closingNote)closingNote

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The note entered when the session was closed.

[Anchor to closingStaffMember](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
CashTrackingSession.fields.closingStaffMember)closingStaffMember

•[StaffMember](/docs/api/admin-graphql/latest/objects/StaffMember)

    

The user who closed the session.

Show fields

[Anchor to closingTime](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
CashTrackingSession.fields.closingTime)closingTime

•[DateTime](/docs/api/admin-graphql/latest/scalars/DateTime)

    

When the session was closed.

[Anchor to expectedBalance](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
CashTrackingSession.fields.expectedBalance)expectedBalance

•[MoneyV2!](/docs/api/admin-graphql/latest/objects/MoneyV2)

non-null

    

The expected balance at the end of the session or the expected current balance
for sessions that are still open.

Show fields

[Anchor to expectedClosingBalance](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
CashTrackingSession.fields.expectedClosingBalance)expectedClosingBalance

•[MoneyV2](/docs/api/admin-graphql/latest/objects/MoneyV2)

    

The amount that was expected to be in the cash drawer at the end of the
session, calculated after the session was closed.

Show fields

[Anchor to expectedOpeningBalance](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
CashTrackingSession.fields.expectedOpeningBalance)expectedOpeningBalance

•[MoneyV2](/docs/api/admin-graphql/latest/objects/MoneyV2)

    

The amount expected to be in the cash drawer based on the previous session.

Show fields

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
CashTrackingSession.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to location](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-CashTrackingSession.fields.location)location

•[Location](/docs/api/admin-graphql/latest/objects/Location)

    

The location of the point of sale device during this session.

Show fields

[Anchor to netCashSales](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
CashTrackingSession.fields.netCashSales)netCashSales

•[MoneyV2!](/docs/api/admin-graphql/latest/objects/MoneyV2)

non-null

    

The net cash sales made for the duration of this cash tracking session.

Show fields

[Anchor to openingBalance](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
CashTrackingSession.fields.openingBalance)openingBalance

•[MoneyV2!](/docs/api/admin-graphql/latest/objects/MoneyV2)

non-null

    

The counted cash balance when the session was opened.

Show fields

[Anchor to openingNote](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
CashTrackingSession.fields.openingNote)openingNote

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The note entered when the session was opened.

[Anchor to openingStaffMember](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
CashTrackingSession.fields.openingStaffMember)openingStaffMember

•[StaffMember](/docs/api/admin-graphql/latest/objects/StaffMember)

    

The user who opened the session.

Show fields

[Anchor to openingTime](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
CashTrackingSession.fields.openingTime)openingTime

•[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime)

non-null

    

When the session was opened.

[Anchor to registerName](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
CashTrackingSession.fields.registerName)registerName

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The register name for the point of sale device that this session is tracking
cash for.

[Anchor to totalAdjustments](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
CashTrackingSession.fields.totalAdjustments)totalAdjustments

•[MoneyV2](/docs/api/admin-graphql/latest/objects/MoneyV2)

    

The sum of all adjustments made during the session, excluding the final
adjustment.

Show fields

[Anchor to totalCashRefunds](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
CashTrackingSession.fields.totalCashRefunds)totalCashRefunds

•[MoneyV2!](/docs/api/admin-graphql/latest/objects/MoneyV2)

non-null

    

The sum of all cash refunds for the duration of this cash tracking session.

Show fields

[Anchor to totalCashSales](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
CashTrackingSession.fields.totalCashSales)totalCashSales

•[MoneyV2!](/docs/api/admin-graphql/latest/objects/MoneyV2)

non-null

    

The sum of all cash sales for the duration of this cash tracking session.

Show fields

[Anchor to totalDiscrepancy](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
CashTrackingSession.fields.totalDiscrepancy)totalDiscrepancy

•[MoneyV2](/docs/api/admin-graphql/latest/objects/MoneyV2)

    

The total discrepancy for the session including starting and ending.

Show fields

[Anchor to CatalogCsvOperation](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
CatalogCsvOperation)[CatalogCsvOperation](/docs/api/admin-
graphql/latest/objects/CatalogCsvOperation)

•OBJECT

    

A catalog csv operation represents a CSV file import.

Show fields

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
CatalogCsvOperation.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to processedRowCount](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
CatalogCsvOperation.fields.processedRowCount)processedRowCount

•[Int](/docs/api/admin-graphql/latest/scalars/Int)

    

The count of processed rows, summing imported, failed, and skipped rows.

[Anchor to rowCount](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-CatalogCsvOperation.fields.rowCount)rowCount

•[RowCount](/docs/api/admin-graphql/latest/objects/RowCount)

    

Represents a rows objects within this background operation.

Show fields

[Anchor to status](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-CatalogCsvOperation.fields.status)status

•[ResourceOperationStatus!](/docs/api/admin-
graphql/latest/enums/ResourceOperationStatus)

non-null

    

The status of this operation.

Show enum values

[Anchor to Channel](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Channel)[Channel](/docs/api/admin-graphql/latest/objects/Channel)

•OBJECT

    

A channel represents an app where you sell a group of products and
collections. A channel can be a platform or marketplace such as Facebook or
Pinterest, an online store, or POS.

Show fields

[Anchor to app](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
Channel.fields.app)app

•[App!](/docs/api/admin-graphql/latest/objects/App)

non-null

    

The underlying app used by the channel.

Show fields

[Anchor to collectionPublicationsV3](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Channel.fields.collectionPublicationsV3)collectionPublicationsV3

•[ResourcePublicationConnection!](/docs/api/admin-
graphql/latest/connections/ResourcePublicationConnection)

non-null

    

The list of collection publications. Each record represents information about
the publication of a collection.

Show fields

[Anchor to collections](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Channel.fields.collections)collections

•[CollectionConnection!](/docs/api/admin-
graphql/latest/connections/CollectionConnection)

non-null

    

The list of collections published to the channel.

Show fields

[Anchor to handle](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Channel.fields.handle)handle

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The unique identifier for the channel.

[Anchor to hasCollection](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Channel.fields.hasCollection)hasCollection

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether the collection is available to the channel.

Show arguments

### Arguments

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
Channel.fields.hasCollection.arguments.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

required

    

The collection ID to check.

* * *

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
Channel.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to name](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Channel.fields.name)name

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The name of the channel.

[Anchor to productPublicationsV3](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Channel.fields.productPublicationsV3)productPublicationsV3

•[ResourcePublicationConnection!](/docs/api/admin-
graphql/latest/connections/ResourcePublicationConnection)

non-null

    

The list of product publication records for products published to this
channel.

Show fields

[Anchor to products](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Channel.fields.products)products

•[ProductConnection!](/docs/api/admin-
graphql/latest/connections/ProductConnection)

non-null

    

The list of products published to the channel.

Show fields

[Anchor to productsCount](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Channel.fields.productsCount)productsCount

•[Count](/docs/api/admin-graphql/latest/objects/Count)

    

Retrieves the total count of [`products`](https://shopify.dev/docs/api/admin-
graphql/latest/objects/Product) published to a specific sales channel. Limited
to a maximum of 10000 by default.

Show fields

[Anchor to supportsFuturePublishing](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Channel.fields.supportsFuturePublishing)supportsFuturePublishing

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether the channel supports future publishing.

[Anchor to navigationItems](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Channel.fields.navigationItems)navigationItems

•[[NavigationItem!]!](/docs/api/admin-graphql/latest/objects/NavigationItem)

non-nullDeprecated

    

Show fields

[Anchor to overviewPath](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Channel.fields.overviewPath)overviewPath

•[URL](/docs/api/admin-graphql/latest/scalars/URL)

Deprecated

    

[Anchor to productPublications](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Channel.fields.productPublications)productPublications

•[ProductPublicationConnection!](/docs/api/admin-
graphql/latest/connections/ProductPublicationConnection)

non-nullDeprecated

    

Show fields

[Anchor to ChannelDefinition](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ChannelDefinition)[ChannelDefinition](/docs/api/admin-
graphql/latest/objects/ChannelDefinition)

•OBJECT

    

A channel definition represents channels surfaces on the platform. A channel
definition can be a platform or a subsegment of it such as Facebook Home,
Instagram Live, Instagram Shops, or WhatsApp chat.

Show fields

[Anchor to channelName](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ChannelDefinition.fields.channelName)channelName

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

Name of the channel that this sub channel belongs to.

[Anchor to handle](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-ChannelDefinition.fields.handle)handle

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

Unique string used as a public identifier for the channel definition.

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
ChannelDefinition.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

The unique ID for the channel definition.

[Anchor to isMarketplace](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ChannelDefinition.fields.isMarketplace)isMarketplace

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether this channel definition represents a marketplace.

[Anchor to subChannelName](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ChannelDefinition.fields.subChannelName)subChannelName

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

Name of the sub channel (e.g. Online Store, Instagram Shopping, TikTok Live).

[Anchor to svgIcon](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-ChannelDefinition.fields.svgIcon)svgIcon

•[String](/docs/api/admin-graphql/latest/scalars/String)

Deprecated

    

[Anchor to ChannelInformation](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ChannelInformation)[ChannelInformation](/docs/api/admin-
graphql/latest/objects/ChannelInformation)

•OBJECT

    

Contains the information for a given sales channel.

Show fields

[Anchor to app](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
ChannelInformation.fields.app)app

•[App!](/docs/api/admin-graphql/latest/objects/App)

non-null

    

The app associated with the channel.

Show fields

[Anchor to channelDefinition](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ChannelInformation.fields.channelDefinition)channelDefinition

•[ChannelDefinition](/docs/api/admin-graphql/latest/objects/ChannelDefinition)

    

The channel definition associated with the channel.

Show fields

[Anchor to channelId](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-ChannelInformation.fields.channelId)channelId

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

The unique ID for the channel.

[Anchor to displayName](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ChannelInformation.fields.displayName)displayName

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The publishing destination display name or channel name.

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
ChannelInformation.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to CheckoutProfile](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
CheckoutProfile)[CheckoutProfile](/docs/api/admin-
graphql/latest/objects/CheckoutProfile)

•OBJECT

    

A checkout profile defines the branding settings and the UI extensions for a
store's checkout. A checkout profile could be published or draft. A store
might have at most one published checkout profile, which is used to render
their live checkout. The store could also have multiple draft profiles that
were created, previewed, and published using the admin checkout editor.

Show fields

[Anchor to createdAt](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-CheckoutProfile.fields.createdAt)createdAt

•[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime)

non-null

    

The date and time when the checkout profile was created.

[Anchor to editedAt](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-CheckoutProfile.fields.editedAt)editedAt

•[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime)

non-null

    

The date and time when the checkout profile was last edited.

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
CheckoutProfile.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to isPublished](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
CheckoutProfile.fields.isPublished)isPublished

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether the checkout profile is published or not.

[Anchor to name](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-CheckoutProfile.fields.name)name

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The profile name.

[Anchor to typOspPagesActive](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
CheckoutProfile.fields.typOspPagesActive)typOspPagesActive

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether the checkout profile Thank You Page and Order Status Page are actively
using extensibility or not.

[Anchor to updatedAt](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-CheckoutProfile.fields.updatedAt)updatedAt

•[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime)

non-null

    

The date and time when the checkout profile was last updated.

[Anchor to Collection](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Collection)[Collection](/docs/api/admin-graphql/latest/objects/Collection)

•OBJECT

    

The `Collection` object represents a group of
[products](https://shopify.dev/docs/api/admin-graphql/latest/objects/Product)
that merchants can organize to make their stores easier to browse and help
customers find related products. Collections serve as the primary way to
categorize and display products across [online
stores](https://shopify.dev/docs/apps/build/online-store), [sales
channels](https://shopify.dev/docs/apps/build/sales-channels), and marketing
campaigns.

There are two types of collections:

  * **[Custom (manual) collections](https://help.shopify.com/manual/products/collections/manual-shopify-collection)** : You specify the products to include in a collection.
  * **[Smart (automated) collections](https://help.shopify.com/manual/products/collections/automated-collections)** : You define rules, and products matching those rules are automatically included in the collection.

The `Collection` object provides information to:

  * Organize products by category, season, or promotion.
  * Automate product grouping using rules (for example, by tag, type, or price).
  * Configure product sorting and display order (for example, alphabetical, best-selling, price, or manual).
  * Manage collection visibility and publication across sales channels.
  * Add rich descriptions, images, and metadata to enhance discovery.

* * *

Note

Collections are unpublished by default. To make them available to customers,
use the [`publishablePublish`](https://shopify.dev/docs/api/admin-
graphql/latest/mutations/publishablePublish) mutation after creation.

* * *

Collections can be displayed in a store with Shopify's theme system through
[Liquid
templates](https://shopify.dev/docs/storefronts/themes/architecture/templates/collection)
and can be customized with [template
suffixes](https://shopify.dev/docs/storefronts/themes/architecture/templates/alternate-
templates) for unique layouts. They also support advanced features like
translated content, resource feedback, and contextual publication for
location-based catalogs.

Learn about [using metafields with smart
collections](https://shopify.dev/docs/apps/build/custom-data/metafields/use-
metafield-capabilities).

Show fields

[Anchor to availablePublicationsCount](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Collection.fields.availablePublicationsCount)availablePublicationsCount

•[Count](/docs/api/admin-graphql/latest/objects/Count)

    

The number of [publications](https://shopify.dev/docs/api/admin-
graphql/latest/objects/Publication) that a resource is published to, without
[feedback errors](https://shopify.dev/docs/api/admin-
graphql/latest/objects/ResourceFeedback).

Show fields

[Anchor to description](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Collection.fields.description)description

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

A single-line, text-only description of the collection, stripped of any HTML
tags and formatting that were included in the description.

Show arguments

### Arguments

[Anchor to truncateAt](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Collection.fields.description.arguments.truncateAt)truncateAt

•[Int](/docs/api/admin-graphql/latest/scalars/Int)

    

Truncates a string after the given length.

* * *

[Anchor to descriptionHtml](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Collection.fields.descriptionHtml)descriptionHtml

•[HTML!](/docs/api/admin-graphql/latest/scalars/HTML)

non-null

    

The description of the collection, including any HTML tags and formatting.
This content is typically displayed to customers, such as on an online store,
depending on the theme.

[Anchor to events](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Collection.fields.events)events

•[EventConnection!](/docs/api/admin-
graphql/latest/connections/EventConnection)

non-null

    

The paginated list of events associated with the host subject.

Show fields

[Anchor to feedback](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Collection.fields.feedback)feedback

•[ResourceFeedback](/docs/api/admin-graphql/latest/objects/ResourceFeedback)

    

Information about the collection that's provided through resource feedback.

Show fields

[Anchor to handle](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Collection.fields.handle)handle

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

A unique string that identifies the collection. If a handle isn't specified
when a collection is created, it's automatically generated from the
collection's original title, and typically includes words from the title
separated by hyphens. For example, a collection that was created with the
title `Summer Catalog 2022` might have the handle `summer-catalog-2022`.

If the title is changed, the handle doesn't automatically change.

The handle can be used in themes by the Liquid templating language to refer to
the collection, but using the ID is preferred because it never changes.

[Anchor to hasProduct](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Collection.fields.hasProduct)hasProduct

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether the collection includes the specified product.

Show arguments

### Arguments

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
Collection.fields.hasProduct.arguments.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

required

    

The ID of the product to check.

* * *

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
Collection.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to image](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Collection.fields.image)image

•[Image](/docs/api/admin-graphql/latest/objects/Image)

    

The image associated with the collection.

Show fields

[Anchor to legacyResourceId](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Collection.fields.legacyResourceId)legacyResourceId

•[UnsignedInt64!](/docs/api/admin-graphql/latest/scalars/UnsignedInt64)

non-null

    

The ID of the corresponding resource in the REST Admin API.

[Anchor to metafield](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Collection.fields.metafield)metafield

•[Metafield](/docs/api/admin-graphql/latest/objects/Metafield)

    

A [custom field](https://shopify.dev/docs/apps/build/custom-data), including
its `namespace` and `key`, that's associated with a Shopify resource for the
purposes of adding and storing additional information.

Show fields

[Anchor to metafields](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Collection.fields.metafields)metafields

•[MetafieldConnection!](/docs/api/admin-
graphql/latest/connections/MetafieldConnection)

non-null

    

A list of [custom fields](https://shopify.dev/docs/apps/build/custom-data)
that a merchant associates with a Shopify resource.

Show fields

[Anchor to products](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Collection.fields.products)products

•[ProductConnection!](/docs/api/admin-
graphql/latest/connections/ProductConnection)

non-null

    

The products that are included in the collection.

Show fields

[Anchor to productsCount](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Collection.fields.productsCount)productsCount

•[Count](/docs/api/admin-graphql/latest/objects/Count)

    

The number of products in the collection.

Show fields

[Anchor to publishedOnCurrentPublication](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Collection.fields.publishedOnCurrentPublication)publishedOnCurrentPublication

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether the resource is published to the app's
[publication](https://shopify.dev/docs/api/admin-
graphql/latest/objects/Publication). For example, the resource might be
published to the app's online store channel.

[Anchor to publishedOnPublication](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Collection.fields.publishedOnPublication)publishedOnPublication

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether the resource is published to a specified
[publication](https://shopify.dev/docs/api/admin-
graphql/latest/objects/Publication).

Show arguments

### Arguments

[Anchor to publicationId](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Collection.fields.publishedOnPublication.arguments.publicationId)publicationId

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

required

    

The ID of the publication to check. For example, `id:
"gid://shopify/Publication/123"`.

* * *

[Anchor to resourcePublications](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Collection.fields.resourcePublications)resourcePublications

•[ResourcePublicationConnection!](/docs/api/admin-
graphql/latest/connections/ResourcePublicationConnection)

non-null

    

The list of resources that are published to a
[publication](https://shopify.dev/docs/api/admin-
graphql/latest/objects/Publication).

Show fields

[Anchor to resourcePublicationsCount](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Collection.fields.resourcePublicationsCount)resourcePublicationsCount

•[Count](/docs/api/admin-graphql/latest/objects/Count)

    

The number of [publications](https://shopify.dev/docs/api/admin-
graphql/latest/objects/Publication) that a resource is published to, without
[feedback errors](https://shopify.dev/docs/api/admin-
graphql/latest/objects/ResourceFeedback).

Show fields

[Anchor to resourcePublicationsV2](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Collection.fields.resourcePublicationsV2)resourcePublicationsV2

•[ResourcePublicationV2Connection!](/docs/api/admin-
graphql/latest/connections/ResourcePublicationV2Connection)

non-null

    

The list of resources that are either published or staged to be published to a
[publication](https://shopify.dev/docs/api/admin-
graphql/latest/objects/Publication).

Show fields

[Anchor to ruleSet](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Collection.fields.ruleSet)ruleSet

•[CollectionRuleSet](/docs/api/admin-graphql/latest/objects/CollectionRuleSet)

    

For a smart (automated) collection, specifies the rules that determine whether
a product is included.

Show fields

[Anchor to seo](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
Collection.fields.seo)seo

•[SEO!](/docs/api/admin-graphql/latest/objects/SEO)

non-null

    

If the default SEO fields for page title and description have been modified,
contains the modified information.

Show fields

[Anchor to sortOrder](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Collection.fields.sortOrder)sortOrder

•[CollectionSortOrder!](/docs/api/admin-
graphql/latest/enums/CollectionSortOrder)

non-null

    

The order in which the products in the collection are displayed by default in
the Shopify admin and in sales channels, such as an online store.

Show enum values

[Anchor to templateSuffix](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Collection.fields.templateSuffix)templateSuffix

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The suffix of the Liquid template being used to show the collection in an
online store. For example, if the value is `custom`, then the collection is
using the `collection.custom.liquid` template. If the value is `null`, then
the collection is using the default `collection.liquid` template.

[Anchor to title](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Collection.fields.title)title

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The name of the collection. It's displayed in the Shopify admin and is
typically displayed in sales channels, such as an online store.

[Anchor to translations](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Collection.fields.translations)translations

•[[Translation!]!](/docs/api/admin-graphql/latest/objects/Translation)

non-null

    

The published translations associated with the resource.

Show fields

[Anchor to unpublishedPublications](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Collection.fields.unpublishedPublications)unpublishedPublications

•[PublicationConnection!](/docs/api/admin-
graphql/latest/connections/PublicationConnection)

non-null

    

The list of [publications](https://shopify.dev/docs/api/admin-
graphql/latest/objects/Publication) that the resource isn't published to.

Show fields

[Anchor to updatedAt](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Collection.fields.updatedAt)updatedAt

•[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime)

non-null

    

The date and time ([ISO 8601 format](http://en.wikipedia.org/wiki/ISO_8601))
when the collection was last modified.

[Anchor to metafieldDefinitions](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Collection.fields.metafieldDefinitions)metafieldDefinitions

•[MetafieldDefinitionConnection!](/docs/api/admin-
graphql/latest/connections/MetafieldDefinitionConnection)

non-nullDeprecated

    

Show fields

[Anchor to publicationCount](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Collection.fields.publicationCount)publicationCount

•[Int!](/docs/api/admin-graphql/latest/scalars/Int)

non-nullDeprecated

    

Show arguments

### Arguments

[Anchor to onlyPublished](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Collection.fields.publicationCount.arguments.onlyPublished)onlyPublished

•[Boolean](/docs/api/admin-graphql/latest/scalars/Boolean)

Default:true

    

Include only the resource's publications that are published. If false, then
return all the resource's publications including future publications.

* * *

[Anchor to publications](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Collection.fields.publications)publications

•[CollectionPublicationConnection!](/docs/api/admin-
graphql/latest/connections/CollectionPublicationConnection)

non-nullDeprecated

    

Show fields

[Anchor to publishedOnChannel](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Collection.fields.publishedOnChannel)publishedOnChannel

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-nullDeprecated

    

Show arguments

### Arguments

[Anchor to channelId](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Collection.fields.publishedOnChannel.arguments.channelId)channelId

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

required

    

The ID of the channel to check.

* * *

[Anchor to publishedOnCurrentChannel](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Collection.fields.publishedOnCurrentChannel)publishedOnCurrentChannel

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-nullDeprecated

    

[Anchor to storefrontId](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Collection.fields.storefrontId)storefrontId

•[StorefrontID!](/docs/api/admin-graphql/latest/scalars/StorefrontID)

non-nullDeprecated

    

[Anchor to unpublishedChannels](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Collection.fields.unpublishedChannels)unpublishedChannels

•[ChannelConnection!](/docs/api/admin-
graphql/latest/connections/ChannelConnection)

non-nullDeprecated

    

Show fields

[Anchor to Comment](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Comment)[Comment](/docs/api/admin-graphql/latest/objects/Comment)

•OBJECT

    

A comment on an article.

Show fields

[Anchor to article](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Comment.fields.article)article

•[Article](/docs/api/admin-graphql/latest/objects/Article)

    

The article associated with the comment.

Show fields

[Anchor to author](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Comment.fields.author)author

•[CommentAuthor!](/docs/api/admin-graphql/latest/objects/CommentAuthor)

non-null

    

The comment’s author.

Show fields

[Anchor to body](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Comment.fields.body)body

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The content of the comment.

[Anchor to bodyHtml](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Comment.fields.bodyHtml)bodyHtml

•[HTML!](/docs/api/admin-graphql/latest/scalars/HTML)

non-null

    

The content of the comment, complete with HTML formatting.

[Anchor to createdAt](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Comment.fields.createdAt)createdAt

•[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime)

non-null

    

The date and time when the comment was created.

[Anchor to events](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Comment.fields.events)events

•[EventConnection!](/docs/api/admin-
graphql/latest/connections/EventConnection)

non-null

    

The paginated list of events associated with the host subject.

Show fields

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
Comment.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to ip](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
Comment.fields.ip)ip

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The IP address of the commenter.

[Anchor to isPublished](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Comment.fields.isPublished)isPublished

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether or not the comment is published.

[Anchor to publishedAt](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Comment.fields.publishedAt)publishedAt

•[DateTime](/docs/api/admin-graphql/latest/scalars/DateTime)

    

The date and time when the comment was published.

[Anchor to status](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Comment.fields.status)status

•[CommentStatus!](/docs/api/admin-graphql/latest/enums/CommentStatus)

non-null

    

The status of the comment.

Show enum values

[Anchor to updatedAt](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Comment.fields.updatedAt)updatedAt

•[DateTime](/docs/api/admin-graphql/latest/scalars/DateTime)

    

The date and time when the comment was last updated.

[Anchor to userAgent](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Comment.fields.userAgent)userAgent

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The user agent of the commenter.

[Anchor to CommentEvent](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
CommentEvent)[CommentEvent](/docs/api/admin-
graphql/latest/objects/CommentEvent)

•OBJECT

    

Comment events are generated by staff members of a shop. They are created when
a staff member adds a comment to the timeline of an order, draft order,
customer, or transfer.

Show fields

[Anchor to action](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-CommentEvent.fields.action)action

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The action that occured.

[Anchor to appTitle](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-CommentEvent.fields.appTitle)appTitle

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The name of the app that created the event.

[Anchor to attachments](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
CommentEvent.fields.attachments)attachments

•[[CommentEventAttachment!]!](/docs/api/admin-
graphql/latest/objects/CommentEventAttachment)

non-null

    

The attachments associated with the comment event.

Show fields

[Anchor to attributeToApp](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
CommentEvent.fields.attributeToApp)attributeToApp

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether the event was created by an app.

[Anchor to attributeToUser](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
CommentEvent.fields.attributeToUser)attributeToUser

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether the event was caused by an admin user.

[Anchor to author](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-CommentEvent.fields.author)author

•[StaffMember!](/docs/api/admin-graphql/latest/objects/StaffMember)

non-null

    

The name of the user that authored the comment event.

Show fields

[Anchor to canDelete](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-CommentEvent.fields.canDelete)canDelete

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether the comment event can be deleted. If true, then the comment event can
be deleted.

[Anchor to canEdit](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-CommentEvent.fields.canEdit)canEdit

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether the comment event can be edited. If true, then the comment event can
be edited.

[Anchor to createdAt](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-CommentEvent.fields.createdAt)createdAt

•[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime)

non-null

    

The date and time when the event was created.

[Anchor to criticalAlert](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
CommentEvent.fields.criticalAlert)criticalAlert

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether the event is critical.

[Anchor to edited](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-CommentEvent.fields.edited)edited

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether the comment event has been edited. If true, then the comment event has
been edited.

[Anchor to embed](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-CommentEvent.fields.embed)embed

•[CommentEventEmbed](/docs/api/admin-graphql/latest/unions/CommentEventEmbed)

    

The object reference associated with the comment event. For example, a product
or discount).

Show union types

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
CommentEvent.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to message](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-CommentEvent.fields.message)message

•[FormattedString!](/docs/api/admin-graphql/latest/scalars/FormattedString)

non-null

    

Human readable text that describes the event.

[Anchor to rawMessage](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
CommentEvent.fields.rawMessage)rawMessage

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The raw body of the comment event.

[Anchor to subject](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-CommentEvent.fields.subject)subject

•[CommentEventSubject](/docs/api/admin-
graphql/latest/interfaces/CommentEventSubject)

    

The parent subject to which the comment event belongs.

Show fields

[Anchor to Company](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Company)[Company](/docs/api/admin-graphql/latest/objects/Company)

•OBJECT

    

Represents information about a company which is also a customer of the shop.

Show fields

[Anchor to contactRoles](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Company.fields.contactRoles)contactRoles

•[CompanyContactRoleConnection!](/docs/api/admin-
graphql/latest/connections/CompanyContactRoleConnection)

non-null

    

The list of roles for the company contacts.

Show fields

[Anchor to contacts](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Company.fields.contacts)contacts

•[CompanyContactConnection!](/docs/api/admin-
graphql/latest/connections/CompanyContactConnection)

non-null

    

The list of contacts in the company.

Show fields

[Anchor to contactsCount](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Company.fields.contactsCount)contactsCount

•[Count](/docs/api/admin-graphql/latest/objects/Count)

    

The number of contacts that belong to the company.

Show fields

[Anchor to createdAt](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Company.fields.createdAt)createdAt

•[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime)

non-null

    

The date and time ([ISO 8601 format](http://en.wikipedia.org/wiki/ISO_8601))
at which the company was created in Shopify.

[Anchor to customerSince](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Company.fields.customerSince)customerSince

•[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime)

non-null

    

The date and time ([ISO 8601 format](http://en.wikipedia.org/wiki/ISO_8601))
at which the company became the customer.

[Anchor to defaultCursor](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Company.fields.defaultCursor)defaultCursor

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

A default [cursor](https://shopify.dev/api/usage/pagination-graphql) that
returns the single next record, sorted ascending by ID.

[Anchor to defaultRole](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Company.fields.defaultRole)defaultRole

•[CompanyContactRole](/docs/api/admin-
graphql/latest/objects/CompanyContactRole)

    

The role proposed by default for a contact at the company.

Show fields

[Anchor to draftOrders](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Company.fields.draftOrders)draftOrders

•[DraftOrderConnection!](/docs/api/admin-
graphql/latest/connections/DraftOrderConnection)

non-null

    

The list of the company's draft orders.

Show fields

[Anchor to events](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Company.fields.events)events

•[EventConnection!](/docs/api/admin-
graphql/latest/connections/EventConnection)

non-null

    

The paginated list of events associated with the host subject.

Show fields

[Anchor to externalId](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Company.fields.externalId)externalId

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

A unique externally-supplied ID for the company.

[Anchor to hasTimelineComment](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Company.fields.hasTimelineComment)hasTimelineComment

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether the merchant added a timeline comment to the company.

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
Company.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to lifetimeDuration](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Company.fields.lifetimeDuration)lifetimeDuration

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The lifetime duration of the company, since it became a customer of the shop.
Examples: `2 days`, `3 months`, `1 year`.

[Anchor to locations](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Company.fields.locations)locations

•[CompanyLocationConnection!](/docs/api/admin-
graphql/latest/connections/CompanyLocationConnection)

non-null

    

The list of locations in the company.

Show fields

[Anchor to locationsCount](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Company.fields.locationsCount)locationsCount

•[Count](/docs/api/admin-graphql/latest/objects/Count)

    

The number of locations that belong to the company.

Show fields

[Anchor to mainContact](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Company.fields.mainContact)mainContact

•[CompanyContact](/docs/api/admin-graphql/latest/objects/CompanyContact)

    

The main contact for the company.

Show fields

[Anchor to metafield](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Company.fields.metafield)metafield

•[Metafield](/docs/api/admin-graphql/latest/objects/Metafield)

    

A [custom field](https://shopify.dev/docs/apps/build/custom-data), including
its `namespace` and `key`, that's associated with a Shopify resource for the
purposes of adding and storing additional information.

Show fields

[Anchor to metafields](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Company.fields.metafields)metafields

•[MetafieldConnection!](/docs/api/admin-
graphql/latest/connections/MetafieldConnection)

non-null

    

A list of [custom fields](https://shopify.dev/docs/apps/build/custom-data)
that a merchant associates with a Shopify resource.

Show fields

[Anchor to name](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Company.fields.name)name

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The name of the company.

[Anchor to note](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Company.fields.note)note

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

A note about the company.

[Anchor to orders](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Company.fields.orders)orders

•[OrderConnection!](/docs/api/admin-
graphql/latest/connections/OrderConnection)

non-null

    

The list of the company's orders.

Show fields

[Anchor to ordersCount](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Company.fields.ordersCount)ordersCount

•[Count](/docs/api/admin-graphql/latest/objects/Count)

    

The total number of orders placed for this company, across all its locations.

Show fields

[Anchor to totalSpent](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Company.fields.totalSpent)totalSpent

•[MoneyV2!](/docs/api/admin-graphql/latest/objects/MoneyV2)

non-null

    

The total amount spent by this company, across all its locations.

Show fields

[Anchor to updatedAt](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Company.fields.updatedAt)updatedAt

•[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime)

non-null

    

The date and time ([ISO 8601 format](http://en.wikipedia.org/wiki/ISO_8601))
at which the company was last modified.

[Anchor to contactCount](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Company.fields.contactCount)contactCount

•[Int!](/docs/api/admin-graphql/latest/scalars/Int)

non-nullDeprecated

    

[Anchor to metafieldDefinitions](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Company.fields.metafieldDefinitions)metafieldDefinitions

•[MetafieldDefinitionConnection!](/docs/api/admin-
graphql/latest/connections/MetafieldDefinitionConnection)

non-nullDeprecated

    

Show fields

[Anchor to CompanyAddress](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
CompanyAddress)[CompanyAddress](/docs/api/admin-
graphql/latest/objects/CompanyAddress)

•OBJECT

    

Represents a billing or shipping address for a company location.

Show fields

[Anchor to address1](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-CompanyAddress.fields.address1)address1

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The first line of the address. Typically the street address or PO Box number.

[Anchor to address2](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-CompanyAddress.fields.address2)address2

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The second line of the address. Typically the number of the apartment, suite,
or unit.

[Anchor to city](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-CompanyAddress.fields.city)city

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The name of the city, district, village, or town.

[Anchor to companyName](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
CompanyAddress.fields.companyName)companyName

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The name of the company.

[Anchor to country](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-CompanyAddress.fields.country)country

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The name of the country.

[Anchor to countryCode](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
CompanyAddress.fields.countryCode)countryCode

•[CountryCode!](/docs/api/admin-graphql/latest/enums/CountryCode)

non-null

    

The two-letter code for the country of the address. For example, US.

Show enum values

[Anchor to createdAt](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-CompanyAddress.fields.createdAt)createdAt

•[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime)

non-null

    

The date and time ([ISO 8601 format](http://en.wikipedia.org/wiki/ISO_8601))
at which the company address was created.

[Anchor to firstName](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-CompanyAddress.fields.firstName)firstName

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The first name of the recipient.

[Anchor to formattedAddress](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
CompanyAddress.fields.formattedAddress)formattedAddress

•[[String!]!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The formatted version of the address.

Show arguments

### Arguments

[Anchor to withName](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-CompanyAddress.fields.formattedAddress.arguments.withName)withName

•[Boolean](/docs/api/admin-graphql/latest/scalars/Boolean)

Default:false

    

Whether to include the recipient's name in the formatted address.

[Anchor to withCompanyName](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
CompanyAddress.fields.formattedAddress.arguments.withCompanyName)withCompanyName

•[Boolean](/docs/api/admin-graphql/latest/scalars/Boolean)

Default:true

    

Whether to include the company name in the formatted address.

* * *

[Anchor to formattedArea](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
CompanyAddress.fields.formattedArea)formattedArea

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

A comma-separated list of the values for city, province, and country.

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
CompanyAddress.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to lastName](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-CompanyAddress.fields.lastName)lastName

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The last name of the recipient.

[Anchor to phone](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-CompanyAddress.fields.phone)phone

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

A unique phone number for the customer. Formatted using E.164 standard. For
example, _+16135551111_.

[Anchor to province](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-CompanyAddress.fields.province)province

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The region of the address, such as the province, state, or district.

[Anchor to recipient](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-CompanyAddress.fields.recipient)recipient

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The identity of the recipient e.g. 'Receiving Department'.

[Anchor to updatedAt](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-CompanyAddress.fields.updatedAt)updatedAt

•[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime)

non-null

    

The date and time ([ISO 8601 format](http://en.wikipedia.org/wiki/ISO_8601))
at which the company address was last updated.

[Anchor to zip](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
CompanyAddress.fields.zip)zip

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The zip or postal code of the address.

[Anchor to zoneCode](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-CompanyAddress.fields.zoneCode)zoneCode

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The alphanumeric code for the region. For example, ON.

[Anchor to CompanyContact](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
CompanyContact)[CompanyContact](/docs/api/admin-
graphql/latest/objects/CompanyContact)

•OBJECT

    

A person that acts on behalf of company associated to [a
customer](https://shopify.dev/api/admin-graphql/latest/objects/customer).

Show fields

[Anchor to company](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-CompanyContact.fields.company)company

•[Company!](/docs/api/admin-graphql/latest/objects/Company)

non-null

    

The company to which the contact belongs.

Show fields

[Anchor to createdAt](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-CompanyContact.fields.createdAt)createdAt

•[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime)

non-null

    

The date and time ([ISO 8601 format](http://en.wikipedia.org/wiki/ISO_8601))
at which the company contact was created at Shopify.

[Anchor to customer](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-CompanyContact.fields.customer)customer

•[Customer!](/docs/api/admin-graphql/latest/objects/Customer)

non-null

    

The customer associated to this contact.

Show fields

[Anchor to draftOrders](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
CompanyContact.fields.draftOrders)draftOrders

•[DraftOrderConnection!](/docs/api/admin-
graphql/latest/connections/DraftOrderConnection)

non-null

    

The list of draft orders for the company contact.

Show fields

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
CompanyContact.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to isMainContact](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
CompanyContact.fields.isMainContact)isMainContact

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether the contact is the main contact of the company.

[Anchor to lifetimeDuration](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
CompanyContact.fields.lifetimeDuration)lifetimeDuration

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The lifetime duration of the company contact, since its creation date on
Shopify. Examples: `1 year`, `2 months`, `3 days`.

[Anchor to locale](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-CompanyContact.fields.locale)locale

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The company contact's locale (language).

[Anchor to orders](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-CompanyContact.fields.orders)orders

•[OrderConnection!](/docs/api/admin-
graphql/latest/connections/OrderConnection)

non-null

    

The list of orders for the company contact.

Show fields

[Anchor to roleAssignments](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
CompanyContact.fields.roleAssignments)roleAssignments

•[CompanyContactRoleAssignmentConnection!](/docs/api/admin-
graphql/latest/connections/CompanyContactRoleAssignmentConnection)

non-null

    

The list of roles assigned to this company contact.

Show fields

[Anchor to title](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-CompanyContact.fields.title)title

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The company contact's job title.

[Anchor to updatedAt](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-CompanyContact.fields.updatedAt)updatedAt

•[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime)

non-null

    

The date and time ([ISO 8601 format](http://en.wikipedia.org/wiki/ISO_8601))
at which the company contact was last updated.

[Anchor to CompanyContactRole](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
CompanyContactRole)[CompanyContactRole](/docs/api/admin-
graphql/latest/objects/CompanyContactRole)

•OBJECT

    

The role for a [company contact](https://shopify.dev/api/admin-
graphql/latest/objects/companycontact).

Show fields

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
CompanyContactRole.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to name](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-CompanyContactRole.fields.name)name

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The name of a role. For example, `admin` or `buyer`.

[Anchor to note](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-CompanyContactRole.fields.note)note

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

A note for the role.

[Anchor to CompanyContactRoleAssignment](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
CompanyContactRoleAssignment)[CompanyContactRoleAssignment](/docs/api/admin-
graphql/latest/objects/CompanyContactRoleAssignment)

•OBJECT

    

The CompanyContactRoleAssignment describes the company and location associated
to a company contact's role.

Show fields

[Anchor to company](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-CompanyContactRoleAssignment.fields.company)company

•[Company!](/docs/api/admin-graphql/latest/objects/Company)

non-null

    

The company this role assignment belongs to.

Show fields

[Anchor to companyContact](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
CompanyContactRoleAssignment.fields.companyContact)companyContact

•[CompanyContact!](/docs/api/admin-graphql/latest/objects/CompanyContact)

non-null

    

The company contact for whom this role is assigned.

Show fields

[Anchor to companyLocation](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
CompanyContactRoleAssignment.fields.companyLocation)companyLocation

•[CompanyLocation!](/docs/api/admin-graphql/latest/objects/CompanyLocation)

non-null

    

The company location to which the role is assigned.

Show fields

[Anchor to createdAt](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-CompanyContactRoleAssignment.fields.createdAt)createdAt

•[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime)

non-null

    

The date and time ([ISO 8601 format](http://en.wikipedia.org/wiki/ISO_8601))
when the assignment record was created.

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
CompanyContactRoleAssignment.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to role](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-CompanyContactRoleAssignment.fields.role)role

•[CompanyContactRole!](/docs/api/admin-
graphql/latest/objects/CompanyContactRole)

non-null

    

The role that's assigned to the company contact.

Show fields

[Anchor to updatedAt](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-CompanyContactRoleAssignment.fields.updatedAt)updatedAt

•[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime)

non-null

    

The date and time ([ISO 8601 format](http://en.wikipedia.org/wiki/ISO_8601))
when the assignment record was last updated.

[Anchor to CompanyLocation](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
CompanyLocation)[CompanyLocation](/docs/api/admin-
graphql/latest/objects/CompanyLocation)

•OBJECT

    

A location or branch of a [company that's a
customer](https://shopify.dev/api/admin-graphql/latest/objects/company) of the
shop. Configuration of B2B relationship, for example prices lists and checkout
settings, may be done for a location.

Show fields

[Anchor to billingAddress](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
CompanyLocation.fields.billingAddress)billingAddress

•[CompanyAddress](/docs/api/admin-graphql/latest/objects/CompanyAddress)

    

The address used as billing address for the location.

Show fields

[Anchor to buyerExperienceConfiguration](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
CompanyLocation.fields.buyerExperienceConfiguration)buyerExperienceConfiguration

•[BuyerExperienceConfiguration](/docs/api/admin-
graphql/latest/objects/BuyerExperienceConfiguration)

    

The configuration for the buyer's B2B checkout.

Show fields

[Anchor to catalogs](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-CompanyLocation.fields.catalogs)catalogs

•[CatalogConnection!](/docs/api/admin-
graphql/latest/connections/CatalogConnection)

non-null

    

The list of catalogs associated with the company location.

Show fields

[Anchor to catalogsCount](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
CompanyLocation.fields.catalogsCount)catalogsCount

•[Count](/docs/api/admin-graphql/latest/objects/Count)

    

The number of catalogs associated with the company location. Limited to a
maximum of 10000 by default.

Show fields

[Anchor to company](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-CompanyLocation.fields.company)company

•[Company!](/docs/api/admin-graphql/latest/objects/Company)

non-null

    

The company that the company location belongs to.

Show fields

[Anchor to createdAt](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-CompanyLocation.fields.createdAt)createdAt

•[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime)

non-null

    

The date and time ([ISO 8601 format](http://en.wikipedia.org/wiki/ISO_8601))
at which the company location was created in Shopify.

[Anchor to currency](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-CompanyLocation.fields.currency)currency

•[CurrencyCode!](/docs/api/admin-graphql/latest/enums/CurrencyCode)

non-null

    

The location's currency based on the shipping address. If the shipping address
is empty, then the value is the shop's primary market.

Show enum values

[Anchor to defaultCursor](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
CompanyLocation.fields.defaultCursor)defaultCursor

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

A default [cursor](https://shopify.dev/api/usage/pagination-graphql) that
returns the single next record, sorted ascending by ID.

[Anchor to draftOrders](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
CompanyLocation.fields.draftOrders)draftOrders

•[DraftOrderConnection!](/docs/api/admin-
graphql/latest/connections/DraftOrderConnection)

non-null

    

The list of draft orders for the company location.

Show fields

[Anchor to events](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-CompanyLocation.fields.events)events

•[EventConnection!](/docs/api/admin-
graphql/latest/connections/EventConnection)

non-null

    

The paginated list of events associated with the host subject.

Show fields

[Anchor to externalId](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
CompanyLocation.fields.externalId)externalId

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

A unique externally-supplied ID for the company location.

[Anchor to hasTimelineComment](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
CompanyLocation.fields.hasTimelineComment)hasTimelineComment

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether the merchant added a timeline comment to the company location.

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
CompanyLocation.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to inCatalog](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-CompanyLocation.fields.inCatalog)inCatalog

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether the company location is assigned a specific catalog.

Show arguments

### Arguments

[Anchor to catalogId](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-CompanyLocation.fields.inCatalog.arguments.catalogId)catalogId

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

required

    

The ID of the catalog.

* * *

[Anchor to locale](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-CompanyLocation.fields.locale)locale

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The preferred locale of the company location.

[Anchor to metafield](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-CompanyLocation.fields.metafield)metafield

•[Metafield](/docs/api/admin-graphql/latest/objects/Metafield)

    

A [custom field](https://shopify.dev/docs/apps/build/custom-data), including
its `namespace` and `key`, that's associated with a Shopify resource for the
purposes of adding and storing additional information.

Show fields

[Anchor to metafields](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
CompanyLocation.fields.metafields)metafields

•[MetafieldConnection!](/docs/api/admin-
graphql/latest/connections/MetafieldConnection)

non-null

    

A list of [custom fields](https://shopify.dev/docs/apps/build/custom-data)
that a merchant associates with a Shopify resource.

Show fields

[Anchor to name](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-CompanyLocation.fields.name)name

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The name of the company location.

[Anchor to note](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-CompanyLocation.fields.note)note

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

A note about the company location.

[Anchor to orders](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-CompanyLocation.fields.orders)orders

•[OrderConnection!](/docs/api/admin-
graphql/latest/connections/OrderConnection)

non-null

    

The list of orders for the company location.

Show fields

[Anchor to ordersCount](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
CompanyLocation.fields.ordersCount)ordersCount

•[Count](/docs/api/admin-graphql/latest/objects/Count)

    

The total number of orders placed for the location.

Show fields

[Anchor to phone](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-CompanyLocation.fields.phone)phone

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The phone number of the company location.

[Anchor to roleAssignments](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
CompanyLocation.fields.roleAssignments)roleAssignments

•[CompanyContactRoleAssignmentConnection!](/docs/api/admin-
graphql/latest/connections/CompanyContactRoleAssignmentConnection)

non-null

    

The list of roles assigned to the company location.

Show fields

[Anchor to shippingAddress](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
CompanyLocation.fields.shippingAddress)shippingAddress

•[CompanyAddress](/docs/api/admin-graphql/latest/objects/CompanyAddress)

    

The address used as shipping address for the location.

Show fields

[Anchor to staffMemberAssignments](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
CompanyLocation.fields.staffMemberAssignments)staffMemberAssignments

•[CompanyLocationStaffMemberAssignmentConnection!](/docs/api/admin-
graphql/latest/connections/CompanyLocationStaffMemberAssignmentConnection)

non-null

    

The list of staff members assigned to the company location.

Show fields

[Anchor to storeCreditAccounts](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
CompanyLocation.fields.storeCreditAccounts)storeCreditAccounts

•[StoreCreditAccountConnection!](/docs/api/admin-
graphql/latest/connections/StoreCreditAccountConnection)

non-null

    

Returns a list of store credit accounts that belong to the owner resource. A
store credit account owner can hold multiple accounts each with a different
currency.

Show fields

[Anchor to taxSettings](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
CompanyLocation.fields.taxSettings)taxSettings

•[CompanyLocationTaxSettings!](/docs/api/admin-
graphql/latest/objects/CompanyLocationTaxSettings)

non-null

    

The tax settings for the company location.

Show fields

[Anchor to totalSpent](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
CompanyLocation.fields.totalSpent)totalSpent

•[MoneyV2!](/docs/api/admin-graphql/latest/objects/MoneyV2)

non-null

    

The total amount spent by the location.

Show fields

[Anchor to updatedAt](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-CompanyLocation.fields.updatedAt)updatedAt

•[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime)

non-null

    

The date and time ([ISO 8601 format](http://en.wikipedia.org/wiki/ISO_8601))
at which the company location was last modified.

[Anchor to market](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-CompanyLocation.fields.market)market

•[Market!](/docs/api/admin-graphql/latest/objects/Market)

non-nullDeprecated

    

Show fields

[Anchor to metafieldDefinitions](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
CompanyLocation.fields.metafieldDefinitions)metafieldDefinitions

•[MetafieldDefinitionConnection!](/docs/api/admin-
graphql/latest/connections/MetafieldDefinitionConnection)

non-nullDeprecated

    

Show fields

[Anchor to orderCount](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
CompanyLocation.fields.orderCount)orderCount

•[Int!](/docs/api/admin-graphql/latest/scalars/Int)

non-nullDeprecated

    

[Anchor to taxExemptions](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
CompanyLocation.fields.taxExemptions)taxExemptions

•[[TaxExemption!]!](/docs/api/admin-graphql/latest/enums/TaxExemption)

non-nullDeprecated

    

Show enum values

[Anchor to taxRegistrationId](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
CompanyLocation.fields.taxRegistrationId)taxRegistrationId

•[String](/docs/api/admin-graphql/latest/scalars/String)

Deprecated

    

[Anchor to CompanyLocationCatalog](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
CompanyLocationCatalog)[CompanyLocationCatalog](/docs/api/admin-
graphql/latest/objects/CompanyLocationCatalog)

•OBJECT

    

A list of products with publishing and pricing information associated with
company locations.

Show fields

[Anchor to companyLocations](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
CompanyLocationCatalog.fields.companyLocations)companyLocations

•[CompanyLocationConnection!](/docs/api/admin-
graphql/latest/connections/CompanyLocationConnection)

non-null

    

The company locations associated with the catalog.

Show fields

[Anchor to companyLocationsCount](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
CompanyLocationCatalog.fields.companyLocationsCount)companyLocationsCount

•[Count](/docs/api/admin-graphql/latest/objects/Count)

    

The number of company locations associated with the catalog.

Show fields

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
CompanyLocationCatalog.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to operations](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
CompanyLocationCatalog.fields.operations)operations

•[[ResourceOperation!]!](/docs/api/admin-
graphql/latest/interfaces/ResourceOperation)

non-null

    

Most recent catalog operations.

Show fields

[Anchor to priceList](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-CompanyLocationCatalog.fields.priceList)priceList

•[PriceList](/docs/api/admin-graphql/latest/objects/PriceList)

    

The price list associated with the catalog.

Show fields

[Anchor to publication](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
CompanyLocationCatalog.fields.publication)publication

•[Publication](/docs/api/admin-graphql/latest/objects/Publication)

    

A group of products and collections that's published to a catalog.

Show fields

[Anchor to status](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-CompanyLocationCatalog.fields.status)status

•[CatalogStatus!](/docs/api/admin-graphql/latest/enums/CatalogStatus)

non-null

    

The status of the catalog.

Show enum values

[Anchor to title](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-CompanyLocationCatalog.fields.title)title

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The name of the catalog.

[Anchor to CompanyLocationStaffMemberAssignment](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
CompanyLocationStaffMemberAssignment)[CompanyLocationStaffMemberAssignment](/docs/api/admin-
graphql/latest/objects/CompanyLocationStaffMemberAssignment)

•OBJECT

    

A representation of store's staff member who is assigned to a [company
location](https://shopify.dev/api/admin-
graphql/latest/objects/CompanyLocation) of the shop. The staff member's
actions will be limited to objects associated with the assigned company
location.

Show fields

[Anchor to companyLocation](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
CompanyLocationStaffMemberAssignment.fields.companyLocation)companyLocation

•[CompanyLocation!](/docs/api/admin-graphql/latest/objects/CompanyLocation)

non-null

    

The company location the staff member is assigned to.

Show fields

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
CompanyLocationStaffMemberAssignment.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to staffMember](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
CompanyLocationStaffMemberAssignment.fields.staffMember)staffMember

•[StaffMember!](/docs/api/admin-graphql/latest/objects/StaffMember)

non-null

    

Represents the data of a staff member who's assigned to a company location.

Show fields

[Anchor to ConsentPolicy](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ConsentPolicy)[ConsentPolicy](/docs/api/admin-
graphql/latest/objects/ConsentPolicy)

•OBJECT

    

A consent policy describes the level of consent that the merchant requires
from the user before actually collecting and processing the data.

Show fields

[Anchor to consentRequired](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ConsentPolicy.fields.consentRequired)consentRequired

•[Boolean](/docs/api/admin-graphql/latest/scalars/Boolean)

    

Whether consent is required for the region.

[Anchor to countryCode](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ConsentPolicy.fields.countryCode)countryCode

•[PrivacyCountryCode](/docs/api/admin-graphql/latest/enums/PrivacyCountryCode)

    

The `ISO 3166` country code for which the policy applies.

Show enum values

[Anchor to dataSaleOptOutRequired](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ConsentPolicy.fields.dataSaleOptOutRequired)dataSaleOptOutRequired

•[Boolean](/docs/api/admin-graphql/latest/scalars/Boolean)

    

Whether data sale opt-out is required for the region.

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
ConsentPolicy.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

The global ID of the consent policy. IDs prefixed with `SD-` are system
default policies.

[Anchor to regionCode](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ConsentPolicy.fields.regionCode)regionCode

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The `ISO 3166` region code for which the policy applies.

[Anchor to shopId](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-ConsentPolicy.fields.shopId)shopId

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

The global ID of the shop that owns the policy.

[Anchor to CurrencyExchangeAdjustment](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
CurrencyExchangeAdjustment)[CurrencyExchangeAdjustment](/docs/api/admin-
graphql/latest/objects/CurrencyExchangeAdjustment)

•OBJECT

    

Represents a currency exchange adjustment applied to an order transaction.

Show fields

[Anchor to adjustment](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
CurrencyExchangeAdjustment.fields.adjustment)adjustment

•[MoneyV2!](/docs/api/admin-graphql/latest/objects/MoneyV2)

non-null

    

The adjustment amount in both shop and presentment currencies.

Show fields

[Anchor to finalAmountSet](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
CurrencyExchangeAdjustment.fields.finalAmountSet)finalAmountSet

•[MoneyV2!](/docs/api/admin-graphql/latest/objects/MoneyV2)

non-null

    

The final amount in both shop and presentment currencies after the adjustment.

Show fields

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
CurrencyExchangeAdjustment.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to originalAmountSet](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
CurrencyExchangeAdjustment.fields.originalAmountSet)originalAmountSet

•[MoneyV2!](/docs/api/admin-graphql/latest/objects/MoneyV2)

non-null

    

The original amount in both shop and presentment currencies before the
adjustment.

Show fields

[Anchor to Customer](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Customer)[Customer](/docs/api/admin-graphql/latest/objects/Customer)

•OBJECT

    

Represents information about a customer of the shop, such as the customer's
contact details, their order history, and whether they've agreed to receive
marketing material by email.

**Caution:** Only use this data if it's required for your app's functionality.
Shopify will restrict [access to scopes](https://shopify.dev/api/usage/access-
scopes) for apps that don't have a legitimate use for the associated data.

Show fields

[Anchor to addresses](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Customer.fields.addresses)addresses

•[[MailingAddress!]!](/docs/api/admin-graphql/latest/objects/MailingAddress)

non-null

    

A list of addresses associated with the customer.

Show fields

[Anchor to addressesV2](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Customer.fields.addressesV2)addressesV2

•[MailingAddressConnection!](/docs/api/admin-
graphql/latest/connections/MailingAddressConnection)

non-null

    

The addresses associated with the customer.

Show fields

[Anchor to amountSpent](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Customer.fields.amountSpent)amountSpent

•[MoneyV2!](/docs/api/admin-graphql/latest/objects/MoneyV2)

non-null

    

The total amount that the customer has spent on orders in their lifetime.

Show fields

[Anchor to canDelete](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Customer.fields.canDelete)canDelete

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether the merchant can delete the customer from their store.

A customer can be deleted from a store only if they haven't yet made an order.
After a customer makes an order, they can't be deleted from a store.

[Anchor to companyContactProfiles](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Customer.fields.companyContactProfiles)companyContactProfiles

•[[CompanyContact!]!](/docs/api/admin-graphql/latest/objects/CompanyContact)

non-null

    

A list of the customer's company contact profiles.

Show fields

[Anchor to createdAt](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Customer.fields.createdAt)createdAt

•[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime)

non-null

    

The date and time when the customer was added to the store.

[Anchor to dataSaleOptOut](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Customer.fields.dataSaleOptOut)dataSaleOptOut

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether the customer has opted out of having their data sold.

[Anchor to defaultAddress](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Customer.fields.defaultAddress)defaultAddress

•[MailingAddress](/docs/api/admin-graphql/latest/objects/MailingAddress)

    

The default address associated with the customer.

Show fields

[Anchor to defaultEmailAddress](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Customer.fields.defaultEmailAddress)defaultEmailAddress

•[CustomerEmailAddress](/docs/api/admin-
graphql/latest/objects/CustomerEmailAddress)

    

The customer's default email address.

Show fields

[Anchor to defaultPhoneNumber](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Customer.fields.defaultPhoneNumber)defaultPhoneNumber

•[CustomerPhoneNumber](/docs/api/admin-
graphql/latest/objects/CustomerPhoneNumber)

    

The customer's default phone number.

Show fields

[Anchor to displayName](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Customer.fields.displayName)displayName

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The full name of the customer, based on the values for first_name and
last_name. If the first_name and last_name are not available, then this falls
back to the customer's email address, and if that is not available, the
customer's phone number.

[Anchor to events](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Customer.fields.events)events

•[EventConnection!](/docs/api/admin-
graphql/latest/connections/EventConnection)

non-null

    

A list of events associated with the customer.

Show fields

[Anchor to firstName](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Customer.fields.firstName)firstName

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The customer's first name.

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
Customer.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to image](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Customer.fields.image)image

•[Image!](/docs/api/admin-graphql/latest/objects/Image)

non-null

    

The image associated with the customer.

Show fields

[Anchor to lastName](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Customer.fields.lastName)lastName

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The customer's last name.

[Anchor to lastOrder](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Customer.fields.lastOrder)lastOrder

•[Order](/docs/api/admin-graphql/latest/objects/Order)

    

The customer's last order.

Show fields

[Anchor to legacyResourceId](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Customer.fields.legacyResourceId)legacyResourceId

•[UnsignedInt64!](/docs/api/admin-graphql/latest/scalars/UnsignedInt64)

non-null

    

The ID of the corresponding resource in the REST Admin API.

[Anchor to lifetimeDuration](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Customer.fields.lifetimeDuration)lifetimeDuration

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The amount of time since the customer was first added to the store.

Example: 'about 12 years'.

[Anchor to locale](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Customer.fields.locale)locale

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The customer's locale.

[Anchor to mergeable](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Customer.fields.mergeable)mergeable

•[CustomerMergeable!](/docs/api/admin-
graphql/latest/objects/CustomerMergeable)

non-null

    

Whether the customer can be merged with another customer.

Show fields

[Anchor to metafield](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Customer.fields.metafield)metafield

•[Metafield](/docs/api/admin-graphql/latest/objects/Metafield)

    

A [custom field](https://shopify.dev/docs/apps/build/custom-data), including
its `namespace` and `key`, that's associated with a Shopify resource for the
purposes of adding and storing additional information.

Show fields

[Anchor to metafields](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Customer.fields.metafields)metafields

•[MetafieldConnection!](/docs/api/admin-
graphql/latest/connections/MetafieldConnection)

non-null

    

A list of [custom fields](https://shopify.dev/docs/apps/build/custom-data)
that a merchant associates with a Shopify resource.

Show fields

[Anchor to multipassIdentifier](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Customer.fields.multipassIdentifier)multipassIdentifier

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

A unique identifier for the customer that's used with Multipass login.

[Anchor to note](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Customer.fields.note)note

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

A note about the customer.

[Anchor to numberOfOrders](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Customer.fields.numberOfOrders)numberOfOrders

•[UnsignedInt64!](/docs/api/admin-graphql/latest/scalars/UnsignedInt64)

non-null

    

The number of orders that the customer has made at the store in their
lifetime.

[Anchor to orders](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Customer.fields.orders)orders

•[OrderConnection!](/docs/api/admin-
graphql/latest/connections/OrderConnection)

non-null

    

A list of the customer's orders.

Show fields

[Anchor to paymentMethods](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Customer.fields.paymentMethods)paymentMethods

•[CustomerPaymentMethodConnection!](/docs/api/admin-
graphql/latest/connections/CustomerPaymentMethodConnection)

non-null

    

A list of the customer's payment methods.

Show fields

[Anchor to productSubscriberStatus](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Customer.fields.productSubscriberStatus)productSubscriberStatus

•[CustomerProductSubscriberStatus!](/docs/api/admin-
graphql/latest/enums/CustomerProductSubscriberStatus)

non-null

    

Possible subscriber states of a customer defined by their subscription
contracts.

Show enum values

[Anchor to state](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Customer.fields.state)state

•[CustomerState!](/docs/api/admin-graphql/latest/enums/CustomerState)

non-null

    

The state of the customer's account with the shop.

Please note that this only meaningful when Classic Customer Accounts is
active.

Show enum values

[Anchor to statistics](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Customer.fields.statistics)statistics

•[CustomerStatistics!](/docs/api/admin-
graphql/latest/objects/CustomerStatistics)

non-null

    

The statistics for a given customer.

Show fields

[Anchor to storeCreditAccounts](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Customer.fields.storeCreditAccounts)storeCreditAccounts

•[StoreCreditAccountConnection!](/docs/api/admin-
graphql/latest/connections/StoreCreditAccountConnection)

non-null

    

Returns a list of store credit accounts that belong to the owner resource. A
store credit account owner can hold multiple accounts each with a different
currency.

Show fields

[Anchor to subscriptionContracts](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Customer.fields.subscriptionContracts)subscriptionContracts

•[SubscriptionContractConnection!](/docs/api/admin-
graphql/latest/connections/SubscriptionContractConnection)

non-null

    

A list of the customer's subscription contracts.

Show fields

[Anchor to tags](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Customer.fields.tags)tags

•[[String!]!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

A comma separated list of tags that have been added to the customer.

[Anchor to taxExempt](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Customer.fields.taxExempt)taxExempt

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether the customer is exempt from being charged taxes on their orders.

[Anchor to taxExemptions](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Customer.fields.taxExemptions)taxExemptions

•[[TaxExemption!]!](/docs/api/admin-graphql/latest/enums/TaxExemption)

non-null

    

The list of tax exemptions applied to the customer.

Show enum values

[Anchor to updatedAt](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Customer.fields.updatedAt)updatedAt

•[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime)

non-null

    

The date and time when the customer was last updated.

[Anchor to verifiedEmail](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Customer.fields.verifiedEmail)verifiedEmail

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether the customer has verified their email address. Defaults to `true` if
the customer is created through the Shopify admin or API.

[Anchor to email](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Customer.fields.email)email

•[String](/docs/api/admin-graphql/latest/scalars/String)

Deprecated

    

[Anchor to emailMarketingConsent](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Customer.fields.emailMarketingConsent)emailMarketingConsent

•[CustomerEmailMarketingConsentState](/docs/api/admin-
graphql/latest/objects/CustomerEmailMarketingConsentState)

Deprecated

    

Show fields

[Anchor to hasTimelineComment](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Customer.fields.hasTimelineComment)hasTimelineComment

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-nullDeprecated

    

[Anchor to market](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Customer.fields.market)market

•[Market](/docs/api/admin-graphql/latest/objects/Market)

Deprecated

    

Show fields

[Anchor to metafieldDefinitions](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Customer.fields.metafieldDefinitions)metafieldDefinitions

•[MetafieldDefinitionConnection!](/docs/api/admin-
graphql/latest/connections/MetafieldDefinitionConnection)

non-nullDeprecated

    

Show fields

[Anchor to phone](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Customer.fields.phone)phone

•[String](/docs/api/admin-graphql/latest/scalars/String)

Deprecated

    

[Anchor to smsMarketingConsent](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Customer.fields.smsMarketingConsent)smsMarketingConsent

•[CustomerSmsMarketingConsentState](/docs/api/admin-
graphql/latest/objects/CustomerSmsMarketingConsentState)

Deprecated

    

Show fields

[Anchor to unsubscribeUrl](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Customer.fields.unsubscribeUrl)unsubscribeUrl

•[URL!](/docs/api/admin-graphql/latest/scalars/URL)

non-nullDeprecated

    

[Anchor to validEmailAddress](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Customer.fields.validEmailAddress)validEmailAddress

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-nullDeprecated

    

[Anchor to CustomerAccountAppExtensionPage](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
CustomerAccountAppExtensionPage)[CustomerAccountAppExtensionPage](/docs/api/admin-
graphql/latest/objects/CustomerAccountAppExtensionPage)

•OBJECT

    

An app extension page for the customer account navigation menu.

Show fields

[Anchor to appExtensionUuid](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
CustomerAccountAppExtensionPage.fields.appExtensionUuid)appExtensionUuid

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The UUID of the app extension.

[Anchor to defaultCursor](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
CustomerAccountAppExtensionPage.fields.defaultCursor)defaultCursor

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

A default [cursor](https://shopify.dev/api/usage/pagination-graphql) that
returns the single next record, sorted ascending by ID.

[Anchor to handle](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-CustomerAccountAppExtensionPage.fields.handle)handle

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

A unique, human-friendly string for the customer account page.

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
CustomerAccountAppExtensionPage.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

The unique ID for the customer account page.

[Anchor to title](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-CustomerAccountAppExtensionPage.fields.title)title

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The title of the customer account page.

[Anchor to CustomerAccountNativePage](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
CustomerAccountNativePage)[CustomerAccountNativePage](/docs/api/admin-
graphql/latest/objects/CustomerAccountNativePage)

•OBJECT

    

A native page for the customer account navigation menu.

Show fields

[Anchor to defaultCursor](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
CustomerAccountNativePage.fields.defaultCursor)defaultCursor

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

A default [cursor](https://shopify.dev/api/usage/pagination-graphql) that
returns the single next record, sorted ascending by ID.

[Anchor to handle](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-CustomerAccountNativePage.fields.handle)handle

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

A unique, human-friendly string for the customer account page.

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
CustomerAccountNativePage.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

The unique ID for the customer account page.

[Anchor to pageType](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-CustomerAccountNativePage.fields.pageType)pageType

•[CustomerAccountNativePagePageType!](/docs/api/admin-
graphql/latest/enums/CustomerAccountNativePagePageType)

non-null

    

The type of customer account native page.

Show enum values

[Anchor to title](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-CustomerAccountNativePage.fields.title)title

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The title of the customer account page.

[Anchor to CustomerPaymentMethod](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
CustomerPaymentMethod)[CustomerPaymentMethod](/docs/api/admin-
graphql/latest/objects/CustomerPaymentMethod)

•OBJECT

    

A customer's payment method.

Show fields

[Anchor to customer](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-CustomerPaymentMethod.fields.customer)customer

•[Customer](/docs/api/admin-graphql/latest/objects/Customer)

    

The customer to whom the payment method belongs.

Show fields

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
CustomerPaymentMethod.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

The ID of this payment method.

[Anchor to instrument](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
CustomerPaymentMethod.fields.instrument)instrument

•[CustomerPaymentInstrument](/docs/api/admin-
graphql/latest/unions/CustomerPaymentInstrument)

    

The instrument for this payment method.

Show union types

[Anchor to mandates](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-CustomerPaymentMethod.fields.mandates)mandates

•[PaymentMandateResourceConnection!](/docs/api/admin-
graphql/latest/connections/PaymentMandateResourceConnection)

non-null

    

The mandates associated with the payment method.

Show fields

[Anchor to revokedAt](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-CustomerPaymentMethod.fields.revokedAt)revokedAt

•[DateTime](/docs/api/admin-graphql/latest/scalars/DateTime)

    

The time that the payment method was revoked.

[Anchor to revokedReason](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
CustomerPaymentMethod.fields.revokedReason)revokedReason

•[CustomerPaymentMethodRevocationReason](/docs/api/admin-
graphql/latest/enums/CustomerPaymentMethodRevocationReason)

    

The revocation reason for this payment method.

Show enum values

[Anchor to subscriptionContracts](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
CustomerPaymentMethod.fields.subscriptionContracts)subscriptionContracts

•[SubscriptionContractConnection!](/docs/api/admin-
graphql/latest/connections/SubscriptionContractConnection)

non-null

    

List Subscription Contracts.

Show fields

[Anchor to CustomerSegmentMembersQuery](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
CustomerSegmentMembersQuery)[CustomerSegmentMembersQuery](/docs/api/admin-
graphql/latest/objects/CustomerSegmentMembersQuery)

•OBJECT

    

A job to determine a list of members, such as customers, that are associated
with an individual segment.

Show fields

[Anchor to currentCount](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
CustomerSegmentMembersQuery.fields.currentCount)currentCount

•[Int!](/docs/api/admin-graphql/latest/scalars/Int)

non-null

    

The current total number of members in a given segment.

[Anchor to done](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-CustomerSegmentMembersQuery.fields.done)done

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

This indicates if the job is still queued or has been run.

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
CustomerSegmentMembersQuery.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID that's returned when running an asynchronous mutation.

[Anchor to CustomerVisit](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
CustomerVisit)[CustomerVisit](/docs/api/admin-
graphql/latest/objects/CustomerVisit)

•OBJECT

    

Represents a customer's session visiting a shop's online store, including
information about the marketing activity attributed to starting the session.

Show fields

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
CustomerVisit.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to landingPage](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
CustomerVisit.fields.landingPage)landingPage

•[URL](/docs/api/admin-graphql/latest/scalars/URL)

    

URL of the first page the customer landed on for the session.

[Anchor to landingPageHtml](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
CustomerVisit.fields.landingPageHtml)landingPageHtml

•[HTML](/docs/api/admin-graphql/latest/scalars/HTML)

    

Landing page information with URL linked in HTML. For example, the first page
the customer visited was store.myshopify.com/products/1.

[Anchor to marketingEvent](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
CustomerVisit.fields.marketingEvent)marketingEvent

•[MarketingEvent](/docs/api/admin-graphql/latest/objects/MarketingEvent)

    

Represent actions taken by an app, on behalf of a merchant, to market Shopify
resources such as products, collections, and discounts.

Show fields

[Anchor to occurredAt](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
CustomerVisit.fields.occurredAt)occurredAt

•[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime)

non-null

    

The date and time when the customer's session occurred.

[Anchor to referralCode](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
CustomerVisit.fields.referralCode)referralCode

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

Marketing referral code from the link that the customer clicked to visit the
store. Supports the following URL attributes: _ref_ , _source_ , or _r_. For
example, if the URL is myshopifystore.com/products/slide?ref=j2tj1tn2, then
this value is j2tj1tn2.

[Anchor to referralInfoHtml](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
CustomerVisit.fields.referralInfoHtml)referralInfoHtml

•[FormattedString!](/docs/api/admin-graphql/latest/scalars/FormattedString)

non-null

    

Referral information with URLs linked in HTML.

[Anchor to referrerUrl](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
CustomerVisit.fields.referrerUrl)referrerUrl

•[URL](/docs/api/admin-graphql/latest/scalars/URL)

    

Webpage where the customer clicked a link that sent them to the online store.
For example, _<https://randomblog.com/page1>_ or _android-
app://com.google.android.gm_.

[Anchor to source](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-CustomerVisit.fields.source)source

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

Source from which the customer visited the store, such as a platform
(Facebook, Google), email, direct, a website domain, QR code, or unknown.

[Anchor to sourceDescription](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
CustomerVisit.fields.sourceDescription)sourceDescription

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

Describes the source explicitly for first or last session.

[Anchor to sourceType](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
CustomerVisit.fields.sourceType)sourceType

•[MarketingTactic](/docs/api/admin-graphql/latest/enums/MarketingTactic)

    

Type of marketing tactic.

Show enum values

[Anchor to utmParameters](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
CustomerVisit.fields.utmParameters)utmParameters

•[UTMParameters](/docs/api/admin-graphql/latest/objects/UTMParameters)

    

A set of UTM parameters gathered from the URL parameters of the referrer.

Show fields

[Anchor to DeliveryCarrierService](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DeliveryCarrierService)[DeliveryCarrierService](/docs/api/admin-
graphql/latest/objects/DeliveryCarrierService)

•OBJECT

    

A carrier service (also known as a carrier calculated service or shipping
service) provides real-time shipping rates to Shopify. Some common carrier
services include Canada Post, FedEx, UPS, and USPS. The term **carrier** is
often used interchangeably with the terms **shipping company** and **rate
provider**.

Using the CarrierService resource, you can add a carrier service to a shop and
then provide a list of applicable shipping rates at checkout. You can even use
the cart data to adjust shipping rates and offer shipping discounts based on
what is in the customer's cart.

## Requirements for accessing the CarrierService resource

To access the CarrierService resource, add the `write_shipping` permission to
your app's requested scopes. For more information, see [API access
scopes](https://shopify.dev/docs/admin-api/access-scopes).

Your app's request to create a carrier service will fail unless the store
installing your carrier service meets one of the following requirements:

  * It's on the Advanced Shopify plan or higher.
  * It's on the Shopify plan with yearly billing, or the carrier service feature has been added to the store for a monthly fee. For more information, contact [Shopify Support](https://help.shopify.com/questions).
  * It's a development store.

* * *

Note

If a store changes its Shopify plan, then the store's association with a
carrier service is deactivated if the store no long meets one of the
requirements above.

* * *

## Providing shipping rates to Shopify

When adding a carrier service to a store, you need to provide a POST endpoint
rooted in the `callbackUrl` property where Shopify can retrieve applicable
shipping rates. The callback URL should be a public endpoint that expects
these requests from Shopify.

### Example shipping rate request sent to a carrier service

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

20

21

22

23

24

25

26

27

28

29

30

31

32

33

34

35

36

37

38

39

40

41

42

43

44

45

46

47

48

49

50

{

"rate": {

"origin": {

"country": "CA",

"postal_code": "K2P1L4",

"province": "ON",

"city": "Ottawa",

"name": null,

"address1": "150 Elgin St.",

"address2": "",

"address3": null,

"phone": null,

"fax": null,

"email": null,

"address_type": null,

"company_name": "Jamie D's Emporium"

},

"destination": {

"country": "CA",

"postal_code": "K1M1M4",

"province": "ON",

"city": "Ottawa",

"name": "Bob Norman",

"address1": "24 Sussex Dr.",

"address2": "",

"address3": null,

"phone": null,

"fax": null,

"email": null,

"address_type": null,

"company_name": null

},

"items": [{

"name": "Short Sleeve T-Shirt",

"sku": "",

"quantity": 1,

"grams": 1000,

"price": 1999,

"vendor": "Jamie D's Emporium",

"requires_shipping": true,

"taxable": true,

"fulfillment_service": "manual",

"properties": null,

"product_id": 48447225880,

"variant_id": 258644705304

}],

"currency": "USD",

"locale": "en"

}

}

### Example response

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

20

21

22

23

24

25

26

27

28

29

{

"rates": [

{

"service_name": "canadapost-overnight",

"service_code": "ON",

"total_price": "1295",

"description": "This is the fastest option by far",

"currency": "CAD",

"min_delivery_date": "2013-04-12 14:48:45 -0400",

"max_delivery_date": "2013-04-12 14:48:45 -0400"

},

{

"service_name": "fedex-2dayground",

"service_code": "2D",

"total_price": "2934",

"currency": "USD",

"min_delivery_date": "2013-04-12 14:48:45 -0400",

"max_delivery_date": "2013-04-12 14:48:45 -0400"

},

{

"service_name": "fedex-priorityovernight",

"service_code": "1D",

"total_price": "3587",

"currency": "USD",

"min_delivery_date": "2013-04-12 14:48:45 -0400",

"max_delivery_date": "2013-04-12 14:48:45 -0400"

}

]

}

The `address3`, `fax`, `address_type`, and `company_name` fields are returned
by specific [ActiveShipping](https://github.com/Shopify/active_shipping)
providers. For API-created carrier services, you should use only the following
shipping address fields:

  * `address1`
  * `address2`
  * `city`
  * `zip`
  * `province`
  * `country`

Other values remain as `null` and are not sent to the callback URL.

### Response fields

When Shopify requests shipping rates using your callback URL, the response
object `rates` must be a JSON array of objects with the following fields.
Required fields must be included in the response for the carrier service
integration to work properly.

Field| Required| Description  
---|---|---  
`service_name`| Yes| The name of the rate, which customers see at checkout.
For example: `Expedited Mail`.  
`description`| Yes| A description of the rate, which customers see at
checkout. For example: `Includes tracking and insurance`.  
`service_code`| Yes| A unique code associated with the rate. For example:
`expedited_mail`.  
`currency`| Yes| The currency of the shipping rate.  
`total_price`| Yes| The total price expressed in subunits. If the currency
doesn't use subunits, then the value must be multiplied by 100. For example:
`"total_price": 500` for 5.00 CAD, `"total_price": 100000` for 1000 JPY.  
`phone_required`| No| Whether the customer must provide a phone number at
checkout.  
`min_delivery_date`| No| The earliest delivery date for the displayed rate.  
`max_delivery_date`| No| The latest delivery date for the displayed rate to
still be valid.  
  
### Special conditions

  * To indicate that this carrier service cannot handle this shipping request, return an empty array and any successful (20x) HTTP code.
  * To force backup rates instead, return a 40x or 50x HTTP code with any content. A good choice is the regular 404 Not Found code.
  * Redirects (30x codes) will only be followed for the same domain as the original callback URL. Attempting to redirect to a different domain will trigger backup rates.
  * There is no retry mechanism. The response must be successful on the first try, within the time budget listed below. Timeouts or errors will trigger backup rates.

## Response Timeouts

The read timeout for rate requests are dynamic, based on the number of
requests per minute (RPM). These limits are applied to each shop-app pair. The
timeout values are as follows.

RPM Range| Timeout  
---|---  
Under 1500| 10s  
1500 to 3000| 5s  
Over 3000| 3s  
  
* * *

Note

These values are upper limits and should not be interpretted as a goal to
develop towards. Shopify is constantly evaluating the performance of the
platform and working towards improving resilience as well as app capabilities.
As such, these numbers may be adjusted outside of our normal versioning
timelines.

* * *

## Server-side caching of requests

Shopify provides server-side caching to reduce the number of requests it
makes. Any shipping rate request that identically matches the following fields
will be retrieved from Shopify's cache of the initial response:

  * variant IDs
  * default shipping box weight and dimensions
  * variant quantities
  * carrier service ID
  * origin address
  * destination address
  * item weights and signatures

If any of these fields differ, or if the cache has expired since the original
request, then new shipping rates are requested. The cache expires 15 minutes
after rates are successfully returned. If an error occurs, then the cache
expires after 30 seconds.

Show fields

[Anchor to active](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-DeliveryCarrierService.fields.active)active

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether the carrier service is active.

[Anchor to availableServicesForCountries](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DeliveryCarrierService.fields.availableServicesForCountries)availableServicesForCountries

•[[DeliveryAvailableService!]!](/docs/api/admin-
graphql/latest/objects/DeliveryAvailableService)

non-null

    

The list of services offered for given destinations.

Show fields

[Anchor to callbackUrl](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DeliveryCarrierService.fields.callbackUrl)callbackUrl

•[URL](/docs/api/admin-graphql/latest/scalars/URL)

    

The URL endpoint that Shopify needs to retrieve shipping rates.

[Anchor to formattedName](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DeliveryCarrierService.fields.formattedName)formattedName

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The properly formatted name of the shipping service provider, ready to
display.

[Anchor to icon](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-DeliveryCarrierService.fields.icon)icon

•[Image!](/docs/api/admin-graphql/latest/objects/Image)

non-null

    

The logo of the service provider.

Show fields

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
DeliveryCarrierService.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to name](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-DeliveryCarrierService.fields.name)name

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The name of the shipping service provider.

[Anchor to supportsServiceDiscovery](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DeliveryCarrierService.fields.supportsServiceDiscovery)supportsServiceDiscovery

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether merchants are able to send dummy data to your service through the
Shopify admin to see shipping rate examples.

[Anchor to DeliveryCondition](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DeliveryCondition)[DeliveryCondition](/docs/api/admin-
graphql/latest/objects/DeliveryCondition)

•OBJECT

    

A condition that must pass for a delivery method definition to be applied to
an order.

Show fields

[Anchor to conditionCriteria](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DeliveryCondition.fields.conditionCriteria)conditionCriteria

•[DeliveryConditionCriteria!](/docs/api/admin-
graphql/latest/unions/DeliveryConditionCriteria)

non-null

    

The value (weight or price) that the condition field is compared to.

Show union types

[Anchor to field](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-DeliveryCondition.fields.field)field

•[DeliveryConditionField!](/docs/api/admin-
graphql/latest/enums/DeliveryConditionField)

non-null

    

The field to compare the criterion value against, using the operator.

Show enum values

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
DeliveryCondition.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to operator](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-DeliveryCondition.fields.operator)operator

•[DeliveryConditionOperator!](/docs/api/admin-
graphql/latest/enums/DeliveryConditionOperator)

non-null

    

The operator to compare the field and criterion value.

Show enum values

[Anchor to DeliveryCountry](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DeliveryCountry)[DeliveryCountry](/docs/api/admin-
graphql/latest/objects/DeliveryCountry)

•OBJECT

    

A country that is used to define a shipping zone.

Show fields

[Anchor to code](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-DeliveryCountry.fields.code)code

•[DeliveryCountryCodeOrRestOfWorld!](/docs/api/admin-
graphql/latest/objects/DeliveryCountryCodeOrRestOfWorld)

non-null

    

A two-letter country code in ISO 3166-1 alpha-2 standard. It also includes a
flag indicating whether the country should be a part of the 'Rest Of World'
shipping zone.

Show fields

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
DeliveryCountry.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to name](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-DeliveryCountry.fields.name)name

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The full name of the country.

[Anchor to provinces](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-DeliveryCountry.fields.provinces)provinces

•[[DeliveryProvince!]!](/docs/api/admin-
graphql/latest/objects/DeliveryProvince)

non-null

    

The list of regions associated with this country.

Show fields

[Anchor to translatedName](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DeliveryCountry.fields.translatedName)translatedName

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The translated name of the country. The translation returned is based on the
system's locale.

[Anchor to DeliveryCustomization](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DeliveryCustomization)[DeliveryCustomization](/docs/api/admin-
graphql/latest/objects/DeliveryCustomization)

•OBJECT

    

A delivery customization.

Show fields

[Anchor to enabled](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-DeliveryCustomization.fields.enabled)enabled

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

The enabled status of the delivery customization.

[Anchor to errorHistory](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DeliveryCustomization.fields.errorHistory)errorHistory

•[FunctionsErrorHistory](/docs/api/admin-
graphql/latest/objects/FunctionsErrorHistory)

    

The error history on the most recent version of the delivery customization.

Show fields

[Anchor to functionId](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DeliveryCustomization.fields.functionId)functionId

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The ID of the Shopify Function implementing the delivery customization.

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
DeliveryCustomization.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to metafield](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-DeliveryCustomization.fields.metafield)metafield

•[Metafield](/docs/api/admin-graphql/latest/objects/Metafield)

    

A [custom field](https://shopify.dev/docs/apps/build/custom-data), including
its `namespace` and `key`, that's associated with a Shopify resource for the
purposes of adding and storing additional information.

Show fields

[Anchor to metafields](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DeliveryCustomization.fields.metafields)metafields

•[MetafieldConnection!](/docs/api/admin-
graphql/latest/connections/MetafieldConnection)

non-null

    

A list of [custom fields](https://shopify.dev/docs/apps/build/custom-data)
that a merchant associates with a Shopify resource.

Show fields

[Anchor to shopifyFunction](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DeliveryCustomization.fields.shopifyFunction)shopifyFunction

•[ShopifyFunction!](/docs/api/admin-graphql/latest/objects/ShopifyFunction)

non-null

    

The Shopify Function implementing the delivery customization.

Show fields

[Anchor to title](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-DeliveryCustomization.fields.title)title

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The title of the delivery customization.

[Anchor to metafieldDefinitions](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DeliveryCustomization.fields.metafieldDefinitions)metafieldDefinitions

•[MetafieldDefinitionConnection!](/docs/api/admin-
graphql/latest/connections/MetafieldDefinitionConnection)

non-nullDeprecated

    

Show fields

[Anchor to DeliveryLocationGroup](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DeliveryLocationGroup)[DeliveryLocationGroup](/docs/api/admin-
graphql/latest/objects/DeliveryLocationGroup)

•OBJECT

    

A location group is a collection of locations. They share zones and delivery
methods across delivery profiles.

Show fields

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
DeliveryLocationGroup.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to locations](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-DeliveryLocationGroup.fields.locations)locations

•[LocationConnection!](/docs/api/admin-
graphql/latest/connections/LocationConnection)

non-null

    

A list of all locations that are part of this location group.

Show fields

[Anchor to locationsCount](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DeliveryLocationGroup.fields.locationsCount)locationsCount

•[Count](/docs/api/admin-graphql/latest/objects/Count)

    

A count of all locations that are part of this location group.

Show fields

[Anchor to DeliveryMethod](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DeliveryMethod)[DeliveryMethod](/docs/api/admin-
graphql/latest/objects/DeliveryMethod)

•OBJECT

    

The delivery method used by a fulfillment order.

Show fields

[Anchor to additionalInformation](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DeliveryMethod.fields.additionalInformation)additionalInformation

•[DeliveryMethodAdditionalInformation](/docs/api/admin-
graphql/latest/objects/DeliveryMethodAdditionalInformation)

    

The Additional information to consider when performing the delivery.

Show fields

[Anchor to brandedPromise](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DeliveryMethod.fields.brandedPromise)brandedPromise

•[DeliveryBrandedPromise](/docs/api/admin-
graphql/latest/objects/DeliveryBrandedPromise)

    

The branded promise that was presented to the buyer during checkout. For
example: Shop Promise.

Show fields

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
DeliveryMethod.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to maxDeliveryDateTime](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DeliveryMethod.fields.maxDeliveryDateTime)maxDeliveryDateTime

•[DateTime](/docs/api/admin-graphql/latest/scalars/DateTime)

    

The latest delivery date and time when the fulfillment is expected to arrive
at the buyer's location.

[Anchor to methodType](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DeliveryMethod.fields.methodType)methodType

•[DeliveryMethodType!](/docs/api/admin-
graphql/latest/enums/DeliveryMethodType)

non-null

    

The type of the delivery method.

Show enum values

[Anchor to minDeliveryDateTime](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DeliveryMethod.fields.minDeliveryDateTime)minDeliveryDateTime

•[DateTime](/docs/api/admin-graphql/latest/scalars/DateTime)

    

The earliest delivery date and time when the fulfillment is expected to arrive
at the buyer's location.

[Anchor to presentedName](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DeliveryMethod.fields.presentedName)presentedName

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The name of the delivery option that was presented to the buyer during
checkout.

[Anchor to serviceCode](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DeliveryMethod.fields.serviceCode)serviceCode

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

A reference to the shipping method.

[Anchor to sourceReference](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DeliveryMethod.fields.sourceReference)sourceReference

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

Source reference is promise provider specific data associated with delivery
promise.

[Anchor to DeliveryMethodDefinition](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DeliveryMethodDefinition)[DeliveryMethodDefinition](/docs/api/admin-
graphql/latest/objects/DeliveryMethodDefinition)

•OBJECT

    

A method definition contains the delivery rate and the conditions that must be
met for the method to be applied.

Show fields

[Anchor to active](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-DeliveryMethodDefinition.fields.active)active

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether this method definition is active.

[Anchor to description](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DeliveryMethodDefinition.fields.description)description

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The description of the method definition. Only available on shipping rates
that are custom.

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
DeliveryMethodDefinition.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to methodConditions](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DeliveryMethodDefinition.fields.methodConditions)methodConditions

•[[DeliveryCondition!]!](/docs/api/admin-
graphql/latest/objects/DeliveryCondition)

non-null

    

The method conditions that must pass for this method definition to be applied
to an order.

Show fields

[Anchor to name](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-DeliveryMethodDefinition.fields.name)name

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The name of the method definition.

[Anchor to rateProvider](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DeliveryMethodDefinition.fields.rateProvider)rateProvider

•[DeliveryRateProvider!](/docs/api/admin-
graphql/latest/unions/DeliveryRateProvider)

non-null

    

The provided rate for this method definition, from a rate definition or
participant.

Show union types

[Anchor to DeliveryParticipant](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DeliveryParticipant)[DeliveryParticipant](/docs/api/admin-
graphql/latest/objects/DeliveryParticipant)

•OBJECT

    

A participant defines carrier-calculated rates for shipping services with a
possible merchant-defined fixed fee or a percentage-of-rate fee.

Show fields

[Anchor to adaptToNewServicesFlag](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DeliveryParticipant.fields.adaptToNewServicesFlag)adaptToNewServicesFlag

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether to display new shipping services automatically to the customer when
the service becomes available.

[Anchor to carrierService](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DeliveryParticipant.fields.carrierService)carrierService

•[DeliveryCarrierService!](/docs/api/admin-
graphql/latest/objects/DeliveryCarrierService)

non-null

    

The carrier used for this participant.

Show fields

[Anchor to fixedFee](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-DeliveryParticipant.fields.fixedFee)fixedFee

•[MoneyV2](/docs/api/admin-graphql/latest/objects/MoneyV2)

    

The merchant-defined fixed fee for this participant.

Show fields

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
DeliveryParticipant.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to participantServices](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DeliveryParticipant.fields.participantServices)participantServices

•[[DeliveryParticipantService!]!](/docs/api/admin-
graphql/latest/objects/DeliveryParticipantService)

non-null

    

The carrier-specific services offered by the participant, and whether each
service is active.

Show fields

[Anchor to percentageOfRateFee](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DeliveryParticipant.fields.percentageOfRateFee)percentageOfRateFee

•[Float!](/docs/api/admin-graphql/latest/scalars/Float)

non-null

    

The merchant-defined percentage-of-rate fee for this participant.

[Anchor to DeliveryProfile](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DeliveryProfile)[DeliveryProfile](/docs/api/admin-
graphql/latest/objects/DeliveryProfile)

•OBJECT

    

A shipping profile. In Shopify, a shipping profile is a set of shipping rates
scoped to a set of products or variants that can be shipped from selected
locations to zones. Learn more about [building with delivery
profiles](https://shopify.dev/apps/build/purchase-options/deferred/delivery-
and-deferment/build-delivery-profiles).

Show fields

[Anchor to activeMethodDefinitionsCount](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DeliveryProfile.fields.activeMethodDefinitionsCount)activeMethodDefinitionsCount

•[Int!](/docs/api/admin-graphql/latest/scalars/Int)

non-null

    

The number of active shipping rates for the profile.

[Anchor to default](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-DeliveryProfile.fields.default)default

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether this is the default profile.

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
DeliveryProfile.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to legacyMode](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DeliveryProfile.fields.legacyMode)legacyMode

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether this shop has enabled legacy compatibility mode for delivery profiles.

[Anchor to locationsWithoutRatesCount](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DeliveryProfile.fields.locationsWithoutRatesCount)locationsWithoutRatesCount

•[Int!](/docs/api/admin-graphql/latest/scalars/Int)

non-null

    

The number of locations without rates defined.

[Anchor to name](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-DeliveryProfile.fields.name)name

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The name of the delivery profile.

[Anchor to originLocationCount](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DeliveryProfile.fields.originLocationCount)originLocationCount

•[Int!](/docs/api/admin-graphql/latest/scalars/Int)

non-null

    

The number of active origin locations for the profile.

[Anchor to productVariantsCount](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DeliveryProfile.fields.productVariantsCount)productVariantsCount

•[Count](/docs/api/admin-graphql/latest/objects/Count)

    

How many product variants are in this profile.

Show fields

[Anchor to profileItems](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DeliveryProfile.fields.profileItems)profileItems

•[DeliveryProfileItemConnection!](/docs/api/admin-
graphql/latest/connections/DeliveryProfileItemConnection)

non-null

    

The products and variants associated with this profile.

Show fields

[Anchor to profileLocationGroups](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DeliveryProfile.fields.profileLocationGroups)profileLocationGroups

•[[DeliveryProfileLocationGroup!]!](/docs/api/admin-
graphql/latest/objects/DeliveryProfileLocationGroup)

non-null

    

The location groups and associated zones using this profile.

Show fields

[Anchor to sellingPlanGroups](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DeliveryProfile.fields.sellingPlanGroups)sellingPlanGroups

•[SellingPlanGroupConnection!](/docs/api/admin-
graphql/latest/connections/SellingPlanGroupConnection)

non-null

    

Selling plan groups associated with the specified delivery profile.

Show fields

[Anchor to unassignedLocations](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DeliveryProfile.fields.unassignedLocations)unassignedLocations

•[[Location!]!](/docs/api/admin-graphql/latest/objects/Location)

non-null

    

List of locations that haven't been assigned to a location group for this
profile.

Show fields

[Anchor to unassignedLocationsPaginated](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DeliveryProfile.fields.unassignedLocationsPaginated)unassignedLocationsPaginated

•[LocationConnection!](/docs/api/admin-
graphql/latest/connections/LocationConnection)

non-null

    

List of locations that have not been assigned to a location group for this
profile.

Show fields

[Anchor to version](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-DeliveryProfile.fields.version)version

•[Int!](/docs/api/admin-graphql/latest/scalars/Int)

non-null

    

The version of the delivery profile.

[Anchor to zoneCountryCount](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DeliveryProfile.fields.zoneCountryCount)zoneCountryCount

•[Int!](/docs/api/admin-graphql/latest/scalars/Int)

non-null

    

The number of countries with active rates to deliver to.

[Anchor to productVariantsCountV2](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DeliveryProfile.fields.productVariantsCountV2)productVariantsCountV2

•[DeliveryProductVariantsCount!](/docs/api/admin-
graphql/latest/objects/DeliveryProductVariantsCount)

non-nullDeprecated

    

Show fields

[Anchor to DeliveryProfileItem](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DeliveryProfileItem)[DeliveryProfileItem](/docs/api/admin-
graphql/latest/objects/DeliveryProfileItem)

•OBJECT

    

A product and the subset of associated variants that are part of this delivery
profile.

Show fields

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
DeliveryProfileItem.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to product](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-DeliveryProfileItem.fields.product)product

•[Product!](/docs/api/admin-graphql/latest/objects/Product)

non-null

    

A product associated with this profile.

Show fields

[Anchor to variants](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-DeliveryProfileItem.fields.variants)variants

•[ProductVariantConnection!](/docs/api/admin-
graphql/latest/connections/ProductVariantConnection)

non-null

    

The product variants associated with this delivery profile.

Show fields

[Anchor to DeliveryPromiseParticipant](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DeliveryPromiseParticipant)[DeliveryPromiseParticipant](/docs/api/admin-
graphql/latest/objects/DeliveryPromiseParticipant)

•OBJECT

    

Returns enabled delivery promise participants.

Show fields

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
DeliveryPromiseParticipant.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

The ID of the promise participant.

[Anchor to owner](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-DeliveryPromiseParticipant.fields.owner)owner

•[DeliveryPromiseParticipantOwner](/docs/api/admin-
graphql/latest/unions/DeliveryPromiseParticipantOwner)

    

The resource that the participant is attached to.

Show union types

[Anchor to ownerType](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-DeliveryPromiseParticipant.fields.ownerType)ownerType

•[DeliveryPromiseParticipantOwnerType!](/docs/api/admin-
graphql/latest/enums/DeliveryPromiseParticipantOwnerType)

non-null

    

The owner type of the participant.

Show enum values

[Anchor to DeliveryPromiseProvider](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DeliveryPromiseProvider)[DeliveryPromiseProvider](/docs/api/admin-
graphql/latest/objects/DeliveryPromiseProvider)

•OBJECT

    

A delivery promise provider. Currently restricted to select approved delivery
promise partners.

Show fields

[Anchor to active](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-DeliveryPromiseProvider.fields.active)active

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether the delivery promise provider is active. Defaults to `true` when
creating a provider.

[Anchor to fulfillmentDelay](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DeliveryPromiseProvider.fields.fulfillmentDelay)fulfillmentDelay

•[Int](/docs/api/admin-graphql/latest/scalars/Int)

    

The number of seconds to add to the current time as a buffer when looking up
delivery promises. Represents how long the shop requires before releasing an
order to the fulfillment provider.

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
DeliveryPromiseProvider.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to location](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-DeliveryPromiseProvider.fields.location)location

•[Location!](/docs/api/admin-graphql/latest/objects/Location)

non-null

    

The location associated with this delivery promise provider.

Show fields

[Anchor to timeZone](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-DeliveryPromiseProvider.fields.timeZone)timeZone

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The time zone to be used for interpreting day of week and cutoff times in
delivery schedules when looking up delivery promises.

[Anchor to DeliveryProvince](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DeliveryProvince)[DeliveryProvince](/docs/api/admin-
graphql/latest/objects/DeliveryProvince)

•OBJECT

    

A region that is used to define a shipping zone.

Show fields

[Anchor to code](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-DeliveryProvince.fields.code)code

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The code of the region.

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
DeliveryProvince.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to name](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-DeliveryProvince.fields.name)name

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The full name of the region.

[Anchor to translatedName](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DeliveryProvince.fields.translatedName)translatedName

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The translated name of the region. The translation returned is based on the
system's locale.

[Anchor to DeliveryRateDefinition](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DeliveryRateDefinition)[DeliveryRateDefinition](/docs/api/admin-
graphql/latest/objects/DeliveryRateDefinition)

•OBJECT

    

The merchant-defined rate of the
[DeliveryMethodDefinition](https://shopify.dev/api/admin-
graphql/latest/objects/DeliveryMethodDefinition).

Show fields

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
DeliveryRateDefinition.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to price](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-DeliveryRateDefinition.fields.price)price

•[MoneyV2!](/docs/api/admin-graphql/latest/objects/MoneyV2)

non-null

    

The price of this rate.

Show fields

[Anchor to DeliveryZone](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DeliveryZone)[DeliveryZone](/docs/api/admin-
graphql/latest/objects/DeliveryZone)

•OBJECT

    

A zone is a group of countries that have the same shipping rates. Customers
can order products from a store only if they choose a shipping destination
that's included in one of the store's zones.

Show fields

[Anchor to countries](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-DeliveryZone.fields.countries)countries

•[[DeliveryCountry!]!](/docs/api/admin-graphql/latest/objects/DeliveryCountry)

non-null

    

The list of countries within the zone.

Show fields

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
DeliveryZone.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to name](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-DeliveryZone.fields.name)name

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The name of the zone.

[Anchor to DiscountAutomaticBxgy](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DiscountAutomaticBxgy)[DiscountAutomaticBxgy](/docs/api/admin-
graphql/latest/objects/DiscountAutomaticBxgy)

•OBJECT

    

The `DiscountAutomaticBxgy` object lets you manage [buy X get Y discounts
(BXGY)](https://help.shopify.com/manual/discounts/discount-types/buy-x-get-y)
that are automatically applied on a cart and at checkout. BXGY discounts
incentivize customers by offering them additional items at a discounted price
or for free when they purchase a specified quantity of items.

The `DiscountAutomaticBxgy` object stores information about automatic BXGY
discounts that apply to specific [products and
variants](https://shopify.dev/docs/api/admin-
graphql/latest/objects/DiscountProducts),
[collections](https://shopify.dev/docs/api/admin-
graphql/latest/objects/DiscountCollections), or [all items in a
cart](https://shopify.dev/docs/api/admin-
graphql/latest/objects/AllDiscountItems).

Learn more about working with [Shopify's discount
model](https://shopify.dev/docs/apps/build/discounts), including limitations
and considerations.

* * *

Note

The [`DiscountCodeBxgy`](https://shopify.dev/docs/api/admin-
graphql/latest/objects/DiscountCodeBxgy) object has similar functionality to
the `DiscountAutomaticBxgy` object, but customers need to enter a code to
receive a discount.

API versions prior to `2025-10` only return automatic discounts with `context`
set to `all`, discounts with other values are filtered out.

* * *

Show fields

[Anchor to asyncUsageCount](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DiscountAutomaticBxgy.fields.asyncUsageCount)asyncUsageCount

•[Int!](/docs/api/admin-graphql/latest/scalars/Int)

non-null

    

The number of times that the discount has been used. For example, if a "Buy 3,
Get 1 Free" t-shirt discount is automatically applied in 200 transactions,
then the discount has been used 200 times. This value is updated
asynchronously. As a result, it might be lower than the actual usage count
until the asynchronous process is completed.

[Anchor to combinesWith](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DiscountAutomaticBxgy.fields.combinesWith)combinesWith

•[DiscountCombinesWith!](/docs/api/admin-
graphql/latest/objects/DiscountCombinesWith)

non-null

    

The [discount classes](https://help.shopify.com/manual/discounts/combining-
discounts/discount-combinations) that you can use in combination with [Shopify
discount types](https://help.shopify.com/manual/discounts/discount-types).

Show fields

[Anchor to context](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-DiscountAutomaticBxgy.fields.context)context

•[DiscountContext!](/docs/api/admin-graphql/latest/unions/DiscountContext)

non-null

    

The context defining which buyers can use the discount.

Show union types

[Anchor to createdAt](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-DiscountAutomaticBxgy.fields.createdAt)createdAt

•[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime)

non-null

    

The date and time when the discount was created.

[Anchor to customerBuys](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DiscountAutomaticBxgy.fields.customerBuys)customerBuys

•[DiscountCustomerBuys!](/docs/api/admin-
graphql/latest/objects/DiscountCustomerBuys)

non-null

    

The items eligible for the discount and the required quantity of each to
receive the discount.

Show fields

[Anchor to customerGets](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DiscountAutomaticBxgy.fields.customerGets)customerGets

•[DiscountCustomerGets!](/docs/api/admin-
graphql/latest/objects/DiscountCustomerGets)

non-null

    

The items in the order that qualify for the discount, their quantities, and
the total value of the discount.

Show fields

[Anchor to discountClasses](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DiscountAutomaticBxgy.fields.discountClasses)discountClasses

•[[DiscountClass!]!](/docs/api/admin-graphql/latest/enums/DiscountClass)

non-null

    

The classes of the discount.

Show enum values

[Anchor to endsAt](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-DiscountAutomaticBxgy.fields.endsAt)endsAt

•[DateTime](/docs/api/admin-graphql/latest/scalars/DateTime)

    

The date and time when the discount expires and is no longer available to
customers. For discounts without a fixed expiration date, specify `null`.

[Anchor to events](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-DiscountAutomaticBxgy.fields.events)events

•[EventConnection!](/docs/api/admin-
graphql/latest/connections/EventConnection)

non-null

    

The paginated list of events associated with the host subject.

Show fields

[Anchor to startsAt](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-DiscountAutomaticBxgy.fields.startsAt)startsAt

•[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime)

non-null

    

The date and time when the discount becomes active and is available to
customers.

[Anchor to status](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-DiscountAutomaticBxgy.fields.status)status

•[DiscountStatus!](/docs/api/admin-graphql/latest/enums/DiscountStatus)

non-null

    

The status of the discount that describes its availability, expiration, or
pending activation.

Show enum values

[Anchor to summary](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-DiscountAutomaticBxgy.fields.summary)summary

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

A detailed explanation of what the discount is, who can use it, when and where
it applies, and any associated rules or limitations.

[Anchor to title](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-DiscountAutomaticBxgy.fields.title)title

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The discount's name that displays to merchants in the Shopify admin and to
customers.

[Anchor to updatedAt](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-DiscountAutomaticBxgy.fields.updatedAt)updatedAt

•[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime)

non-null

    

The date and time when the discount was updated.

[Anchor to usesPerOrderLimit](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DiscountAutomaticBxgy.fields.usesPerOrderLimit)usesPerOrderLimit

•[Int](/docs/api/admin-graphql/latest/scalars/Int)

    

The maximum number of times that the discount can be applied to an order.

[Anchor to discountClass](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DiscountAutomaticBxgy.fields.discountClass)discountClass

•[MerchandiseDiscountClass!](/docs/api/admin-
graphql/latest/enums/MerchandiseDiscountClass)

non-nullDeprecated

    

Show enum values

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
DiscountAutomaticBxgy.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-nullDeprecated

    

[Anchor to usageCount](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DiscountAutomaticBxgy.fields.usageCount)usageCount

•[Int!](/docs/api/admin-graphql/latest/scalars/Int)

non-nullDeprecated

    

[Anchor to DiscountAutomaticNode](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DiscountAutomaticNode)[DiscountAutomaticNode](/docs/api/admin-
graphql/latest/objects/DiscountAutomaticNode)

•OBJECT

    

The `DiscountAutomaticNode` object enables you to manage [automatic
discounts](https://help.shopify.com/manual/discounts/discount-types#automatic-
discounts) that are applied when an order meets specific criteria. You can
create amount off, free shipping, or buy X get Y automatic discounts. For
example, you can offer customers a free shipping discount that applies when
conditions are met. Or you can offer customers a buy X get Y discount that's
automatically applied when customers spend a specified amount of money, or a
specified quantity of products.

Learn more about working with [Shopify's discount
model](https://shopify.dev/docs/apps/build/discounts), including related
queries, mutations, limitations, and considerations.

Show fields

[Anchor to automaticDiscount](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DiscountAutomaticNode.fields.automaticDiscount)automaticDiscount

•[DiscountAutomatic!](/docs/api/admin-graphql/latest/unions/DiscountAutomatic)

non-null

    

A discount that's applied automatically when an order meets specific criteria.
Learn more about [automatic
discounts](https://help.shopify.com/manual/discounts/discount-types#automatic-
discounts).

Show union types

[Anchor to events](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-DiscountAutomaticNode.fields.events)events

•[EventConnection!](/docs/api/admin-
graphql/latest/connections/EventConnection)

non-null

    

The paginated list of events associated with the host subject.

Show fields

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
DiscountAutomaticNode.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to metafield](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-DiscountAutomaticNode.fields.metafield)metafield

•[Metafield](/docs/api/admin-graphql/latest/objects/Metafield)

    

A [custom field](https://shopify.dev/docs/apps/build/custom-data), including
its `namespace` and `key`, that's associated with a Shopify resource for the
purposes of adding and storing additional information.

Show fields

[Anchor to metafields](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DiscountAutomaticNode.fields.metafields)metafields

•[MetafieldConnection!](/docs/api/admin-
graphql/latest/connections/MetafieldConnection)

non-null

    

A list of [custom fields](https://shopify.dev/docs/apps/build/custom-data)
that a merchant associates with a Shopify resource.

Show fields

[Anchor to metafieldDefinitions](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DiscountAutomaticNode.fields.metafieldDefinitions)metafieldDefinitions

•[MetafieldDefinitionConnection!](/docs/api/admin-
graphql/latest/connections/MetafieldDefinitionConnection)

non-nullDeprecated

    

Show fields

[Anchor to DiscountCodeNode](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DiscountCodeNode)[DiscountCodeNode](/docs/api/admin-
graphql/latest/objects/DiscountCodeNode)

•OBJECT

    

The `DiscountCodeNode` object enables you to manage [code
discounts](https://help.shopify.com/manual/discounts/discount-types#discount-
codes) that are applied when customers enter a code at checkout. For example,
you can offer discounts where customers have to enter a code to redeem an
amount off discount on products, variants, or collections in a store. Or, you
can offer discounts where customers have to enter a code to get free shipping.
Merchants can create and share discount codes individually with customers.

Learn more about working with [Shopify's discount
model](https://shopify.dev/docs/apps/build/discounts), including related
queries, mutations, limitations, and considerations.

Show fields

[Anchor to codeDiscount](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DiscountCodeNode.fields.codeDiscount)codeDiscount

•[DiscountCode!](/docs/api/admin-graphql/latest/unions/DiscountCode)

non-null

    

The underlying code discount object.

Show union types

[Anchor to events](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-DiscountCodeNode.fields.events)events

•[EventConnection!](/docs/api/admin-
graphql/latest/connections/EventConnection)

non-null

    

The paginated list of events associated with the host subject.

Show fields

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
DiscountCodeNode.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to metafield](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-DiscountCodeNode.fields.metafield)metafield

•[Metafield](/docs/api/admin-graphql/latest/objects/Metafield)

    

A [custom field](https://shopify.dev/docs/apps/build/custom-data), including
its `namespace` and `key`, that's associated with a Shopify resource for the
purposes of adding and storing additional information.

Show fields

[Anchor to metafields](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DiscountCodeNode.fields.metafields)metafields

•[MetafieldConnection!](/docs/api/admin-
graphql/latest/connections/MetafieldConnection)

non-null

    

A list of [custom fields](https://shopify.dev/docs/apps/build/custom-data)
that a merchant associates with a Shopify resource.

Show fields

[Anchor to metafieldDefinitions](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DiscountCodeNode.fields.metafieldDefinitions)metafieldDefinitions

•[MetafieldDefinitionConnection!](/docs/api/admin-
graphql/latest/connections/MetafieldDefinitionConnection)

non-nullDeprecated

    

Show fields

[Anchor to DiscountNode](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DiscountNode)[DiscountNode](/docs/api/admin-
graphql/latest/objects/DiscountNode)

•OBJECT

    

The `DiscountNode` object enables you to manage
[discounts](https://help.shopify.com/manual/discounts), which are applied at
checkout or on a cart.

Discounts are a way for merchants to promote sales and special offers, or as
customer loyalty rewards. Discounts can apply to [orders, products, or
shipping](https://shopify.dev/docs/apps/build/discounts#discount-classes), and
can be either automatic or code-based. For example, you can offer customers a
buy X get Y discount that's automatically applied when purchases meet specific
criteria. Or, you can offer discounts where customers have to enter a code to
redeem an amount off discount on products, variants, or collections in a
store.

Learn more about working with [Shopify's discount
model](https://shopify.dev/docs/apps/build/discounts), including related
mutations, limitations, and considerations.

Show fields

[Anchor to discount](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-DiscountNode.fields.discount)discount

•[Discount!](/docs/api/admin-graphql/latest/unions/Discount)

non-null

    

A discount that's applied at checkout or on cart.

Discounts can be [automatic or code-
based](https://shopify.dev/docs/apps/build/discounts#discount-methods).

Show union types

[Anchor to events](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-DiscountNode.fields.events)events

•[EventConnection!](/docs/api/admin-
graphql/latest/connections/EventConnection)

non-null

    

The paginated list of events associated with the host subject.

Show fields

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
DiscountNode.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to metafield](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-DiscountNode.fields.metafield)metafield

•[Metafield](/docs/api/admin-graphql/latest/objects/Metafield)

    

A [custom field](https://shopify.dev/docs/apps/build/custom-data), including
its `namespace` and `key`, that's associated with a Shopify resource for the
purposes of adding and storing additional information.

Show fields

[Anchor to metafields](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DiscountNode.fields.metafields)metafields

•[MetafieldConnection!](/docs/api/admin-
graphql/latest/connections/MetafieldConnection)

non-null

    

A list of [custom fields](https://shopify.dev/docs/apps/build/custom-data)
that a merchant associates with a Shopify resource.

Show fields

[Anchor to metafieldDefinitions](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DiscountNode.fields.metafieldDefinitions)metafieldDefinitions

•[MetafieldDefinitionConnection!](/docs/api/admin-
graphql/latest/connections/MetafieldDefinitionConnection)

non-nullDeprecated

    

Show fields

[Anchor to DiscountRedeemCodeBulkCreation](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DiscountRedeemCodeBulkCreation)[DiscountRedeemCodeBulkCreation](/docs/api/admin-
graphql/latest/objects/DiscountRedeemCodeBulkCreation)

•OBJECT

    

The properties and status of a bulk discount redeem code creation operation.

Show fields

[Anchor to codes](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-DiscountRedeemCodeBulkCreation.fields.codes)codes

•[DiscountRedeemCodeBulkCreationCodeConnection!](/docs/api/admin-
graphql/latest/connections/DiscountRedeemCodeBulkCreationCodeConnection)

non-null

    

The result of each code creation operation associated with the bulk creation
operation including any errors that might have occurred during the operation.

Show fields

[Anchor to codesCount](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DiscountRedeemCodeBulkCreation.fields.codesCount)codesCount

•[Int!](/docs/api/admin-graphql/latest/scalars/Int)

non-null

    

The number of codes to create.

[Anchor to createdAt](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-DiscountRedeemCodeBulkCreation.fields.createdAt)createdAt

•[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime)

non-null

    

The date and time when the bulk creation was created.

[Anchor to discountCode](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DiscountRedeemCodeBulkCreation.fields.discountCode)discountCode

•[DiscountCodeNode](/docs/api/admin-graphql/latest/objects/DiscountCodeNode)

    

The code discount associated with the created codes.

Show fields

[Anchor to done](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-DiscountRedeemCodeBulkCreation.fields.done)done

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether the bulk creation is still queued (`false`) or has been run (`true`).

[Anchor to failedCount](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DiscountRedeemCodeBulkCreation.fields.failedCount)failedCount

•[Int!](/docs/api/admin-graphql/latest/scalars/Int)

non-null

    

The number of codes that weren't created successfully.

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
DiscountRedeemCodeBulkCreation.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to importedCount](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DiscountRedeemCodeBulkCreation.fields.importedCount)importedCount

•[Int!](/docs/api/admin-graphql/latest/scalars/Int)

non-null

    

The number of codes created successfully.

[Anchor to Domain](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Domain)[Domain](/docs/api/admin-graphql/latest/objects/Domain)

•OBJECT

    

A unique string that represents the address of a Shopify store on the
Internet.

Show fields

[Anchor to host](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Domain.fields.host)host

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The host name of the domain. For example, `example.com`.

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
Domain.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to localization](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Domain.fields.localization)localization

•[DomainLocalization](/docs/api/admin-
graphql/latest/objects/DomainLocalization)

    

The localization of the domain, if the domain doesn't redirect.

Show fields

[Anchor to marketWebPresence](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Domain.fields.marketWebPresence)marketWebPresence

•[MarketWebPresence](/docs/api/admin-graphql/latest/objects/MarketWebPresence)

    

The web presence of the domain.

Show fields

[Anchor to sslEnabled](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Domain.fields.sslEnabled)sslEnabled

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether SSL is enabled.

[Anchor to url](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
Domain.fields.url)url

•[URL!](/docs/api/admin-graphql/latest/scalars/URL)

non-null

    

The URL of the domain (for example, `https://example.com`).

[Anchor to DraftOrder](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DraftOrder)[DraftOrder](/docs/api/admin-graphql/latest/objects/DraftOrder)

•OBJECT

    

An order that a merchant creates on behalf of a customer. Draft orders are
useful for merchants that need to do the following tasks:

  * Create new orders for sales made by phone, in person, by chat, or elsewhere. When a merchant accepts payment for a draft order, an order is created.
  * Send invoices to customers to pay with a secure checkout link.
  * Use custom items to represent additional costs or products that aren't displayed in a shop's inventory.
  * Re-create orders manually from active sales channels.
  * Sell products at discount or wholesale rates.
  * Take pre-orders.

For draft orders in multiple currencies `presentment_money` is the source of
truth for what a customer is going to be charged and `shop_money` is an
estimate of what the merchant might receive in their shop currency.

**Caution:** Only use this data if it's required for your app's functionality.
Shopify will restrict [access to scopes](https://shopify.dev/api/usage/access-
scopes) for apps that don't have a legitimate use for the associated data.

Draft orders created on or after April 1, 2025 will be automatically purged
after one year of inactivity.

Show fields

[Anchor to acceptAutomaticDiscounts](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DraftOrder.fields.acceptAutomaticDiscounts)acceptAutomaticDiscounts

•[Boolean](/docs/api/admin-graphql/latest/scalars/Boolean)

    

Whether or not to accept automatic discounts on the draft order during
calculation. If false, only discount codes and custom draft order discounts
(see `appliedDiscount`) will be applied. If true, eligible automatic discounts
will be applied in addition to discount codes and custom draft order
discounts.

[Anchor to allowDiscountCodesInCheckout](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DraftOrder.fields.allowDiscountCodesInCheckout)allowDiscountCodesInCheckout

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether discount codes are allowed during checkout of this draft order.

[Anchor to allVariantPricesOverridden](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DraftOrder.fields.allVariantPricesOverridden)allVariantPricesOverridden

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether all variant prices have been overridden.

[Anchor to anyVariantPricesOverridden](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DraftOrder.fields.anyVariantPricesOverridden)anyVariantPricesOverridden

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether any variant prices have been overridden.

[Anchor to appliedDiscount](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DraftOrder.fields.appliedDiscount)appliedDiscount

•[DraftOrderAppliedDiscount](/docs/api/admin-
graphql/latest/objects/DraftOrderAppliedDiscount)

    

The custom order-level discount applied.

Show fields

[Anchor to billingAddress](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DraftOrder.fields.billingAddress)billingAddress

•[MailingAddress](/docs/api/admin-graphql/latest/objects/MailingAddress)

    

The billing address of the customer.

Show fields

[Anchor to billingAddressMatchesShippingAddress](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DraftOrder.fields.billingAddressMatchesShippingAddress)billingAddressMatchesShippingAddress

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether the billing address matches the shipping address.

[Anchor to completedAt](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DraftOrder.fields.completedAt)completedAt

•[DateTime](/docs/api/admin-graphql/latest/scalars/DateTime)

    

The date and time when the draft order was converted to a new order, and had
it's status changed to **Completed**.

[Anchor to createdAt](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-DraftOrder.fields.createdAt)createdAt

•[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime)

non-null

    

The date and time when the draft order was created in Shopify.

[Anchor to currencyCode](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DraftOrder.fields.currencyCode)currencyCode

•[CurrencyCode!](/docs/api/admin-graphql/latest/enums/CurrencyCode)

non-null

    

The shop currency used for calculation.

Show enum values

[Anchor to customAttributes](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DraftOrder.fields.customAttributes)customAttributes

•[[Attribute!]!](/docs/api/admin-graphql/latest/objects/Attribute)

non-null

    

The custom information added to the draft order on behalf of the customer.

Show fields

[Anchor to customer](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-DraftOrder.fields.customer)customer

•[Customer](/docs/api/admin-graphql/latest/objects/Customer)

    

The customer who will be sent an invoice.

Show fields

[Anchor to defaultCursor](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DraftOrder.fields.defaultCursor)defaultCursor

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

A default [cursor](https://shopify.dev/api/usage/pagination-graphql) that
returns the single next record, sorted ascending by ID.

[Anchor to discountCodes](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DraftOrder.fields.discountCodes)discountCodes

•[[String!]!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

All discount codes applied.

[Anchor to email](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-DraftOrder.fields.email)email

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The email address of the customer, which is used to send notifications.

[Anchor to events](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-DraftOrder.fields.events)events

•[EventConnection!](/docs/api/admin-
graphql/latest/connections/EventConnection)

non-null

    

The list of events associated with the draft order.

Show fields

[Anchor to hasTimelineComment](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DraftOrder.fields.hasTimelineComment)hasTimelineComment

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether the merchant has added timeline comments to the draft order.

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
DraftOrder.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to invoiceEmailTemplateSubject](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DraftOrder.fields.invoiceEmailTemplateSubject)invoiceEmailTemplateSubject

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The subject defined for the draft invoice email template.

[Anchor to invoiceSentAt](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DraftOrder.fields.invoiceSentAt)invoiceSentAt

•[DateTime](/docs/api/admin-graphql/latest/scalars/DateTime)

    

The date and time when the invoice was last emailed to the customer.

[Anchor to invoiceUrl](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DraftOrder.fields.invoiceUrl)invoiceUrl

•[URL](/docs/api/admin-graphql/latest/scalars/URL)

    

The link to the checkout, which is sent to the customer in the invoice email.

[Anchor to legacyResourceId](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DraftOrder.fields.legacyResourceId)legacyResourceId

•[UnsignedInt64!](/docs/api/admin-graphql/latest/scalars/UnsignedInt64)

non-null

    

The ID of the corresponding resource in the REST Admin API.

[Anchor to lineItems](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-DraftOrder.fields.lineItems)lineItems

•[DraftOrderLineItemConnection!](/docs/api/admin-
graphql/latest/connections/DraftOrderLineItemConnection)

non-null

    

The list of the line items in the draft order.

Show fields

[Anchor to lineItemsSubtotalPrice](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DraftOrder.fields.lineItemsSubtotalPrice)lineItemsSubtotalPrice

•[MoneyBag!](/docs/api/admin-graphql/latest/objects/MoneyBag)

non-null

    

A subtotal of the line items and corresponding discounts, excluding shipping
charges, shipping discounts, taxes, or order discounts.

Show fields

[Anchor to localizedFields](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DraftOrder.fields.localizedFields)localizedFields

•[LocalizedFieldConnection!](/docs/api/admin-
graphql/latest/connections/LocalizedFieldConnection)

non-null

    

List of localized fields for the resource.

Show fields

[Anchor to metafield](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-DraftOrder.fields.metafield)metafield

•[Metafield](/docs/api/admin-graphql/latest/objects/Metafield)

    

A [custom field](https://shopify.dev/docs/apps/build/custom-data), including
its `namespace` and `key`, that's associated with a Shopify resource for the
purposes of adding and storing additional information.

Show fields

[Anchor to metafields](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DraftOrder.fields.metafields)metafields

•[MetafieldConnection!](/docs/api/admin-
graphql/latest/connections/MetafieldConnection)

non-null

    

A list of [custom fields](https://shopify.dev/docs/apps/build/custom-data)
that a merchant associates with a Shopify resource.

Show fields

[Anchor to name](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-DraftOrder.fields.name)name

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The identifier for the draft order, which is unique within the store. For
example, _#D1223_.

[Anchor to note2](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-DraftOrder.fields.note2)note2

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The text from an optional note attached to the draft order.

[Anchor to order](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-DraftOrder.fields.order)order

•[Order](/docs/api/admin-graphql/latest/objects/Order)

    

The order that was created from the draft order.

Show fields

[Anchor to paymentTerms](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DraftOrder.fields.paymentTerms)paymentTerms

•[PaymentTerms](/docs/api/admin-graphql/latest/objects/PaymentTerms)

    

The associated payment terms for this draft order.

Show fields

[Anchor to phone](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-DraftOrder.fields.phone)phone

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The assigned phone number.

[Anchor to platformDiscounts](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DraftOrder.fields.platformDiscounts)platformDiscounts

•[[DraftOrderPlatformDiscount!]!](/docs/api/admin-
graphql/latest/objects/DraftOrderPlatformDiscount)

non-null

    

The list of platform discounts applied.

Show fields

[Anchor to poNumber](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-DraftOrder.fields.poNumber)poNumber

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The purchase order number.

[Anchor to presentmentCurrencyCode](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DraftOrder.fields.presentmentCurrencyCode)presentmentCurrencyCode

•[CurrencyCode!](/docs/api/admin-graphql/latest/enums/CurrencyCode)

non-null

    

The payment currency used for calculation.

Show enum values

[Anchor to purchasingEntity](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DraftOrder.fields.purchasingEntity)purchasingEntity

•[PurchasingEntity](/docs/api/admin-graphql/latest/unions/PurchasingEntity)

    

The purchasing entity.

Show union types

[Anchor to ready](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-DraftOrder.fields.ready)ready

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether the draft order is ready and can be completed. Draft orders might have
asynchronous operations that can take time to finish.

[Anchor to reserveInventoryUntil](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DraftOrder.fields.reserveInventoryUntil)reserveInventoryUntil

•[DateTime](/docs/api/admin-graphql/latest/scalars/DateTime)

    

The time after which inventory will automatically be restocked.

[Anchor to shippingAddress](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DraftOrder.fields.shippingAddress)shippingAddress

•[MailingAddress](/docs/api/admin-graphql/latest/objects/MailingAddress)

    

The shipping address of the customer.

Show fields

[Anchor to shippingLine](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DraftOrder.fields.shippingLine)shippingLine

•[ShippingLine](/docs/api/admin-graphql/latest/objects/ShippingLine)

    

The line item containing the shipping information and costs.

Show fields

[Anchor to status](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-DraftOrder.fields.status)status

•[DraftOrderStatus!](/docs/api/admin-graphql/latest/enums/DraftOrderStatus)

non-null

    

The status of the draft order.

Show enum values

[Anchor to subtotalPriceSet](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DraftOrder.fields.subtotalPriceSet)subtotalPriceSet

•[MoneyBag!](/docs/api/admin-graphql/latest/objects/MoneyBag)

non-null

    

The subtotal, of the line items and their discounts, excluding shipping
charges, shipping discounts, and taxes.

Show fields

[Anchor to tags](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-DraftOrder.fields.tags)tags

•[[String!]!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The comma separated list of tags associated with the draft order. Updating
`tags` overwrites any existing tags that were previously added to the draft
order. To add new tags without overwriting existing tags, use the
[tagsAdd](https://shopify.dev/api/admin-graphql/latest/mutations/tagsadd)
mutation.

[Anchor to taxesIncluded](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DraftOrder.fields.taxesIncluded)taxesIncluded

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether the line item prices include taxes.

[Anchor to taxExempt](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-DraftOrder.fields.taxExempt)taxExempt

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether the draft order is tax exempt.

[Anchor to taxLines](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-DraftOrder.fields.taxLines)taxLines

•[[TaxLine!]!](/docs/api/admin-graphql/latest/objects/TaxLine)

non-null

    

The list of of taxes lines charged for each line item and shipping line.

Show fields

[Anchor to totalDiscountsSet](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DraftOrder.fields.totalDiscountsSet)totalDiscountsSet

•[MoneyBag!](/docs/api/admin-graphql/latest/objects/MoneyBag)

non-null

    

Total discounts.

Show fields

[Anchor to totalLineItemsPriceSet](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DraftOrder.fields.totalLineItemsPriceSet)totalLineItemsPriceSet

•[MoneyBag!](/docs/api/admin-graphql/latest/objects/MoneyBag)

non-null

    

Total price of line items, excluding discounts.

Show fields

[Anchor to totalPriceSet](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DraftOrder.fields.totalPriceSet)totalPriceSet

•[MoneyBag!](/docs/api/admin-graphql/latest/objects/MoneyBag)

non-null

    

The total price, includes taxes, shipping charges, and discounts.

Show fields

[Anchor to totalQuantityOfLineItems](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DraftOrder.fields.totalQuantityOfLineItems)totalQuantityOfLineItems

•[Int!](/docs/api/admin-graphql/latest/scalars/Int)

non-null

    

The sum of individual line item quantities. If the draft order has bundle
items, this is the sum containing the quantities of individual items in the
bundle.

[Anchor to totalShippingPriceSet](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DraftOrder.fields.totalShippingPriceSet)totalShippingPriceSet

•[MoneyBag!](/docs/api/admin-graphql/latest/objects/MoneyBag)

non-null

    

The total shipping price.

Show fields

[Anchor to totalTaxSet](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DraftOrder.fields.totalTaxSet)totalTaxSet

•[MoneyBag!](/docs/api/admin-graphql/latest/objects/MoneyBag)

non-null

    

The total tax.

Show fields

[Anchor to totalWeight](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DraftOrder.fields.totalWeight)totalWeight

•[UnsignedInt64!](/docs/api/admin-graphql/latest/scalars/UnsignedInt64)

non-null

    

The total weight in grams of the draft order.

[Anchor to transformerFingerprint](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DraftOrder.fields.transformerFingerprint)transformerFingerprint

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

Fingerprint of the current cart. In order to have bundles work, the
fingerprint must be passed to each request as it was previously returned,
unmodified.

[Anchor to updatedAt](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-DraftOrder.fields.updatedAt)updatedAt

•[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime)

non-null

    

The date and time when the draft order was last changed. The format is YYYY-
MM-DD HH:mm:ss. For example, 2016-02-05 17:04:01.

[Anchor to visibleToCustomer](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DraftOrder.fields.visibleToCustomer)visibleToCustomer

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether the draft order will be visible to the customer on the self-serve
portal.

[Anchor to warnings](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-DraftOrder.fields.warnings)warnings

•[[DraftOrderWarning!]!](/docs/api/admin-
graphql/latest/interfaces/DraftOrderWarning)

non-null

    

The list of warnings raised while calculating.

Show fields

[Anchor to localizationExtensions](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DraftOrder.fields.localizationExtensions)localizationExtensions

•[LocalizationExtensionConnection!](/docs/api/admin-
graphql/latest/connections/LocalizationExtensionConnection)

non-nullDeprecated

    

Show fields

[Anchor to marketName](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DraftOrder.fields.marketName)marketName

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-nullDeprecated

    

[Anchor to marketRegionCountryCode](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DraftOrder.fields.marketRegionCountryCode)marketRegionCountryCode

•[CountryCode!](/docs/api/admin-graphql/latest/enums/CountryCode)

non-nullDeprecated

    

Show enum values

[Anchor to subtotalPrice](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DraftOrder.fields.subtotalPrice)subtotalPrice

•[Money!](/docs/api/admin-graphql/latest/scalars/Money)

non-nullDeprecated

    

[Anchor to totalPrice](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DraftOrder.fields.totalPrice)totalPrice

•[Money!](/docs/api/admin-graphql/latest/scalars/Money)

non-nullDeprecated

    

[Anchor to totalShippingPrice](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DraftOrder.fields.totalShippingPrice)totalShippingPrice

•[Money!](/docs/api/admin-graphql/latest/scalars/Money)

non-nullDeprecated

    

[Anchor to totalTax](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-DraftOrder.fields.totalTax)totalTax

•[Money!](/docs/api/admin-graphql/latest/scalars/Money)

non-nullDeprecated

    

[Anchor to DraftOrderLineItem](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DraftOrderLineItem)[DraftOrderLineItem](/docs/api/admin-
graphql/latest/objects/DraftOrderLineItem)

•OBJECT

    

The line item for a draft order.

Show fields

[Anchor to appliedDiscount](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DraftOrderLineItem.fields.appliedDiscount)appliedDiscount

•[DraftOrderAppliedDiscount](/docs/api/admin-
graphql/latest/objects/DraftOrderAppliedDiscount)

    

The custom applied discount.

Show fields

[Anchor to approximateDiscountedUnitPriceSet](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DraftOrderLineItem.fields.approximateDiscountedUnitPriceSet)approximateDiscountedUnitPriceSet

•[MoneyBag!](/docs/api/admin-graphql/latest/objects/MoneyBag)

non-null

    

The `discountedTotal` divided by `quantity`, equal to the average value of the
line item price per unit after discounts are applied. This value doesn't
include discounts applied to the entire draft order.

Show fields

[Anchor to components](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DraftOrderLineItem.fields.components)components

•[[DraftOrderLineItem!]!](/docs/api/admin-
graphql/latest/objects/DraftOrderLineItem)

non-null

    

The components of the draft order line item.

Show fields

[Anchor to custom](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-DraftOrderLineItem.fields.custom)custom

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether the line item is custom (`true`) or contains a product variant
(`false`).

[Anchor to customAttributes](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DraftOrderLineItem.fields.customAttributes)customAttributes

•[[Attribute!]!](/docs/api/admin-graphql/latest/objects/Attribute)

non-null

    

A list of attributes that represent custom features or special requests.

Show fields

[Anchor to customAttributesV2](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DraftOrderLineItem.fields.customAttributesV2)customAttributesV2

•[[TypedAttribute!]!](/docs/api/admin-graphql/latest/objects/TypedAttribute)

non-null

    

The list of additional information (metafields) with the associated types.

Show fields

[Anchor to discountedTotalSet](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DraftOrderLineItem.fields.discountedTotalSet)discountedTotalSet

•[MoneyBag!](/docs/api/admin-graphql/latest/objects/MoneyBag)

non-null

    

The total price with discounts applied.

Show fields

[Anchor to fulfillmentService](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DraftOrderLineItem.fields.fulfillmentService)fulfillmentService

•[FulfillmentService](/docs/api/admin-
graphql/latest/objects/FulfillmentService)

    

Name of the service provider who fulfilled the order.

Valid values are either **manual** or the name of the provider. For example,
**amazon** , **shipwire**.

Deleted fulfillment services will return null.

Show fields

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
DraftOrderLineItem.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to image](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-DraftOrderLineItem.fields.image)image

•[Image](/docs/api/admin-graphql/latest/objects/Image)

    

The image of the product variant.

Show fields

[Anchor to isGiftCard](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DraftOrderLineItem.fields.isGiftCard)isGiftCard

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether the line item represents the purchase of a gift card.

[Anchor to name](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-DraftOrderLineItem.fields.name)name

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The name of the product.

[Anchor to originalTotalSet](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DraftOrderLineItem.fields.originalTotalSet)originalTotalSet

•[MoneyBag!](/docs/api/admin-graphql/latest/objects/MoneyBag)

non-null

    

The total price excluding discounts, equal to the original unit price
multiplied by quantity.

Show fields

[Anchor to originalUnitPriceSet](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DraftOrderLineItem.fields.originalUnitPriceSet)originalUnitPriceSet

•[MoneyBag!](/docs/api/admin-graphql/latest/objects/MoneyBag)

non-null

    

The price without any discounts applied.

Show fields

[Anchor to originalUnitPriceWithCurrency](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DraftOrderLineItem.fields.originalUnitPriceWithCurrency)originalUnitPriceWithCurrency

•[MoneyV2](/docs/api/admin-graphql/latest/objects/MoneyV2)

    

The original custom line item input price.

Show fields

[Anchor to priceOverride](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DraftOrderLineItem.fields.priceOverride)priceOverride

•[MoneyV2](/docs/api/admin-graphql/latest/objects/MoneyV2)

    

The price override for the line item.

Show fields

[Anchor to product](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-DraftOrderLineItem.fields.product)product

•[Product](/docs/api/admin-graphql/latest/objects/Product)

    

The product for the line item.

Show fields

[Anchor to quantity](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-DraftOrderLineItem.fields.quantity)quantity

•[Int!](/docs/api/admin-graphql/latest/scalars/Int)

non-null

    

The quantity of items. For a bundle item, this is the quantity of bundles, not
the quantity of items contained in the bundles themselves.

[Anchor to requiresShipping](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DraftOrderLineItem.fields.requiresShipping)requiresShipping

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether physical shipping is required for the variant.

[Anchor to sku](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
DraftOrderLineItem.fields.sku)sku

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The SKU number of the product variant.

[Anchor to taxable](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-DraftOrderLineItem.fields.taxable)taxable

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether the variant is taxable.

[Anchor to taxLines](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-DraftOrderLineItem.fields.taxLines)taxLines

•[[TaxLine!]!](/docs/api/admin-graphql/latest/objects/TaxLine)

non-null

    

A list of tax lines.

Show fields

[Anchor to title](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-DraftOrderLineItem.fields.title)title

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The title of the product or variant. This field only applies to custom line
items.

[Anchor to totalDiscountSet](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DraftOrderLineItem.fields.totalDiscountSet)totalDiscountSet

•[MoneyBag!](/docs/api/admin-graphql/latest/objects/MoneyBag)

non-null

    

The total discount amount.

Show fields

[Anchor to uuid](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-DraftOrderLineItem.fields.uuid)uuid

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The UUID of the draft order line item. Must be unique and consistent across
requests. This field is mandatory in order to manipulate drafts with bundles.

[Anchor to variant](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-DraftOrderLineItem.fields.variant)variant

•[ProductVariant](/docs/api/admin-graphql/latest/objects/ProductVariant)

    

The product variant for the line item.

Show fields

[Anchor to variantTitle](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DraftOrderLineItem.fields.variantTitle)variantTitle

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The name of the variant.

[Anchor to vendor](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-DraftOrderLineItem.fields.vendor)vendor

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The name of the vendor who created the product variant.

[Anchor to weight](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-DraftOrderLineItem.fields.weight)weight

•[Weight](/docs/api/admin-graphql/latest/objects/Weight)

    

The weight unit and value.

Show fields

[Anchor to bundleComponents](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DraftOrderLineItem.fields.bundleComponents)bundleComponents

•[[DraftOrderLineItem!]!](/docs/api/admin-
graphql/latest/objects/DraftOrderLineItem)

non-nullDeprecated

    

Show fields

[Anchor to discountedTotal](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DraftOrderLineItem.fields.discountedTotal)discountedTotal

•[Money!](/docs/api/admin-graphql/latest/scalars/Money)

non-nullDeprecated

    

[Anchor to discountedUnitPrice](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DraftOrderLineItem.fields.discountedUnitPrice)discountedUnitPrice

•[Money!](/docs/api/admin-graphql/latest/scalars/Money)

non-nullDeprecated

    

[Anchor to discountedUnitPriceSet](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DraftOrderLineItem.fields.discountedUnitPriceSet)discountedUnitPriceSet

•[MoneyBag!](/docs/api/admin-graphql/latest/objects/MoneyBag)

non-nullDeprecated

    

Show fields

[Anchor to grams](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-DraftOrderLineItem.fields.grams)grams

•[Int](/docs/api/admin-graphql/latest/scalars/Int)

Deprecated

    

[Anchor to originalTotal](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DraftOrderLineItem.fields.originalTotal)originalTotal

•[Money!](/docs/api/admin-graphql/latest/scalars/Money)

non-nullDeprecated

    

[Anchor to originalUnitPrice](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DraftOrderLineItem.fields.originalUnitPrice)originalUnitPrice

•[Money!](/docs/api/admin-graphql/latest/scalars/Money)

non-nullDeprecated

    

[Anchor to totalDiscount](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DraftOrderLineItem.fields.totalDiscount)totalDiscount

•[Money!](/docs/api/admin-graphql/latest/scalars/Money)

non-nullDeprecated

    

[Anchor to DraftOrderTag](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
DraftOrderTag)[DraftOrderTag](/docs/api/admin-
graphql/latest/objects/DraftOrderTag)

•OBJECT

    

Represents a draft order tag.

Show fields

[Anchor to handle](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-DraftOrderTag.fields.handle)handle

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

Handle of draft order tag.

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
DraftOrderTag.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

ID of draft order tag.

[Anchor to title](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-DraftOrderTag.fields.title)title

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

Title of draft order tag.

[Anchor to Duty](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Duty)[Duty](/docs/api/admin-graphql/latest/objects/Duty)

•OBJECT

    

The duty details for a line item.

Show fields

[Anchor to countryCodeOfOrigin](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Duty.fields.countryCodeOfOrigin)countryCodeOfOrigin

•[CountryCode](/docs/api/admin-graphql/latest/enums/CountryCode)

    

The ISO 3166-1 alpha-2 country code of the country of origin used in
calculating the duty.

Show enum values

[Anchor to harmonizedSystemCode](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Duty.fields.harmonizedSystemCode)harmonizedSystemCode

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The harmonized system code of the item used in calculating the duty.

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
Duty.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to price](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Duty.fields.price)price

•[MoneyBag!](/docs/api/admin-graphql/latest/objects/MoneyBag)

non-null

    

The amount of the duty.

Show fields

[Anchor to taxLines](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Duty.fields.taxLines)taxLines

•[[TaxLine!]!](/docs/api/admin-graphql/latest/objects/TaxLine)

non-null

    

A list of taxes charged on the duty.

Show fields

[Anchor to ExchangeLineItem](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ExchangeLineItem)[ExchangeLineItem](/docs/api/admin-
graphql/latest/objects/ExchangeLineItem)

•OBJECT

    

An item for exchange.

Show fields

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
ExchangeLineItem.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to lineItems](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-ExchangeLineItem.fields.lineItems)lineItems

•[[LineItem!]](/docs/api/admin-graphql/latest/objects/LineItem)

    

The order line items for the exchange.

Show fields

[Anchor to processableQuantity](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ExchangeLineItem.fields.processableQuantity)processableQuantity

•[Int!](/docs/api/admin-graphql/latest/scalars/Int)

non-null

    

The quantity of the exchange item that can be processed.

[Anchor to processedQuantity](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ExchangeLineItem.fields.processedQuantity)processedQuantity

•[Int!](/docs/api/admin-graphql/latest/scalars/Int)

non-null

    

The quantity of the exchange item that have been processed.

[Anchor to quantity](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-ExchangeLineItem.fields.quantity)quantity

•[Int!](/docs/api/admin-graphql/latest/scalars/Int)

non-null

    

The number of units ordered, including refunded and removed units.

[Anchor to unprocessedQuantity](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ExchangeLineItem.fields.unprocessedQuantity)unprocessedQuantity

•[Int!](/docs/api/admin-graphql/latest/scalars/Int)

non-null

    

The quantity of the exchange item that haven't been processed.

[Anchor to variantId](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-ExchangeLineItem.fields.variantId)variantId

•[ID](/docs/api/admin-graphql/latest/scalars/ID)

    

The ID of the variant at time of return creation.

[Anchor to lineItem](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-ExchangeLineItem.fields.lineItem)lineItem

•[LineItem](/docs/api/admin-graphql/latest/objects/LineItem)

Deprecated

    

Show fields

[Anchor to ExternalVideo](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ExternalVideo)[ExternalVideo](/docs/api/admin-
graphql/latest/objects/ExternalVideo)

•OBJECT

    

Represents a video hosted outside of Shopify.

Show fields

[Anchor to alt](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
ExternalVideo.fields.alt)alt

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

A word or phrase to describe the contents or the function of a file.

[Anchor to createdAt](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-ExternalVideo.fields.createdAt)createdAt

•[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime)

non-null

    

The date and time ([ISO 8601 format](http://en.wikipedia.org/wiki/ISO_8601))
when the file was created.

[Anchor to embedUrl](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-ExternalVideo.fields.embedUrl)embedUrl

•[URL!](/docs/api/admin-graphql/latest/scalars/URL)

non-null

    

The embed URL of the video for the respective host.

[Anchor to fileErrors](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ExternalVideo.fields.fileErrors)fileErrors

•[[FileError!]!](/docs/api/admin-graphql/latest/objects/FileError)

non-null

    

Any errors that have occurred on the file.

Show fields

[Anchor to fileStatus](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ExternalVideo.fields.fileStatus)fileStatus

•[FileStatus!](/docs/api/admin-graphql/latest/enums/FileStatus)

non-null

    

The status of the file.

Show enum values

[Anchor to host](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-ExternalVideo.fields.host)host

•[MediaHost!](/docs/api/admin-graphql/latest/enums/MediaHost)

non-null

    

The host of the external video.

Show enum values

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
ExternalVideo.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to mediaContentType](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ExternalVideo.fields.mediaContentType)mediaContentType

•[MediaContentType!](/docs/api/admin-graphql/latest/enums/MediaContentType)

non-null

    

The media content type.

Show enum values

[Anchor to mediaErrors](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ExternalVideo.fields.mediaErrors)mediaErrors

•[[MediaError!]!](/docs/api/admin-graphql/latest/objects/MediaError)

non-null

    

Any errors which have occurred on the media.

Show fields

[Anchor to mediaWarnings](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ExternalVideo.fields.mediaWarnings)mediaWarnings

•[[MediaWarning!]!](/docs/api/admin-graphql/latest/objects/MediaWarning)

non-null

    

The warnings attached to the media.

Show fields

[Anchor to originUrl](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-ExternalVideo.fields.originUrl)originUrl

•[URL!](/docs/api/admin-graphql/latest/scalars/URL)

non-null

    

The origin URL of the video on the respective host.

[Anchor to preview](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-ExternalVideo.fields.preview)preview

•[MediaPreviewImage](/docs/api/admin-graphql/latest/objects/MediaPreviewImage)

    

The preview image for the media.

Show fields

[Anchor to status](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-ExternalVideo.fields.status)status

•[MediaStatus!](/docs/api/admin-graphql/latest/enums/MediaStatus)

non-null

    

Current status of the media.

Show enum values

[Anchor to updatedAt](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-ExternalVideo.fields.updatedAt)updatedAt

•[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime)

non-null

    

The date and time ([ISO 8601 format](http://en.wikipedia.org/wiki/ISO_8601))
when the file was last updated.

[Anchor to embeddedUrl](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ExternalVideo.fields.embeddedUrl)embeddedUrl

•[URL!](/docs/api/admin-graphql/latest/scalars/URL)

non-nullDeprecated

    

[Anchor to Fulfillment](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Fulfillment)[Fulfillment](/docs/api/admin-graphql/latest/objects/Fulfillment)

•OBJECT

    

Represents a fulfillment. In Shopify, a fulfillment represents a shipment of
one or more items in an order. When an order has been completely fulfilled, it
means that all the items that are included in the order have been sent to the
customer. There can be more than one fulfillment for an order.

Show fields

[Anchor to createdAt](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Fulfillment.fields.createdAt)createdAt

•[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime)

non-null

    

The date and time when the fulfillment was created.

[Anchor to deliveredAt](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Fulfillment.fields.deliveredAt)deliveredAt

•[DateTime](/docs/api/admin-graphql/latest/scalars/DateTime)

    

The date that this fulfillment was delivered.

[Anchor to displayStatus](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Fulfillment.fields.displayStatus)displayStatus

•[FulfillmentDisplayStatus](/docs/api/admin-
graphql/latest/enums/FulfillmentDisplayStatus)

    

Human readable display status for this fulfillment.

Show enum values

[Anchor to estimatedDeliveryAt](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Fulfillment.fields.estimatedDeliveryAt)estimatedDeliveryAt

•[DateTime](/docs/api/admin-graphql/latest/scalars/DateTime)

    

The estimated date that this fulfillment will arrive.

[Anchor to events](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Fulfillment.fields.events)events

•[FulfillmentEventConnection!](/docs/api/admin-
graphql/latest/connections/FulfillmentEventConnection)

non-null

    

The history of events associated with this fulfillment.

Show fields

[Anchor to fulfillmentLineItems](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Fulfillment.fields.fulfillmentLineItems)fulfillmentLineItems

•[FulfillmentLineItemConnection!](/docs/api/admin-
graphql/latest/connections/FulfillmentLineItemConnection)

non-null

    

List of the fulfillment's line items.

Show fields

[Anchor to fulfillmentOrders](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Fulfillment.fields.fulfillmentOrders)fulfillmentOrders

•[FulfillmentOrderConnection!](/docs/api/admin-
graphql/latest/connections/FulfillmentOrderConnection)

non-null

    

A paginated list of fulfillment orders for the fulfillment.

Show fields

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
Fulfillment.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to inTransitAt](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Fulfillment.fields.inTransitAt)inTransitAt

•[DateTime](/docs/api/admin-graphql/latest/scalars/DateTime)

    

The date and time when the fulfillment went into transit.

[Anchor to legacyResourceId](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Fulfillment.fields.legacyResourceId)legacyResourceId

•[UnsignedInt64!](/docs/api/admin-graphql/latest/scalars/UnsignedInt64)

non-null

    

The ID of the corresponding resource in the REST Admin API.

[Anchor to location](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Fulfillment.fields.location)location

•[Location](/docs/api/admin-graphql/latest/objects/Location)

    

The location that the fulfillment was processed at.

Show fields

[Anchor to name](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Fulfillment.fields.name)name

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

Human readable reference identifier for this fulfillment.

[Anchor to order](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Fulfillment.fields.order)order

•[Order!](/docs/api/admin-graphql/latest/objects/Order)

non-null

    

The order for which the fulfillment was created.

Show fields

[Anchor to originAddress](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Fulfillment.fields.originAddress)originAddress

•[FulfillmentOriginAddress](/docs/api/admin-
graphql/latest/objects/FulfillmentOriginAddress)

    

The address at which the fulfillment occurred. This field is intended for tax
purposes, as a full address is required for tax providers to accurately
calculate taxes. Typically this is the address of the warehouse or fulfillment
center. To retrieve a fulfillment location's address, use the
`assignedLocation` field on the [`FulfillmentOrder`](/docs/api/admin-
graphql/latest/objects/FulfillmentOrder) object instead.

Show fields

[Anchor to requiresShipping](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Fulfillment.fields.requiresShipping)requiresShipping

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether any of the line items in the fulfillment require shipping.

[Anchor to service](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Fulfillment.fields.service)service

•[FulfillmentService](/docs/api/admin-
graphql/latest/objects/FulfillmentService)

    

Fulfillment service associated with the fulfillment.

Show fields

[Anchor to status](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Fulfillment.fields.status)status

•[FulfillmentStatus!](/docs/api/admin-graphql/latest/enums/FulfillmentStatus)

non-null

    

The status of the fulfillment.

Show enum values

[Anchor to totalQuantity](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Fulfillment.fields.totalQuantity)totalQuantity

•[Int!](/docs/api/admin-graphql/latest/scalars/Int)

non-null

    

Sum of all line item quantities for the fulfillment.

[Anchor to trackingInfo](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Fulfillment.fields.trackingInfo)trackingInfo

•[[FulfillmentTrackingInfo!]!](/docs/api/admin-
graphql/latest/objects/FulfillmentTrackingInfo)

non-null

    

Tracking information associated with the fulfillment, such as the tracking
company, tracking number, and tracking URL.

Show fields

[Anchor to updatedAt](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Fulfillment.fields.updatedAt)updatedAt

•[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime)

non-null

    

The date and time when the fulfillment was last modified.

[Anchor to FulfillmentConstraintRule](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
FulfillmentConstraintRule)[FulfillmentConstraintRule](/docs/api/admin-
graphql/latest/objects/FulfillmentConstraintRule)

•OBJECT

    

A fulfillment constraint rule.

Show fields

[Anchor to deliveryMethodTypes](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
FulfillmentConstraintRule.fields.deliveryMethodTypes)deliveryMethodTypes

•[[DeliveryMethodType!]!](/docs/api/admin-
graphql/latest/enums/DeliveryMethodType)

non-null

    

Delivery method types that the function is associated with.

Show enum values

[Anchor to function](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-FulfillmentConstraintRule.fields.function)function

•[ShopifyFunction!](/docs/api/admin-graphql/latest/objects/ShopifyFunction)

non-null

    

The ID for the fulfillment constraint function.

Show fields

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
FulfillmentConstraintRule.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to metafield](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-FulfillmentConstraintRule.fields.metafield)metafield

•[Metafield](/docs/api/admin-graphql/latest/objects/Metafield)

    

A [custom field](https://shopify.dev/docs/apps/build/custom-data), including
its `namespace` and `key`, that's associated with a Shopify resource for the
purposes of adding and storing additional information.

Show fields

[Anchor to metafields](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
FulfillmentConstraintRule.fields.metafields)metafields

•[MetafieldConnection!](/docs/api/admin-
graphql/latest/connections/MetafieldConnection)

non-null

    

A list of [custom fields](https://shopify.dev/docs/apps/build/custom-data)
that a merchant associates with a Shopify resource.

Show fields

[Anchor to FulfillmentEvent](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
FulfillmentEvent)[FulfillmentEvent](/docs/api/admin-
graphql/latest/objects/FulfillmentEvent)

•OBJECT

    

The fulfillment event that describes the fulfilllment status at a particular
time.

Show fields

[Anchor to address1](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-FulfillmentEvent.fields.address1)address1

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The street address where this fulfillment event occurred.

[Anchor to city](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-FulfillmentEvent.fields.city)city

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The city where this fulfillment event occurred.

[Anchor to country](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-FulfillmentEvent.fields.country)country

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The country where this fulfillment event occurred.

[Anchor to createdAt](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-FulfillmentEvent.fields.createdAt)createdAt

•[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime)

non-null

    

The date and time when the fulfillment event was created.

[Anchor to estimatedDeliveryAt](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
FulfillmentEvent.fields.estimatedDeliveryAt)estimatedDeliveryAt

•[DateTime](/docs/api/admin-graphql/latest/scalars/DateTime)

    

The estimated delivery date and time of the fulfillment.

[Anchor to happenedAt](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
FulfillmentEvent.fields.happenedAt)happenedAt

•[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime)

non-null

    

The time at which this fulfillment event happened.

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
FulfillmentEvent.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to latitude](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-FulfillmentEvent.fields.latitude)latitude

•[Float](/docs/api/admin-graphql/latest/scalars/Float)

    

The latitude where this fulfillment event occurred.

[Anchor to longitude](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-FulfillmentEvent.fields.longitude)longitude

•[Float](/docs/api/admin-graphql/latest/scalars/Float)

    

The longitude where this fulfillment event occurred.

[Anchor to message](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-FulfillmentEvent.fields.message)message

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

A message associated with this fulfillment event.

[Anchor to province](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-FulfillmentEvent.fields.province)province

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The province where this fulfillment event occurred.

[Anchor to status](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-FulfillmentEvent.fields.status)status

•[FulfillmentEventStatus!](/docs/api/admin-
graphql/latest/enums/FulfillmentEventStatus)

non-null

    

The status of this fulfillment event.

Show enum values

[Anchor to zip](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
FulfillmentEvent.fields.zip)zip

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The zip code of the location where this fulfillment event occurred.

[Anchor to FulfillmentHold](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
FulfillmentHold)[FulfillmentHold](/docs/api/admin-
graphql/latest/objects/FulfillmentHold)

•OBJECT

    

A fulfillment hold currently applied on a fulfillment order.

Show fields

[Anchor to displayReason](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
FulfillmentHold.fields.displayReason)displayReason

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The localized reason for the fulfillment hold for display purposes.

[Anchor to handle](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-FulfillmentHold.fields.handle)handle

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

An identifier an app can use to reference one of many holds it applied to a
fulfillment order. This field must be unique among the holds that a single app
applies to a single fulfillment order.

[Anchor to heldByApp](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-FulfillmentHold.fields.heldByApp)heldByApp

•[App](/docs/api/admin-graphql/latest/objects/App)

    

The app that created the fulfillment hold.

Show fields

[Anchor to heldByRequestingApp](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
FulfillmentHold.fields.heldByRequestingApp)heldByRequestingApp

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

A boolean value that indicates whether the requesting app created the
fulfillment hold.

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
FulfillmentHold.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to reason](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-FulfillmentHold.fields.reason)reason

•[FulfillmentHoldReason!](/docs/api/admin-
graphql/latest/enums/FulfillmentHoldReason)

non-null

    

The reason for the fulfillment hold.

Show enum values

[Anchor to reasonNotes](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
FulfillmentHold.fields.reasonNotes)reasonNotes

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

Additional information about the fulfillment hold reason.

[Anchor to FulfillmentLineItem](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
FulfillmentLineItem)[FulfillmentLineItem](/docs/api/admin-
graphql/latest/objects/FulfillmentLineItem)

•OBJECT

    

Represents a line item from an order that's included in a fulfillment.

Show fields

[Anchor to discountedTotalSet](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
FulfillmentLineItem.fields.discountedTotalSet)discountedTotalSet

•[MoneyBag!](/docs/api/admin-graphql/latest/objects/MoneyBag)

non-null

    

The total price after discounts are applied in shop and presentment
currencies. This value doesn't include order-level discounts.

Show fields

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
FulfillmentLineItem.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to lineItem](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-FulfillmentLineItem.fields.lineItem)lineItem

•[LineItem!](/docs/api/admin-graphql/latest/objects/LineItem)

non-null

    

The associated order's line item.

Show fields

[Anchor to originalTotalSet](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
FulfillmentLineItem.fields.originalTotalSet)originalTotalSet

•[MoneyBag!](/docs/api/admin-graphql/latest/objects/MoneyBag)

non-null

    

The total price before discounts are applied in shop and presentment
currencies.

Show fields

[Anchor to quantity](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-FulfillmentLineItem.fields.quantity)quantity

•[Int](/docs/api/admin-graphql/latest/scalars/Int)

    

Number of line items in the fulfillment.

[Anchor to discountedTotal](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
FulfillmentLineItem.fields.discountedTotal)discountedTotal

•[Money!](/docs/api/admin-graphql/latest/scalars/Money)

non-nullDeprecated

    

[Anchor to originalTotal](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
FulfillmentLineItem.fields.originalTotal)originalTotal

•[Money!](/docs/api/admin-graphql/latest/scalars/Money)

non-nullDeprecated

    

[Anchor to FulfillmentOrder](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
FulfillmentOrder)[FulfillmentOrder](/docs/api/admin-
graphql/latest/objects/FulfillmentOrder)

•OBJECT

    

The FulfillmentOrder object represents either an item or a group of items in
an [Order](https://shopify.dev/api/admin-graphql/latest/objects/Order) that
are expected to be fulfilled from the same location. There can be more than
one fulfillment order for an [order](https://shopify.dev/api/admin-
graphql/latest/objects/Order) at a given location.

![](/assets/api/reference/fulfillment_order_relationships.png)

Fulfillment orders represent the work which is intended to be done in relation
to an order. When fulfillment has started for one or more line items, a
[Fulfillment](https://shopify.dev/api/admin-
graphql/latest/objects/Fulfillment) is created by a merchant or third party to
represent the ongoing or completed work of fulfillment.

See below for more details on creating fulfillments.

* * *

Note

Shopify creates fulfillment orders automatically when an order is created. It
is not possible to manually create fulfillment orders.

See below for more details on the lifecycle of a fulfillment order.

* * *

## Retrieving fulfillment orders

### Fulfillment orders from an order

All fulfillment orders related to a given order can be retrieved with the
[Order.fulfillmentOrders](https://shopify.dev/api/admin-
graphql/latest/objects/Order#connection-order-fulfillmentorders) connection.

API access scopes govern which fulfillments orders are returned to clients. An
API client will only receive a subset of the fulfillment orders which belong
to an order if they don't have the necessary access scopes to view all of the
fulfillment orders.

### Fulfillment orders assigned to the app for fulfillment

Fulfillment service apps can retrieve the fulfillment orders which have been
assigned to their locations with the
[assignedFulfillmentOrders](https://shopify.dev/api/admin-
graphql/2024-07/objects/queryroot#connection-assignedfulfillmentorders)
connection. Use the `assignmentStatus` argument to control whether all
assigned fulfillment orders should be returned or only those where a merchant
has sent a [fulfillment request](https://shopify.dev/api/admin-
graphql/latest/objects/FulfillmentOrderMerchantRequest) and it has yet to be
responded to.

The API client must be granted the `read_assigned_fulfillment_orders` access
scope to access the assigned fulfillment orders.

### All fulfillment orders

Apps can retrieve all fulfillment orders with the
[fulfillmentOrders](https://shopify.dev/api/admin-
graphql/latest/queries/fulfillmentOrders) query. This query returns all
assigned, merchant-managed, and third-party fulfillment orders on the shop,
which are accessible to the app according to the fulfillment order access
scopes it was granted with.

## The lifecycle of a fulfillment order

### Fulfillment Order Creation

After an order is created, a background worker performs the order routing
process which determines which locations will be responsible for fulfilling
the purchased items. Once the order routing process is complete, one or more
fulfillment orders will be created and assigned to these locations. It is not
possible to manually create fulfillment orders.

Once a fulfillment order has been created, it will have one of two different
lifecycles depending on the type of location which the fulfillment order is
assigned to.

### The lifecycle of a fulfillment order at a merchant managed location

Fulfillment orders are completed by creating
[fulfillments](https://shopify.dev/api/admin-
graphql/latest/objects/Fulfillment). Fulfillments represents the work done.

For digital products a merchant or an order management app would create a
fulfilment once the digital asset has been provisioned. For example, in the
case of a digital gift card, a merchant would to do this once the gift card
has been activated - before the email has been shipped.

On the other hand, for a traditional shipped order, a merchant or an order
management app would create a fulfillment after picking and packing the items
relating to a fulfillment order, but before the courier has collected the
goods.

[Learn about managing fulfillment orders as an order management
app](https://shopify.dev/apps/fulfillment/order-management-apps/manage-
fulfillments).

### The lifecycle of a fulfillment order at a location which is managed by a
fulfillment service

For fulfillment orders which are assigned to a location that is managed by a
fulfillment service, a merchant or an Order Management App can [send a
fulfillment request](https://shopify.dev/api/admin-
graphql/latest/mutations/fulfillmentOrderSubmitFulfillmentRequest) to the
fulfillment service which operates the location to request that they fulfill
the associated items. A fulfillment service has the option to
[accept](https://shopify.dev/api/admin-
graphql/latest/mutations/fulfillmentOrderAcceptFulfillmentRequest) or
[reject](https://shopify.dev/api/admin-
graphql/latest/mutations/fulfillmentOrderRejectFulfillmentRequest) this
fulfillment request.

Once the fulfillment service has accepted the request, the request can no
longer be cancelled by the merchant or order management app and instead a
[cancellation request must be submitted](https://shopify.dev/api/admin-
graphql/latest/mutations/fulfillmentOrderSubmitCancellationRequest) to the
fulfillment service.

Once a fulfillment service accepts a fulfillment request, then after they are
ready to pack items and send them for delivery, they create fulfillments with
the [fulfillmentCreate](https://shopify.dev/api/admin-
graphql/unstable/mutations/fulfillmentCreate) mutation. They can provide
tracking information right away or create fulfillments without it and then
update the tracking information for fulfillments with the
[fulfillmentTrackingInfoUpdate](https://shopify.dev/api/admin-
graphql/unstable/mutations/fulfillmentTrackingInfoUpdate) mutation.

[Learn about managing fulfillment orders as a fulfillment
service](https://shopify.dev/apps/fulfillment/fulfillment-service-apps/manage-
fulfillments).

## API access scopes

Fulfillment orders are governed by the following API access scopes:

  * The `read_merchant_managed_fulfillment_orders` and `write_merchant_managed_fulfillment_orders` access scopes grant access to fulfillment orders assigned to merchant-managed locations.
  * The `read_assigned_fulfillment_orders` and `write_assigned_fulfillment_orders` access scopes are intended for fulfillment services. These scopes grant access to fulfillment orders assigned to locations that are being managed by fulfillment services.
  * The `read_third_party_fulfillment_orders` and `write_third_party_fulfillment_orders` access scopes grant access to fulfillment orders assigned to locations managed by other fulfillment services.

### Fulfillment service app access scopes

Usually, **fulfillment services** have the `write_assigned_fulfillment_orders`
access scope and don't have the `*_third_party_fulfillment_orders` or
`*_merchant_managed_fulfillment_orders` access scopes. The app will only have
access to the fulfillment orders assigned to their location (or multiple
locations if the app registers multiple fulfillment services on the shop). The
app will not have access to fulfillment orders assigned to merchant-managed
locations or locations owned by other fulfillment service apps.

### Order management app access scopes

**Order management apps** will usually request
`write_merchant_managed_fulfillment_orders` and
`write_third_party_fulfillment_orders` access scopes. This will allow them to
manage all fulfillment orders on behalf of a merchant.

If an app combines the functions of an order management app and a fulfillment
service, then the app should request all access scopes to manage all assigned
and all unassigned fulfillment orders.

## Notifications about fulfillment orders

Fulfillment services are required to [register](https://shopify.dev/api/admin-
graphql/latest/objects/FulfillmentService) a self-hosted callback URL which
has a number of uses. One of these uses is that this callback URL will be
notified whenever a merchant submits a fulfillment or cancellation request.

Both merchants and apps can
[subscribe](https://shopify.dev/apps/fulfillment/fulfillment-service-
apps/manage-fulfillments#webhooks) to the [fulfillment order
webhooks](https://shopify.dev/api/admin-
graphql/latest/enums/WebhookSubscriptionTopic#value-
fulfillmentorderscancellationrequestaccepted) to be notified whenever
fulfillment order related domain events occur.

[Learn about fulfillment workflows](https://shopify.dev/apps/fulfillment).

Show fields

[Anchor to assignedLocation](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
FulfillmentOrder.fields.assignedLocation)assignedLocation

•[FulfillmentOrderAssignedLocation!](/docs/api/admin-
graphql/latest/objects/FulfillmentOrderAssignedLocation)

non-null

    

The fulfillment order's assigned location. This is the location where the
fulfillment is expected to happen.

The fulfillment order's assigned location might change in the following cases:

  * The fulfillment order has been entirely moved to a new location. For example, the [fulfillmentOrderMove](https://shopify.dev/api/admin-graphql/latest/mutations/fulfillmentOrderMove) mutation has been called, and you see the original fulfillment order in the [movedFulfillmentOrder](https://shopify.dev/api/admin-graphql/latest/mutations/fulfillmentOrderMove#field-fulfillmentordermovepayload-movedfulfillmentorder) field within the mutation's response.
  * Work on the fulfillment order hasn't yet begun, which means that the fulfillment order has the [OPEN](https://shopify.dev/api/admin-graphql/latest/enums/FulfillmentOrderStatus#value-open), [SCHEDULED](https://shopify.dev/api/admin-graphql/latest/enums/FulfillmentOrderStatus#value-scheduled), or [ON_HOLD](https://shopify.dev/api/admin-graphql/latest/enums/FulfillmentOrderStatus#value-onhold) status, and the shop's location properties might be undergoing edits (for example, in the Shopify admin).

Show fields

[Anchor to channelId](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-FulfillmentOrder.fields.channelId)channelId

•[ID](/docs/api/admin-graphql/latest/scalars/ID)

    

ID of the channel that created the order.

[Anchor to createdAt](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-FulfillmentOrder.fields.createdAt)createdAt

•[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime)

non-null

    

Date and time when the fulfillment order was created.

[Anchor to deliveryMethod](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
FulfillmentOrder.fields.deliveryMethod)deliveryMethod

•[DeliveryMethod](/docs/api/admin-graphql/latest/objects/DeliveryMethod)

    

Delivery method of this fulfillment order.

Show fields

[Anchor to destination](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
FulfillmentOrder.fields.destination)destination

•[FulfillmentOrderDestination](/docs/api/admin-
graphql/latest/objects/FulfillmentOrderDestination)

    

The destination where the items should be sent.

Show fields

[Anchor to fulfillAt](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-FulfillmentOrder.fields.fulfillAt)fulfillAt

•[DateTime](/docs/api/admin-graphql/latest/scalars/DateTime)

    

The date and time at which the fulfillment order will be fulfillable. When
this date and time is reached, the scheduled fulfillment order is
automatically transitioned to open. For example, the `fulfill_at` date for a
subscription order might be the 1st of each month, a pre-order `fulfill_at`
date would be `nil`, and a standard order `fulfill_at` date would be the order
creation date.

[Anchor to fulfillBy](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-FulfillmentOrder.fields.fulfillBy)fulfillBy

•[DateTime](/docs/api/admin-graphql/latest/scalars/DateTime)

    

The latest date and time by which all items in the fulfillment order need to
be fulfilled.

[Anchor to fulfillmentHolds](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
FulfillmentOrder.fields.fulfillmentHolds)fulfillmentHolds

•[[FulfillmentHold!]!](/docs/api/admin-graphql/latest/objects/FulfillmentHold)

non-null

    

The fulfillment holds applied on the fulfillment order.

Show fields

[Anchor to fulfillmentOrdersForMerge](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
FulfillmentOrder.fields.fulfillmentOrdersForMerge)fulfillmentOrdersForMerge

•[FulfillmentOrderConnection!](/docs/api/admin-
graphql/latest/connections/FulfillmentOrderConnection)

non-null

    

Fulfillment orders eligible for merging with the given fulfillment order.

Show fields

[Anchor to fulfillments](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
FulfillmentOrder.fields.fulfillments)fulfillments

•[FulfillmentConnection!](/docs/api/admin-
graphql/latest/connections/FulfillmentConnection)

non-null

    

A list of fulfillments for the fulfillment order.

Show fields

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
FulfillmentOrder.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to internationalDuties](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
FulfillmentOrder.fields.internationalDuties)internationalDuties

•[FulfillmentOrderInternationalDuties](/docs/api/admin-
graphql/latest/objects/FulfillmentOrderInternationalDuties)

    

The duties delivery method of this fulfillment order.

Show fields

[Anchor to lineItems](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-FulfillmentOrder.fields.lineItems)lineItems

•[FulfillmentOrderLineItemConnection!](/docs/api/admin-
graphql/latest/connections/FulfillmentOrderLineItemConnection)

non-null

    

A list of the fulfillment order's line items.

Show fields

[Anchor to locationsForMove](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
FulfillmentOrder.fields.locationsForMove)locationsForMove

•[FulfillmentOrderLocationForMoveConnection!](/docs/api/admin-
graphql/latest/connections/FulfillmentOrderLocationForMoveConnection)

non-null

    

A list of locations that the fulfillment order can potentially move to.

Show fields

[Anchor to merchantRequests](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
FulfillmentOrder.fields.merchantRequests)merchantRequests

•[FulfillmentOrderMerchantRequestConnection!](/docs/api/admin-
graphql/latest/connections/FulfillmentOrderMerchantRequestConnection)

non-null

    

A list of requests sent by the merchant or an order management app to the
fulfillment service for the fulfillment order.

Show fields

[Anchor to order](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-FulfillmentOrder.fields.order)order

•[Order!](/docs/api/admin-graphql/latest/objects/Order)

non-null

    

The order that's associated with the fulfillment order.

Show fields

[Anchor to orderId](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-FulfillmentOrder.fields.orderId)orderId

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

ID of the order that's associated with the fulfillment order.

[Anchor to orderName](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-FulfillmentOrder.fields.orderName)orderName

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The unique identifier for the order that appears on the order page in the
Shopify admin and the **Order status** page. For example, "#1001", "EN1001",
or "1001-A". This value isn't unique across multiple stores.

[Anchor to orderProcessedAt](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
FulfillmentOrder.fields.orderProcessedAt)orderProcessedAt

•[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime)

non-null

    

The date and time when the order was processed. This date and time might not
match the date and time when the order was created.

[Anchor to requestStatus](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
FulfillmentOrder.fields.requestStatus)requestStatus

•[FulfillmentOrderRequestStatus!](/docs/api/admin-
graphql/latest/enums/FulfillmentOrderRequestStatus)

non-null

    

The request status of the fulfillment order.

Show enum values

[Anchor to status](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-FulfillmentOrder.fields.status)status

•[FulfillmentOrderStatus!](/docs/api/admin-
graphql/latest/enums/FulfillmentOrderStatus)

non-null

    

The status of the fulfillment order.

Show enum values

[Anchor to supportedActions](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
FulfillmentOrder.fields.supportedActions)supportedActions

•[[FulfillmentOrderSupportedAction!]!](/docs/api/admin-
graphql/latest/objects/FulfillmentOrderSupportedAction)

non-null

    

The actions that can be performed on this fulfillment order.

Show fields

[Anchor to updatedAt](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-FulfillmentOrder.fields.updatedAt)updatedAt

•[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime)

non-null

    

The date and time when the fulfillment order was last updated.

[Anchor to FulfillmentOrderDestination](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
FulfillmentOrderDestination)[FulfillmentOrderDestination](/docs/api/admin-
graphql/latest/objects/FulfillmentOrderDestination)

•OBJECT

    

Represents the destination where the items should be sent upon fulfillment.

Show fields

[Anchor to address1](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-FulfillmentOrderDestination.fields.address1)address1

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The first line of the address of the destination.

[Anchor to address2](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-FulfillmentOrderDestination.fields.address2)address2

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The second line of the address of the destination.

[Anchor to city](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-FulfillmentOrderDestination.fields.city)city

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The city of the destination.

[Anchor to company](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-FulfillmentOrderDestination.fields.company)company

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The company of the destination.

[Anchor to countryCode](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
FulfillmentOrderDestination.fields.countryCode)countryCode

•[CountryCode](/docs/api/admin-graphql/latest/enums/CountryCode)

    

The two-letter country code of the destination.

Show enum values

[Anchor to email](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-FulfillmentOrderDestination.fields.email)email

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The email of the customer at the destination.

[Anchor to firstName](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-FulfillmentOrderDestination.fields.firstName)firstName

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The first name of the customer at the destination.

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
FulfillmentOrderDestination.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to lastName](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-FulfillmentOrderDestination.fields.lastName)lastName

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The last name of the customer at the destination.

[Anchor to location](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-FulfillmentOrderDestination.fields.location)location

•[Location](/docs/api/admin-graphql/latest/objects/Location)

    

The location designated for the pick-up of the fulfillment order.

Show fields

[Anchor to phone](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-FulfillmentOrderDestination.fields.phone)phone

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The phone number of the customer at the destination.

[Anchor to province](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-FulfillmentOrderDestination.fields.province)province

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The province of the destination.

[Anchor to zip](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
FulfillmentOrderDestination.fields.zip)zip

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The ZIP code of the destination.

[Anchor to FulfillmentOrderLineItem](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
FulfillmentOrderLineItem)[FulfillmentOrderLineItem](/docs/api/admin-
graphql/latest/objects/FulfillmentOrderLineItem)

•OBJECT

    

Associates an order line item with quantities requiring fulfillment from the
respective fulfillment order.

Show fields

[Anchor to financialSummaries](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
FulfillmentOrderLineItem.fields.financialSummaries)financialSummaries

•[[FulfillmentOrderLineItemFinancialSummary!]!](/docs/api/admin-
graphql/latest/objects/FulfillmentOrderLineItemFinancialSummary)

non-null

    

The financial summary for the Fulfillment Order's Line Items.

Show fields

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
FulfillmentOrderLineItem.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to image](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-FulfillmentOrderLineItem.fields.image)image

•[Image](/docs/api/admin-graphql/latest/objects/Image)

    

The image associated to the line item's variant.

Show fields

[Anchor to inventoryItemId](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
FulfillmentOrderLineItem.fields.inventoryItemId)inventoryItemId

•[ID](/docs/api/admin-graphql/latest/scalars/ID)

    

The ID of the inventory item.

[Anchor to lineItem](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-FulfillmentOrderLineItem.fields.lineItem)lineItem

•[LineItem!](/docs/api/admin-graphql/latest/objects/LineItem)

non-null

    

The associated order line item.

Show fields

[Anchor to productTitle](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
FulfillmentOrderLineItem.fields.productTitle)productTitle

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The title of the product.

[Anchor to remainingQuantity](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
FulfillmentOrderLineItem.fields.remainingQuantity)remainingQuantity

•[Int!](/docs/api/admin-graphql/latest/scalars/Int)

non-null

    

The number of units remaining to be fulfilled.

[Anchor to requiresShipping](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
FulfillmentOrderLineItem.fields.requiresShipping)requiresShipping

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether physical shipping is required for the variant.

[Anchor to sku](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
FulfillmentOrderLineItem.fields.sku)sku

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The variant SKU number.

[Anchor to totalQuantity](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
FulfillmentOrderLineItem.fields.totalQuantity)totalQuantity

•[Int!](/docs/api/admin-graphql/latest/scalars/Int)

non-null

    

The total number of units to be fulfilled.

[Anchor to variant](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-FulfillmentOrderLineItem.fields.variant)variant

•[ProductVariant](/docs/api/admin-graphql/latest/objects/ProductVariant)

    

The product variant associated to the fulfillment order line item.

Show fields

[Anchor to variantTitle](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
FulfillmentOrderLineItem.fields.variantTitle)variantTitle

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The name of the variant.

[Anchor to vendor](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-FulfillmentOrderLineItem.fields.vendor)vendor

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The name of the vendor who made the variant.

[Anchor to warnings](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-FulfillmentOrderLineItem.fields.warnings)warnings

•[[FulfillmentOrderLineItemWarning!]!](/docs/api/admin-
graphql/latest/objects/FulfillmentOrderLineItemWarning)

non-null

    

Warning messages for a fulfillment order line item.

Show fields

[Anchor to weight](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-FulfillmentOrderLineItem.fields.weight)weight

•[Weight](/docs/api/admin-graphql/latest/objects/Weight)

    

The weight of a line item unit.

Show fields

[Anchor to originalUnitPriceSet](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
FulfillmentOrderLineItem.fields.originalUnitPriceSet)originalUnitPriceSet

•[MoneyBag!](/docs/api/admin-graphql/latest/objects/MoneyBag)

non-nullDeprecated

    

Show fields

[Anchor to FulfillmentOrderMerchantRequest](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
FulfillmentOrderMerchantRequest)[FulfillmentOrderMerchantRequest](/docs/api/admin-
graphql/latest/objects/FulfillmentOrderMerchantRequest)

•OBJECT

    

A request made by the merchant or an order management app to a fulfillment
service for a fulfillment order.

Show fields

[Anchor to fulfillmentOrder](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
FulfillmentOrderMerchantRequest.fields.fulfillmentOrder)fulfillmentOrder

•[FulfillmentOrder!](/docs/api/admin-graphql/latest/objects/FulfillmentOrder)

non-null

    

The fulfillment order associated with the merchant request.

Show fields

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
FulfillmentOrderMerchantRequest.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to kind](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-FulfillmentOrderMerchantRequest.fields.kind)kind

•[FulfillmentOrderMerchantRequestKind!](/docs/api/admin-
graphql/latest/enums/FulfillmentOrderMerchantRequestKind)

non-null

    

The kind of request made.

Show enum values

[Anchor to message](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-FulfillmentOrderMerchantRequest.fields.message)message

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The optional message that the merchant included in the request.

[Anchor to requestOptions](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
FulfillmentOrderMerchantRequest.fields.requestOptions)requestOptions

•[JSON](/docs/api/admin-graphql/latest/scalars/JSON)

    

Additional options requested by the merchant. These depend on the `kind` of
the request. For example, for a `FULFILLMENT_REQUEST`, one option is
`notify_customer`, which indicates whether the merchant intends to notify the
customer upon fulfillment. The fulfillment service can then set
`notifyCustomer` when making calls to `FulfillmentCreate`.

[Anchor to responseData](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
FulfillmentOrderMerchantRequest.fields.responseData)responseData

•[JSON](/docs/api/admin-graphql/latest/scalars/JSON)

    

The response from the fulfillment service.

[Anchor to sentAt](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-FulfillmentOrderMerchantRequest.fields.sentAt)sentAt

•[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime)

non-null

    

The timestamp when the request was made.

[Anchor to GenericFile](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
GenericFile)[GenericFile](/docs/api/admin-graphql/latest/objects/GenericFile)

•OBJECT

    

Represents any file other than HTML.

Show fields

[Anchor to alt](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
GenericFile.fields.alt)alt

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

A word or phrase to describe the contents or the function of a file.

[Anchor to createdAt](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-GenericFile.fields.createdAt)createdAt

•[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime)

non-null

    

The date and time ([ISO 8601 format](http://en.wikipedia.org/wiki/ISO_8601))
when the file was created.

[Anchor to fileErrors](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
GenericFile.fields.fileErrors)fileErrors

•[[FileError!]!](/docs/api/admin-graphql/latest/objects/FileError)

non-null

    

Any errors that have occurred on the file.

Show fields

[Anchor to fileStatus](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
GenericFile.fields.fileStatus)fileStatus

•[FileStatus!](/docs/api/admin-graphql/latest/enums/FileStatus)

non-null

    

The status of the file.

Show enum values

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
GenericFile.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to mimeType](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-GenericFile.fields.mimeType)mimeType

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The generic file's MIME type.

[Anchor to originalFileSize](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
GenericFile.fields.originalFileSize)originalFileSize

•[Int](/docs/api/admin-graphql/latest/scalars/Int)

    

The generic file's size in bytes.

[Anchor to preview](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-GenericFile.fields.preview)preview

•[MediaPreviewImage](/docs/api/admin-graphql/latest/objects/MediaPreviewImage)

    

The preview image for the media.

Show fields

[Anchor to updatedAt](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-GenericFile.fields.updatedAt)updatedAt

•[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime)

non-null

    

The date and time ([ISO 8601 format](http://en.wikipedia.org/wiki/ISO_8601))
when the file was last updated.

[Anchor to url](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
GenericFile.fields.url)url

•[URL](/docs/api/admin-graphql/latest/scalars/URL)

    

The generic file's URL.

[Anchor to GiftCard](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-GiftCard)[GiftCard](/docs/api/admin-graphql/latest/objects/GiftCard)

•OBJECT

    

Represents an issued gift card.

Show fields

[Anchor to balance](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-GiftCard.fields.balance)balance

•[MoneyV2!](/docs/api/admin-graphql/latest/objects/MoneyV2)

non-null

    

The gift card's remaining balance.

Show fields

[Anchor to createdAt](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-GiftCard.fields.createdAt)createdAt

•[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime)

non-null

    

The date and time at which the gift card was created.

[Anchor to customer](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-GiftCard.fields.customer)customer

•[Customer](/docs/api/admin-graphql/latest/objects/Customer)

    

The customer who will receive the gift card.

Show fields

[Anchor to deactivatedAt](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
GiftCard.fields.deactivatedAt)deactivatedAt

•[DateTime](/docs/api/admin-graphql/latest/scalars/DateTime)

    

The date and time at which the gift card was deactivated.

[Anchor to enabled](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-GiftCard.fields.enabled)enabled

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether the gift card is enabled.

[Anchor to expiresOn](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-GiftCard.fields.expiresOn)expiresOn

•[Date](/docs/api/admin-graphql/latest/scalars/Date)

    

The date at which the gift card will expire.

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
GiftCard.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to initialValue](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
GiftCard.fields.initialValue)initialValue

•[MoneyV2!](/docs/api/admin-graphql/latest/objects/MoneyV2)

non-null

    

The initial value of the gift card.

Show fields

[Anchor to lastCharacters](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
GiftCard.fields.lastCharacters)lastCharacters

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The final four characters of the gift card code.

[Anchor to maskedCode](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
GiftCard.fields.maskedCode)maskedCode

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The gift card code. Everything but the final four characters is masked.

[Anchor to note](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-GiftCard.fields.note)note

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The note associated with the gift card, which isn't visible to the customer.

[Anchor to order](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-GiftCard.fields.order)order

•[Order](/docs/api/admin-graphql/latest/objects/Order)

    

The order associated with the gift card. This value is `null` if the gift card
was issued manually.

Show fields

[Anchor to recipientAttributes](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
GiftCard.fields.recipientAttributes)recipientAttributes

•[GiftCardRecipient](/docs/api/admin-graphql/latest/objects/GiftCardRecipient)

    

The recipient who will receive the gift card.

Show fields

[Anchor to templateSuffix](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
GiftCard.fields.templateSuffix)templateSuffix

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The theme template used to render the gift card online.

[Anchor to transactions](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
GiftCard.fields.transactions)transactions

•[GiftCardTransactionConnection](/docs/api/admin-
graphql/latest/connections/GiftCardTransactionConnection)

    

The transaction history of the gift card.

Show fields

[Anchor to updatedAt](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-GiftCard.fields.updatedAt)updatedAt

•[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime)

non-null

    

The date and time at which the gift card was updated.

[Anchor to GiftCardCreditTransaction](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
GiftCardCreditTransaction)[GiftCardCreditTransaction](/docs/api/admin-
graphql/latest/objects/GiftCardCreditTransaction)

•OBJECT

    

A credit transaction which increases the gift card balance.

Show fields

[Anchor to amount](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-GiftCardCreditTransaction.fields.amount)amount

•[MoneyV2!](/docs/api/admin-graphql/latest/objects/MoneyV2)

non-null

    

The amount of the transaction.

Show fields

[Anchor to giftCard](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-GiftCardCreditTransaction.fields.giftCard)giftCard

•[GiftCard!](/docs/api/admin-graphql/latest/objects/GiftCard)

non-null

    

The gift card that the transaction belongs to.

Show fields

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
GiftCardCreditTransaction.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to metafield](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-GiftCardCreditTransaction.fields.metafield)metafield

•[Metafield](/docs/api/admin-graphql/latest/objects/Metafield)

    

A [custom field](https://shopify.dev/docs/apps/build/custom-data), including
its `namespace` and `key`, that's associated with a Shopify resource for the
purposes of adding and storing additional information.

Show fields

[Anchor to metafields](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
GiftCardCreditTransaction.fields.metafields)metafields

•[MetafieldConnection!](/docs/api/admin-
graphql/latest/connections/MetafieldConnection)

non-null

    

A list of [custom fields](https://shopify.dev/docs/apps/build/custom-data)
that a merchant associates with a Shopify resource.

Show fields

[Anchor to note](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-GiftCardCreditTransaction.fields.note)note

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

A note about the transaction.

[Anchor to processedAt](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
GiftCardCreditTransaction.fields.processedAt)processedAt

•[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime)

non-null

    

The date and time when the transaction was processed.

[Anchor to GiftCardDebitTransaction](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
GiftCardDebitTransaction)[GiftCardDebitTransaction](/docs/api/admin-
graphql/latest/objects/GiftCardDebitTransaction)

•OBJECT

    

A debit transaction which decreases the gift card balance.

Show fields

[Anchor to amount](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-GiftCardDebitTransaction.fields.amount)amount

•[MoneyV2!](/docs/api/admin-graphql/latest/objects/MoneyV2)

non-null

    

The amount of the transaction.

Show fields

[Anchor to giftCard](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-GiftCardDebitTransaction.fields.giftCard)giftCard

•[GiftCard!](/docs/api/admin-graphql/latest/objects/GiftCard)

non-null

    

The gift card that the transaction belongs to.

Show fields

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
GiftCardDebitTransaction.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to metafield](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-GiftCardDebitTransaction.fields.metafield)metafield

•[Metafield](/docs/api/admin-graphql/latest/objects/Metafield)

    

A [custom field](https://shopify.dev/docs/apps/build/custom-data), including
its `namespace` and `key`, that's associated with a Shopify resource for the
purposes of adding and storing additional information.

Show fields

[Anchor to metafields](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
GiftCardDebitTransaction.fields.metafields)metafields

•[MetafieldConnection!](/docs/api/admin-
graphql/latest/connections/MetafieldConnection)

non-null

    

A list of [custom fields](https://shopify.dev/docs/apps/build/custom-data)
that a merchant associates with a Shopify resource.

Show fields

[Anchor to note](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-GiftCardDebitTransaction.fields.note)note

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

A note about the transaction.

[Anchor to processedAt](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
GiftCardDebitTransaction.fields.processedAt)processedAt

•[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime)

non-null

    

The date and time when the transaction was processed.

[Anchor to InventoryAdjustmentGroup](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
InventoryAdjustmentGroup)[InventoryAdjustmentGroup](/docs/api/admin-
graphql/latest/objects/InventoryAdjustmentGroup)

•OBJECT

    

Represents a group of adjustments made as part of the same operation.

Show fields

[Anchor to app](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
InventoryAdjustmentGroup.fields.app)app

•[App](/docs/api/admin-graphql/latest/objects/App)

    

The app that triggered the inventory event, if one exists.

Show fields

[Anchor to changes](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-InventoryAdjustmentGroup.fields.changes)changes

•[[InventoryChange!]!](/docs/api/admin-graphql/latest/objects/InventoryChange)

non-null

    

The set of inventory quantity changes that occurred in the inventory event.

Show fields

[Anchor to createdAt](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-InventoryAdjustmentGroup.fields.createdAt)createdAt

•[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime)

non-null

    

The date and time the inventory adjustment group was created.

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
InventoryAdjustmentGroup.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to reason](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-InventoryAdjustmentGroup.fields.reason)reason

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The reason for the group of adjustments.

[Anchor to referenceDocumentUri](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
InventoryAdjustmentGroup.fields.referenceDocumentUri)referenceDocumentUri

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

A freeform URI that represents why the inventory change happened. This can be
the entity adjusting inventory quantities or the Shopify resource that's
associated with the inventory adjustment. For example, a unit in a draft order
might have been previously reserved, and a merchant later creates an order
from the draft order. In this case, the `referenceDocumentUri` for the
inventory adjustment is a URI referencing the order ID.

[Anchor to staffMember](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
InventoryAdjustmentGroup.fields.staffMember)staffMember

•[StaffMember](/docs/api/admin-graphql/latest/objects/StaffMember)

    

The staff member associated with the inventory event.

Show fields

[Anchor to InventoryItem](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
InventoryItem)[InventoryItem](/docs/api/admin-
graphql/latest/objects/InventoryItem)

•OBJECT

    

Represents the goods available to be shipped to a customer. It holds essential
information about the goods, including SKU and whether it is tracked. Learn
[more about the relationships between inventory
objects](https://shopify.dev/docs/apps/build/orders-fulfillment/inventory-
management-apps/manage-quantities-states#inventory-object-relationships).

Show fields

[Anchor to countryCodeOfOrigin](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
InventoryItem.fields.countryCodeOfOrigin)countryCodeOfOrigin

•[CountryCode](/docs/api/admin-graphql/latest/enums/CountryCode)

    

The ISO 3166-1 alpha-2 country code of where the item originated from.

Show enum values

[Anchor to countryHarmonizedSystemCodes](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
InventoryItem.fields.countryHarmonizedSystemCodes)countryHarmonizedSystemCodes

•[CountryHarmonizedSystemCodeConnection!](/docs/api/admin-
graphql/latest/connections/CountryHarmonizedSystemCodeConnection)

non-null

    

A list of country specific harmonized system codes.

Show fields

[Anchor to createdAt](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-InventoryItem.fields.createdAt)createdAt

•[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime)

non-null

    

The date and time when the inventory item was created.

[Anchor to duplicateSkuCount](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
InventoryItem.fields.duplicateSkuCount)duplicateSkuCount

•[Int!](/docs/api/admin-graphql/latest/scalars/Int)

non-null

    

The number of inventory items that share the same SKU with this item.

[Anchor to harmonizedSystemCode](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
InventoryItem.fields.harmonizedSystemCode)harmonizedSystemCode

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The harmonized system code of the item. This must be a number between 6 and 13
digits.

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
InventoryItem.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to inventoryHistoryUrl](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
InventoryItem.fields.inventoryHistoryUrl)inventoryHistoryUrl

•[URL](/docs/api/admin-graphql/latest/scalars/URL)

    

The URL that points to the inventory history for the item.

[Anchor to inventoryLevel](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
InventoryItem.fields.inventoryLevel)inventoryLevel

•[InventoryLevel](/docs/api/admin-graphql/latest/objects/InventoryLevel)

    

The inventory item's quantities at the specified location.

Show fields

[Anchor to inventoryLevels](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
InventoryItem.fields.inventoryLevels)inventoryLevels

•[InventoryLevelConnection!](/docs/api/admin-
graphql/latest/connections/InventoryLevelConnection)

non-null

    

A list of the inventory item's quantities for each location that the inventory
item can be stocked at.

Show fields

[Anchor to legacyResourceId](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
InventoryItem.fields.legacyResourceId)legacyResourceId

•[UnsignedInt64!](/docs/api/admin-graphql/latest/scalars/UnsignedInt64)

non-null

    

The ID of the corresponding resource in the REST Admin API.

[Anchor to locationsCount](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
InventoryItem.fields.locationsCount)locationsCount

•[Count](/docs/api/admin-graphql/latest/objects/Count)

    

The number of locations where this inventory item is stocked.

Show fields

[Anchor to measurement](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
InventoryItem.fields.measurement)measurement

•[InventoryItemMeasurement!](/docs/api/admin-
graphql/latest/objects/InventoryItemMeasurement)

non-null

    

The packaging dimensions of the inventory item.

Show fields

[Anchor to provinceCodeOfOrigin](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
InventoryItem.fields.provinceCodeOfOrigin)provinceCodeOfOrigin

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The ISO 3166-2 alpha-2 province code of where the item originated from.

[Anchor to requiresShipping](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
InventoryItem.fields.requiresShipping)requiresShipping

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether the inventory item requires shipping.

[Anchor to sku](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
InventoryItem.fields.sku)sku

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

Inventory item SKU. Case-sensitive string.

[Anchor to tracked](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-InventoryItem.fields.tracked)tracked

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether inventory levels are tracked for the item.

[Anchor to trackedEditable](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
InventoryItem.fields.trackedEditable)trackedEditable

•[EditableProperty!](/docs/api/admin-graphql/latest/objects/EditableProperty)

non-null

    

Whether the value of the `tracked` field for the inventory item can be
changed.

Show fields

[Anchor to unitCost](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-InventoryItem.fields.unitCost)unitCost

•[MoneyV2](/docs/api/admin-graphql/latest/objects/MoneyV2)

    

Unit cost associated with the inventory item. Note: the user must have "View
product costs" permission granted in order to access this field once product
granular permissions are enabled.

Show fields

[Anchor to updatedAt](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-InventoryItem.fields.updatedAt)updatedAt

•[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime)

non-null

    

The date and time when the inventory item was updated.

[Anchor to variant](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-InventoryItem.fields.variant)variant

•[ProductVariant!](/docs/api/admin-graphql/latest/objects/ProductVariant)

non-null

    

The variant that owns this inventory item.

Show fields

[Anchor to InventoryItemMeasurement](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
InventoryItemMeasurement)[InventoryItemMeasurement](/docs/api/admin-
graphql/latest/objects/InventoryItemMeasurement)

•OBJECT

    

Represents the packaged dimension for an inventory item.

Show fields

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
InventoryItemMeasurement.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to weight](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-InventoryItemMeasurement.fields.weight)weight

•[Weight](/docs/api/admin-graphql/latest/objects/Weight)

    

The weight of the inventory item.

Show fields

[Anchor to InventoryLevel](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
InventoryLevel)[InventoryLevel](/docs/api/admin-
graphql/latest/objects/InventoryLevel)

•OBJECT

    

The quantities of an inventory item that are related to a specific location.
Learn [more about the relationships between inventory
objects](https://shopify.dev/docs/apps/build/orders-fulfillment/inventory-
management-apps/manage-quantities-states#inventory-object-relationships).

Show fields

[Anchor to canDeactivate](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
InventoryLevel.fields.canDeactivate)canDeactivate

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether the inventory items associated with the inventory level can be
deactivated.

[Anchor to createdAt](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-InventoryLevel.fields.createdAt)createdAt

•[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime)

non-null

    

The date and time when the inventory level was created.

[Anchor to deactivationAlert](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
InventoryLevel.fields.deactivationAlert)deactivationAlert

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

Describes either the impact of deactivating the inventory level, or why the
inventory level can't be deactivated.

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
InventoryLevel.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to item](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-InventoryLevel.fields.item)item

•[InventoryItem!](/docs/api/admin-graphql/latest/objects/InventoryItem)

non-null

    

Inventory item associated with the inventory level.

Show fields

[Anchor to location](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-InventoryLevel.fields.location)location

•[Location!](/docs/api/admin-graphql/latest/objects/Location)

non-null

    

The location associated with the inventory level.

Show fields

[Anchor to quantities](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
InventoryLevel.fields.quantities)quantities

•[[InventoryQuantity!]!](/docs/api/admin-
graphql/latest/objects/InventoryQuantity)

non-null

    

The quantity of an inventory item at a specific location, for a quantity
[name](https://shopify.dev/docs/apps/fulfillment/inventory-management-
apps#inventory-states).

Show fields

[Anchor to scheduledChanges](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
InventoryLevel.fields.scheduledChanges)scheduledChanges

•[InventoryScheduledChangeConnection!](/docs/api/admin-
graphql/latest/connections/InventoryScheduledChangeConnection)

non-null

    

Scheduled changes for the requested quantity names.

Show fields

[Anchor to updatedAt](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-InventoryLevel.fields.updatedAt)updatedAt

•[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime)

non-null

    

The date and time when the inventory level was updated.

[Anchor to InventoryQuantity](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
InventoryQuantity)[InventoryQuantity](/docs/api/admin-
graphql/latest/objects/InventoryQuantity)

•OBJECT

    

The `InventoryQuantity` object lets you manage and track inventory quantities
for specific [states](https://shopify.dev/docs/apps/fulfillment/inventory-
management-apps#inventory-states). Inventory quantities represent different
states of items such as available for purchase, committed to orders, reserved
for drafts, incoming from suppliers, or set aside for quality control or
safety stock.

You can use [inventory levels](https://shopify.dev/docs/api/admin-
graphql/latest/objects/inventorylevel) to manage where inventory items are
stocked. You can also [make inventory
adjustments](https://shopify.dev/docs/api/admin-
graphql/latest/mutations/inventoryAdjustQuantities) to apply changes to
inventory quantities.

Inventory quantities can be managed by a merchant or by [fulfillment
services](https://shopify.dev/docs/api/admin-
graphql/latest/objects/fulfillmentservice) that handle inventory tracking.
Learn more about working with [Shopify's inventory management
system](https://shopify.dev/docs/apps/fulfillment/inventory-management-apps).

Show fields

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
InventoryQuantity.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to name](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-InventoryQuantity.fields.name)name

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The inventory state
[name](https://shopify.dev/docs/apps/fulfillment/inventory-management-
apps#inventory-states) that identifies the inventory quantity.

[Anchor to quantity](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-InventoryQuantity.fields.quantity)quantity

•[Int!](/docs/api/admin-graphql/latest/scalars/Int)

non-null

    

The quantity of an inventory item at a specific location, for a quantity
[name](https://shopify.dev/docs/apps/fulfillment/inventory-management-
apps#inventory-states).

[Anchor to updatedAt](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-InventoryQuantity.fields.updatedAt)updatedAt

•[DateTime](/docs/api/admin-graphql/latest/scalars/DateTime)

    

When the inventory quantity was last updated.

[Anchor to InventoryShipment](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
InventoryShipment)[InventoryShipment](/docs/api/admin-
graphql/latest/objects/InventoryShipment)

•OBJECT

    

Represents an inventory shipment.

Show fields

[Anchor to dateCreated](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
InventoryShipment.fields.dateCreated)dateCreated

•[DateTime](/docs/api/admin-graphql/latest/scalars/DateTime)

    

The date the shipment was created in UTC.

[Anchor to dateReceived](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
InventoryShipment.fields.dateReceived)dateReceived

•[DateTime](/docs/api/admin-graphql/latest/scalars/DateTime)

    

The date the shipment was initially received in UTC.

[Anchor to dateShipped](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
InventoryShipment.fields.dateShipped)dateShipped

•[DateTime](/docs/api/admin-graphql/latest/scalars/DateTime)

    

The date the shipment was shipped in UTC.

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
InventoryShipment.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to lineItems](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-InventoryShipment.fields.lineItems)lineItems

•[InventoryShipmentLineItemConnection](/docs/api/admin-
graphql/latest/connections/InventoryShipmentLineItemConnection)

    

The line items included in this shipment.

Show fields

[Anchor to lineItemsCount](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
InventoryShipment.fields.lineItemsCount)lineItemsCount

•[Count](/docs/api/admin-graphql/latest/objects/Count)

    

The number of line items associated with the inventory shipment. Limited to a
maximum of 10000 by default.

Show fields

[Anchor to lineItemTotalQuantity](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
InventoryShipment.fields.lineItemTotalQuantity)lineItemTotalQuantity

•[Int!](/docs/api/admin-graphql/latest/scalars/Int)

non-null

    

The total quantity of all items in the shipment.

[Anchor to name](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-InventoryShipment.fields.name)name

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The name of the inventory shipment.

[Anchor to status](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-InventoryShipment.fields.status)status

•[InventoryShipmentStatus!](/docs/api/admin-
graphql/latest/enums/InventoryShipmentStatus)

non-null

    

The current status of the shipment.

Show enum values

[Anchor to totalAcceptedQuantity](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
InventoryShipment.fields.totalAcceptedQuantity)totalAcceptedQuantity

•[Int!](/docs/api/admin-graphql/latest/scalars/Int)

non-null

    

The total quantity of items accepted across all line items in this shipment.

[Anchor to totalReceivedQuantity](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
InventoryShipment.fields.totalReceivedQuantity)totalReceivedQuantity

•[Int!](/docs/api/admin-graphql/latest/scalars/Int)

non-null

    

The total quantity of items received (both accepted and rejected) across all
line items in this shipment.

[Anchor to totalRejectedQuantity](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
InventoryShipment.fields.totalRejectedQuantity)totalRejectedQuantity

•[Int!](/docs/api/admin-graphql/latest/scalars/Int)

non-null

    

The total quantity of items rejected across all line items in this shipment.

[Anchor to tracking](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-InventoryShipment.fields.tracking)tracking

•[InventoryShipmentTracking](/docs/api/admin-
graphql/latest/objects/InventoryShipmentTracking)

    

The tracking information for the shipment.

Show fields

[Anchor to InventoryShipmentLineItem](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
InventoryShipmentLineItem)[InventoryShipmentLineItem](/docs/api/admin-
graphql/latest/objects/InventoryShipmentLineItem)

•OBJECT

    

Represents a single line item within an inventory shipment.

Show fields

[Anchor to acceptedQuantity](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
InventoryShipmentLineItem.fields.acceptedQuantity)acceptedQuantity

•[Int!](/docs/api/admin-graphql/latest/scalars/Int)

non-null

    

The quantity of items that were accepted in this shipment line item.

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
InventoryShipmentLineItem.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to inventoryItem](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
InventoryShipmentLineItem.fields.inventoryItem)inventoryItem

•[InventoryItem](/docs/api/admin-graphql/latest/objects/InventoryItem)

    

The inventory item associated with this line item.

Show fields

[Anchor to quantity](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-InventoryShipmentLineItem.fields.quantity)quantity

•[Int!](/docs/api/admin-graphql/latest/scalars/Int)

non-null

    

The quantity of items in this shipment line item.

[Anchor to rejectedQuantity](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
InventoryShipmentLineItem.fields.rejectedQuantity)rejectedQuantity

•[Int!](/docs/api/admin-graphql/latest/scalars/Int)

non-null

    

The quantity of items that were rejected in this shipment line item.

[Anchor to unreceivedQuantity](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
InventoryShipmentLineItem.fields.unreceivedQuantity)unreceivedQuantity

•[Int!](/docs/api/admin-graphql/latest/scalars/Int)

non-null

    

The total quantity of units that haven't been received (neither accepted or
rejected) in this shipment line item.

[Anchor to InventoryTransfer](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
InventoryTransfer)[InventoryTransfer](/docs/api/admin-
graphql/latest/objects/InventoryTransfer)

•OBJECT

    

Represents the intention to move inventory between locations.

Show fields

[Anchor to dateCreated](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
InventoryTransfer.fields.dateCreated)dateCreated

•[DateTime](/docs/api/admin-graphql/latest/scalars/DateTime)

    

The date and time the inventory transfer was created in UTC format.

[Anchor to destination](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
InventoryTransfer.fields.destination)destination

•[LocationSnapshot](/docs/api/admin-graphql/latest/objects/LocationSnapshot)

    

Snapshot of the destination location (name, address, when snapped) with an
optional link to the live Location object. If the original location is
deleted, the snapshot data will still be available but the location link will
be nil.

Show fields

[Anchor to events](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-InventoryTransfer.fields.events)events

•[EventConnection!](/docs/api/admin-
graphql/latest/connections/EventConnection)

non-null

    

The list of events associated with the inventory transfer.

Show fields

[Anchor to hasTimelineComment](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
InventoryTransfer.fields.hasTimelineComment)hasTimelineComment

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether the merchant has added timeline comments to the inventory transfer.

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
InventoryTransfer.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to lineItems](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-InventoryTransfer.fields.lineItems)lineItems

•[InventoryTransferLineItemConnection!](/docs/api/admin-
graphql/latest/connections/InventoryTransferLineItemConnection)

non-null

    

The line items associated with the inventory transfer.

Show fields

[Anchor to lineItemsCount](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
InventoryTransfer.fields.lineItemsCount)lineItemsCount

•[Count](/docs/api/admin-graphql/latest/objects/Count)

    

The number of line items associated with the inventory transfer. Limited to a
maximum of 10000 by default.

Show fields

[Anchor to metafield](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-InventoryTransfer.fields.metafield)metafield

•[Metafield](/docs/api/admin-graphql/latest/objects/Metafield)

    

A [custom field](https://shopify.dev/docs/apps/build/custom-data), including
its `namespace` and `key`, that's associated with a Shopify resource for the
purposes of adding and storing additional information.

Show fields

[Anchor to metafields](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
InventoryTransfer.fields.metafields)metafields

•[MetafieldConnection!](/docs/api/admin-
graphql/latest/connections/MetafieldConnection)

non-null

    

A list of [custom fields](https://shopify.dev/docs/apps/build/custom-data)
that a merchant associates with a Shopify resource.

Show fields

[Anchor to name](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-InventoryTransfer.fields.name)name

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The name of the inventory transfer.

[Anchor to note](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-InventoryTransfer.fields.note)note

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

Additional note attached to the inventory transfer.

[Anchor to origin](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-InventoryTransfer.fields.origin)origin

•[LocationSnapshot](/docs/api/admin-graphql/latest/objects/LocationSnapshot)

    

Snapshot of the origin location (name, address, when snapped) with an optional
link to the live Location object. If the original location is deleted, the
snapshot data will still be available but the location link will be nil.

Show fields

[Anchor to receivedQuantity](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
InventoryTransfer.fields.receivedQuantity)receivedQuantity

•[Int!](/docs/api/admin-graphql/latest/scalars/Int)

non-null

    

The total quantity of items received in the transfer.

[Anchor to referenceName](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
InventoryTransfer.fields.referenceName)referenceName

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The reference name of the inventory transfer.

[Anchor to shipments](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-InventoryTransfer.fields.shipments)shipments

•[InventoryShipmentConnection!](/docs/api/admin-
graphql/latest/connections/InventoryShipmentConnection)

non-null

    

The shipments associated with the inventory transfer.

Show fields

[Anchor to status](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-InventoryTransfer.fields.status)status

•[InventoryTransferStatus!](/docs/api/admin-
graphql/latest/enums/InventoryTransferStatus)

non-null

    

The current status of the transfer.

Show enum values

[Anchor to tags](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-InventoryTransfer.fields.tags)tags

•[[String!]!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

A list of tags that have been added to the inventory transfer.

[Anchor to totalQuantity](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
InventoryTransfer.fields.totalQuantity)totalQuantity

•[Int!](/docs/api/admin-graphql/latest/scalars/Int)

non-null

    

The total quantity of items being transferred.

[Anchor to metafieldDefinitions](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
InventoryTransfer.fields.metafieldDefinitions)metafieldDefinitions

•[MetafieldDefinitionConnection!](/docs/api/admin-
graphql/latest/connections/MetafieldDefinitionConnection)

non-nullDeprecated

    

Show fields

[Anchor to InventoryTransferLineItem](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
InventoryTransferLineItem)[InventoryTransferLineItem](/docs/api/admin-
graphql/latest/objects/InventoryTransferLineItem)

•OBJECT

    

Represents a line item belonging to an inventory transfer.

Show fields

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
InventoryTransferLineItem.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to inventoryItem](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
InventoryTransferLineItem.fields.inventoryItem)inventoryItem

•[InventoryItem](/docs/api/admin-graphql/latest/objects/InventoryItem)

    

The inventory item associated with this line item.

Show fields

[Anchor to pickedForShipmentQuantity](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
InventoryTransferLineItem.fields.pickedForShipmentQuantity)pickedForShipmentQuantity

•[Int!](/docs/api/admin-graphql/latest/scalars/Int)

non-null

    

The quantity of the item that has been picked for a draft shipment but not yet
shipped.

[Anchor to processableQuantity](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
InventoryTransferLineItem.fields.processableQuantity)processableQuantity

•[Int!](/docs/api/admin-graphql/latest/scalars/Int)

non-null

    

The quantity of the item that can be actioned upon, such as editing the item
quantity on the transfer or adding to a shipment.

[Anchor to shippableQuantity](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
InventoryTransferLineItem.fields.shippableQuantity)shippableQuantity

•[Int!](/docs/api/admin-graphql/latest/scalars/Int)

non-null

    

The quantity of the item that can be shipped.

[Anchor to shippedQuantity](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
InventoryTransferLineItem.fields.shippedQuantity)shippedQuantity

•[Int!](/docs/api/admin-graphql/latest/scalars/Int)

non-null

    

The quantity of the item that has been shipped.

[Anchor to title](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-InventoryTransferLineItem.fields.title)title

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The title of the product associated with this line item.

[Anchor to totalQuantity](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
InventoryTransferLineItem.fields.totalQuantity)totalQuantity

•[Int!](/docs/api/admin-graphql/latest/scalars/Int)

non-null

    

The total quantity of items being transferred.

[Anchor to LineItem](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-LineItem)[LineItem](/docs/api/admin-graphql/latest/objects/LineItem)

•OBJECT

    

The `LineItem` object represents a single product or service that a customer
purchased in an [order](https://shopify.dev/docs/api/admin-
graphql/latest/objects/Order). Each line item is associated with a [product
variant](https://shopify.dev/docs/api/admin-
graphql/latest/objects/ProductVariant) and can have multiple [discount
allocations](https://shopify.dev/docs/api/admin-
graphql/latest/objects/DiscountAllocation). Line items contain details about
what was purchased, including the product variant, quantity, pricing, and
fulfillment status.

Use the `LineItem` object to manage the following processes:

  * [Track the quantity of items](https://shopify.dev/docs/apps/build/orders-fulfillment/order-management-apps/build-fulfillment-solutions) ordered, fulfilled, and unfulfilled.
  * [Calculate prices](https://shopify.dev/docs/apps/build/orders-fulfillment/order-management-apps/edit-orders), including discounts and taxes.
  * Manage fulfillment through [fulfillment services](https://shopify.dev/docs/apps/build/orders-fulfillment/fulfillment-service-apps).
  * Manage [returns](https://shopify.dev/docs/apps/build/orders-fulfillment/returns-apps/build-return-management) and [exchanges](https://shopify.dev/docs/apps/build/orders-fulfillment/returns-apps/manage-exchanges).
  * Handle [subscriptions](https://shopify.dev/docs/apps/build/purchase-options/subscriptions) and recurring orders.

Line items can also include custom attributes and properties, allowing
merchants to add specific details about each item in an order. Learn more
about [managing orders and
fulfillment](https://shopify.dev/docs/apps/build/orders-fulfillment).

Show fields

[Anchor to contract](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-LineItem.fields.contract)contract

•[SubscriptionContract](/docs/api/admin-
graphql/latest/objects/SubscriptionContract)

    

The subscription contract associated with this line item.

Show fields

[Anchor to currentQuantity](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
LineItem.fields.currentQuantity)currentQuantity

•[Int!](/docs/api/admin-graphql/latest/scalars/Int)

non-null

    

The number of units ordered, excluding refunded and removed units.

[Anchor to customAttributes](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
LineItem.fields.customAttributes)customAttributes

•[[Attribute!]!](/docs/api/admin-graphql/latest/objects/Attribute)

non-null

    

A list of attributes that represent custom features or special requests.

Show fields

[Anchor to discountAllocations](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
LineItem.fields.discountAllocations)discountAllocations

•[[DiscountAllocation!]!](/docs/api/admin-
graphql/latest/objects/DiscountAllocation)

non-null

    

The discounts that have been allocated to the line item by discount
applications, including discounts allocated to refunded and removed
quantities.

Show fields

[Anchor to discountedTotalSet](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
LineItem.fields.discountedTotalSet)discountedTotalSet

•[MoneyBag!](/docs/api/admin-graphql/latest/objects/MoneyBag)

non-null

    

The total discounted price of the line item in shop and presentment
currencies, including refunded and removed quantities. This value doesn't
include order-level discounts. Code-based discounts aren't included by
default.

Show fields

[Anchor to discountedUnitPriceAfterAllDiscountsSet](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
LineItem.fields.discountedUnitPriceAfterAllDiscountsSet)discountedUnitPriceAfterAllDiscountsSet

•[MoneyBag!](/docs/api/admin-graphql/latest/objects/MoneyBag)

non-null

    

The approximate unit price of the line item in shop and presentment
currencies. This value includes discounts applied to refunded and removed
quantities.

Show fields

[Anchor to discountedUnitPriceSet](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
LineItem.fields.discountedUnitPriceSet)discountedUnitPriceSet

•[MoneyBag!](/docs/api/admin-graphql/latest/objects/MoneyBag)

non-null

    

The approximate unit price of the line item in shop and presentment
currencies. This value includes line-level discounts and discounts applied to
refunded and removed quantities. It doesn't include order-level or code-based
discounts.

Show fields

[Anchor to duties](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-LineItem.fields.duties)duties

•[[Duty!]!](/docs/api/admin-graphql/latest/objects/Duty)

non-null

    

The duties associated with the line item.

Show fields

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
LineItem.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to image](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-LineItem.fields.image)image

•[Image](/docs/api/admin-graphql/latest/objects/Image)

    

The image associated to the line item's variant.

Show fields

[Anchor to isGiftCard](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
LineItem.fields.isGiftCard)isGiftCard

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether the line item represents the purchase of a gift card.

[Anchor to lineItemGroup](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
LineItem.fields.lineItemGroup)lineItemGroup

•[LineItemGroup](/docs/api/admin-graphql/latest/objects/LineItemGroup)

    

The line item group associated to the line item.

Show fields

[Anchor to merchantEditable](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
LineItem.fields.merchantEditable)merchantEditable

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether the line item can be edited or not.

[Anchor to name](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-LineItem.fields.name)name

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The title of the product, optionally appended with the title of the variant
(if applicable).

[Anchor to nonFulfillableQuantity](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
LineItem.fields.nonFulfillableQuantity)nonFulfillableQuantity

•[Int!](/docs/api/admin-graphql/latest/scalars/Int)

non-null

    

The total number of units that can't be fulfilled. For example, if items have
been refunded, or the item is not something that can be fulfilled, like a tip.
Please see the [FulfillmentOrder](https://shopify.dev/api/admin-
graphql/latest/objects/FulfillmentOrder) object for more fulfillment details.

[Anchor to originalTotalSet](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
LineItem.fields.originalTotalSet)originalTotalSet

•[MoneyBag!](/docs/api/admin-graphql/latest/objects/MoneyBag)

non-null

    

In shop and presentment currencies, the total price of the line item when the
order was created. This value doesn't include discounts.

Show fields

[Anchor to originalUnitPriceSet](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
LineItem.fields.originalUnitPriceSet)originalUnitPriceSet

•[MoneyBag!](/docs/api/admin-graphql/latest/objects/MoneyBag)

non-null

    

In shop and presentment currencies, the unit price of the line item when the
order was created. This value doesn't include discounts.

Show fields

[Anchor to product](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-LineItem.fields.product)product

•[Product](/docs/api/admin-graphql/latest/objects/Product)

    

The Product object associated with this line item's variant.

Show fields

[Anchor to quantity](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-LineItem.fields.quantity)quantity

•[Int!](/docs/api/admin-graphql/latest/scalars/Int)

non-null

    

The number of units ordered, including refunded and removed units.

[Anchor to refundableQuantity](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
LineItem.fields.refundableQuantity)refundableQuantity

•[Int!](/docs/api/admin-graphql/latest/scalars/Int)

non-null

    

The number of units ordered, excluding refunded units and removed units.

[Anchor to requiresShipping](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
LineItem.fields.requiresShipping)requiresShipping

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether physical shipping is required for the variant.

[Anchor to restockable](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
LineItem.fields.restockable)restockable

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether the line item can be restocked.

[Anchor to sellingPlan](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
LineItem.fields.sellingPlan)sellingPlan

•[LineItemSellingPlan](/docs/api/admin-
graphql/latest/objects/LineItemSellingPlan)

    

The selling plan details associated with the line item.

Show fields

[Anchor to sku](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
LineItem.fields.sku)sku

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The variant SKU number.

[Anchor to staffMember](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
LineItem.fields.staffMember)staffMember

•[StaffMember](/docs/api/admin-graphql/latest/objects/StaffMember)

    

Staff attributed to the line item.

Show fields

[Anchor to taxable](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-LineItem.fields.taxable)taxable

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether the variant is taxable.

[Anchor to taxLines](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-LineItem.fields.taxLines)taxLines

•[[TaxLine!]!](/docs/api/admin-graphql/latest/objects/TaxLine)

non-null

    

The taxes charged for the line item, including taxes charged for refunded and
removed quantities.

Show fields

[Anchor to title](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-LineItem.fields.title)title

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The title of the product at time of order creation.

[Anchor to totalDiscountSet](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
LineItem.fields.totalDiscountSet)totalDiscountSet

•[MoneyBag!](/docs/api/admin-graphql/latest/objects/MoneyBag)

non-null

    

The total discount allocated to the line item in shop and presentment
currencies, including the total allocated to refunded and removed quantities.
This value doesn't include order-level discounts.

Show fields

[Anchor to unfulfilledDiscountedTotalSet](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
LineItem.fields.unfulfilledDiscountedTotalSet)unfulfilledDiscountedTotalSet

•[MoneyBag!](/docs/api/admin-graphql/latest/objects/MoneyBag)

non-null

    

In shop and presentment currencies, the total discounted price of the
unfulfilled quantity for the line item.

Show fields

[Anchor to unfulfilledOriginalTotalSet](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
LineItem.fields.unfulfilledOriginalTotalSet)unfulfilledOriginalTotalSet

•[MoneyBag!](/docs/api/admin-graphql/latest/objects/MoneyBag)

non-null

    

In shop and presentment currencies, the total price of the unfulfilled
quantity for the line item. This value doesn't include discounts.

Show fields

[Anchor to unfulfilledQuantity](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
LineItem.fields.unfulfilledQuantity)unfulfilledQuantity

•[Int!](/docs/api/admin-graphql/latest/scalars/Int)

non-null

    

The number of units not yet fulfilled.

[Anchor to variant](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-LineItem.fields.variant)variant

•[ProductVariant](/docs/api/admin-graphql/latest/objects/ProductVariant)

    

The Variant object associated with this line item.

Show fields

[Anchor to variantTitle](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
LineItem.fields.variantTitle)variantTitle

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The title of the variant at time of order creation.

[Anchor to vendor](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-LineItem.fields.vendor)vendor

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The name of the vendor who made the variant.

[Anchor to canRestock](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
LineItem.fields.canRestock)canRestock

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-nullDeprecated

    

[Anchor to discountedTotal](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
LineItem.fields.discountedTotal)discountedTotal

•[Money!](/docs/api/admin-graphql/latest/scalars/Money)

non-nullDeprecated

    

[Anchor to discountedUnitPrice](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
LineItem.fields.discountedUnitPrice)discountedUnitPrice

•[Money!](/docs/api/admin-graphql/latest/scalars/Money)

non-nullDeprecated

    

[Anchor to fulfillableQuantity](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
LineItem.fields.fulfillableQuantity)fulfillableQuantity

•[Int!](/docs/api/admin-graphql/latest/scalars/Int)

non-nullDeprecated

    

[Anchor to fulfillmentService](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
LineItem.fields.fulfillmentService)fulfillmentService

•[FulfillmentService](/docs/api/admin-
graphql/latest/objects/FulfillmentService)

Deprecated

    

Show fields

[Anchor to fulfillmentStatus](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
LineItem.fields.fulfillmentStatus)fulfillmentStatus

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-nullDeprecated

    

[Anchor to originalTotal](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
LineItem.fields.originalTotal)originalTotal

•[Money!](/docs/api/admin-graphql/latest/scalars/Money)

non-nullDeprecated

    

[Anchor to originalUnitPrice](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
LineItem.fields.originalUnitPrice)originalUnitPrice

•[Money!](/docs/api/admin-graphql/latest/scalars/Money)

non-nullDeprecated

    

[Anchor to totalDiscount](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
LineItem.fields.totalDiscount)totalDiscount

•[Money!](/docs/api/admin-graphql/latest/scalars/Money)

non-nullDeprecated

    

[Anchor to unfulfilledDiscountedTotal](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
LineItem.fields.unfulfilledDiscountedTotal)unfulfilledDiscountedTotal

•[Money!](/docs/api/admin-graphql/latest/scalars/Money)

non-nullDeprecated

    

[Anchor to unfulfilledOriginalTotal](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
LineItem.fields.unfulfilledOriginalTotal)unfulfilledOriginalTotal

•[Money!](/docs/api/admin-graphql/latest/scalars/Money)

non-nullDeprecated

    

[Anchor to LineItemGroup](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
LineItemGroup)[LineItemGroup](/docs/api/admin-
graphql/latest/objects/LineItemGroup)

•OBJECT

    

A line item group (bundle) to which a line item belongs to.

Show fields

[Anchor to customAttributes](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
LineItemGroup.fields.customAttributes)customAttributes

•[[Attribute!]!](/docs/api/admin-graphql/latest/objects/Attribute)

non-null

    

A list of attributes that represent custom features or special requests.

Show fields

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
LineItemGroup.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to productId](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-LineItemGroup.fields.productId)productId

•[ID](/docs/api/admin-graphql/latest/scalars/ID)

    

ID of the product of the line item group.

[Anchor to quantity](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-LineItemGroup.fields.quantity)quantity

•[Int!](/docs/api/admin-graphql/latest/scalars/Int)

non-null

    

Quantity of the line item group on the order.

[Anchor to title](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-LineItemGroup.fields.title)title

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

Title of the line item group.

[Anchor to variantId](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-LineItemGroup.fields.variantId)variantId

•[ID](/docs/api/admin-graphql/latest/scalars/ID)

    

ID of the variant of the line item group.

[Anchor to variantSku](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
LineItemGroup.fields.variantSku)variantSku

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

SKU of the variant of the line item group.

[Anchor to Location](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Location)[Location](/docs/api/admin-graphql/latest/objects/Location)

•OBJECT

    

Represents the location where the physical good resides. You can stock
inventory at active locations. Active locations that have
`fulfills_online_orders: true` and are configured with a shipping rate, pickup
enabled or local delivery will be able to sell from their storefront.

Show fields

[Anchor to activatable](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Location.fields.activatable)activatable

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether the location can be reactivated. If `false`, then trying to activate
the location with the [`LocationActivate`](https://shopify.dev/docs/api/admin-
graphql/latest/mutations/locationActivate) mutation will return an error that
describes why the location can't be activated.

[Anchor to address](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Location.fields.address)address

•[LocationAddress!](/docs/api/admin-graphql/latest/objects/LocationAddress)

non-null

    

The address of this location.

Show fields

[Anchor to addressVerified](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Location.fields.addressVerified)addressVerified

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether the location address has been verified.

[Anchor to createdAt](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Location.fields.createdAt)createdAt

•[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime)

non-null

    

The date and time ([ISO 8601 format](http://en.wikipedia.org/wiki/ISO_8601))
that the location was added to a shop.

[Anchor to deactivatable](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Location.fields.deactivatable)deactivatable

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether this location can be deactivated. If `true`, then the location can be
deactivated by calling the
[`LocationDeactivate`](https://shopify.dev/docs/api/admin-
graphql/latest/mutations/locationDeactivate) mutation. If `false`, then
calling the mutation to deactivate it will return an error that describes why
the location can't be deactivated.

[Anchor to deactivatedAt](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Location.fields.deactivatedAt)deactivatedAt

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The date and time ([ISO 8601 format](http://en.wikipedia.org/wiki/ISO_8601))
that the location was deactivated at. For example, 3:30 pm on September 7,
2019 in the time zone of UTC (Universal Time Coordinated) is represented as
`"2019-09-07T15:50:00Z`".

[Anchor to deletable](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Location.fields.deletable)deletable

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether this location can be deleted.

[Anchor to fulfillmentService](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Location.fields.fulfillmentService)fulfillmentService

•[FulfillmentService](/docs/api/admin-
graphql/latest/objects/FulfillmentService)

    

Name of the service provider that fulfills from this location.

Show fields

[Anchor to fulfillsOnlineOrders](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Location.fields.fulfillsOnlineOrders)fulfillsOnlineOrders

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether this location can fulfill online orders.

[Anchor to hasActiveInventory](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Location.fields.hasActiveInventory)hasActiveInventory

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether this location has active inventory.

[Anchor to hasUnfulfilledOrders](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Location.fields.hasUnfulfilledOrders)hasUnfulfilledOrders

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether this location has orders that need to be fulfilled.

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
Location.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to inventoryLevel](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Location.fields.inventoryLevel)inventoryLevel

•[InventoryLevel](/docs/api/admin-graphql/latest/objects/InventoryLevel)

    

The quantities of an inventory item at this location.

Show fields

[Anchor to inventoryLevels](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Location.fields.inventoryLevels)inventoryLevels

•[InventoryLevelConnection!](/docs/api/admin-
graphql/latest/connections/InventoryLevelConnection)

non-null

    

A list of the quantities of the inventory items that can be stocked at this
location.

Show fields

[Anchor to isActive](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Location.fields.isActive)isActive

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether the location is active. A deactivated location can be activated
(change `isActive: true`) if it has `activatable` set to `true` by calling the
[`locationActivate`](https://shopify.dev/docs/api/admin-
graphql/latest/mutations/locationActivate) mutation.

[Anchor to isFulfillmentService](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Location.fields.isFulfillmentService)isFulfillmentService

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether this location is a fulfillment service.

[Anchor to legacyResourceId](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Location.fields.legacyResourceId)legacyResourceId

•[UnsignedInt64!](/docs/api/admin-graphql/latest/scalars/UnsignedInt64)

non-null

    

The ID of the corresponding resource in the REST Admin API.

[Anchor to localPickupSettingsV2](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Location.fields.localPickupSettingsV2)localPickupSettingsV2

•[DeliveryLocalPickupSettings](/docs/api/admin-
graphql/latest/objects/DeliveryLocalPickupSettings)

    

Local pickup settings for the location.

Show fields

[Anchor to metafield](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Location.fields.metafield)metafield

•[Metafield](/docs/api/admin-graphql/latest/objects/Metafield)

    

A [custom field](https://shopify.dev/docs/apps/build/custom-data), including
its `namespace` and `key`, that's associated with a Shopify resource for the
purposes of adding and storing additional information.

Show fields

[Anchor to metafields](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Location.fields.metafields)metafields

•[MetafieldConnection!](/docs/api/admin-
graphql/latest/connections/MetafieldConnection)

non-null

    

A list of [custom fields](https://shopify.dev/docs/apps/build/custom-data)
that a merchant associates with a Shopify resource.

Show fields

[Anchor to name](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Location.fields.name)name

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The name of the location.

[Anchor to shipsInventory](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Location.fields.shipsInventory)shipsInventory

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether this location is used for calculating shipping rates. In multi-origin
shipping mode, this flag is ignored.

[Anchor to suggestedAddresses](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Location.fields.suggestedAddresses)suggestedAddresses

•[[LocationSuggestedAddress!]!](/docs/api/admin-
graphql/latest/objects/LocationSuggestedAddress)

non-null

    

List of suggested addresses for this location (empty if none).

Show fields

[Anchor to updatedAt](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Location.fields.updatedAt)updatedAt

•[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime)

non-null

    

The date and time ([ISO 8601 format](http://en.wikipedia.org/wiki/ISO_8601))
when the location was last updated.

[Anchor to isPrimary](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Location.fields.isPrimary)isPrimary

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-nullDeprecated

    

[Anchor to metafieldDefinitions](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Location.fields.metafieldDefinitions)metafieldDefinitions

•[MetafieldDefinitionConnection!](/docs/api/admin-
graphql/latest/connections/MetafieldDefinitionConnection)

non-nullDeprecated

    

Show fields

[Anchor to MailingAddress](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
MailingAddress)[MailingAddress](/docs/api/admin-
graphql/latest/objects/MailingAddress)

•OBJECT

    

Represents a customer mailing address.

For example, a customer's default address and an order's billing address are
both mailling addresses.

Show fields

[Anchor to address1](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-MailingAddress.fields.address1)address1

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The first line of the address. Typically the street address or PO Box number.

[Anchor to address2](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-MailingAddress.fields.address2)address2

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The second line of the address. Typically the number of the apartment, suite,
or unit.

[Anchor to city](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-MailingAddress.fields.city)city

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The name of the city, district, village, or town.

[Anchor to company](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-MailingAddress.fields.company)company

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The name of the customer's company or organization.

[Anchor to coordinatesValidated](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
MailingAddress.fields.coordinatesValidated)coordinatesValidated

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether the address corresponds to recognized latitude and longitude values.

[Anchor to country](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-MailingAddress.fields.country)country

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The name of the country.

[Anchor to countryCodeV2](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
MailingAddress.fields.countryCodeV2)countryCodeV2

•[CountryCode](/docs/api/admin-graphql/latest/enums/CountryCode)

    

The two-letter code for the country of the address.

For example, US.

Show enum values

[Anchor to firstName](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-MailingAddress.fields.firstName)firstName

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The first name of the customer.

[Anchor to formatted](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-MailingAddress.fields.formatted)formatted

•[[String!]!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

A formatted version of the address, customized by the provided arguments.

Show arguments

### Arguments

[Anchor to withName](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-MailingAddress.fields.formatted.arguments.withName)withName

•[Boolean](/docs/api/admin-graphql/latest/scalars/Boolean)

Default:false

    

Whether to include the customer's name in the formatted address.

[Anchor to withCompany](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
MailingAddress.fields.formatted.arguments.withCompany)withCompany

•[Boolean](/docs/api/admin-graphql/latest/scalars/Boolean)

Default:true

    

Whether to include the customer's company in the formatted address.

* * *

[Anchor to formattedArea](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
MailingAddress.fields.formattedArea)formattedArea

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

A comma-separated list of the values for city, province, and country.

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
MailingAddress.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to lastName](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-MailingAddress.fields.lastName)lastName

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The last name of the customer.

[Anchor to latitude](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-MailingAddress.fields.latitude)latitude

•[Float](/docs/api/admin-graphql/latest/scalars/Float)

    

The latitude coordinate of the customer address.

[Anchor to longitude](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-MailingAddress.fields.longitude)longitude

•[Float](/docs/api/admin-graphql/latest/scalars/Float)

    

The longitude coordinate of the customer address.

[Anchor to name](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-MailingAddress.fields.name)name

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The full name of the customer, based on firstName and lastName.

[Anchor to phone](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-MailingAddress.fields.phone)phone

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

A unique phone number for the customer.

[Anchor to province](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-MailingAddress.fields.province)province

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The region of the address, such as the province, state, or district.

[Anchor to provinceCode](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
MailingAddress.fields.provinceCode)provinceCode

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The alphanumeric code for the region.

For example, ON.

[Anchor to timeZone](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-MailingAddress.fields.timeZone)timeZone

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The time zone of the address.

[Anchor to validationResultSummary](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
MailingAddress.fields.validationResultSummary)validationResultSummary

•[MailingAddressValidationResult](/docs/api/admin-
graphql/latest/enums/MailingAddressValidationResult)

    

The validation status that is leveraged by the address validation feature in
the Shopify Admin. See ["Validating addresses in your Shopify
admin"](https://help.shopify.com/manual/fulfillment/managing-
orders/validating-order-address) for more details.

Show enum values

[Anchor to zip](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
MailingAddress.fields.zip)zip

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The zip or postal code of the address.

[Anchor to countryCode](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
MailingAddress.fields.countryCode)countryCode

•[String](/docs/api/admin-graphql/latest/scalars/String)

Deprecated

    

[Anchor to Market](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Market)[Market](/docs/api/admin-graphql/latest/objects/Market)

•OBJECT

    

A market is a group of one or more regions that you want to target for
international sales. By creating a market, you can configure a distinct,
localized shopping experience for customers from a specific area of the world.
For example, you can [change currency](https://shopify.dev/api/admin-
graphql/current/mutations/marketCurrencySettingsUpdate), [configure
international pricing](https://shopify.dev/apps/internationalization/product-
price-lists), or [add market-specific domains or
subfolders](https://shopify.dev/api/admin-
graphql/current/objects/MarketWebPresence).

Show fields

[Anchor to assignedCustomization](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Market.fields.assignedCustomization)assignedCustomization

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether the market has a customization with the given ID.

Show arguments

### Arguments

[Anchor to customizationId](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Market.fields.assignedCustomization.arguments.customizationId)customizationId

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

required

    

The ID of the customization that the market has been assigned to.

* * *

[Anchor to catalogs](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Market.fields.catalogs)catalogs

•[MarketCatalogConnection!](/docs/api/admin-
graphql/latest/connections/MarketCatalogConnection)

non-null

    

The catalogs that belong to the market.

Show fields

[Anchor to catalogsCount](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Market.fields.catalogsCount)catalogsCount

•[Count](/docs/api/admin-graphql/latest/objects/Count)

    

The number of catalogs that belong to the market.

Show fields

[Anchor to conditions](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Market.fields.conditions)conditions

•[MarketConditions](/docs/api/admin-graphql/latest/objects/MarketConditions)

    

The conditions under which a visitor is in the market.

Show fields

[Anchor to currencySettings](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Market.fields.currencySettings)currencySettings

•[MarketCurrencySettings](/docs/api/admin-
graphql/latest/objects/MarketCurrencySettings)

    

The market’s currency settings.

Show fields

[Anchor to handle](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Market.fields.handle)handle

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

A short, human-readable unique identifier for the market. This is changeable
by the merchant.

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
Market.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to metafield](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Market.fields.metafield)metafield

•[Metafield](/docs/api/admin-graphql/latest/objects/Metafield)

    

A [custom field](https://shopify.dev/docs/apps/build/custom-data), including
its `namespace` and `key`, that's associated with a Shopify resource for the
purposes of adding and storing additional information.

Show fields

[Anchor to metafields](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Market.fields.metafields)metafields

•[MetafieldConnection!](/docs/api/admin-
graphql/latest/connections/MetafieldConnection)

non-null

    

A list of [custom fields](https://shopify.dev/docs/apps/build/custom-data)
that a merchant associates with a Shopify resource.

Show fields

[Anchor to name](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Market.fields.name)name

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The name of the market. Not shown to customers.

[Anchor to priceInclusions](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Market.fields.priceInclusions)priceInclusions

•[MarketPriceInclusions](/docs/api/admin-
graphql/latest/objects/MarketPriceInclusions)

    

The inclusive pricing strategy for a market. This determines if prices include
duties and / or taxes.

Show fields

[Anchor to status](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Market.fields.status)status

•[MarketStatus!](/docs/api/admin-graphql/latest/enums/MarketStatus)

non-null

    

Status of the market. Replaces the enabled field.

Show enum values

[Anchor to type](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Market.fields.type)type

•[MarketType!](/docs/api/admin-graphql/latest/enums/MarketType)

non-null

    

The type of the market.

Show enum values

[Anchor to webPresences](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Market.fields.webPresences)webPresences

•[MarketWebPresenceConnection!](/docs/api/admin-
graphql/latest/connections/MarketWebPresenceConnection)

non-null

    

The market’s web presences, which defines its SEO strategy. This can be a
different domain, subdomain, or subfolders of the primary domain. Each web
presence comprises one or more language variants. If a market doesn't have any
web presences, then the market is accessible on the primary market's domains
using [country
selectors](https://shopify.dev/themes/internationalization/multiple-
currencies-languages#the-country-selector).

Show fields

[Anchor to enabled](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Market.fields.enabled)enabled

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-nullDeprecated

    

[Anchor to metafieldDefinitions](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Market.fields.metafieldDefinitions)metafieldDefinitions

•[MetafieldDefinitionConnection!](/docs/api/admin-
graphql/latest/connections/MetafieldDefinitionConnection)

non-nullDeprecated

    

Show fields

[Anchor to priceList](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Market.fields.priceList)priceList

•[PriceList](/docs/api/admin-graphql/latest/objects/PriceList)

Deprecated

    

Show fields

[Anchor to primary](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Market.fields.primary)primary

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-nullDeprecated

    

[Anchor to regions](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Market.fields.regions)regions

•[MarketRegionConnection!](/docs/api/admin-
graphql/latest/connections/MarketRegionConnection)

non-nullDeprecated

    

Show fields

[Anchor to webPresence](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Market.fields.webPresence)webPresence

•[MarketWebPresence](/docs/api/admin-graphql/latest/objects/MarketWebPresence)

Deprecated

    

Show fields

[Anchor to MarketCatalog](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
MarketCatalog)[MarketCatalog](/docs/api/admin-
graphql/latest/objects/MarketCatalog)

•OBJECT

    

A list of products with publishing and pricing information associated with
markets.

Show fields

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
MarketCatalog.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to markets](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-MarketCatalog.fields.markets)markets

•[MarketConnection!](/docs/api/admin-
graphql/latest/connections/MarketConnection)

non-null

    

The markets associated with the catalog.

Show fields

[Anchor to marketsCount](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
MarketCatalog.fields.marketsCount)marketsCount

•[Count](/docs/api/admin-graphql/latest/objects/Count)

    

The number of markets associated with the catalog.

Show fields

[Anchor to operations](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
MarketCatalog.fields.operations)operations

•[[ResourceOperation!]!](/docs/api/admin-
graphql/latest/interfaces/ResourceOperation)

non-null

    

Most recent catalog operations.

Show fields

[Anchor to priceList](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-MarketCatalog.fields.priceList)priceList

•[PriceList](/docs/api/admin-graphql/latest/objects/PriceList)

    

The price list associated with the catalog.

Show fields

[Anchor to publication](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
MarketCatalog.fields.publication)publication

•[Publication](/docs/api/admin-graphql/latest/objects/Publication)

    

A group of products and collections that's published to a catalog.

Show fields

[Anchor to status](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-MarketCatalog.fields.status)status

•[CatalogStatus!](/docs/api/admin-graphql/latest/enums/CatalogStatus)

non-null

    

The status of the catalog.

Show enum values

[Anchor to title](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-MarketCatalog.fields.title)title

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The name of the catalog.

[Anchor to MarketingActivity](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
MarketingActivity)[MarketingActivity](/docs/api/admin-
graphql/latest/objects/MarketingActivity)

•OBJECT

    

The marketing activity resource represents marketing that a merchant created
through an app.

Show fields

[Anchor to activityListUrl](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
MarketingActivity.fields.activityListUrl)activityListUrl

•[URL](/docs/api/admin-graphql/latest/scalars/URL)

    

The URL of the marketing activity listing page in the marketing section.

[Anchor to adSpend](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-MarketingActivity.fields.adSpend)adSpend

•[MoneyV2](/docs/api/admin-graphql/latest/objects/MoneyV2)

    

The amount spent on the marketing activity.

Show fields

[Anchor to app](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
MarketingActivity.fields.app)app

•[App!](/docs/api/admin-graphql/latest/objects/App)

non-null

    

The app which created this marketing activity.

Show fields

[Anchor to appErrors](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-MarketingActivity.fields.appErrors)appErrors

•[MarketingActivityExtensionAppErrors](/docs/api/admin-
graphql/latest/objects/MarketingActivityExtensionAppErrors)

    

The errors generated when an app publishes the marketing activity.

Show fields

[Anchor to budget](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-MarketingActivity.fields.budget)budget

•[MarketingBudget](/docs/api/admin-graphql/latest/objects/MarketingBudget)

    

The allocated budget for the marketing activity.

Show fields

[Anchor to createdAt](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-MarketingActivity.fields.createdAt)createdAt

•[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime)

non-null

    

The date and time when the marketing activity was created.

[Anchor to formData](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-MarketingActivity.fields.formData)formData

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The completed content in the marketing activity creation form.

[Anchor to hierarchyLevel](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
MarketingActivity.fields.hierarchyLevel)hierarchyLevel

•[MarketingActivityHierarchyLevel](/docs/api/admin-
graphql/latest/enums/MarketingActivityHierarchyLevel)

    

The hierarchy level of the marketing activity.

Show enum values

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
MarketingActivity.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to inMainWorkflowVersion](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
MarketingActivity.fields.inMainWorkflowVersion)inMainWorkflowVersion

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether the marketing activity is in the main workflow version of the
marketing automation.

[Anchor to isExternal](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
MarketingActivity.fields.isExternal)isExternal

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

The marketing activity represents an external marketing activity.

[Anchor to marketingChannelType](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
MarketingActivity.fields.marketingChannelType)marketingChannelType

•[MarketingChannel!](/docs/api/admin-graphql/latest/enums/MarketingChannel)

non-null

    

The medium through which the marketing activity and event reached consumers.
This is used for reporting aggregation.

Show enum values

[Anchor to marketingEvent](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
MarketingActivity.fields.marketingEvent)marketingEvent

•[MarketingEvent](/docs/api/admin-graphql/latest/objects/MarketingEvent)

    

Associated marketing event of this marketing activity.

Show fields

[Anchor to parentActivityId](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
MarketingActivity.fields.parentActivityId)parentActivityId

•[ID](/docs/api/admin-graphql/latest/scalars/ID)

    

ID of the parent activity of this marketing activity.

[Anchor to parentRemoteId](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
MarketingActivity.fields.parentRemoteId)parentRemoteId

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

ID of the parent activity of this marketing activity.

[Anchor to sourceAndMedium](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
MarketingActivity.fields.sourceAndMedium)sourceAndMedium

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

A contextual description of the marketing activity based on the platform and
tactic used.

[Anchor to status](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-MarketingActivity.fields.status)status

•[MarketingActivityStatus!](/docs/api/admin-
graphql/latest/enums/MarketingActivityStatus)

non-null

    

The current state of the marketing activity.

Show enum values

[Anchor to statusBadgeTypeV2](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
MarketingActivity.fields.statusBadgeTypeV2)statusBadgeTypeV2

•[BadgeType](/docs/api/admin-graphql/latest/enums/BadgeType)

    

The severity of the marketing activity's status.

Show enum values

[Anchor to statusLabel](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
MarketingActivity.fields.statusLabel)statusLabel

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The rendered status of the marketing activity.

[Anchor to statusTransitionedAt](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
MarketingActivity.fields.statusTransitionedAt)statusTransitionedAt

•[DateTime](/docs/api/admin-graphql/latest/scalars/DateTime)

    

The [date and
time](https://help.shopify.com/https://en.wikipedia.org/wiki/ISO_8601) when
the activity's status last changed.

[Anchor to tactic](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-MarketingActivity.fields.tactic)tactic

•[MarketingTactic!](/docs/api/admin-graphql/latest/enums/MarketingTactic)

non-null

    

The method of marketing used for this marketing activity.

Show enum values

[Anchor to targetStatus](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
MarketingActivity.fields.targetStatus)targetStatus

•[MarketingActivityStatus](/docs/api/admin-
graphql/latest/enums/MarketingActivityStatus)

    

The status to which the marketing activity is currently transitioning.

Show enum values

[Anchor to title](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-MarketingActivity.fields.title)title

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The marketing activity's title, which is rendered on the marketing listing
page.

[Anchor to updatedAt](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-MarketingActivity.fields.updatedAt)updatedAt

•[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime)

non-null

    

The date and time when the marketing activity was updated.

[Anchor to urlParameterValue](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
MarketingActivity.fields.urlParameterValue)urlParameterValue

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The value portion of the URL query parameter used in attributing sessions to
this activity.

[Anchor to utmParameters](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
MarketingActivity.fields.utmParameters)utmParameters

•[UTMParameters](/docs/api/admin-graphql/latest/objects/UTMParameters)

    

The set of [Urchin Tracking
Module](https://help.shopify.com/https://en.wikipedia.org/wiki/UTM_parameters)
used in the URL for tracking this marketing activity.

Show fields

[Anchor to marketingChannel](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
MarketingActivity.fields.marketingChannel)marketingChannel

•[MarketingChannel!](/docs/api/admin-graphql/latest/enums/MarketingChannel)

non-nullDeprecated

    

Show enum values

[Anchor to statusBadgeType](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
MarketingActivity.fields.statusBadgeType)statusBadgeType

•[MarketingActivityStatusBadgeType](/docs/api/admin-
graphql/latest/enums/MarketingActivityStatusBadgeType)

Deprecated

    

Show enum values

[Anchor to MarketingEvent](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
MarketingEvent)[MarketingEvent](/docs/api/admin-
graphql/latest/objects/MarketingEvent)

•OBJECT

    

Represents actions that market a merchant's store or products.

Show fields

[Anchor to app](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
MarketingEvent.fields.app)app

•[App!](/docs/api/admin-graphql/latest/objects/App)

non-null

    

The app that the marketing event is attributed to.

Show fields

[Anchor to channelHandle](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
MarketingEvent.fields.channelHandle)channelHandle

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The unique string identifier of the channel to which this activity belongs.
For the correct handle for your channel, contact your partner manager.

[Anchor to description](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
MarketingEvent.fields.description)description

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

A human-readable description of the marketing event.

[Anchor to endedAt](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-MarketingEvent.fields.endedAt)endedAt

•[DateTime](/docs/api/admin-graphql/latest/scalars/DateTime)

    

The date and time when the marketing event ended.

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
MarketingEvent.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to legacyResourceId](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
MarketingEvent.fields.legacyResourceId)legacyResourceId

•[UnsignedInt64!](/docs/api/admin-graphql/latest/scalars/UnsignedInt64)

non-null

    

The ID of the corresponding resource in the REST Admin API.

[Anchor to manageUrl](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-MarketingEvent.fields.manageUrl)manageUrl

•[URL](/docs/api/admin-graphql/latest/scalars/URL)

    

The URL where the marketing event can be managed.

[Anchor to marketingChannelType](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
MarketingEvent.fields.marketingChannelType)marketingChannelType

•[MarketingChannel](/docs/api/admin-graphql/latest/enums/MarketingChannel)

    

The medium through which the marketing activity and event reached consumers.
This is used for reporting aggregation.

Show enum values

[Anchor to previewUrl](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
MarketingEvent.fields.previewUrl)previewUrl

•[URL](/docs/api/admin-graphql/latest/scalars/URL)

    

The URL where the marketing event can be previewed.

[Anchor to remoteId](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-MarketingEvent.fields.remoteId)remoteId

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

An optional ID that helps Shopify validate engagement data.

[Anchor to scheduledToEndAt](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
MarketingEvent.fields.scheduledToEndAt)scheduledToEndAt

•[DateTime](/docs/api/admin-graphql/latest/scalars/DateTime)

    

The date and time when the marketing event is scheduled to end.

[Anchor to sourceAndMedium](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
MarketingEvent.fields.sourceAndMedium)sourceAndMedium

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

Where the `MarketingEvent` occurred and what kind of content was used. Because
`utmSource` and `utmMedium` are often used interchangeably, this is based on a
combination of `marketingChannel`, `referringDomain`, and `type` to provide a
consistent representation for any given piece of marketing regardless of the
app that created it.

[Anchor to startedAt](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-MarketingEvent.fields.startedAt)startedAt

•[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime)

non-null

    

The date and time when the marketing event started.

[Anchor to type](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-MarketingEvent.fields.type)type

•[MarketingTactic!](/docs/api/admin-graphql/latest/enums/MarketingTactic)

non-null

    

The marketing event type.

Show enum values

[Anchor to utmCampaign](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
MarketingEvent.fields.utmCampaign)utmCampaign

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The name of the marketing campaign.

[Anchor to utmMedium](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-MarketingEvent.fields.utmMedium)utmMedium

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The medium that the marketing campaign is using. Example values: `cpc`,
`banner`.

[Anchor to utmSource](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-MarketingEvent.fields.utmSource)utmSource

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The referrer of the marketing event. Example values: `google`, `newsletter`.

[Anchor to channel](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-MarketingEvent.fields.channel)channel

•[MarketingChannel](/docs/api/admin-graphql/latest/enums/MarketingChannel)

Deprecated

    

Show enum values

[Anchor to targetTypeDisplayText](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
MarketingEvent.fields.targetTypeDisplayText)targetTypeDisplayText

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-nullDeprecated

    

[Anchor to MarketRegionCountry](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
MarketRegionCountry)[MarketRegionCountry](/docs/api/admin-
graphql/latest/objects/MarketRegionCountry)

•OBJECT

    

A country which comprises a market.

Show fields

[Anchor to code](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-MarketRegionCountry.fields.code)code

•[CountryCode!](/docs/api/admin-graphql/latest/enums/CountryCode)

non-null

    

The ISO code identifying the country.

Show enum values

[Anchor to currency](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-MarketRegionCountry.fields.currency)currency

•[CurrencySetting!](/docs/api/admin-graphql/latest/objects/CurrencySetting)

non-null

    

The currency which this country uses given its market settings.

Show fields

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
MarketRegionCountry.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to name](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-MarketRegionCountry.fields.name)name

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The name of the region.

[Anchor to MarketWebPresence](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
MarketWebPresence)[MarketWebPresence](/docs/api/admin-
graphql/latest/objects/MarketWebPresence)

•OBJECT

    

The market’s web presence, which defines its SEO strategy. This can be a
different domain (e.g. `example.ca`), subdomain (e.g. `ca.example.com`), or
subfolders of the primary domain (e.g. `example.com/en-ca`). Each web presence
comprises one or more language variants. If a market does not have its own web
presence, it is accessible on the shop’s primary domain via [country
selectors](https://shopify.dev/themes/internationalization/multiple-
currencies-languages#the-country-selector).

Note: while the domain/subfolders defined by a market’s web presence are not
applicable to custom storefronts, which must manage their own domains and
routing, the languages chosen here do govern [the languages available on the
Storefront API](https://shopify.dev/custom-
storefronts/internationalization/multiple-languages) for the countries in this
market.

Show fields

[Anchor to alternateLocales](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
MarketWebPresence.fields.alternateLocales)alternateLocales

•[[ShopLocale!]!](/docs/api/admin-graphql/latest/objects/ShopLocale)

non-null

    

The ShopLocale object for the alternate locales. When a domain is used, these
locales will be available as language-specific subfolders. For example, if
English is an alternate locale, and `example.ca` is the market’s domain, then
`example.ca/en` will load in English.

Show fields

[Anchor to defaultLocale](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
MarketWebPresence.fields.defaultLocale)defaultLocale

•[ShopLocale!](/docs/api/admin-graphql/latest/objects/ShopLocale)

non-null

    

The ShopLocale object for the default locale. When a domain is used, this is
the locale that will be used when the domain root is accessed. For example, if
French is the default locale, and `example.ca` is the market’s domain, then
`example.ca` will load in French.

Show fields

[Anchor to domain](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-MarketWebPresence.fields.domain)domain

•[Domain](/docs/api/admin-graphql/latest/objects/Domain)

    

The web presence’s domain. This field will be null if `subfolderSuffix` isn't
null.

Show fields

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
MarketWebPresence.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to markets](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-MarketWebPresence.fields.markets)markets

•[MarketConnection](/docs/api/admin-
graphql/latest/connections/MarketConnection)

    

The associated markets for this web presence.

Show fields

[Anchor to rootUrls](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-MarketWebPresence.fields.rootUrls)rootUrls

•[[MarketWebPresenceRootUrl!]!](/docs/api/admin-
graphql/latest/objects/MarketWebPresenceRootUrl)

non-null

    

The list of root URLs for each of the web presence’s locales. As of version
`2024-04` this value will no longer have a trailing slash.

Show fields

[Anchor to subfolderSuffix](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
MarketWebPresence.fields.subfolderSuffix)subfolderSuffix

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The market-specific suffix of the subfolders defined by the web presence.
Example: in `/en-us` the subfolder suffix is `us`. This field will be null if
`domain` isn't null.

[Anchor to market](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-MarketWebPresence.fields.market)market

•[Market](/docs/api/admin-graphql/latest/objects/Market)

Deprecated

    

Show fields

[Anchor to MediaImage](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
MediaImage)[MediaImage](/docs/api/admin-graphql/latest/objects/MediaImage)

•OBJECT

    

The `MediaImage` object represents an image hosted on Shopify's [content
delivery network (CDN)](https://shopify.dev/docs/storefronts/themes/best-
practices/performance/platform#shopify-cdn). Shopify CDN is a content system
that serves as the primary way to store, manage, and deliver visual content
for products, variants, and other resources across the Shopify platform.

The `MediaImage` object provides information to:

  * Store and display product and variant images across online stores, admin interfaces, and mobile apps.
  * Retrieve visual branding elements, including logos, banners, favicons, and background images in checkout flows.
  * Retrieve signed URLs for secure, time-limited access to original image files.

Each `MediaImage` object provides both the processed image data (with
automatic optimization and CDN delivery) and access to the original source
file. The image processing is handled asynchronously, so images might not be
immediately available after upload. The
[`status`](https://shopify.dev/docs/api/admin-
graphql/latest/objects/mediaimage#field-MediaImage.fields.status) field
indicates when processing is complete and the image is ready for use.

The `MediaImage` object implements the
[`Media`](https://shopify.dev/docs/api/admin-graphql/latest/interfaces/Media)
interface alongside other media types, like videos and 3D models.

Learn about managing media for
[products](https://shopify.dev/docs/apps/build/online-store/product-media),
[product variants](https://shopify.dev/docs/apps/build/online-store/product-
variant-media), and [asynchronous media
management](https://shopify.dev/docs/apps/build/graphql/migrate/new-product-
model/product-model-components#asynchronous-media-management).

Show fields

[Anchor to alt](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
MediaImage.fields.alt)alt

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

A word or phrase to share the nature or contents of a media.

[Anchor to createdAt](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-MediaImage.fields.createdAt)createdAt

•[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime)

non-null

    

The date and time ([ISO 8601 format](http://en.wikipedia.org/wiki/ISO_8601))
when the file was created.

[Anchor to fileErrors](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
MediaImage.fields.fileErrors)fileErrors

•[[FileError!]!](/docs/api/admin-graphql/latest/objects/FileError)

non-null

    

Any errors that have occurred on the file.

Show fields

[Anchor to fileStatus](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
MediaImage.fields.fileStatus)fileStatus

•[FileStatus!](/docs/api/admin-graphql/latest/enums/FileStatus)

non-null

    

The status of the file.

Show enum values

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
MediaImage.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to image](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-MediaImage.fields.image)image

•[Image](/docs/api/admin-graphql/latest/objects/Image)

    

The image for the media. Returns `null` until `status` is `READY`.

Show fields

[Anchor to mediaContentType](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
MediaImage.fields.mediaContentType)mediaContentType

•[MediaContentType!](/docs/api/admin-graphql/latest/enums/MediaContentType)

non-null

    

The media content type.

Show enum values

[Anchor to mediaErrors](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
MediaImage.fields.mediaErrors)mediaErrors

•[[MediaError!]!](/docs/api/admin-graphql/latest/objects/MediaError)

non-null

    

Any errors which have occurred on the media.

Show fields

[Anchor to mediaWarnings](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
MediaImage.fields.mediaWarnings)mediaWarnings

•[[MediaWarning!]!](/docs/api/admin-graphql/latest/objects/MediaWarning)

non-null

    

The warnings attached to the media.

Show fields

[Anchor to mimeType](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-MediaImage.fields.mimeType)mimeType

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The MIME type of the image.

[Anchor to originalSource](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
MediaImage.fields.originalSource)originalSource

•[MediaImageOriginalSource](/docs/api/admin-
graphql/latest/objects/MediaImageOriginalSource)

    

The original source of the image.

Show fields

[Anchor to preview](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-MediaImage.fields.preview)preview

•[MediaPreviewImage](/docs/api/admin-graphql/latest/objects/MediaPreviewImage)

    

The preview image for the media.

Show fields

[Anchor to status](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-MediaImage.fields.status)status

•[MediaStatus!](/docs/api/admin-graphql/latest/enums/MediaStatus)

non-null

    

Current status of the media.

Show enum values

[Anchor to translations](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
MediaImage.fields.translations)translations

•[[Translation!]!](/docs/api/admin-graphql/latest/objects/Translation)

non-null

    

The published translations associated with the resource.

Show fields

[Anchor to updatedAt](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-MediaImage.fields.updatedAt)updatedAt

•[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime)

non-null

    

The date and time ([ISO 8601 format](http://en.wikipedia.org/wiki/ISO_8601))
when the file was last updated.

[Anchor to metafield](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-MediaImage.fields.metafield)metafield

•[Metafield](/docs/api/admin-graphql/latest/objects/Metafield)

Deprecated

    

Show fields

[Anchor to metafields](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
MediaImage.fields.metafields)metafields

•[MetafieldConnection!](/docs/api/admin-
graphql/latest/connections/MetafieldConnection)

non-nullDeprecated

    

Show fields

[Anchor to Menu](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Menu)[Menu](/docs/api/admin-graphql/latest/objects/Menu)

•OBJECT

    

A menu for display on the storefront.

Show fields

[Anchor to handle](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Menu.fields.handle)handle

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The menu's handle.

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
Menu.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to isDefault](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Menu.fields.isDefault)isDefault

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether the menu is a default. The handle for default menus can't be updated
and default menus can't be deleted.

[Anchor to items](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Menu.fields.items)items

•[[MenuItem!]!](/docs/api/admin-graphql/latest/objects/MenuItem)

non-null

    

A list of items on the menu sorted by position.

Show fields

[Anchor to title](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Menu.fields.title)title

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The menu's title.

[Anchor to translations](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Menu.fields.translations)translations

•[[Translation!]!](/docs/api/admin-graphql/latest/objects/Translation)

non-null

    

The published translations associated with the resource.

Show fields

[Anchor to Metafield](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Metafield)[Metafield](/docs/api/admin-graphql/latest/objects/Metafield)

•OBJECT

    

Metafields enable you to attach additional information to a Shopify resource,
such as a [Product](https://shopify.dev/api/admin-
graphql/latest/objects/product) or a
[Collection](https://shopify.dev/api/admin-graphql/latest/objects/collection).
For more information about where you can attach metafields refer to
[HasMetafields](https://shopify.dev/api/admin-
graphql/latest/interfaces/HasMetafields). Some examples of the data that
metafields enable you to store are specifications, size charts, downloadable
documents, release dates, images, or part numbers. Metafields are identified
by an owner resource, namespace, and key. and store a value along with type
information for that value.

Show fields

[Anchor to compareDigest](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Metafield.fields.compareDigest)compareDigest

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The data stored in the resource, represented as a digest.

[Anchor to createdAt](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Metafield.fields.createdAt)createdAt

•[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime)

non-null

    

The date and time when the metafield was created.

[Anchor to definition](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Metafield.fields.definition)definition

•[MetafieldDefinition](/docs/api/admin-
graphql/latest/objects/MetafieldDefinition)

    

The metafield definition that the metafield belongs to, if any.

Show fields

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
Metafield.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to jsonValue](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Metafield.fields.jsonValue)jsonValue

•[JSON!](/docs/api/admin-graphql/latest/scalars/JSON)

non-null

    

The data stored in the metafield in JSON format.

[Anchor to key](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
Metafield.fields.key)key

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The unique identifier for the metafield within its namespace.

[Anchor to legacyResourceId](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Metafield.fields.legacyResourceId)legacyResourceId

•[UnsignedInt64!](/docs/api/admin-graphql/latest/scalars/UnsignedInt64)

non-null

    

The ID of the corresponding resource in the REST Admin API.

[Anchor to namespace](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Metafield.fields.namespace)namespace

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The container for a group of metafields that the metafield is associated with.

[Anchor to owner](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Metafield.fields.owner)owner

•[HasMetafields!](/docs/api/admin-graphql/latest/interfaces/HasMetafields)

non-null

    

The resource that the metafield is attached to.

Show fields

[Anchor to ownerType](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Metafield.fields.ownerType)ownerType

•[MetafieldOwnerType!](/docs/api/admin-
graphql/latest/enums/MetafieldOwnerType)

non-null

    

The type of resource that the metafield is attached to.

Show enum values

[Anchor to reference](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Metafield.fields.reference)reference

•[MetafieldReference](/docs/api/admin-
graphql/latest/unions/MetafieldReference)

    

Returns a reference object if the metafield definition's type is a resource
reference.

Show union types

[Anchor to references](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Metafield.fields.references)references

•[MetafieldReferenceConnection](/docs/api/admin-
graphql/latest/connections/MetafieldReferenceConnection)

    

A list of reference objects if the metafield's type is a resource reference
list.

Show fields

[Anchor to type](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Metafield.fields.type)type

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The type of data that is stored in the metafield. Refer to the list of
[supported types](https://shopify.dev/apps/metafields/types).

[Anchor to updatedAt](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Metafield.fields.updatedAt)updatedAt

•[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime)

non-null

    

The date and time when the metafield was updated.

[Anchor to value](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Metafield.fields.value)value

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The data stored in the metafield. Always stored as a string, regardless of the
metafield's type.

[Anchor to description](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Metafield.fields.description)description

•[String](/docs/api/admin-graphql/latest/scalars/String)

Deprecated

    

[Anchor to MetafieldDefinition](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
MetafieldDefinition)[MetafieldDefinition](/docs/api/admin-
graphql/latest/objects/MetafieldDefinition)

•OBJECT

    

Metafield definitions enable you to define additional validation constraints
for metafields, and enable the merchant to edit metafield values in context.

Show fields

[Anchor to access](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-MetafieldDefinition.fields.access)access

•[MetafieldAccess!](/docs/api/admin-graphql/latest/objects/MetafieldAccess)

non-null

    

The access settings associated with the metafield definition.

Show fields

[Anchor to capabilities](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
MetafieldDefinition.fields.capabilities)capabilities

•[MetafieldCapabilities!](/docs/api/admin-
graphql/latest/objects/MetafieldCapabilities)

non-null

    

The capabilities of the metafield definition.

Show fields

[Anchor to constraints](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
MetafieldDefinition.fields.constraints)constraints

•[MetafieldDefinitionConstraints](/docs/api/admin-
graphql/latest/objects/MetafieldDefinitionConstraints)

    

The [constraints](https://shopify.dev/apps/build/custom-
data/metafields/conditional-metafield-definitions) that determine what
subtypes of resources a metafield definition applies to.

Show fields

[Anchor to description](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
MetafieldDefinition.fields.description)description

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The description of the metafield definition.

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
MetafieldDefinition.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to key](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
MetafieldDefinition.fields.key)key

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The unique identifier for the metafield definition within its namespace.

[Anchor to metafields](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
MetafieldDefinition.fields.metafields)metafields

•[MetafieldConnection!](/docs/api/admin-
graphql/latest/connections/MetafieldConnection)

non-null

    

The metafields that belong to the metafield definition.

Show fields

[Anchor to metafieldsCount](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
MetafieldDefinition.fields.metafieldsCount)metafieldsCount

•[Int!](/docs/api/admin-graphql/latest/scalars/Int)

non-null

    

The count of the metafields that belong to the metafield definition.

Show arguments

### Arguments

[Anchor to validationStatus](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
MetafieldDefinition.fields.metafieldsCount.arguments.validationStatus)validationStatus

•[MetafieldValidationStatus](/docs/api/admin-
graphql/latest/enums/MetafieldValidationStatus)

    

The current validation status.

Show enum values

* * *

[Anchor to name](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-MetafieldDefinition.fields.name)name

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The human-readable name of the metafield definition.

[Anchor to namespace](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-MetafieldDefinition.fields.namespace)namespace

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The container for a group of metafields that the metafield definition is
associated with.

[Anchor to ownerType](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-MetafieldDefinition.fields.ownerType)ownerType

•[MetafieldOwnerType!](/docs/api/admin-
graphql/latest/enums/MetafieldOwnerType)

non-null

    

The resource type that the metafield definition is attached to.

Show enum values

[Anchor to pinnedPosition](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
MetafieldDefinition.fields.pinnedPosition)pinnedPosition

•[Int](/docs/api/admin-graphql/latest/scalars/Int)

    

The position of the metafield definition in the pinned list.

[Anchor to standardTemplate](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
MetafieldDefinition.fields.standardTemplate)standardTemplate

•[StandardMetafieldDefinitionTemplate](/docs/api/admin-
graphql/latest/objects/StandardMetafieldDefinitionTemplate)

    

The standard metafield definition template associated with the metafield
definition.

Show fields

[Anchor to type](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-MetafieldDefinition.fields.type)type

•[MetafieldDefinitionType!](/docs/api/admin-
graphql/latest/objects/MetafieldDefinitionType)

non-null

    

The type of data that each of the metafields that belong to the metafield
definition will store. Refer to the list of [supported
types](https://shopify.dev/apps/metafields/types).

Show fields

[Anchor to useAsCollectionCondition](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
MetafieldDefinition.fields.useAsCollectionCondition)useAsCollectionCondition

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether the metafield definition can be used as a collection condition.

[Anchor to validations](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
MetafieldDefinition.fields.validations)validations

•[[MetafieldDefinitionValidation!]!](/docs/api/admin-
graphql/latest/objects/MetafieldDefinitionValidation)

non-null

    

A list of [validation
options](https://shopify.dev/apps/metafields/definitions/validation) for the
metafields that belong to the metafield definition. For example, for a
metafield definition with the type `date`, you can set a minimum date
validation so that each of the metafields that belong to it can only store
dates after the specified minimum.

Show fields

[Anchor to validationStatus](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
MetafieldDefinition.fields.validationStatus)validationStatus

•[MetafieldDefinitionValidationStatus!](/docs/api/admin-
graphql/latest/enums/MetafieldDefinitionValidationStatus)

non-null

    

The validation status for the metafields that belong to the metafield
definition.

Show enum values

[Anchor to Metaobject](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Metaobject)[Metaobject](/docs/api/admin-graphql/latest/objects/Metaobject)

•OBJECT

    

Provides an object instance represented by a MetaobjectDefinition.

Show fields

[Anchor to capabilities](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Metaobject.fields.capabilities)capabilities

•[MetaobjectCapabilityData!](/docs/api/admin-
graphql/latest/objects/MetaobjectCapabilityData)

non-null

    

Metaobject capabilities for this Metaobject.

Show fields

[Anchor to createdBy](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Metaobject.fields.createdBy)createdBy

•[App!](/docs/api/admin-graphql/latest/objects/App)

non-null

    

The app used to create the object.

Show fields

[Anchor to createdByApp](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Metaobject.fields.createdByApp)createdByApp

•[App!](/docs/api/admin-graphql/latest/objects/App)

non-null

    

The app used to create the object.

Show fields

[Anchor to createdByStaff](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Metaobject.fields.createdByStaff)createdByStaff

•[StaffMember](/docs/api/admin-graphql/latest/objects/StaffMember)

    

The staff member who created the metaobject.

Show fields

[Anchor to definition](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Metaobject.fields.definition)definition

•[MetaobjectDefinition!](/docs/api/admin-
graphql/latest/objects/MetaobjectDefinition)

non-null

    

The MetaobjectDefinition that models this object type.

Show fields

[Anchor to displayName](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Metaobject.fields.displayName)displayName

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The preferred display name field value of the metaobject.

[Anchor to field](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Metaobject.fields.field)field

•[MetaobjectField](/docs/api/admin-graphql/latest/objects/MetaobjectField)

    

The field for an object key, or null if the key has no field definition.

Show fields

[Anchor to fields](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Metaobject.fields.fields)fields

•[[MetaobjectField!]!](/docs/api/admin-graphql/latest/objects/MetaobjectField)

non-null

    

All ordered fields of the metaobject with their definitions and values.

Show fields

[Anchor to handle](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Metaobject.fields.handle)handle

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The unique handle of the object, useful as a custom ID.

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
Metaobject.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to referencedBy](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Metaobject.fields.referencedBy)referencedBy

•[MetafieldRelationConnection!](/docs/api/admin-
graphql/latest/connections/MetafieldRelationConnection)

non-null

    

List of back references metafields that belong to the resource.

Show fields

[Anchor to thumbnailField](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Metaobject.fields.thumbnailField)thumbnailField

•[MetaobjectField](/docs/api/admin-graphql/latest/objects/MetaobjectField)

    

The recommended field to visually represent this metaobject. May be a file
reference or color field.

Show fields

[Anchor to type](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Metaobject.fields.type)type

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The type of the metaobject.

[Anchor to updatedAt](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Metaobject.fields.updatedAt)updatedAt

•[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime)

non-null

    

When the object was last updated.

[Anchor to staffMember](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Metaobject.fields.staffMember)staffMember

•[StaffMember](/docs/api/admin-graphql/latest/objects/StaffMember)

Deprecated

    

Show fields

[Anchor to MetaobjectDefinition](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
MetaobjectDefinition)[MetaobjectDefinition](/docs/api/admin-
graphql/latest/objects/MetaobjectDefinition)

•OBJECT

    

Provides the definition of a generic object structure composed of metafields.

Show fields

[Anchor to access](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-MetaobjectDefinition.fields.access)access

•[MetaobjectAccess!](/docs/api/admin-graphql/latest/objects/MetaobjectAccess)

non-null

    

Access configuration for the metaobject definition.

Show fields

[Anchor to capabilities](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
MetaobjectDefinition.fields.capabilities)capabilities

•[MetaobjectCapabilities!](/docs/api/admin-
graphql/latest/objects/MetaobjectCapabilities)

non-null

    

The capabilities of the metaobject definition.

Show fields

[Anchor to createdByApp](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
MetaobjectDefinition.fields.createdByApp)createdByApp

•[App!](/docs/api/admin-graphql/latest/objects/App)

non-null

    

The app used to create the metaobject definition.

Show fields

[Anchor to createdByStaff](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
MetaobjectDefinition.fields.createdByStaff)createdByStaff

•[StaffMember](/docs/api/admin-graphql/latest/objects/StaffMember)

    

The staff member who created the metaobject definition.

Show fields

[Anchor to description](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
MetaobjectDefinition.fields.description)description

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The administrative description.

[Anchor to displayNameKey](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
MetaobjectDefinition.fields.displayNameKey)displayNameKey

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The key of a field to reference as the display name for each object.

[Anchor to fieldDefinitions](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
MetaobjectDefinition.fields.fieldDefinitions)fieldDefinitions

•[[MetaobjectFieldDefinition!]!](/docs/api/admin-
graphql/latest/objects/MetaobjectFieldDefinition)

non-null

    

The fields defined for this object type.

Show fields

[Anchor to hasThumbnailField](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
MetaobjectDefinition.fields.hasThumbnailField)hasThumbnailField

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether this metaobject definition has field whose type can visually represent
a metaobject with the `thumbnailField`.

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
MetaobjectDefinition.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to metaobjects](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
MetaobjectDefinition.fields.metaobjects)metaobjects

•[MetaobjectConnection!](/docs/api/admin-
graphql/latest/connections/MetaobjectConnection)

non-null

    

A paginated connection to the metaobjects associated with the definition.

Show fields

[Anchor to metaobjectsCount](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
MetaobjectDefinition.fields.metaobjectsCount)metaobjectsCount

•[Int!](/docs/api/admin-graphql/latest/scalars/Int)

non-null

    

The count of metaobjects created for the definition.

[Anchor to name](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-MetaobjectDefinition.fields.name)name

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The human-readable name.

[Anchor to standardTemplate](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
MetaobjectDefinition.fields.standardTemplate)standardTemplate

•[StandardMetaobjectDefinitionTemplate](/docs/api/admin-
graphql/latest/objects/StandardMetaobjectDefinitionTemplate)

    

The standard metaobject template associated with the definition.

Show fields

[Anchor to type](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-MetaobjectDefinition.fields.type)type

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The type of the object definition. Defines the namespace of associated
metafields.

[Anchor to Model3d](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Model3d)[Model3d](/docs/api/admin-graphql/latest/objects/Model3d)

•OBJECT

    

Represents a Shopify hosted 3D model.

Show fields

[Anchor to alt](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
Model3d.fields.alt)alt

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

A word or phrase to describe the contents or the function of a file.

[Anchor to boundingBox](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Model3d.fields.boundingBox)boundingBox

•[Model3dBoundingBox](/docs/api/admin-
graphql/latest/objects/Model3dBoundingBox)

    

The 3d model's bounding box information.

Show fields

[Anchor to createdAt](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Model3d.fields.createdAt)createdAt

•[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime)

non-null

    

The date and time ([ISO 8601 format](http://en.wikipedia.org/wiki/ISO_8601))
when the file was created.

[Anchor to fileErrors](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Model3d.fields.fileErrors)fileErrors

•[[FileError!]!](/docs/api/admin-graphql/latest/objects/FileError)

non-null

    

Any errors that have occurred on the file.

Show fields

[Anchor to filename](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Model3d.fields.filename)filename

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The 3d model's filename.

[Anchor to fileStatus](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Model3d.fields.fileStatus)fileStatus

•[FileStatus!](/docs/api/admin-graphql/latest/enums/FileStatus)

non-null

    

The status of the file.

Show enum values

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
Model3d.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to mediaContentType](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Model3d.fields.mediaContentType)mediaContentType

•[MediaContentType!](/docs/api/admin-graphql/latest/enums/MediaContentType)

non-null

    

The media content type.

Show enum values

[Anchor to mediaErrors](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Model3d.fields.mediaErrors)mediaErrors

•[[MediaError!]!](/docs/api/admin-graphql/latest/objects/MediaError)

non-null

    

Any errors which have occurred on the media.

Show fields

[Anchor to mediaWarnings](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Model3d.fields.mediaWarnings)mediaWarnings

•[[MediaWarning!]!](/docs/api/admin-graphql/latest/objects/MediaWarning)

non-null

    

The warnings attached to the media.

Show fields

[Anchor to originalSource](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Model3d.fields.originalSource)originalSource

•[Model3dSource](/docs/api/admin-graphql/latest/objects/Model3dSource)

    

The 3d model's original source.

Show fields

[Anchor to preview](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Model3d.fields.preview)preview

•[MediaPreviewImage](/docs/api/admin-graphql/latest/objects/MediaPreviewImage)

    

The preview image for the media.

Show fields

[Anchor to sources](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Model3d.fields.sources)sources

•[[Model3dSource!]!](/docs/api/admin-graphql/latest/objects/Model3dSource)

non-null

    

The 3d model's sources.

Show fields

[Anchor to status](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Model3d.fields.status)status

•[MediaStatus!](/docs/api/admin-graphql/latest/enums/MediaStatus)

non-null

    

Current status of the media.

Show enum values

[Anchor to updatedAt](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Model3d.fields.updatedAt)updatedAt

•[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime)

non-null

    

The date and time ([ISO 8601 format](http://en.wikipedia.org/wiki/ISO_8601))
when the file was last updated.

[Anchor to OnlineStoreTheme](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
OnlineStoreTheme)[OnlineStoreTheme](/docs/api/admin-
graphql/latest/objects/OnlineStoreTheme)

•OBJECT

    

A theme for display on the storefront.

Show fields

[Anchor to createdAt](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-OnlineStoreTheme.fields.createdAt)createdAt

•[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime)

non-null

    

The date and time when the theme was created.

[Anchor to files](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-OnlineStoreTheme.fields.files)files

•[OnlineStoreThemeFileConnection](/docs/api/admin-
graphql/latest/connections/OnlineStoreThemeFileConnection)

    

The files in the theme.

Show fields

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
OnlineStoreTheme.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to name](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-OnlineStoreTheme.fields.name)name

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The name of the theme, set by the merchant.

[Anchor to prefix](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-OnlineStoreTheme.fields.prefix)prefix

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The prefix of the theme.

[Anchor to processing](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
OnlineStoreTheme.fields.processing)processing

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether the theme is processing.

[Anchor to processingFailed](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
OnlineStoreTheme.fields.processingFailed)processingFailed

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether the theme processing failed.

[Anchor to role](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-OnlineStoreTheme.fields.role)role

•[ThemeRole!](/docs/api/admin-graphql/latest/enums/ThemeRole)

non-null

    

The role of the theme.

Show enum values

[Anchor to themeStoreId](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
OnlineStoreTheme.fields.themeStoreId)themeStoreId

•[Int](/docs/api/admin-graphql/latest/scalars/Int)

    

The theme store ID.

[Anchor to translations](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
OnlineStoreTheme.fields.translations)translations

•[[Translation!]!](/docs/api/admin-graphql/latest/objects/Translation)

non-null

    

The published translations associated with the resource.

Show fields

[Anchor to updatedAt](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-OnlineStoreTheme.fields.updatedAt)updatedAt

•[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime)

non-null

    

The date and time when the theme was last updated.

[Anchor to Order](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Order)[Order](/docs/api/admin-graphql/latest/objects/Order)

•OBJECT

    

The `Order` object represents a customer's request to purchase one or more
products from a store. Use the `Order` object to handle the complete purchase
lifecycle from checkout to fulfillment.

Use the `Order` object when you need to:

  * Display order details on customer account pages or admin dashboards.
  * Create orders for phone sales, wholesale customers, or subscription services.
  * Update order information like shipping addresses, notes, or fulfillment status.
  * Process returns, exchanges, and partial refunds.
  * Generate invoices, receipts, and shipping labels.

The `Order` object serves as the central hub connecting customer information,
product details, payment processing, and fulfillment data within the GraphQL
Admin API schema.

* * *

Note

Only the last 60 days' worth of orders from a store are accessible from the
`Order` object by default. If you want to access older records, then you need
to [request access to all orders](https://shopify.dev/docs/api/usage/access-
scopes#orders-permissions). If your app is granted access, then you can add
the `read_all_orders`, `read_orders`, and `write_orders` scopes.

* * *

* * *

Caution

Only use orders data if it's required for your app's functionality. Shopify
will restrict [access to scopes](https://shopify.dev/docs/api/usage/access-
scopes#requesting-specific-permissions) for apps that don't have a legitimate
use for the associated data.

* * *

Learn more about [building apps for orders and
fulfillment](https://shopify.dev/docs/apps/build/orders-fulfillment).

Show fields

[Anchor to additionalFees](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Order.fields.additionalFees)additionalFees

•[[AdditionalFee!]!](/docs/api/admin-graphql/latest/objects/AdditionalFee)

non-null

    

A list of additional fees applied to an order, such as duties, import fees, or
[tax lines](https://shopify.dev/docs/api/admin-
graphql/latest/objects/order#field-Order.fields.additionalFees.taxLines).

Show fields

[Anchor to agreements](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Order.fields.agreements)agreements

•[SalesAgreementConnection!](/docs/api/admin-
graphql/latest/connections/SalesAgreementConnection)

non-null

    

A list of sales agreements associated with the order, such as contracts
defining payment terms, or delivery schedules between merchants and customers.

Show fields

[Anchor to alerts](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Order.fields.alerts)alerts

•[[ResourceAlert!]!](/docs/api/admin-graphql/latest/objects/ResourceAlert)

non-null

    

A list of messages that appear on the **Orders** page in the Shopify admin.
These alerts provide merchants with important information about an order's
status or required actions.

Show fields

[Anchor to app](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
Order.fields.app)app

•[OrderApp](/docs/api/admin-graphql/latest/objects/OrderApp)

    

The application that created the order. For example, "Online Store", "Point of
Sale", or a custom app name. Use this to identify the order source for
attribution and fulfillment workflows. Learn more about [building apps for
orders and fulfillment](https://shopify.dev/docs/apps/build/orders-
fulfillment).

Show fields

[Anchor to billingAddress](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Order.fields.billingAddress)billingAddress

•[MailingAddress](/docs/api/admin-graphql/latest/objects/MailingAddress)

    

The billing address associated with the payment method selected by the
customer for an order. Returns `null` if no billing address was provided
during checkout.

Show fields

[Anchor to billingAddressMatchesShippingAddress](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Order.fields.billingAddressMatchesShippingAddress)billingAddressMatchesShippingAddress

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether the billing address matches the [shipping
address](https://shopify.dev/docs/api/admin-
graphql/latest/objects/order#field-Order.fields.shippingAddress). Returns
`true` if both addresses are the same, and `false` if they're different or if
an address is missing.

[Anchor to cancellation](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Order.fields.cancellation)cancellation

•[OrderCancellation](/docs/api/admin-graphql/latest/objects/OrderCancellation)

    

Details of an order's cancellation, if it has been canceled. This includes the
reason, date, and any [staff notes](https://shopify.dev/api/admin-
graphql/latest/objects/OrderCancellation#field-
OrderCancellation.fields.staffNote).

Show fields

[Anchor to cancelledAt](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Order.fields.cancelledAt)cancelledAt

•[DateTime](/docs/api/admin-graphql/latest/scalars/DateTime)

    

The date and time in [ISO 8601 format](https://en.wikipedia.org/wiki/ISO_8601)
when an order was canceled. Returns `null` if the order hasn't been canceled.

[Anchor to cancelReason](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Order.fields.cancelReason)cancelReason

•[OrderCancelReason](/docs/api/admin-graphql/latest/enums/OrderCancelReason)

    

The reason provided for an order cancellation. For example, a merchant might
cancel an order if there's insufficient inventory. Returns `null` if the order
hasn't been canceled.

Show enum values

[Anchor to canMarkAsPaid](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Order.fields.canMarkAsPaid)canMarkAsPaid

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether an order can be manually marked as paid. Returns `false` if the order
is already paid, is canceled, has pending [Shopify
Payments](https://help.shopify.com/en/manual/payments/shopify-
payments/payouts) transactions, or has a negative payment amount.

[Anchor to canNotifyCustomer](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Order.fields.canNotifyCustomer)canNotifyCustomer

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether order notifications can be sent to the customer. Returns `true` if the
customer has a valid [email address](https://shopify.dev/docs/api/admin-
graphql/latest/objects/order#field-Order.fields.email).

[Anchor to capturable](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Order.fields.capturable)capturable

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether an authorized payment for an order can be captured. Returns `true` if
an authorized payment exists that hasn't been fully captured yet. Learn more
about [capturing
payments](https://help.shopify.com/en/manual/fulfillment/managing-
orders/payments/capturing-payments).

[Anchor to cartDiscountAmountSet](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Order.fields.cartDiscountAmountSet)cartDiscountAmountSet

•[MoneyBag](/docs/api/admin-graphql/latest/objects/MoneyBag)

    

The total discount amount applied at the time the order was created, displayed
in both shop and presentment currencies, before returns, refunds, order edits,
and cancellations. This field only includes discounts applied to the entire
order.

Show fields

[Anchor to channelInformation](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Order.fields.channelInformation)channelInformation

•[ChannelInformation](/docs/api/admin-
graphql/latest/objects/ChannelInformation)

    

Details about the sales channel that created the order, such as the [channel
app type](https://shopify.dev/docs/api/admin-
graphql/latest/objects/channel#field-Channel.fields.channelType) and [channel
name](https://shopify.dev/docs/api/admin-
graphql/latest/objects/ChannelDefinition#field-
ChannelDefinition.fields.channelName), which helps to track order sources.

Show fields

[Anchor to clientIp](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Order.fields.clientIp)clientIp

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The IP address of the customer who placed the order. Useful for fraud
detection and geographic analysis.

[Anchor to closed](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Order.fields.closed)closed

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether an order is closed. An order is considered closed if all its line
items have been fulfilled or canceled, and all financial transactions are
complete.

[Anchor to closedAt](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Order.fields.closedAt)closedAt

•[DateTime](/docs/api/admin-graphql/latest/scalars/DateTime)

    

The date and time [ISO 8601 format](https://en.wikipedia.org/wiki/ISO_8601)
when an order was closed. Shopify automatically records this timestamp when
all items have been fulfilled or canceled, and all financial transactions are
complete. Returns `null` if the order isn't closed.

[Anchor to confirmationNumber](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Order.fields.confirmationNumber)confirmationNumber

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

A customer-facing order identifier, often shown instead of the sequential
order name. It uses a random alphanumeric format (for example, `XPAV284CT`)
and isn't guaranteed to be unique across orders.

[Anchor to confirmed](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Order.fields.confirmed)confirmed

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether inventory has been reserved for an order. Returns `true` if inventory
quantities for an order's [line items](https://shopify.dev/docs/api/admin-
graphql/latest/objects/LineItem) have been reserved. Learn more about
[managing inventory quantities and
states](https://shopify.dev/docs/apps/build/orders-fulfillment/inventory-
management-apps/manage-quantities-states).

[Anchor to createdAt](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Order.fields.createdAt)createdAt

•[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime)

non-null

    

The date and time in [ISO 8601 format](https://en.wikipedia.org/wiki/ISO_8601)
when an order was created. This timestamp is set when the customer completes
checkout and remains unchanged throughout an order's lifecycle.

[Anchor to currencyCode](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Order.fields.currencyCode)currencyCode

•[CurrencyCode!](/docs/api/admin-graphql/latest/enums/CurrencyCode)

non-null

    

The shop currency when the order was placed. For example, "USD" or "CAD".

Show enum values

[Anchor to currentCartDiscountAmountSet](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Order.fields.currentCartDiscountAmountSet)currentCartDiscountAmountSet

•[MoneyBag!](/docs/api/admin-graphql/latest/objects/MoneyBag)

non-null

    

The current total of all discounts applied to the entire order, after returns,
refunds, order edits, and cancellations. This includes discount codes,
automatic discounts, and other promotions that affect the whole order rather
than individual line items. To get the original discount amount at the time of
order creation, use the
[`cartDiscountAmountSet`](https://shopify.dev/docs/api/admin-
graphql/latest/objects/order#field-Order.fields.cartDiscountAmountSet) field.

Show fields

[Anchor to currentShippingPriceSet](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Order.fields.currentShippingPriceSet)currentShippingPriceSet

•[MoneyBag!](/docs/api/admin-graphql/latest/objects/MoneyBag)

non-null

    

The current shipping price after applying refunds and discounts. If the parent
`order.taxesIncluded` field is true, then this price includes taxes.
Otherwise, this field is the pre-tax price.

Show fields

[Anchor to currentSubtotalLineItemsQuantity](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Order.fields.currentSubtotalLineItemsQuantity)currentSubtotalLineItemsQuantity

•[Int!](/docs/api/admin-graphql/latest/scalars/Int)

non-null

    

The current sum of the quantities for all line items that contribute to the
order's subtotal price, after returns, refunds, order edits, and
cancellations.

[Anchor to currentSubtotalPriceSet](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Order.fields.currentSubtotalPriceSet)currentSubtotalPriceSet

•[MoneyBag!](/docs/api/admin-graphql/latest/objects/MoneyBag)

non-null

    

The total price of the order, after returns and refunds, in shop and
presentment currencies. This includes taxes and discounts.

Show fields

[Anchor to currentTaxLines](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Order.fields.currentTaxLines)currentTaxLines

•[[TaxLine!]!](/docs/api/admin-graphql/latest/objects/TaxLine)

non-null

    

A list of all tax lines applied to line items on the order, after returns. Tax
line prices represent the total price for all tax lines with the same `rate`
and `title`.

Show fields

[Anchor to currentTotalAdditionalFeesSet](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Order.fields.currentTotalAdditionalFeesSet)currentTotalAdditionalFeesSet

•[MoneyBag](/docs/api/admin-graphql/latest/objects/MoneyBag)

    

The current total of all additional fees for an order, after any returns or
modifications. Modifications include returns, refunds, order edits, and
cancellations. Additional fees can include charges such as duties, import
fees, and special handling.

Show fields

[Anchor to currentTotalDiscountsSet](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Order.fields.currentTotalDiscountsSet)currentTotalDiscountsSet

•[MoneyBag!](/docs/api/admin-graphql/latest/objects/MoneyBag)

non-null

    

The total amount discounted on the order after returns and refunds, in shop
and presentment currencies. This includes both order and line level discounts.

Show fields

[Anchor to currentTotalDutiesSet](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Order.fields.currentTotalDutiesSet)currentTotalDutiesSet

•[MoneyBag](/docs/api/admin-graphql/latest/objects/MoneyBag)

    

The current total duties amount for an order, after any returns or
modifications. Modifications include returns, refunds, order edits, and
cancellations.

Show fields

[Anchor to currentTotalPriceSet](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Order.fields.currentTotalPriceSet)currentTotalPriceSet

•[MoneyBag!](/docs/api/admin-graphql/latest/objects/MoneyBag)

non-null

    

The total price of the order, after returns, in shop and presentment
currencies. This includes taxes and discounts.

Show fields

[Anchor to currentTotalTaxSet](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Order.fields.currentTotalTaxSet)currentTotalTaxSet

•[MoneyBag!](/docs/api/admin-graphql/latest/objects/MoneyBag)

non-null

    

The sum of the prices of all tax lines applied to line items on the order,
after returns and refunds, in shop and presentment currencies.

Show fields

[Anchor to currentTotalWeight](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Order.fields.currentTotalWeight)currentTotalWeight

•[UnsignedInt64!](/docs/api/admin-graphql/latest/scalars/UnsignedInt64)

non-null

    

The total weight of the order after returns and refunds, in grams.

[Anchor to customAttributes](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Order.fields.customAttributes)customAttributes

•[[Attribute!]!](/docs/api/admin-graphql/latest/objects/Attribute)

non-null

    

A list of additional information that has been attached to the order. For
example, gift message, delivery instructions, or internal notes.

Show fields

[Anchor to customer](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Order.fields.customer)customer

•[Customer](/docs/api/admin-graphql/latest/objects/Customer)

    

The customer who placed an order. Returns `null` if an order was created
through a checkout without customer authentication, such as a guest checkout.
Learn more about [customer
accounts](https://help.shopify.com/manual/customers/customer-accounts).

Show fields

[Anchor to customerAcceptsMarketing](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Order.fields.customerAcceptsMarketing)customerAcceptsMarketing

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether the customer agreed to receive marketing emails at the time of
purchase. Use this to ensure compliance with marketing consent laws and to
segment customers for email campaigns. Learn more about [building customer
segments](https://shopify.dev/docs/apps/build/marketing-analytics/customer-
segments).

[Anchor to customerJourneySummary](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Order.fields.customerJourneySummary)customerJourneySummary

•[CustomerJourneySummary](/docs/api/admin-
graphql/latest/objects/CustomerJourneySummary)

    

The customer's visits and interactions with the online store before placing
the order. Use this to understand customer behavior, attribution sources, and
marketing effectiveness to optimize your sales funnel.

Show fields

[Anchor to customerLocale](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Order.fields.customerLocale)customerLocale

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The customer's language and region preference at the time of purchase. For
example, "en" for English, "fr-CA" for French (Canada), or "es-MX" for Spanish
(Mexico). Use this to provide localized customer service and targeted
marketing in the customer's preferred language.

[Anchor to discountApplications](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Order.fields.discountApplications)discountApplications

•[DiscountApplicationConnection!](/docs/api/admin-
graphql/latest/connections/DiscountApplicationConnection)

non-null

    

A list of discounts that are applied to the order, excluding order edits and
refunds. Includes discount codes, automatic discounts, and other promotions
that reduce the order total.

Show fields

[Anchor to discountCode](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Order.fields.discountCode)discountCode

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The discount code used for an order. Returns `null` if no discount code was
applied.

[Anchor to discountCodes](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Order.fields.discountCodes)discountCodes

•[[String!]!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The discount codes used for the order. Multiple codes can be applied to a
single order.

[Anchor to displayAddress](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Order.fields.displayAddress)displayAddress

•[MailingAddress](/docs/api/admin-graphql/latest/objects/MailingAddress)

    

The primary address of the customer, prioritizing shipping address over
billing address when both are available. Returns `null` if neither shipping
address nor billing address was provided.

Show fields

[Anchor to displayFinancialStatus](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Order.fields.displayFinancialStatus)displayFinancialStatus

•[OrderDisplayFinancialStatus](/docs/api/admin-
graphql/latest/enums/OrderDisplayFinancialStatus)

    

An order's financial status for display in the Shopify admin.

Show enum values

[Anchor to displayFulfillmentStatus](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Order.fields.displayFulfillmentStatus)displayFulfillmentStatus

•[OrderDisplayFulfillmentStatus!](/docs/api/admin-
graphql/latest/enums/OrderDisplayFulfillmentStatus)

non-null

    

The order's fulfillment status that displays in the Shopify admin to
merchants. For example, an order might be unfulfilled or scheduled. For
detailed processing, use the
[`FulfillmentOrder`](https://shopify.dev/docs/api/admin-
graphql/latest/objects/FulfillmentOrder) object.

Show enum values

[Anchor to disputes](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Order.fields.disputes)disputes

•[[OrderDisputeSummary!]!](/docs/api/admin-
graphql/latest/objects/OrderDisputeSummary)

non-null

    

A list of payment disputes associated with the order, such as chargebacks or
payment inquiries. Disputes occur when customers challenge transactions with
their bank or payment provider.

Show fields

[Anchor to dutiesIncluded](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Order.fields.dutiesIncluded)dutiesIncluded

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether duties are included in the subtotal price of the order. Duties are
import taxes charged by customs authorities when goods cross international
borders.

[Anchor to edited](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Order.fields.edited)edited

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether the order has had any edits applied. For example, adding or removing
line items, updating quantities, or changing prices.

[Anchor to email](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Order.fields.email)email

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The email address associated with the customer for this order. Used for
sending order confirmations, shipping notifications, and other order-related
communications. Returns `null` if no email address was provided during
checkout.

[Anchor to estimatedTaxes](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Order.fields.estimatedTaxes)estimatedTaxes

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether taxes on the order are estimated. This field returns `false` when
taxes on the order are finalized and aren't subject to any changes.

[Anchor to events](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Order.fields.events)events

•[EventConnection!](/docs/api/admin-
graphql/latest/connections/EventConnection)

non-null

    

A list of events associated with the order. Events track significant changes
and activities related to the order, such as creation, payment, fulfillment,
and cancellation.

Show fields

[Anchor to fulfillable](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Order.fields.fulfillable)fulfillable

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether there are line items that can be fulfilled. This field returns `false`
when the order has no fulfillable line items. For a more granular view of the
fulfillment status, refer to the
[FulfillmentOrder](https://shopify.dev/api/admin-
graphql/latest/objects/FulfillmentOrder) object.

[Anchor to fulfillmentOrders](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Order.fields.fulfillmentOrders)fulfillmentOrders

•[FulfillmentOrderConnection!](/docs/api/admin-
graphql/latest/connections/FulfillmentOrderConnection)

non-null

    

A list of [fulfillment orders](https://shopify.dev/docs/api/admin-
graphql/latest/objects/FulfillmentOrder) for an order. Each fulfillment order
groups [line items](https://shopify.dev/docs/api/admin-
graphql/latest/objects/Order#field-Order.fields.lineItems) that are fulfilled
together, allowing an order to be processed in parts if needed.

Show fields

[Anchor to fulfillments](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Order.fields.fulfillments)fulfillments

•[[Fulfillment!]!](/docs/api/admin-graphql/latest/objects/Fulfillment)

non-null

    

A list of shipments for the order. Fulfillments represent the physical
shipment of products to customers.

Show fields

[Anchor to fulfillmentsCount](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Order.fields.fulfillmentsCount)fulfillmentsCount

•[Count](/docs/api/admin-graphql/latest/objects/Count)

    

The total number of fulfillments for the order, including canceled ones.

Show fields

[Anchor to fullyPaid](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Order.fields.fullyPaid)fullyPaid

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether the order has been paid in full. This field returns `true` when the
total amount received equals or exceeds the order total.

[Anchor to hasTimelineComment](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Order.fields.hasTimelineComment)hasTimelineComment

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether the merchant has added a timeline comment to the order.

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
Order.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to legacyResourceId](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Order.fields.legacyResourceId)legacyResourceId

•[UnsignedInt64!](/docs/api/admin-graphql/latest/scalars/UnsignedInt64)

non-null

    

The ID of the corresponding resource in the REST Admin API.

[Anchor to lineItems](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Order.fields.lineItems)lineItems

•[LineItemConnection!](/docs/api/admin-
graphql/latest/connections/LineItemConnection)

non-null

    

A list of the order's line items. Line items represent the individual products
and quantities that make up the order.

Show fields

[Anchor to localizedFields](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Order.fields.localizedFields)localizedFields

•[LocalizedFieldConnection!](/docs/api/admin-
graphql/latest/connections/LocalizedFieldConnection)

non-null

    

List of localized fields for the resource.

Show fields

[Anchor to merchantBusinessEntity](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Order.fields.merchantBusinessEntity)merchantBusinessEntity

•[BusinessEntity!](/docs/api/admin-graphql/latest/objects/BusinessEntity)

non-null

    

The legal business structure that the merchant operates under for this order,
such as an LLC, corporation, or partnership. Used for tax reporting, legal
compliance, and determining which business entity is responsible for the
order.

Show fields

[Anchor to merchantEditable](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Order.fields.merchantEditable)merchantEditable

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether the order can be edited by the merchant. Returns `false` for orders
that can't be modified, such as canceled orders or orders with specific
payment statuses.

[Anchor to merchantEditableErrors](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Order.fields.merchantEditableErrors)merchantEditableErrors

•[[String!]!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

A list of reasons why the order can't be edited. For example, canceled orders
can't be edited.

[Anchor to merchantOfRecordApp](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Order.fields.merchantOfRecordApp)merchantOfRecordApp

•[OrderApp](/docs/api/admin-graphql/latest/objects/OrderApp)

    

The application acting as the Merchant of Record for the order. The Merchant
of Record is responsible for tax collection and remittance.

Show fields

[Anchor to metafield](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Order.fields.metafield)metafield

•[Metafield](/docs/api/admin-graphql/latest/objects/Metafield)

    

A [custom field](https://shopify.dev/docs/apps/build/custom-data), including
its `namespace` and `key`, that's associated with a Shopify resource for the
purposes of adding and storing additional information.

Show fields

[Anchor to metafields](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Order.fields.metafields)metafields

•[MetafieldConnection!](/docs/api/admin-
graphql/latest/connections/MetafieldConnection)

non-null

    

A list of [custom fields](https://shopify.dev/docs/apps/build/custom-data)
that a merchant associates with a Shopify resource.

Show fields

[Anchor to name](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Order.fields.name)name

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The unique identifier for the order that appears on the order page in the
Shopify admin and the **Order status** page. For example, "#1001", "EN1001",
or "1001-A". This value isn't unique across multiple stores. Use this field to
identify orders in the Shopify admin and for order tracking.

[Anchor to netPaymentSet](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Order.fields.netPaymentSet)netPaymentSet

•[MoneyBag!](/docs/api/admin-graphql/latest/objects/MoneyBag)

non-null

    

The net payment for the order, based on the total amount received minus the
total amount refunded, in shop and presentment currencies.

Show fields

[Anchor to nonFulfillableLineItems](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Order.fields.nonFulfillableLineItems)nonFulfillableLineItems

•[LineItemConnection!](/docs/api/admin-
graphql/latest/connections/LineItemConnection)

non-null

    

A list of line items that can't be fulfilled. For example, tips and fully
refunded line items can't be fulfilled. For a more granular view of the
fulfillment status, refer to the
[FulfillmentOrder](https://shopify.dev/api/admin-
graphql/latest/objects/FulfillmentOrder) object.

Show fields

[Anchor to note](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Order.fields.note)note

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The note associated with the order. Contains additional information or
instructions added by merchants or customers during the order process.
Commonly used for special delivery instructions, gift messages, or internal
processing notes.

[Anchor to number](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Order.fields.number)number

•[Int!](/docs/api/admin-graphql/latest/scalars/Int)

non-null

    

The order number used to generate the name using the store's configured order
number prefix/suffix. This number isn't guaranteed to follow a consecutive
integer sequence (e.g. 1, 2, 3..), nor is it guaranteed to be unique across
multiple stores, or even for a single store.

[Anchor to originalTotalAdditionalFeesSet](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Order.fields.originalTotalAdditionalFeesSet)originalTotalAdditionalFeesSet

•[MoneyBag](/docs/api/admin-graphql/latest/objects/MoneyBag)

    

The total amount of all additional fees, such as import fees or taxes, that
were applied when an order was created. Returns `null` if additional fees
aren't applicable.

Show fields

[Anchor to originalTotalDutiesSet](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Order.fields.originalTotalDutiesSet)originalTotalDutiesSet

•[MoneyBag](/docs/api/admin-graphql/latest/objects/MoneyBag)

    

The total amount of duties calculated when an order was created, before any
modifications. Modifications include returns, refunds, order edits, and
cancellations. Use
[`currentTotalDutiesSet`](https://shopify.dev/docs/api/admin-
graphql/latest/objects/order#field-Order.fields.currentTotalDutiesSet) to
retrieve the current duties amount after adjustments.

Show fields

[Anchor to originalTotalPriceSet](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Order.fields.originalTotalPriceSet)originalTotalPriceSet

•[MoneyBag!](/docs/api/admin-graphql/latest/objects/MoneyBag)

non-null

    

The total price of the order at the time of order creation, in shop and
presentment currencies. Use this to compare the original order value against
the current total after edits, returns, or refunds.

Show fields

[Anchor to paymentCollectionDetails](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Order.fields.paymentCollectionDetails)paymentCollectionDetails

•[OrderPaymentCollectionDetails!](/docs/api/admin-
graphql/latest/objects/OrderPaymentCollectionDetails)

non-null

    

The payment collection details for the order, including payment status,
outstanding amounts, and collection information. Use this to understand when
and how payments should be collected, especially for orders with deferred or
installment payment terms.

Show fields

[Anchor to paymentGatewayNames](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Order.fields.paymentGatewayNames)paymentGatewayNames

•[[String!]!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

A list of the names of all payment gateways used for the order. For example,
"Shopify Payments" and "Cash on Delivery (COD)".

[Anchor to paymentTerms](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Order.fields.paymentTerms)paymentTerms

•[PaymentTerms](/docs/api/admin-graphql/latest/objects/PaymentTerms)

    

The payment terms associated with the order, such as net payment due dates or
early payment discounts. Payment terms define when and how an order should be
paid. Returns `null` if no specific payment terms were set for the order.

Show fields

[Anchor to phone](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Order.fields.phone)phone

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The phone number associated with the customer for this order. Useful for
contacting customers about shipping updates, delivery notifications, or order
issues. Returns `null` if no phone number was provided during checkout.

[Anchor to poNumber](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Order.fields.poNumber)poNumber

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The purchase order (PO) number that's associated with an order. This is
typically provided by business customers who require a PO number for their
procurement.

[Anchor to presentmentCurrencyCode](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Order.fields.presentmentCurrencyCode)presentmentCurrencyCode

•[CurrencyCode!](/docs/api/admin-graphql/latest/enums/CurrencyCode)

non-null

    

The currency used by the customer when placing the order. For example, "USD",
"EUR", or "CAD". This may differ from the shop's base currency when serving
international customers or using multi-currency pricing.

Show enum values

[Anchor to processedAt](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Order.fields.processedAt)processedAt

•[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime)

non-null

    

The date and time in [ISO 8601 format](https://en.wikipedia.org/wiki/ISO_8601)
when the order was processed. This date and time might not match the date and
time when the order was created.

[Anchor to productNetwork](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Order.fields.productNetwork)productNetwork

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether the customer also purchased items from other stores in the network.

[Anchor to publication](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Order.fields.publication)publication

•[Publication](/docs/api/admin-graphql/latest/objects/Publication)

    

The sales channel that the order was created from, such as the [Online
Store](https://shopify.dev/docs/apps/build/app-surfaces#online-store) or
[Shopify POS](https://shopify.dev/docs/apps/build/app-surfaces#point-of-sale).

Show fields

[Anchor to purchasingEntity](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Order.fields.purchasingEntity)purchasingEntity

•[PurchasingEntity](/docs/api/admin-graphql/latest/unions/PurchasingEntity)

    

The business entity that placed the order, including company details and
purchasing relationships. Used for B2B transactions to track which company or
organization is responsible for the purchase and payment terms.

Show union types

[Anchor to refundable](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Order.fields.refundable)refundable

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether the order can be refunded based on its payment transactions. Returns
`false` for orders with no eligible payment transactions, such as fully
refunded orders or orders with non-refundable payment methods.

[Anchor to refundDiscrepancySet](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Order.fields.refundDiscrepancySet)refundDiscrepancySet

•[MoneyBag!](/docs/api/admin-graphql/latest/objects/MoneyBag)

non-null

    

The difference between the suggested and actual refund amount of all refunds
that have been applied to the order. A positive value indicates a difference
in the merchant's favor, and a negative value indicates a difference in the
customer's favor.

Show fields

[Anchor to refunds](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Order.fields.refunds)refunds

•[[Refund!]!](/docs/api/admin-graphql/latest/objects/Refund)

non-null

    

A list of refunds that have been applied to the order. Refunds represent money
returned to customers for returned items, cancellations, or adjustments.

Show fields

[Anchor to registeredSourceUrl](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Order.fields.registeredSourceUrl)registeredSourceUrl

•[URL](/docs/api/admin-graphql/latest/scalars/URL)

    

The URL of the source that the order originated from, if found in the domain
registry. Returns `null` if the source URL isn't in the domain registry.

[Anchor to requiresShipping](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Order.fields.requiresShipping)requiresShipping

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether the order requires physical shipping to the customer. Returns `false`
for digital-only orders (such as gift cards or downloadable products) and
`true` for orders with physical products that need delivery. Use this to
determine shipping workflows and logistics requirements.

[Anchor to restockable](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Order.fields.restockable)restockable

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether any line items on the order can be restocked into inventory. Returns
`false` for digital products, custom items, or items that can't be resold.

[Anchor to retailLocation](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Order.fields.retailLocation)retailLocation

•[Location](/docs/api/admin-graphql/latest/objects/Location)

    

The physical location where a retail order is created or completed, except for
draft POS orders completed using the "mark as paid" flow in the Shopify admin,
which return `null`. Transactions associated with the order might have been
processed at a different location.

Show fields

[Anchor to returns](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Order.fields.returns)returns

•[ReturnConnection!](/docs/api/admin-
graphql/latest/connections/ReturnConnection)

non-null

    

The returns associated with the order. Contains information about items that
customers have requested to return, including return reasons, status, and
refund details. Use this to track and manage the return process for order
items.

Show fields

[Anchor to returnStatus](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Order.fields.returnStatus)returnStatus

•[OrderReturnStatus!](/docs/api/admin-graphql/latest/enums/OrderReturnStatus)

non-null

    

The order's aggregated return status for display purposes. Indicates the
overall state of returns for the order, helping merchants track and manage the
return process.

Show enum values

[Anchor to risk](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Order.fields.risk)risk

•[OrderRiskSummary!](/docs/api/admin-graphql/latest/objects/OrderRiskSummary)

non-null

    

The risk assessment summary for the order. Provides fraud analysis and risk
scoring to help you identify potentially fraudulent orders. Use this to make
informed decisions about order fulfillment and payment processing.

Show fields

[Anchor to shippingAddress](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Order.fields.shippingAddress)shippingAddress

•[MailingAddress](/docs/api/admin-graphql/latest/objects/MailingAddress)

    

The shipping address where the order will be delivered. Contains the
customer's delivery location for fulfillment and shipping label generation.
Returns `null` for digital orders or orders that don't require shipping.

Show fields

[Anchor to shippingLine](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Order.fields.shippingLine)shippingLine

•[ShippingLine](/docs/api/admin-graphql/latest/objects/ShippingLine)

    

A summary of all shipping costs on the order. Aggregates shipping charges,
discounts, and taxes to provide a single view of delivery costs.

Show fields

[Anchor to shippingLines](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Order.fields.shippingLines)shippingLines

•[ShippingLineConnection!](/docs/api/admin-
graphql/latest/connections/ShippingLineConnection)

non-null

    

The shipping methods applied to the order. Each shipping line represents a
shipping option chosen during checkout, including the carrier, service level,
and cost. Use this to understand shipping charges and delivery options for the
order.

Show fields

[Anchor to shopifyProtect](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Order.fields.shopifyProtect)shopifyProtect

•[ShopifyProtectOrderSummary](/docs/api/admin-
graphql/latest/objects/ShopifyProtectOrderSummary)

    

The Shopify Protect details for the order, including fraud protection status
and coverage information. Shopify Protect helps protect eligible orders
against fraudulent chargebacks. Returns `null` if Shopify Protect is disabled
for the shop or the order isn't eligible for protection. Learn more about
[Shopify Protect](https://www.shopify.com/protect).

Show fields

[Anchor to sourceIdentifier](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Order.fields.sourceIdentifier)sourceIdentifier

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

A unique POS or third party order identifier. For example, "1234-12-1000" or
"111-98567-54". The [`receiptNumber`](https://shopify.dev/docs/api/admin-
graphql/latest/objects/Order#field-receiptNumber) field is derived from this
value for POS orders.

[Anchor to sourceName](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Order.fields.sourceName)sourceName

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The name of the source associated with the order, such as "web", "mobile_app",
or "pos". Use this field to identify the platform where the order was placed.

[Anchor to staffMember](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Order.fields.staffMember)staffMember

•[StaffMember](/docs/api/admin-graphql/latest/objects/StaffMember)

    

The staff member who created or is responsible for the order. Useful for
tracking which team member handled phone orders, manual orders, or order
modifications. Returns `null` for orders created directly by customers through
the online store.

Show fields

[Anchor to statusPageUrl](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Order.fields.statusPageUrl)statusPageUrl

•[URL!](/docs/api/admin-graphql/latest/scalars/URL)

non-null

    

The URL where customers can check their order's current status, including
tracking information and delivery updates. Provides order tracking links in
emails, apps, or customer communications.

Show arguments

### Arguments

[Anchor to audience](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Order.fields.statusPageUrl.arguments.audience)audience

•[Audience](/docs/api/admin-graphql/latest/enums/Audience)

    

Specifies the intended audience for the status page URL.

Show enum values

[Anchor to notificationUsage](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Order.fields.statusPageUrl.arguments.notificationUsage)notificationUsage

•[NotificationUsage](/docs/api/admin-graphql/latest/enums/NotificationUsage)

    

Specifies the intended notification usage for the status page URL.

Show enum values

* * *

[Anchor to subtotalLineItemsQuantity](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Order.fields.subtotalLineItemsQuantity)subtotalLineItemsQuantity

•[Int!](/docs/api/admin-graphql/latest/scalars/Int)

non-null

    

The sum of quantities for all line items that contribute to the order's
subtotal price. This excludes quantities for items like tips, shipping costs,
or gift cards that don't affect the subtotal. Use this to quickly understand
the total item count for pricing calculations.

[Anchor to subtotalPriceSet](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Order.fields.subtotalPriceSet)subtotalPriceSet

•[MoneyBag](/docs/api/admin-graphql/latest/objects/MoneyBag)

    

The sum of the prices for all line items after discounts and before returns,
in shop and presentment currencies. If `taxesIncluded` is `true`, then the
subtotal also includes tax.

Show fields

[Anchor to suggestedRefund](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Order.fields.suggestedRefund)suggestedRefund

•[SuggestedRefund](/docs/api/admin-graphql/latest/objects/SuggestedRefund)

    

A calculated refund suggestion for the order based on specified line items,
shipping, and duties. Use this to preview refund amounts, taxes, and
processing fees before creating an actual refund.

Show fields

[Anchor to tags](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Order.fields.tags)tags

•[[String!]!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

A comma separated list of tags associated with the order. Updating `tags`
overwrites any existing tags that were previously added to the order. To add
new tags without overwriting existing tags, use the
[tagsAdd](https://shopify.dev/api/admin-graphql/latest/mutations/tagsadd)
mutation.

[Anchor to taxesIncluded](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Order.fields.taxesIncluded)taxesIncluded

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether taxes are included in the subtotal price of the order. When `true`,
the subtotal and line item prices include tax amounts. When `false`, taxes are
calculated and displayed separately.

[Anchor to taxExempt](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Order.fields.taxExempt)taxExempt

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether taxes are exempt on the order. Returns `true` for orders where the
customer or business has a valid tax exemption, such as non-profit
organizations or tax-free purchases. Use this to understand if tax
calculations were skipped during checkout.

[Anchor to taxLines](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Order.fields.taxLines)taxLines

•[[TaxLine!]!](/docs/api/admin-graphql/latest/objects/TaxLine)

non-null

    

A list of all tax lines applied to line items on the order, before returns.
Tax line prices represent the total price for all tax lines with the same
`rate` and `title`.

Show fields

[Anchor to test](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Order.fields.test)test

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether the order is a test. Test orders are made using the Shopify Bogus
Gateway or a payment provider with test mode enabled. A test order can't be
converted into a real order and vice versa.

[Anchor to totalCapturableSet](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Order.fields.totalCapturableSet)totalCapturableSet

•[MoneyBag!](/docs/api/admin-graphql/latest/objects/MoneyBag)

non-null

    

The authorized amount that's uncaptured or undercaptured, in shop and
presentment currencies. This amount isn't adjusted for returns.

Show fields

[Anchor to totalCashRoundingAdjustment](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Order.fields.totalCashRoundingAdjustment)totalCashRoundingAdjustment

•[CashRoundingAdjustment!](/docs/api/admin-
graphql/latest/objects/CashRoundingAdjustment)

non-null

    

The total rounding adjustment applied to payments or refunds for an order
involving cash payments. Applies to some countries where cash transactions are
rounded to the nearest currency denomination.

Show fields

[Anchor to totalDiscountsSet](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Order.fields.totalDiscountsSet)totalDiscountsSet

•[MoneyBag](/docs/api/admin-graphql/latest/objects/MoneyBag)

    

The total amount discounted on the order before returns, in shop and
presentment currencies. This includes both order and line level discounts.

Show fields

[Anchor to totalOutstandingSet](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Order.fields.totalOutstandingSet)totalOutstandingSet

•[MoneyBag!](/docs/api/admin-graphql/latest/objects/MoneyBag)

non-null

    

The total amount not yet transacted for the order, in shop and presentment
currencies. A positive value indicates a difference in the merchant's favor
(payment from customer to merchant) and a negative value indicates a
difference in the customer's favor (refund from merchant to customer).

Show fields

[Anchor to totalPriceSet](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Order.fields.totalPriceSet)totalPriceSet

•[MoneyBag!](/docs/api/admin-graphql/latest/objects/MoneyBag)

non-null

    

The total price of the order, before returns, in shop and presentment
currencies. This includes taxes and discounts.

Show fields

[Anchor to totalReceivedSet](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Order.fields.totalReceivedSet)totalReceivedSet

•[MoneyBag!](/docs/api/admin-graphql/latest/objects/MoneyBag)

non-null

    

The total amount received from the customer before returns, in shop and
presentment currencies.

Show fields

[Anchor to totalRefundedSet](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Order.fields.totalRefundedSet)totalRefundedSet

•[MoneyBag!](/docs/api/admin-graphql/latest/objects/MoneyBag)

non-null

    

The total amount that was refunded, in shop and presentment currencies.

Show fields

[Anchor to totalRefundedShippingSet](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Order.fields.totalRefundedShippingSet)totalRefundedShippingSet

•[MoneyBag!](/docs/api/admin-graphql/latest/objects/MoneyBag)

non-null

    

The total amount of shipping that was refunded, in shop and presentment
currencies.

Show fields

[Anchor to totalShippingPriceSet](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Order.fields.totalShippingPriceSet)totalShippingPriceSet

•[MoneyBag!](/docs/api/admin-graphql/latest/objects/MoneyBag)

non-null

    

The total shipping costs returned to the customer, in shop and presentment
currencies. This includes fees and any related discounts that were refunded.

Show fields

[Anchor to totalTaxSet](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Order.fields.totalTaxSet)totalTaxSet

•[MoneyBag](/docs/api/admin-graphql/latest/objects/MoneyBag)

    

The total tax amount before returns, in shop and presentment currencies.

Show fields

[Anchor to totalTipReceivedSet](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Order.fields.totalTipReceivedSet)totalTipReceivedSet

•[MoneyBag!](/docs/api/admin-graphql/latest/objects/MoneyBag)

non-null

    

The sum of all tip amounts for the order, in shop and presentment currencies.

Show fields

[Anchor to totalWeight](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Order.fields.totalWeight)totalWeight

•[UnsignedInt64](/docs/api/admin-graphql/latest/scalars/UnsignedInt64)

    

The total weight of the order before returns, in grams.

[Anchor to transactions](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Order.fields.transactions)transactions

•[[OrderTransaction!]!](/docs/api/admin-
graphql/latest/objects/OrderTransaction)

non-null

    

A list of transactions associated with the order.

Show fields

[Anchor to transactionsCount](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Order.fields.transactionsCount)transactionsCount

•[Count](/docs/api/admin-graphql/latest/objects/Count)

    

The number of transactions associated with the order.

Show fields

[Anchor to unpaid](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Order.fields.unpaid)unpaid

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether no payments have been made for the order.

[Anchor to updatedAt](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Order.fields.updatedAt)updatedAt

•[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime)

non-null

    

The date and time in [ISO 8601 format](https://en.wikipedia.org/wiki/ISO_8601)
when the order was last modified.

[Anchor to cartDiscountAmount](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Order.fields.cartDiscountAmount)cartDiscountAmount

•[Money](/docs/api/admin-graphql/latest/scalars/Money)

Deprecated

    

[Anchor to channel](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Order.fields.channel)channel

•[Channel](/docs/api/admin-graphql/latest/objects/Channel)

Deprecated

    

Show fields

[Anchor to customerJourney](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Order.fields.customerJourney)customerJourney

•[CustomerJourney](/docs/api/admin-graphql/latest/objects/CustomerJourney)

Deprecated

    

Show fields

[Anchor to landingPageDisplayText](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Order.fields.landingPageDisplayText)landingPageDisplayText

•[String](/docs/api/admin-graphql/latest/scalars/String)

Deprecated

    

[Anchor to landingPageUrl](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Order.fields.landingPageUrl)landingPageUrl

•[URL](/docs/api/admin-graphql/latest/scalars/URL)

Deprecated

    

[Anchor to localizationExtensions](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Order.fields.localizationExtensions)localizationExtensions

•[LocalizationExtensionConnection!](/docs/api/admin-
graphql/latest/connections/LocalizationExtensionConnection)

non-nullDeprecated

    

Show fields

[Anchor to metafieldDefinitions](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Order.fields.metafieldDefinitions)metafieldDefinitions

•[MetafieldDefinitionConnection!](/docs/api/admin-
graphql/latest/connections/MetafieldDefinitionConnection)

non-nullDeprecated

    

Show fields

[Anchor to netPayment](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Order.fields.netPayment)netPayment

•[Money!](/docs/api/admin-graphql/latest/scalars/Money)

non-nullDeprecated

    

[Anchor to physicalLocation](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Order.fields.physicalLocation)physicalLocation

•[Location](/docs/api/admin-graphql/latest/objects/Location)

Deprecated

    

Show fields

[Anchor to referralCode](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Order.fields.referralCode)referralCode

•[String](/docs/api/admin-graphql/latest/scalars/String)

Deprecated

    

[Anchor to referrerDisplayText](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Order.fields.referrerDisplayText)referrerDisplayText

•[String](/docs/api/admin-graphql/latest/scalars/String)

Deprecated

    

[Anchor to referrerUrl](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Order.fields.referrerUrl)referrerUrl

•[URL](/docs/api/admin-graphql/latest/scalars/URL)

Deprecated

    

[Anchor to riskLevel](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Order.fields.riskLevel)riskLevel

•[OrderRiskLevel!](/docs/api/admin-graphql/latest/enums/OrderRiskLevel)

non-nullDeprecated

    

Show enum values

[Anchor to risks](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Order.fields.risks)risks

•[[OrderRisk!]!](/docs/api/admin-graphql/latest/objects/OrderRisk)

non-nullDeprecated

    

Show fields

[Anchor to subtotalPrice](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Order.fields.subtotalPrice)subtotalPrice

•[Money](/docs/api/admin-graphql/latest/scalars/Money)

Deprecated

    

[Anchor to totalCapturable](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Order.fields.totalCapturable)totalCapturable

•[Money!](/docs/api/admin-graphql/latest/scalars/Money)

non-nullDeprecated

    

[Anchor to totalDiscounts](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Order.fields.totalDiscounts)totalDiscounts

•[Money](/docs/api/admin-graphql/latest/scalars/Money)

Deprecated

    

[Anchor to totalPrice](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Order.fields.totalPrice)totalPrice

•[Money!](/docs/api/admin-graphql/latest/scalars/Money)

non-nullDeprecated

    

[Anchor to totalReceived](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Order.fields.totalReceived)totalReceived

•[Money!](/docs/api/admin-graphql/latest/scalars/Money)

non-nullDeprecated

    

[Anchor to totalRefunded](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Order.fields.totalRefunded)totalRefunded

•[Money!](/docs/api/admin-graphql/latest/scalars/Money)

non-nullDeprecated

    

[Anchor to totalShippingPrice](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Order.fields.totalShippingPrice)totalShippingPrice

•[Money!](/docs/api/admin-graphql/latest/scalars/Money)

non-nullDeprecated

    

[Anchor to totalTax](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Order.fields.totalTax)totalTax

•[Money](/docs/api/admin-graphql/latest/scalars/Money)

Deprecated

    

[Anchor to totalTipReceived](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Order.fields.totalTipReceived)totalTipReceived

•[MoneyV2!](/docs/api/admin-graphql/latest/objects/MoneyV2)

non-nullDeprecated

    

Show fields

[Anchor to OrderAdjustment](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
OrderAdjustment)[OrderAdjustment](/docs/api/admin-
graphql/latest/objects/OrderAdjustment)

•OBJECT

    

An order adjustment accounts for the difference between a calculated and
actual refund amount.

Show fields

[Anchor to amountSet](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-OrderAdjustment.fields.amountSet)amountSet

•[MoneyBag!](/docs/api/admin-graphql/latest/objects/MoneyBag)

non-null

    

The amount of the order adjustment in shop and presentment currencies.

Show fields

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
OrderAdjustment.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to reason](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-OrderAdjustment.fields.reason)reason

•[OrderAdjustmentDiscrepancyReason](/docs/api/admin-
graphql/latest/enums/OrderAdjustmentDiscrepancyReason)

    

An optional reason that explains a discrepancy between calculated and actual
refund amounts.

Show enum values

[Anchor to taxAmountSet](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
OrderAdjustment.fields.taxAmountSet)taxAmountSet

•[MoneyBag!](/docs/api/admin-graphql/latest/objects/MoneyBag)

non-null

    

The tax amount of the order adjustment in shop and presentment currencies.

Show fields

[Anchor to OrderDisputeSummary](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
OrderDisputeSummary)[OrderDisputeSummary](/docs/api/admin-
graphql/latest/objects/OrderDisputeSummary)

•OBJECT

    

A summary of the important details for a dispute on an order.

Show fields

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
OrderDisputeSummary.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to initiatedAs](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
OrderDisputeSummary.fields.initiatedAs)initiatedAs

•[DisputeType!](/docs/api/admin-graphql/latest/enums/DisputeType)

non-null

    

The type that the dispute was initiated as.

Show enum values

[Anchor to status](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-OrderDisputeSummary.fields.status)status

•[DisputeStatus!](/docs/api/admin-graphql/latest/enums/DisputeStatus)

non-null

    

The current status of the dispute.

Show enum values

[Anchor to OrderEditSession](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
OrderEditSession)[OrderEditSession](/docs/api/admin-
graphql/latest/objects/OrderEditSession)

•OBJECT

    

An edit session for an order.

Show fields

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
OrderEditSession.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

The unique ID of the order edit session.

[Anchor to OrderTransaction](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
OrderTransaction)[OrderTransaction](/docs/api/admin-
graphql/latest/objects/OrderTransaction)

•OBJECT

    

The `OrderTransaction` object represents a payment transaction that's
associated with an order. An order transaction is a specific action or event
that happens within the context of an order, such as a customer paying for a
purchase or receiving a refund, or other payment-related activity.

Use the `OrderTransaction` object to capture the complete lifecycle of a
payment, from initial authorization to final settlement, including refunds and
currency exchanges. Common use cases for using the `OrderTransaction` object
include:

  * Processing new payments for orders
  * Managing payment authorizations and captures
  * Processing refunds for returned items
  * Tracking payment status and errors
  * Managing multi-currency transactions
  * Handling payment gateway integrations

Each `OrderTransaction` object has a
[`kind`](https://shopify.dev/docs/api/admin-
graphql/latest/enums/OrderTransactionKind) that defines the type of
transaction and a [`status`](https://shopify.dev/docs/api/admin-
graphql/latest/enums/OrderTransactionStatus) that indicates the current state
of the transaction. The object stores detailed information about payment
methods, gateway processing, and settlement details.

Learn more about [payment
processing](https://help.shopify.com/manual/payments) and [payment gateway
integrations](https://www.shopify.com/ca/payment-gateways).

Show fields

[Anchor to accountNumber](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
OrderTransaction.fields.accountNumber)accountNumber

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The masked account number associated with the payment method.

[Anchor to amountRoundingSet](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
OrderTransaction.fields.amountRoundingSet)amountRoundingSet

•[MoneyBag](/docs/api/admin-graphql/latest/objects/MoneyBag)

    

The rounding adjustment applied on the cash amount in shop and presentment
currencies.

Show fields

[Anchor to amountSet](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-OrderTransaction.fields.amountSet)amountSet

•[MoneyBag!](/docs/api/admin-graphql/latest/objects/MoneyBag)

non-null

    

The amount and currency of the transaction in shop and presentment currencies.

Show fields

[Anchor to authorizationCode](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
OrderTransaction.fields.authorizationCode)authorizationCode

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

Authorization code associated with the transaction.

[Anchor to authorizationExpiresAt](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
OrderTransaction.fields.authorizationExpiresAt)authorizationExpiresAt

•[DateTime](/docs/api/admin-graphql/latest/scalars/DateTime)

    

The time when the authorization expires. This field is available only to
stores on a Shopify Plus plan.

[Anchor to createdAt](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-OrderTransaction.fields.createdAt)createdAt

•[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime)

non-null

    

Date and time when the transaction was created.

[Anchor to currencyExchangeAdjustment](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
OrderTransaction.fields.currencyExchangeAdjustment)currencyExchangeAdjustment

•[CurrencyExchangeAdjustment](/docs/api/admin-
graphql/latest/objects/CurrencyExchangeAdjustment)

    

An adjustment on the transaction showing the amount lost or gained due to
fluctuations in the currency exchange rate.

Show fields

[Anchor to device](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-OrderTransaction.fields.device)device

•[PointOfSaleDevice](/docs/api/admin-graphql/latest/objects/PointOfSaleDevice)

    

The Shopify Point of Sale device used to process the transaction.

Show fields

[Anchor to errorCode](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-OrderTransaction.fields.errorCode)errorCode

•[OrderTransactionErrorCode](/docs/api/admin-
graphql/latest/enums/OrderTransactionErrorCode)

    

A standardized error code, independent of the payment provider.

Show enum values

[Anchor to fees](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-OrderTransaction.fields.fees)fees

•[[TransactionFee!]!](/docs/api/admin-graphql/latest/objects/TransactionFee)

non-null

    

The transaction fees charged on the order transaction. Only present for
Shopify Payments transactions.

Show fields

[Anchor to formattedGateway](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
OrderTransaction.fields.formattedGateway)formattedGateway

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The human-readable payment gateway name used to process the transaction.

[Anchor to gateway](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-OrderTransaction.fields.gateway)gateway

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The payment gateway used to process the transaction.

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
OrderTransaction.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to kind](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-OrderTransaction.fields.kind)kind

•[OrderTransactionKind!](/docs/api/admin-
graphql/latest/enums/OrderTransactionKind)

non-null

    

The kind of transaction.

Show enum values

[Anchor to location](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-OrderTransaction.fields.location)location

•[Location](/docs/api/admin-graphql/latest/objects/Location)

    

The physical location where the transaction was processed.

Show fields

[Anchor to manuallyCapturable](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
OrderTransaction.fields.manuallyCapturable)manuallyCapturable

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether the transaction can be manually captured.

[Anchor to manualPaymentGateway](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
OrderTransaction.fields.manualPaymentGateway)manualPaymentGateway

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether the transaction is processed by manual payment gateway.

[Anchor to maximumRefundableV2](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
OrderTransaction.fields.maximumRefundableV2)maximumRefundableV2

•[MoneyV2](/docs/api/admin-graphql/latest/objects/MoneyV2)

    

Specifies the available amount with currency to refund on the gateway. This
value is only available for transactions of type `SuggestedRefund`.

Show fields

[Anchor to multiCapturable](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
OrderTransaction.fields.multiCapturable)multiCapturable

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether the transaction can be captured multiple times.

[Anchor to order](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-OrderTransaction.fields.order)order

•[Order](/docs/api/admin-graphql/latest/objects/Order)

    

The associated order.

Show fields

[Anchor to parentTransaction](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
OrderTransaction.fields.parentTransaction)parentTransaction

•[OrderTransaction](/docs/api/admin-graphql/latest/objects/OrderTransaction)

    

The associated parent transaction, for example the authorization of a capture.

Show fields

[Anchor to paymentDetails](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
OrderTransaction.fields.paymentDetails)paymentDetails

•[PaymentDetails](/docs/api/admin-graphql/latest/unions/PaymentDetails)

    

The payment details for the transaction.

Show union types

[Anchor to paymentIcon](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
OrderTransaction.fields.paymentIcon)paymentIcon

•[Image](/docs/api/admin-graphql/latest/objects/Image)

    

The payment icon to display for the transaction.

Show fields

[Anchor to paymentId](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-OrderTransaction.fields.paymentId)paymentId

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The payment ID associated with the transaction.

[Anchor to processedAt](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
OrderTransaction.fields.processedAt)processedAt

•[DateTime](/docs/api/admin-graphql/latest/scalars/DateTime)

    

Date and time when the transaction was processed.

[Anchor to receiptJson](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
OrderTransaction.fields.receiptJson)receiptJson

•[JSON](/docs/api/admin-graphql/latest/scalars/JSON)

    

The transaction receipt that the payment gateway attaches to the transaction.
The value of this field depends on which payment gateway processed the
transaction.

[Anchor to settlementCurrency](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
OrderTransaction.fields.settlementCurrency)settlementCurrency

•[CurrencyCode](/docs/api/admin-graphql/latest/enums/CurrencyCode)

    

The settlement currency.

Show enum values

[Anchor to settlementCurrencyRate](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
OrderTransaction.fields.settlementCurrencyRate)settlementCurrencyRate

•[Decimal](/docs/api/admin-graphql/latest/scalars/Decimal)

    

The rate used when converting the transaction amount to settlement currency.

[Anchor to shopifyPaymentsSet](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
OrderTransaction.fields.shopifyPaymentsSet)shopifyPaymentsSet

•[ShopifyPaymentsTransactionSet](/docs/api/admin-
graphql/latest/objects/ShopifyPaymentsTransactionSet)

    

Contains all Shopify Payments information related to an order transaction.
This field is available only to stores on a Shopify Plus plan.

Show fields

[Anchor to status](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-OrderTransaction.fields.status)status

•[OrderTransactionStatus!](/docs/api/admin-
graphql/latest/enums/OrderTransactionStatus)

non-null

    

The status of this transaction.

Show enum values

[Anchor to test](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-OrderTransaction.fields.test)test

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether the transaction is a test transaction.

[Anchor to totalUnsettledSet](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
OrderTransaction.fields.totalUnsettledSet)totalUnsettledSet

•[MoneyBag](/docs/api/admin-graphql/latest/objects/MoneyBag)

    

Specifies the available amount with currency to capture on the gateway in shop
and presentment currencies. Only available when an amount is capturable or
manually mark as paid.

Show fields

[Anchor to user](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-OrderTransaction.fields.user)user

•[StaffMember](/docs/api/admin-graphql/latest/objects/StaffMember)

    

Staff member who was logged into the Shopify POS device when the transaction
was processed.

Show fields

[Anchor to amount](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-OrderTransaction.fields.amount)amount

•[Money!](/docs/api/admin-graphql/latest/scalars/Money)

non-nullDeprecated

    

[Anchor to amountV2](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-OrderTransaction.fields.amountV2)amountV2

•[MoneyV2!](/docs/api/admin-graphql/latest/objects/MoneyV2)

non-nullDeprecated

    

Show fields

[Anchor to maximumRefundable](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
OrderTransaction.fields.maximumRefundable)maximumRefundable

•[Money](/docs/api/admin-graphql/latest/scalars/Money)

Deprecated

    

[Anchor to paymentMethod](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
OrderTransaction.fields.paymentMethod)paymentMethod

•[PaymentMethods](/docs/api/admin-graphql/latest/enums/PaymentMethods)

Deprecated

    

Show enum values

[Anchor to totalUnsettled](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
OrderTransaction.fields.totalUnsettled)totalUnsettled

•[Money](/docs/api/admin-graphql/latest/scalars/Money)

Deprecated

    

[Anchor to totalUnsettledV2](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
OrderTransaction.fields.totalUnsettledV2)totalUnsettledV2

•[MoneyV2](/docs/api/admin-graphql/latest/objects/MoneyV2)

Deprecated

    

Show fields

[Anchor to Page](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Page)[Page](/docs/api/admin-graphql/latest/objects/Page)

•OBJECT

    

A page on the Online Store.

Show fields

[Anchor to body](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Page.fields.body)body

•[HTML!](/docs/api/admin-graphql/latest/scalars/HTML)

non-null

    

The text content of the page, complete with HTML markup.

[Anchor to bodySummary](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Page.fields.bodySummary)bodySummary

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The first 150 characters of the page body. If the page body contains more than
150 characters, additional characters are truncated by ellipses.

[Anchor to createdAt](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Page.fields.createdAt)createdAt

•[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime)

non-null

    

The date and time (ISO 8601 format) of the page creation.

[Anchor to defaultCursor](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Page.fields.defaultCursor)defaultCursor

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

A default [cursor](https://shopify.dev/api/usage/pagination-graphql) that
returns the single next record, sorted ascending by ID.

[Anchor to events](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Page.fields.events)events

•[EventConnection!](/docs/api/admin-
graphql/latest/connections/EventConnection)

non-null

    

The paginated list of events associated with the host subject.

Show fields

[Anchor to handle](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Page.fields.handle)handle

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

A unique, human-friendly string for the page. In themes, the Liquid templating
language refers to a page by its handle.

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
Page.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to isPublished](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Page.fields.isPublished)isPublished

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether or not the page is visible.

[Anchor to metafield](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Page.fields.metafield)metafield

•[Metafield](/docs/api/admin-graphql/latest/objects/Metafield)

    

A [custom field](https://shopify.dev/docs/apps/build/custom-data), including
its `namespace` and `key`, that's associated with a Shopify resource for the
purposes of adding and storing additional information.

Show fields

[Anchor to metafields](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Page.fields.metafields)metafields

•[MetafieldConnection!](/docs/api/admin-
graphql/latest/connections/MetafieldConnection)

non-null

    

A list of [custom fields](https://shopify.dev/docs/apps/build/custom-data)
that a merchant associates with a Shopify resource.

Show fields

[Anchor to publishedAt](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Page.fields.publishedAt)publishedAt

•[DateTime](/docs/api/admin-graphql/latest/scalars/DateTime)

    

The date and time (ISO 8601 format) when the page became or will become
visible. Returns null when the page isn't visible.

[Anchor to templateSuffix](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Page.fields.templateSuffix)templateSuffix

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The suffix of the template that's used to render the page.

[Anchor to title](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Page.fields.title)title

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

Title of the page.

[Anchor to translations](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Page.fields.translations)translations

•[[Translation!]!](/docs/api/admin-graphql/latest/objects/Translation)

non-null

    

The published translations associated with the resource.

Show fields

[Anchor to updatedAt](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Page.fields.updatedAt)updatedAt

•[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime)

non-null

    

The date and time (ISO 8601 format) of the latest page update.

[Anchor to metafieldDefinitions](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Page.fields.metafieldDefinitions)metafieldDefinitions

•[MetafieldDefinitionConnection!](/docs/api/admin-
graphql/latest/connections/MetafieldDefinitionConnection)

non-nullDeprecated

    

Show fields

[Anchor to PaymentCustomization](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
PaymentCustomization)[PaymentCustomization](/docs/api/admin-
graphql/latest/objects/PaymentCustomization)

•OBJECT

    

A payment customization.

Show fields

[Anchor to enabled](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-PaymentCustomization.fields.enabled)enabled

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

The enabled status of the payment customization.

[Anchor to errorHistory](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
PaymentCustomization.fields.errorHistory)errorHistory

•[FunctionsErrorHistory](/docs/api/admin-
graphql/latest/objects/FunctionsErrorHistory)

    

The error history on the most recent version of the payment customization.

Show fields

[Anchor to functionId](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
PaymentCustomization.fields.functionId)functionId

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The ID of the Shopify Function implementing the payment customization.

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
PaymentCustomization.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to metafield](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-PaymentCustomization.fields.metafield)metafield

•[Metafield](/docs/api/admin-graphql/latest/objects/Metafield)

    

A [custom field](https://shopify.dev/docs/apps/build/custom-data), including
its `namespace` and `key`, that's associated with a Shopify resource for the
purposes of adding and storing additional information.

Show fields

[Anchor to metafields](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
PaymentCustomization.fields.metafields)metafields

•[MetafieldConnection!](/docs/api/admin-
graphql/latest/connections/MetafieldConnection)

non-null

    

A list of [custom fields](https://shopify.dev/docs/apps/build/custom-data)
that a merchant associates with a Shopify resource.

Show fields

[Anchor to shopifyFunction](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
PaymentCustomization.fields.shopifyFunction)shopifyFunction

•[ShopifyFunction!](/docs/api/admin-graphql/latest/objects/ShopifyFunction)

non-null

    

The Shopify Function implementing the payment customization.

Show fields

[Anchor to title](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-PaymentCustomization.fields.title)title

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The title of the payment customization.

[Anchor to metafieldDefinitions](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
PaymentCustomization.fields.metafieldDefinitions)metafieldDefinitions

•[MetafieldDefinitionConnection!](/docs/api/admin-
graphql/latest/connections/MetafieldDefinitionConnection)

non-nullDeprecated

    

Show fields

[Anchor to PaymentMandate](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
PaymentMandate)[PaymentMandate](/docs/api/admin-
graphql/latest/objects/PaymentMandate)

•OBJECT

    

A payment instrument and the permission the owner of the instrument gives to
the merchant to debit it.

Show fields

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
PaymentMandate.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

The unique ID of a payment mandate.

[Anchor to paymentInstrument](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
PaymentMandate.fields.paymentInstrument)paymentInstrument

•[PaymentInstrument!](/docs/api/admin-graphql/latest/unions/PaymentInstrument)

non-null

    

The outputs details of the payment instrument.

Show union types

[Anchor to PaymentSchedule](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
PaymentSchedule)[PaymentSchedule](/docs/api/admin-
graphql/latest/objects/PaymentSchedule)

•OBJECT

    

Represents the payment schedule for a single payment defined in the payment
terms.

Show fields

[Anchor to balanceDue](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
PaymentSchedule.fields.balanceDue)balanceDue

•[MoneyV2!](/docs/api/admin-graphql/latest/objects/MoneyV2)

non-null

    

Remaining balance to be captured for this payment schedule.

Show fields

[Anchor to completedAt](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
PaymentSchedule.fields.completedAt)completedAt

•[DateTime](/docs/api/admin-graphql/latest/scalars/DateTime)

    

Date and time when the payment schedule is paid or fulfilled.

[Anchor to due](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
PaymentSchedule.fields.due)due

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether the payment schedule is due.

[Anchor to dueAt](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-PaymentSchedule.fields.dueAt)dueAt

•[DateTime](/docs/api/admin-graphql/latest/scalars/DateTime)

    

Date and time when the payment schedule is due.

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
PaymentSchedule.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to issuedAt](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-PaymentSchedule.fields.issuedAt)issuedAt

•[DateTime](/docs/api/admin-graphql/latest/scalars/DateTime)

    

Date and time when the invoice is sent.

[Anchor to paymentTerms](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
PaymentSchedule.fields.paymentTerms)paymentTerms

•[PaymentTerms!](/docs/api/admin-graphql/latest/objects/PaymentTerms)

non-null

    

The payment terms the payment schedule belongs to.

Show fields

[Anchor to totalBalance](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
PaymentSchedule.fields.totalBalance)totalBalance

•[MoneyV2!](/docs/api/admin-graphql/latest/objects/MoneyV2)

non-null

    

Remaining balance to be paid or authorized by the customer for this payment
schedule.

Show fields

[Anchor to amount](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-PaymentSchedule.fields.amount)amount

•[MoneyV2!](/docs/api/admin-graphql/latest/objects/MoneyV2)

non-nullDeprecated

    

Show fields

[Anchor to PaymentTerms](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
PaymentTerms)[PaymentTerms](/docs/api/admin-
graphql/latest/objects/PaymentTerms)

•OBJECT

    

Represents the payment terms for an order or draft order.

Show fields

[Anchor to draftOrder](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
PaymentTerms.fields.draftOrder)draftOrder

•[DraftOrder](/docs/api/admin-graphql/latest/objects/DraftOrder)

    

The draft order associated with the payment terms.

Show fields

[Anchor to due](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
PaymentTerms.fields.due)due

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether payment terms have a payment schedule that's due.

[Anchor to dueInDays](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-PaymentTerms.fields.dueInDays)dueInDays

•[Int](/docs/api/admin-graphql/latest/scalars/Int)

    

Duration of payment terms in days based on the payment terms template used to
create the payment terms.

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
PaymentTerms.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to order](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-PaymentTerms.fields.order)order

•[Order](/docs/api/admin-graphql/latest/objects/Order)

    

The order associated with the payment terms.

Show fields

[Anchor to overdue](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-PaymentTerms.fields.overdue)overdue

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether the payment terms have overdue payment schedules.

[Anchor to paymentSchedules](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
PaymentTerms.fields.paymentSchedules)paymentSchedules

•[PaymentScheduleConnection!](/docs/api/admin-
graphql/latest/connections/PaymentScheduleConnection)

non-null

    

List of schedules for the payment terms.

Show fields

[Anchor to paymentTermsName](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
PaymentTerms.fields.paymentTermsName)paymentTermsName

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The name of the payment terms template used to create the payment terms.

[Anchor to paymentTermsType](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
PaymentTerms.fields.paymentTermsType)paymentTermsType

•[PaymentTermsType!](/docs/api/admin-graphql/latest/enums/PaymentTermsType)

non-null

    

The payment terms template type used to create the payment terms.

Show enum values

[Anchor to translatedName](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
PaymentTerms.fields.translatedName)translatedName

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The payment terms name, translated into the shop admin's preferred language.

[Anchor to PaymentTermsTemplate](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
PaymentTermsTemplate)[PaymentTermsTemplate](/docs/api/admin-
graphql/latest/objects/PaymentTermsTemplate)

•OBJECT

    

Represents the payment terms template object.

Show fields

[Anchor to description](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
PaymentTermsTemplate.fields.description)description

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The description of the payment terms template.

[Anchor to dueInDays](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-PaymentTermsTemplate.fields.dueInDays)dueInDays

•[Int](/docs/api/admin-graphql/latest/scalars/Int)

    

The number of days between the issued date and due date if this is the net
type of payment terms.

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
PaymentTermsTemplate.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to name](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-PaymentTermsTemplate.fields.name)name

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The name of the payment terms template.

[Anchor to paymentTermsType](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
PaymentTermsTemplate.fields.paymentTermsType)paymentTermsType

•[PaymentTermsType!](/docs/api/admin-graphql/latest/enums/PaymentTermsType)

non-null

    

The type of the payment terms template.

Show enum values

[Anchor to translatedName](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
PaymentTermsTemplate.fields.translatedName)translatedName

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The translated payment terms template name.

[Anchor to PointOfSaleDevice](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
PointOfSaleDevice)[PointOfSaleDevice](/docs/api/admin-
graphql/latest/objects/PointOfSaleDevice)

•OBJECT

    

Represents a mobile device that Shopify Point of Sale has been installed on.

Show fields

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
PointOfSaleDevice.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to PriceList](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-PriceList)[PriceList](/docs/api/admin-graphql/latest/objects/PriceList)

•OBJECT

    

Represents a price list, including information about related prices and
eligibility rules. You can use price lists to specify either fixed prices or
adjusted relative prices that override initial product variant prices. Price
lists are applied to customers using context rules, which determine price list
eligibility.

For more information on price lists, refer to [Support different pricing
models](https://shopify.dev/apps/internationalization/product-price-lists).

Show fields

[Anchor to catalog](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-PriceList.fields.catalog)catalog

•[Catalog](/docs/api/admin-graphql/latest/interfaces/Catalog)

    

The catalog that the price list is associated with.

Show fields

[Anchor to currency](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-PriceList.fields.currency)currency

•[CurrencyCode!](/docs/api/admin-graphql/latest/enums/CurrencyCode)

non-null

    

The currency for fixed prices associated with this price list.

Show enum values

[Anchor to fixedPricesCount](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
PriceList.fields.fixedPricesCount)fixedPricesCount

•[Int!](/docs/api/admin-graphql/latest/scalars/Int)

non-null

    

The number of fixed prices on the price list.

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
PriceList.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to name](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-PriceList.fields.name)name

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The unique name of the price list, used as a human-readable identifier.

[Anchor to parent](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-PriceList.fields.parent)parent

•[PriceListParent](/docs/api/admin-graphql/latest/objects/PriceListParent)

    

Relative adjustments to other prices.

Show fields

[Anchor to prices](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-PriceList.fields.prices)prices

•[PriceListPriceConnection!](/docs/api/admin-
graphql/latest/connections/PriceListPriceConnection)

non-null

    

A list of prices associated with the price list.

Show fields

[Anchor to quantityRules](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
PriceList.fields.quantityRules)quantityRules

•[QuantityRuleConnection!](/docs/api/admin-
graphql/latest/connections/QuantityRuleConnection)

non-null

    

A list of quantity rules associated with the price list, ordered by product
variants.

Show fields

[Anchor to PriceRule](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-PriceRule)[PriceRule](/docs/api/admin-graphql/latest/objects/PriceRule)

•OBJECT

    

Price rules are a set of conditions, including entitlements and prerequisites,
that must be met in order for a discount code to apply.

We recommend using the types and queries detailed at [Getting started with
discounts](https://shopify.dev/docs/apps/selling-strategies/discounts/getting-
started) instead. These will replace the GraphQL `PriceRule` object and REST
Admin `PriceRule` and `DiscountCode` resources.

Show fields

[Anchor to allocationLimit](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
PriceRule.fields.allocationLimit)allocationLimit

•[Int](/docs/api/admin-graphql/latest/scalars/Int)

    

The maximum number of times that the price rule can be allocated onto an
order.

[Anchor to allocationMethod](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
PriceRule.fields.allocationMethod)allocationMethod

•[PriceRuleAllocationMethod!](/docs/api/admin-
graphql/latest/enums/PriceRuleAllocationMethod)

non-null

    

The method by which the price rule's value is allocated to its entitled items.

Show enum values

[Anchor to app](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
PriceRule.fields.app)app

•[App](/docs/api/admin-graphql/latest/objects/App)

    

The application that created the price rule.

Show fields

[Anchor to combinesWith](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
PriceRule.fields.combinesWith)combinesWith

•[DiscountCombinesWith!](/docs/api/admin-
graphql/latest/objects/DiscountCombinesWith)

non-null

    

The [discount classes](https://help.shopify.com/manual/discounts/combining-
discounts/discount-combinations) that you can use in combination with [Shopify
discount types](https://help.shopify.com/manual/discounts/discount-types).

Show fields

[Anchor to createdAt](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-PriceRule.fields.createdAt)createdAt

•[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime)

non-null

    

The date and time when the price rule was created.

[Anchor to customerSelection](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
PriceRule.fields.customerSelection)customerSelection

•[PriceRuleCustomerSelection!](/docs/api/admin-
graphql/latest/objects/PriceRuleCustomerSelection)

non-null

    

The customers that can use this price rule.

Show fields

[Anchor to discountClasses](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
PriceRule.fields.discountClasses)discountClasses

•[[DiscountClass!]!](/docs/api/admin-graphql/latest/enums/DiscountClass)

non-null

    

The classes of the discount.

Show enum values

[Anchor to discountCodes](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
PriceRule.fields.discountCodes)discountCodes

•[PriceRuleDiscountCodeConnection!](/docs/api/admin-
graphql/latest/connections/PriceRuleDiscountCodeConnection)

non-null

    

List of the price rule's discount codes.

Show fields

[Anchor to discountCodesCount](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
PriceRule.fields.discountCodesCount)discountCodesCount

•[Count](/docs/api/admin-graphql/latest/objects/Count)

    

How many discount codes associated with the price rule.

Show fields

[Anchor to endsAt](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-PriceRule.fields.endsAt)endsAt

•[DateTime](/docs/api/admin-graphql/latest/scalars/DateTime)

    

The date and time when the price rule ends. For open-ended price rules, use
`null`.

[Anchor to events](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-PriceRule.fields.events)events

•[EventConnection!](/docs/api/admin-
graphql/latest/connections/EventConnection)

non-null

    

The paginated list of events associated with the price rule.

Show fields

[Anchor to features](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-PriceRule.fields.features)features

•[[PriceRuleFeature!]!](/docs/api/admin-graphql/latest/enums/PriceRuleFeature)

non-null

    

A list of the price rule's features.

Show enum values

[Anchor to hasTimelineComment](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
PriceRule.fields.hasTimelineComment)hasTimelineComment

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Indicates whether there are any timeline comments on the price rule.

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
PriceRule.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to itemEntitlements](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
PriceRule.fields.itemEntitlements)itemEntitlements

•[PriceRuleItemEntitlements!](/docs/api/admin-
graphql/latest/objects/PriceRuleItemEntitlements)

non-null

    

The items to which the price rule applies.

Show fields

[Anchor to itemPrerequisites](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
PriceRule.fields.itemPrerequisites)itemPrerequisites

•[PriceRuleLineItemPrerequisites!](/docs/api/admin-
graphql/latest/objects/PriceRuleLineItemPrerequisites)

non-null

    

The items required for the price rule to be applicable.

Show fields

[Anchor to legacyResourceId](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
PriceRule.fields.legacyResourceId)legacyResourceId

•[UnsignedInt64!](/docs/api/admin-graphql/latest/scalars/UnsignedInt64)

non-null

    

The ID of the corresponding resource in the REST Admin API.

[Anchor to oncePerCustomer](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
PriceRule.fields.oncePerCustomer)oncePerCustomer

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether the price rule can be applied only once per customer.

[Anchor to prerequisiteQuantityRange](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
PriceRule.fields.prerequisiteQuantityRange)prerequisiteQuantityRange

•[PriceRuleQuantityRange](/docs/api/admin-
graphql/latest/objects/PriceRuleQuantityRange)

    

The number of the entitled items must fall within this range for the price
rule to be applicable.

Show fields

[Anchor to prerequisiteShippingPriceRange](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
PriceRule.fields.prerequisiteShippingPriceRange)prerequisiteShippingPriceRange

•[PriceRuleMoneyRange](/docs/api/admin-
graphql/latest/objects/PriceRuleMoneyRange)

    

The shipping cost must fall within this range for the price rule to be
applicable.

Show fields

[Anchor to prerequisiteSubtotalRange](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
PriceRule.fields.prerequisiteSubtotalRange)prerequisiteSubtotalRange

•[PriceRuleMoneyRange](/docs/api/admin-
graphql/latest/objects/PriceRuleMoneyRange)

    

The sum of the entitled items subtotal prices must fall within this range for
the price rule to be applicable.

Show fields

[Anchor to prerequisiteToEntitlementQuantityRatio](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
PriceRule.fields.prerequisiteToEntitlementQuantityRatio)prerequisiteToEntitlementQuantityRatio

•[PriceRulePrerequisiteToEntitlementQuantityRatio](/docs/api/admin-
graphql/latest/objects/PriceRulePrerequisiteToEntitlementQuantityRatio)

    

Quantity of prerequisite items required for the price rule to be applicable,
compared to quantity of entitled items.

Show fields

[Anchor to shareableUrls](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
PriceRule.fields.shareableUrls)shareableUrls

•[[PriceRuleShareableUrl!]!](/docs/api/admin-
graphql/latest/objects/PriceRuleShareableUrl)

non-null

    

URLs that can be used to share the discount.

Show fields

[Anchor to shippingEntitlements](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
PriceRule.fields.shippingEntitlements)shippingEntitlements

•[PriceRuleShippingLineEntitlements!](/docs/api/admin-
graphql/latest/objects/PriceRuleShippingLineEntitlements)

non-null

    

The shipping lines to which the price rule applies.

Show fields

[Anchor to startsAt](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-PriceRule.fields.startsAt)startsAt

•[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime)

non-null

    

The date and time when the price rule starts.

[Anchor to status](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-PriceRule.fields.status)status

•[PriceRuleStatus!](/docs/api/admin-graphql/latest/enums/PriceRuleStatus)

non-null

    

The status of the price rule.

Show enum values

[Anchor to summary](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-PriceRule.fields.summary)summary

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

A detailed summary of the price rule.

[Anchor to target](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-PriceRule.fields.target)target

•[PriceRuleTarget!](/docs/api/admin-graphql/latest/enums/PriceRuleTarget)

non-null

    

The type of lines (line_item or shipping_line) to which the price rule
applies.

Show enum values

[Anchor to title](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-PriceRule.fields.title)title

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The title of the price rule.

[Anchor to totalSales](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
PriceRule.fields.totalSales)totalSales

•[MoneyV2](/docs/api/admin-graphql/latest/objects/MoneyV2)

    

The total sales from orders where the price rule was used.

Show fields

[Anchor to usageCount](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
PriceRule.fields.usageCount)usageCount

•[Int!](/docs/api/admin-graphql/latest/scalars/Int)

non-null

    

The number of times that the price rule has been used. This value is updated
asynchronously and can be different than the actual usage count.

[Anchor to usageLimit](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
PriceRule.fields.usageLimit)usageLimit

•[Int](/docs/api/admin-graphql/latest/scalars/Int)

    

The maximum number of times that the price rule can be used in total.

[Anchor to validityPeriod](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
PriceRule.fields.validityPeriod)validityPeriod

•[PriceRuleValidityPeriod!](/docs/api/admin-
graphql/latest/objects/PriceRuleValidityPeriod)

non-null

    

A time period during which a price rule is applicable.

Show fields

[Anchor to valueV2](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-PriceRule.fields.valueV2)valueV2

•[PricingValue!](/docs/api/admin-graphql/latest/unions/PricingValue)

non-null

    

The value of the price rule.

Show union types

[Anchor to discountClass](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
PriceRule.fields.discountClass)discountClass

•[DiscountClass!](/docs/api/admin-graphql/latest/enums/DiscountClass)

non-nullDeprecated

    

Show enum values

[Anchor to entitlementToPrerequisiteQuantityRatio](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
PriceRule.fields.entitlementToPrerequisiteQuantityRatio)entitlementToPrerequisiteQuantityRatio

•[PriceRuleEntitlementToPrerequisiteQuantityRatio](/docs/api/admin-
graphql/latest/objects/PriceRuleEntitlementToPrerequisiteQuantityRatio)

Deprecated

    

Show fields

[Anchor to traits](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-PriceRule.fields.traits)traits

•[[PriceRuleTrait!]!](/docs/api/admin-graphql/latest/enums/PriceRuleTrait)

non-nullDeprecated

    

Show enum values

[Anchor to value](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-PriceRule.fields.value)value

•[PriceRuleValue!](/docs/api/admin-graphql/latest/unions/PriceRuleValue)

non-nullDeprecated

    

Show union types

[Anchor to PriceRuleDiscountCode](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
PriceRuleDiscountCode)[PriceRuleDiscountCode](/docs/api/admin-
graphql/latest/objects/PriceRuleDiscountCode)

•OBJECT

    

A discount code of a price rule.

Show fields

[Anchor to app](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
PriceRuleDiscountCode.fields.app)app

•[App](/docs/api/admin-graphql/latest/objects/App)

    

The application that created the discount code.

Show fields

[Anchor to code](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-PriceRuleDiscountCode.fields.code)code

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The code to apply the discount.

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
PriceRuleDiscountCode.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to usageCount](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
PriceRuleDiscountCode.fields.usageCount)usageCount

•[Int!](/docs/api/admin-graphql/latest/scalars/Int)

non-null

    

The number of times that the price rule has been used. This value is updated
asynchronously and can be different than the actual usage count.

[Anchor to Product](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Product)[Product](/docs/api/admin-graphql/latest/objects/Product)

•OBJECT

    

The `Product` object lets you manage products in a merchant’s store.

Products are the goods and services that merchants offer to customers. They
can include various details such as title, description, price, images, and
options such as size or color. You can use [product
variants](https://shopify.dev/docs/api/admin-
graphql/latest/objects/productvariant) to create or update different versions
of the same product. You can also add or update product
[media](https://shopify.dev/docs/api/admin-graphql/latest/interfaces/media).
Products can be organized by grouping them into a
[collection](https://shopify.dev/docs/api/admin-
graphql/latest/objects/collection).

Learn more about working with [Shopify's product
model](https://shopify.dev/docs/apps/build/graphql/migrate/new-product-
model/product-model-components), including limitations and considerations.

Show fields

[Anchor to availablePublicationsCount](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Product.fields.availablePublicationsCount)availablePublicationsCount

•[Count](/docs/api/admin-graphql/latest/objects/Count)

    

The number of [publications](https://shopify.dev/docs/api/admin-
graphql/latest/objects/Publication) that a resource is published to, without
[feedback errors](https://shopify.dev/docs/api/admin-
graphql/latest/objects/ResourceFeedback).

Show fields

[Anchor to bundleComponents](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Product.fields.bundleComponents)bundleComponents

•[ProductBundleComponentConnection!](/docs/api/admin-
graphql/latest/connections/ProductBundleComponentConnection)

non-null

    

A list of [components](https://shopify.dev/docs/apps/build/product-
merchandising/bundles/add-product-fixed-bundle) that are associated with a
product in a bundle.

Show fields

[Anchor to category](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Product.fields.category)category

•[TaxonomyCategory](/docs/api/admin-graphql/latest/objects/TaxonomyCategory)

    

The category of a product from [Shopify's Standard Product
Taxonomy](https://shopify.github.io/product-
taxonomy/releases/unstable/?categoryId=sg-4-17-2-17).

Show fields

[Anchor to collections](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Product.fields.collections)collections

•[CollectionConnection!](/docs/api/admin-
graphql/latest/connections/CollectionConnection)

non-null

    

A list of [collections](https://shopify.dev/docs/api/admin-
graphql/latest/objects/Collection) that include the product.

Show fields

[Anchor to combinedListing](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Product.fields.combinedListing)combinedListing

•[CombinedListing](/docs/api/admin-graphql/latest/objects/CombinedListing)

    

A special product type that combines separate products from a store into a
single product listing. [Combined
listings](https://shopify.dev/apps/build/product-merchandising/combined-
listings) are connected by a shared option, such as color, model, or
dimension.

Show fields

[Anchor to combinedListingRole](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Product.fields.combinedListingRole)combinedListingRole

•[CombinedListingsRole](/docs/api/admin-
graphql/latest/enums/CombinedListingsRole)

    

The [role of the product](https://shopify.dev/docs/apps/build/product-
merchandising/combined-listings/build-for-combined-listings) in a combined
listing.

If `null`, then the product isn't part of any combined listing.

Show enum values

[Anchor to compareAtPriceRange](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Product.fields.compareAtPriceRange)compareAtPriceRange

•[ProductCompareAtPriceRange](/docs/api/admin-
graphql/latest/objects/ProductCompareAtPriceRange)

    

The [compare-at price
range](https://help.shopify.com/manual/products/details/product-pricing/sale-
pricing) of the product in the shop's default currency.

Show fields

[Anchor to contextualPricing](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Product.fields.contextualPricing)contextualPricing

•[ProductContextualPricing!](/docs/api/admin-
graphql/latest/objects/ProductContextualPricing)

non-null

    

The pricing that applies to a customer in a specific context. For example, a
price might vary depending on the customer's location. Only active markets are
considered in the price resolution.

Show fields

[Anchor to createdAt](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Product.fields.createdAt)createdAt

•[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime)

non-null

    

The date and time when the product was created.

[Anchor to defaultCursor](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Product.fields.defaultCursor)defaultCursor

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

A default [cursor](https://shopify.dev/api/usage/pagination-graphql) that
returns the single next record, sorted ascending by ID.

[Anchor to description](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Product.fields.description)description

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

A single-line description of the product, with [HTML
tags](https://developer.mozilla.org/en-US/docs/Web/HTML) removed.

Show arguments

### Arguments

[Anchor to truncateAt](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Product.fields.description.arguments.truncateAt)truncateAt

•[Int](/docs/api/admin-graphql/latest/scalars/Int)

    

Truncates a string after the given length.

* * *

[Anchor to descriptionHtml](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Product.fields.descriptionHtml)descriptionHtml

•[HTML!](/docs/api/admin-graphql/latest/scalars/HTML)

non-null

    

The description of the product, with HTML tags. For example, the description
might include bold `<strong></strong>` and italic `<i></i>` text.

[Anchor to events](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Product.fields.events)events

•[EventConnection!](/docs/api/admin-
graphql/latest/connections/EventConnection)

non-null

    

The paginated list of events associated with the host subject.

Show fields

[Anchor to featuredMedia](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Product.fields.featuredMedia)featuredMedia

•[Media](/docs/api/admin-graphql/latest/interfaces/Media)

    

The featured [media](https://shopify.dev/docs/apps/build/online-store/product-
media) associated with the product.

Show fields

[Anchor to feedback](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Product.fields.feedback)feedback

•[ResourceFeedback](/docs/api/admin-graphql/latest/objects/ResourceFeedback)

    

The information that lets merchants know what steps they need to take to make
sure that the app is set up correctly.

For example, if a merchant hasn't set up a product correctly in the app, then
the feedback might include a message that says "You need to add a price to
this product".

Show fields

[Anchor to giftCardTemplateSuffix](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Product.fields.giftCardTemplateSuffix)giftCardTemplateSuffix

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The [theme
template](https://shopify.dev/docs/storefronts/themes/architecture/templates)
that's used when customers view the gift card in a store.

[Anchor to handle](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Product.fields.handle)handle

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

A unique, human-readable string of the product's title. A handle can contain
letters, hyphens (`-`), and numbers, but no spaces. The handle is used in the
online store URL for the product.

[Anchor to hasOnlyDefaultVariant](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Product.fields.hasOnlyDefaultVariant)hasOnlyDefaultVariant

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether the product has only a single variant with the default option and
value.

[Anchor to hasOutOfStockVariants](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Product.fields.hasOutOfStockVariants)hasOutOfStockVariants

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether the product has variants that are out of stock.

[Anchor to hasVariantsThatRequiresComponents](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Product.fields.hasVariantsThatRequiresComponents)hasVariantsThatRequiresComponents

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether at least one of the product variants requires [bundle
components](https://shopify.dev/docs/apps/build/product-
merchandising/bundles/add-product-fixed-bundle).

Learn more about [store eligibility for
bundles](https://shopify.dev/docs/apps/build/product-
merchandising/bundles#store-eligibility).

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
Product.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to inCollection](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Product.fields.inCollection)inCollection

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether the product is in a specified
[collection](https://shopify.dev/docs/api/admin-
graphql/latest/objects/collection).

Show arguments

### Arguments

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
Product.fields.inCollection.arguments.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

required

    

The ID of the collection to check. For example, `id:
"gid://shopify/Collection/123"`.

* * *

[Anchor to isGiftCard](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Product.fields.isGiftCard)isGiftCard

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether the product is a gift card.

[Anchor to legacyResourceId](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Product.fields.legacyResourceId)legacyResourceId

•[UnsignedInt64!](/docs/api/admin-graphql/latest/scalars/UnsignedInt64)

non-null

    

The ID of the corresponding resource in the REST Admin API.

[Anchor to media](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Product.fields.media)media

•[MediaConnection!](/docs/api/admin-
graphql/latest/connections/MediaConnection)

non-null

    

The [media](https://shopify.dev/docs/apps/build/online-store/product-media)
associated with the product. Valid media are images, 3D models, videos.

Show fields

[Anchor to mediaCount](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Product.fields.mediaCount)mediaCount

•[Count](/docs/api/admin-graphql/latest/objects/Count)

    

The total count of [media](https://shopify.dev/docs/apps/build/online-
store/product-media) that's associated with a product.

Show fields

[Anchor to metafield](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Product.fields.metafield)metafield

•[Metafield](/docs/api/admin-graphql/latest/objects/Metafield)

    

A [custom field](https://shopify.dev/docs/apps/build/custom-data), including
its `namespace` and `key`, that's associated with a Shopify resource for the
purposes of adding and storing additional information.

Show fields

[Anchor to metafields](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Product.fields.metafields)metafields

•[MetafieldConnection!](/docs/api/admin-
graphql/latest/connections/MetafieldConnection)

non-null

    

A list of [custom fields](https://shopify.dev/docs/apps/build/custom-data)
that a merchant associates with a Shopify resource.

Show fields

[Anchor to onlineStorePreviewUrl](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Product.fields.onlineStorePreviewUrl)onlineStorePreviewUrl

•[URL](/docs/api/admin-graphql/latest/scalars/URL)

    

The [preview URL](https://help.shopify.com/manual/online-store/setting-
up#preview-your-store) for the online store.

[Anchor to onlineStoreUrl](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Product.fields.onlineStoreUrl)onlineStoreUrl

•[URL](/docs/api/admin-graphql/latest/scalars/URL)

    

The product's URL on the online store. If `null`, then the product isn't
published to the online store sales channel.

[Anchor to options](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Product.fields.options)options

•[[ProductOption!]!](/docs/api/admin-graphql/latest/objects/ProductOption)

non-null

    

A list of product options. The limit is defined by the [shop's resource limits
for product options](https://shopify.dev/docs/api/admin-
graphql/latest/objects/Shop#field-resourcelimits)
(`Shop.resourceLimits.maxProductOptions`).

Show fields

[Anchor to priceRangeV2](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Product.fields.priceRangeV2)priceRangeV2

•[ProductPriceRangeV2!](/docs/api/admin-
graphql/latest/objects/ProductPriceRangeV2)

non-null

    

The minimum and maximum prices of a product, expressed in decimal numbers. For
example, if the product is priced between $10.00 and $50.00, then the price
range is $10.00 - $50.00.

Show fields

[Anchor to productComponents](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Product.fields.productComponents)productComponents

•[ProductComponentTypeConnection!](/docs/api/admin-
graphql/latest/connections/ProductComponentTypeConnection)

non-null

    

A list of products that contain at least one variant associated with at least
one of the current products' variants via group relationship.

Show fields

[Anchor to productComponentsCount](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Product.fields.productComponentsCount)productComponentsCount

•[Count](/docs/api/admin-graphql/latest/objects/Count)

    

A count of unique products that contain at least one variant associated with
at least one of the current products' variants via group relationship.

Show fields

[Anchor to productParents](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Product.fields.productParents)productParents

•[ProductConnection!](/docs/api/admin-
graphql/latest/connections/ProductConnection)

non-null

    

A list of products that has a variant that contains any of this product's
variants as a component.

Show fields

[Anchor to productType](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Product.fields.productType)productType

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The [product type](https://help.shopify.com/manual/products/details/product-
type) that merchants define.

[Anchor to publishedAt](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Product.fields.publishedAt)publishedAt

•[DateTime](/docs/api/admin-graphql/latest/scalars/DateTime)

    

The date and time when the product was published to the online store.

[Anchor to publishedInContext](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Product.fields.publishedInContext)publishedInContext

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether the product is published for a customer only in a specified context.
For example, a product might be published for a customer only in a specific
location.

Show arguments

### Arguments

[Anchor to context](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Product.fields.publishedInContext.arguments.context)context

•[ContextualPublicationContext!](/docs/api/admin-graphql/latest/input-
objects/ContextualPublicationContext)

required

    

The context used to determine publication status.

Show input fields

* * *

[Anchor to publishedOnCurrentPublication](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Product.fields.publishedOnCurrentPublication)publishedOnCurrentPublication

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether the resource is published to the app's
[publication](https://shopify.dev/docs/api/admin-
graphql/latest/objects/Publication). For example, the resource might be
published to the app's online store channel.

[Anchor to publishedOnPublication](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Product.fields.publishedOnPublication)publishedOnPublication

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether the resource is published to a specified
[publication](https://shopify.dev/docs/api/admin-
graphql/latest/objects/Publication).

Show arguments

### Arguments

[Anchor to publicationId](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Product.fields.publishedOnPublication.arguments.publicationId)publicationId

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

required

    

The ID of the publication to check. For example, `id:
"gid://shopify/Publication/123"`.

* * *

[Anchor to requiresSellingPlan](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Product.fields.requiresSellingPlan)requiresSellingPlan

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether the product can only be purchased with a [selling
plan](https://shopify.dev/docs/apps/build/purchase-
options/subscriptions/selling-plans). Products that are sold on subscription
(`requiresSellingPlan: true`) can be updated only for online stores. If you
update a product to be subscription-only (`requiresSellingPlan:false`), then
the product is unpublished from all channels, except the online store.

[Anchor to resourcePublicationOnCurrentPublication](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Product.fields.resourcePublicationOnCurrentPublication)resourcePublicationOnCurrentPublication

•[ResourcePublicationV2](/docs/api/admin-
graphql/latest/objects/ResourcePublicationV2)

    

The resource that's either published or staged to be published to the
[publication](https://shopify.dev/docs/api/admin-
graphql/latest/objects/Publication).

Show fields

[Anchor to resourcePublications](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Product.fields.resourcePublications)resourcePublications

•[ResourcePublicationConnection!](/docs/api/admin-
graphql/latest/connections/ResourcePublicationConnection)

non-null

    

The list of resources that are published to a
[publication](https://shopify.dev/docs/api/admin-
graphql/latest/objects/Publication).

Show fields

[Anchor to resourcePublicationsCount](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Product.fields.resourcePublicationsCount)resourcePublicationsCount

•[Count](/docs/api/admin-graphql/latest/objects/Count)

    

The number of [publications](https://shopify.dev/docs/api/admin-
graphql/latest/objects/Publication) that a resource is published to, without
[feedback errors](https://shopify.dev/docs/api/admin-
graphql/latest/objects/ResourceFeedback).

Show fields

[Anchor to resourcePublicationsV2](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Product.fields.resourcePublicationsV2)resourcePublicationsV2

•[ResourcePublicationV2Connection!](/docs/api/admin-
graphql/latest/connections/ResourcePublicationV2Connection)

non-null

    

The list of resources that are either published or staged to be published to a
[publication](https://shopify.dev/docs/api/admin-
graphql/latest/objects/Publication).

Show fields

[Anchor to restrictedForResource](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Product.fields.restrictedForResource)restrictedForResource

•[RestrictedForResource](/docs/api/admin-
graphql/latest/objects/RestrictedForResource)

    

Whether the merchant can make changes to the product when they [edit the
order](https://shopify.dev/docs/apps/build/orders-fulfillment/order-
management-apps/edit-orders) associated with the product. For example, a
merchant might be restricted from changing product details when they edit an
order.

Show fields

[Anchor to sellingPlanGroups](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Product.fields.sellingPlanGroups)sellingPlanGroups

•[SellingPlanGroupConnection!](/docs/api/admin-
graphql/latest/connections/SellingPlanGroupConnection)

non-null

    

A list of all [selling plan
groups](https://shopify.dev/docs/apps/build/purchase-
options/subscriptions/selling-plans/build-a-selling-plan) that are associated
with the product either directly, or through the product's variants.

Show fields

[Anchor to sellingPlanGroupsCount](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Product.fields.sellingPlanGroupsCount)sellingPlanGroupsCount

•[Count](/docs/api/admin-graphql/latest/objects/Count)

    

A count of [selling plan groups](https://shopify.dev/docs/apps/build/purchase-
options/subscriptions/selling-plans/build-a-selling-plan) that are associated
with the product.

Show fields

[Anchor to seo](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
Product.fields.seo)seo

•[SEO!](/docs/api/admin-graphql/latest/objects/SEO)

non-null

    

The [SEO title and description](https://help.shopify.com/manual/promoting-
marketing/seo/adding-keywords) that are associated with a product.

Show fields

[Anchor to status](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Product.fields.status)status

•[ProductStatus!](/docs/api/admin-graphql/latest/enums/ProductStatus)

non-null

    

The [product status](https://help.shopify.com/manual/products/details/product-
details-page#product-status), which controls visibility across all sales
channels.

Show enum values

[Anchor to tags](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Product.fields.tags)tags

•[[String!]!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

A comma-separated list of searchable keywords that are associated with the
product. For example, a merchant might apply the `sports` and `summer` tags to
products that are associated with sportwear for summer.

Updating `tags` overwrites any existing tags that were previously added to the
product. To add new tags without overwriting existing tags, use the
[`tagsAdd`](https://shopify.dev/api/admin-graphql/latest/mutations/tagsadd)
mutation.

[Anchor to templateSuffix](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Product.fields.templateSuffix)templateSuffix

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The [theme
template](https://shopify.dev/docs/storefronts/themes/architecture/templates)
that's used when customers view the product in a store.

[Anchor to title](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Product.fields.title)title

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The name for the product that displays to customers. The title is used to
construct the product's handle. For example, if a product is titled "Black
Sunglasses", then the handle is `black-sunglasses`.

[Anchor to totalInventory](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Product.fields.totalInventory)totalInventory

•[Int!](/docs/api/admin-graphql/latest/scalars/Int)

non-null

    

The quantity of inventory that's in stock.

[Anchor to tracksInventory](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Product.fields.tracksInventory)tracksInventory

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether [inventory
tracking](https://help.shopify.com/manual/products/inventory/getting-started-
with-inventory/set-up-inventory-tracking) has been enabled for the product.

[Anchor to translations](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Product.fields.translations)translations

•[[Translation!]!](/docs/api/admin-graphql/latest/objects/Translation)

non-null

    

The published translations associated with the resource.

Show fields

[Anchor to unpublishedPublications](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Product.fields.unpublishedPublications)unpublishedPublications

•[PublicationConnection!](/docs/api/admin-
graphql/latest/connections/PublicationConnection)

non-null

    

The list of [publications](https://shopify.dev/docs/api/admin-
graphql/latest/objects/Publication) that the resource isn't published to.

Show fields

[Anchor to updatedAt](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Product.fields.updatedAt)updatedAt

•[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime)

non-null

    

The date and time when the product was last modified. A product's `updatedAt`
value can change for different reasons. For example, if an order is placed for
a product that has inventory tracking set up, then the inventory adjustment is
counted as an update.

[Anchor to variants](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Product.fields.variants)variants

•[ProductVariantConnection!](/docs/api/admin-
graphql/latest/connections/ProductVariantConnection)

non-null

    

A list of [variants](https://shopify.dev/docs/api/admin-
graphql/latest/objects/ProductVariant) associated with the product. If
querying a single product at the root, you can fetch up to 2048 variants.

Show fields

[Anchor to variantsCount](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Product.fields.variantsCount)variantsCount

•[Count](/docs/api/admin-graphql/latest/objects/Count)

    

The number of [variants](https://shopify.dev/docs/api/admin-
graphql/latest/objects/ProductVariant) that are associated with the product.

Show fields

[Anchor to vendor](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Product.fields.vendor)vendor

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The name of the product's vendor.

[Anchor to bodyHtml](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Product.fields.bodyHtml)bodyHtml

•[String](/docs/api/admin-graphql/latest/scalars/String)

Deprecated

    

[Anchor to customProductType](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Product.fields.customProductType)customProductType

•[String](/docs/api/admin-graphql/latest/scalars/String)

Deprecated

    

[Anchor to descriptionPlainSummary](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Product.fields.descriptionPlainSummary)descriptionPlainSummary

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-nullDeprecated

    

[Anchor to featuredImage](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Product.fields.featuredImage)featuredImage

•[Image](/docs/api/admin-graphql/latest/objects/Image)

Deprecated

    

Show fields

[Anchor to images](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Product.fields.images)images

•[ImageConnection!](/docs/api/admin-
graphql/latest/connections/ImageConnection)

non-nullDeprecated

    

Show fields

[Anchor to metafieldDefinitions](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Product.fields.metafieldDefinitions)metafieldDefinitions

•[MetafieldDefinitionConnection!](/docs/api/admin-
graphql/latest/connections/MetafieldDefinitionConnection)

non-nullDeprecated

    

Show fields

[Anchor to priceRange](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Product.fields.priceRange)priceRange

•[ProductPriceRange!](/docs/api/admin-
graphql/latest/objects/ProductPriceRange)

non-nullDeprecated

    

Show fields

[Anchor to productCategory](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Product.fields.productCategory)productCategory

•[ProductCategory](/docs/api/admin-graphql/latest/objects/ProductCategory)

Deprecated

    

Show fields

[Anchor to productPublications](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Product.fields.productPublications)productPublications

•[ProductPublicationConnection!](/docs/api/admin-
graphql/latest/connections/ProductPublicationConnection)

non-nullDeprecated

    

Show fields

[Anchor to publicationCount](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Product.fields.publicationCount)publicationCount

•[Int!](/docs/api/admin-graphql/latest/scalars/Int)

non-nullDeprecated

    

Show arguments

### Arguments

[Anchor to onlyPublished](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Product.fields.publicationCount.arguments.onlyPublished)onlyPublished

•[Boolean](/docs/api/admin-graphql/latest/scalars/Boolean)

Default:true

    

Include only the resource's publications that are published. If false, then
return all the resource's publications including future publications.

* * *

[Anchor to publications](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Product.fields.publications)publications

•[ProductPublicationConnection!](/docs/api/admin-
graphql/latest/connections/ProductPublicationConnection)

non-nullDeprecated

    

Show fields

[Anchor to publishedOnChannel](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Product.fields.publishedOnChannel)publishedOnChannel

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-nullDeprecated

    

Show arguments

### Arguments

[Anchor to channelId](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Product.fields.publishedOnChannel.arguments.channelId)channelId

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

required

    

The ID of the channel to check.

* * *

[Anchor to publishedOnCurrentChannel](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Product.fields.publishedOnCurrentChannel)publishedOnCurrentChannel

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-nullDeprecated

    

[Anchor to sellingPlanGroupCount](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Product.fields.sellingPlanGroupCount)sellingPlanGroupCount

•[Int!](/docs/api/admin-graphql/latest/scalars/Int)

non-nullDeprecated

    

[Anchor to standardizedProductType](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Product.fields.standardizedProductType)standardizedProductType

•[StandardizedProductType](/docs/api/admin-
graphql/latest/objects/StandardizedProductType)

Deprecated

    

Show fields

[Anchor to storefrontId](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Product.fields.storefrontId)storefrontId

•[StorefrontID!](/docs/api/admin-graphql/latest/scalars/StorefrontID)

non-nullDeprecated

    

[Anchor to totalVariants](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Product.fields.totalVariants)totalVariants

•[Int!](/docs/api/admin-graphql/latest/scalars/Int)

non-nullDeprecated

    

[Anchor to unpublishedChannels](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Product.fields.unpublishedChannels)unpublishedChannels

•[ChannelConnection!](/docs/api/admin-
graphql/latest/connections/ChannelConnection)

non-nullDeprecated

    

Show fields

[Anchor to ProductBundleOperation](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ProductBundleOperation)[ProductBundleOperation](/docs/api/admin-
graphql/latest/objects/ProductBundleOperation)

•OBJECT

    

An entity that represents details of an asynchronous
[ProductBundleCreate](https://shopify.dev/api/admin-
graphql/current/mutations/productBundleCreate) or
[ProductBundleUpdate](https://shopify.dev/api/admin-
graphql/current/mutations/productBundleUpdate) mutation.

By querying this entity with the
[productOperation](https://shopify.dev/api/admin-
graphql/current/queries/productOperation) query using the ID that was returned
when the bundle was created or updated, this can be used to check the status
of an operation.

The `status` field indicates whether the operation is `CREATED`, `ACTIVE`, or
`COMPLETE`.

The `product` field provides the details of the created or updated product.

The `userErrors` field provides mutation errors that occurred during the
operation.

Show fields

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
ProductBundleOperation.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to product](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-ProductBundleOperation.fields.product)product

•[Product](/docs/api/admin-graphql/latest/objects/Product)

    

The product on which the operation is being performed.

Show fields

[Anchor to status](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-ProductBundleOperation.fields.status)status

•[ProductOperationStatus!](/docs/api/admin-
graphql/latest/enums/ProductOperationStatus)

non-null

    

The status of this operation.

Show enum values

[Anchor to userErrors](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ProductBundleOperation.fields.userErrors)userErrors

•[[ProductBundleMutationUserError!]!](/docs/api/admin-
graphql/latest/objects/ProductBundleMutationUserError)

non-null

    

Returns mutation errors occurred during background mutation processing.

Show fields

[Anchor to ProductDeleteOperation](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ProductDeleteOperation)[ProductDeleteOperation](/docs/api/admin-
graphql/latest/objects/ProductDeleteOperation)

•OBJECT

    

An entity that represents details of an asynchronous
[ProductDelete](https://shopify.dev/api/admin-
graphql/current/mutations/productDelete) mutation.

By querying this entity with the
[productOperation](https://shopify.dev/api/admin-
graphql/current/queries/productOperation) query using the ID that was returned
when the product was deleted, this can be used to check the status of an
operation.

The `status` field indicates whether the operation is `CREATED`, `ACTIVE`, or
`COMPLETE`.

The `deletedProductId` field provides the ID of the deleted product.

The `userErrors` field provides mutation errors that occurred during the
operation.

Show fields

[Anchor to deletedProductId](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ProductDeleteOperation.fields.deletedProductId)deletedProductId

•[ID](/docs/api/admin-graphql/latest/scalars/ID)

    

The ID of the deleted product.

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
ProductDeleteOperation.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to product](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-ProductDeleteOperation.fields.product)product

•[Product](/docs/api/admin-graphql/latest/objects/Product)

    

The product on which the operation is being performed.

Show fields

[Anchor to status](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-ProductDeleteOperation.fields.status)status

•[ProductOperationStatus!](/docs/api/admin-
graphql/latest/enums/ProductOperationStatus)

non-null

    

The status of this operation.

Show enum values

[Anchor to userErrors](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ProductDeleteOperation.fields.userErrors)userErrors

•[[UserError!]!](/docs/api/admin-graphql/latest/objects/UserError)

non-null

    

Returns mutation errors occurred during background mutation processing.

Show fields

[Anchor to ProductDuplicateOperation](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ProductDuplicateOperation)[ProductDuplicateOperation](/docs/api/admin-
graphql/latest/objects/ProductDuplicateOperation)

•OBJECT

    

An entity that represents details of an asynchronous
[ProductDuplicate](https://shopify.dev/api/admin-
graphql/current/mutations/productDuplicate) mutation.

By querying this entity with the
[productOperation](https://shopify.dev/api/admin-
graphql/current/queries/productOperation) query using the ID that was returned
[when the product was duplicated](https://shopify.dev/api/admin/migrate/new-
product-model/sync-data#create-a-product-with-variants-and-options-
asynchronously), this can be used to check the status of an operation.

The `status` field indicates whether the operation is `CREATED`, `ACTIVE`, or
`COMPLETE`.

The `product` field provides the details of the original product.

The `newProduct` field provides the details of the new duplicate of the
product.

The `userErrors` field provides mutation errors that occurred during the
operation.

Show fields

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
ProductDuplicateOperation.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to newProduct](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ProductDuplicateOperation.fields.newProduct)newProduct

•[Product](/docs/api/admin-graphql/latest/objects/Product)

    

The newly created duplicate of the original product.

Show fields

[Anchor to product](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-ProductDuplicateOperation.fields.product)product

•[Product](/docs/api/admin-graphql/latest/objects/Product)

    

The product on which the operation is being performed.

Show fields

[Anchor to status](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-ProductDuplicateOperation.fields.status)status

•[ProductOperationStatus!](/docs/api/admin-
graphql/latest/enums/ProductOperationStatus)

non-null

    

The status of this operation.

Show enum values

[Anchor to userErrors](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ProductDuplicateOperation.fields.userErrors)userErrors

•[[UserError!]!](/docs/api/admin-graphql/latest/objects/UserError)

non-null

    

Returns mutation errors occurred during background mutation processing.

Show fields

[Anchor to ProductFeed](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ProductFeed)[ProductFeed](/docs/api/admin-graphql/latest/objects/ProductFeed)

•OBJECT

    

A product feed.

Show fields

[Anchor to country](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-ProductFeed.fields.country)country

•[CountryCode](/docs/api/admin-graphql/latest/enums/CountryCode)

    

The country of the product feed.

Show enum values

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
ProductFeed.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to language](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-ProductFeed.fields.language)language

•[LanguageCode](/docs/api/admin-graphql/latest/enums/LanguageCode)

    

The language of the product feed.

Show enum values

[Anchor to status](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-ProductFeed.fields.status)status

•[ProductFeedStatus!](/docs/api/admin-graphql/latest/enums/ProductFeedStatus)

non-null

    

The status of the product feed.

Show enum values

[Anchor to ProductOption](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ProductOption)[ProductOption](/docs/api/admin-
graphql/latest/objects/ProductOption)

•OBJECT

    

The product property names. For example, "Size", "Color", and "Material".
Variants are selected based on permutations of these options. The limit for
each product property name is 255 characters.

Show fields

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
ProductOption.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to linkedMetafield](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ProductOption.fields.linkedMetafield)linkedMetafield

•[LinkedMetafield](/docs/api/admin-graphql/latest/objects/LinkedMetafield)

    

The metafield identifier linked to this option.

Show fields

[Anchor to name](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-ProductOption.fields.name)name

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The product option’s name.

[Anchor to optionValues](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ProductOption.fields.optionValues)optionValues

•[[ProductOptionValue!]!](/docs/api/admin-
graphql/latest/objects/ProductOptionValue)

non-null

    

Similar to values, option_values returns all the corresponding option value
objects to the product option, including values not assigned to any variants.

Show fields

[Anchor to position](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-ProductOption.fields.position)position

•[Int!](/docs/api/admin-graphql/latest/scalars/Int)

non-null

    

The product option's position.

[Anchor to translations](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ProductOption.fields.translations)translations

•[[Translation!]!](/docs/api/admin-graphql/latest/objects/Translation)

non-null

    

The published translations associated with the resource.

Show fields

[Anchor to values](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-ProductOption.fields.values)values

•[[String!]!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The corresponding value to the product option name.

[Anchor to ProductOptionValue](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ProductOptionValue)[ProductOptionValue](/docs/api/admin-
graphql/latest/objects/ProductOptionValue)

•OBJECT

    

The product option value names. For example, "Red", "Blue", and "Green" for a
"Color" option.

Show fields

[Anchor to hasVariants](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ProductOptionValue.fields.hasVariants)hasVariants

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether the product option value has any linked variants.

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
ProductOptionValue.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to linkedMetafieldValue](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ProductOptionValue.fields.linkedMetafieldValue)linkedMetafieldValue

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The value of the linked metafield.

[Anchor to name](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-ProductOptionValue.fields.name)name

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The name of the product option value.

[Anchor to swatch](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-ProductOptionValue.fields.swatch)swatch

•[ProductOptionValueSwatch](/docs/api/admin-
graphql/latest/objects/ProductOptionValueSwatch)

    

The swatch associated with the product option value.

Show fields

[Anchor to translations](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ProductOptionValue.fields.translations)translations

•[[Translation!]!](/docs/api/admin-graphql/latest/objects/Translation)

non-null

    

The published translations associated with the resource.

Show fields

[Anchor to ProductSetOperation](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ProductSetOperation)[ProductSetOperation](/docs/api/admin-
graphql/latest/objects/ProductSetOperation)

•OBJECT

    

An entity that represents details of an asynchronous
[ProductSet](https://shopify.dev/api/admin-
graphql/current/mutations/productSet) mutation.

By querying this entity with the
[productOperation](https://shopify.dev/api/admin-
graphql/current/queries/productOperation) query using the ID that was returned
[when the product was created or
updated](https://shopify.dev/api/admin/migrate/new-product-model/sync-
data#create-a-product-with-variants-and-options-asynchronously), this can be
used to check the status of an operation.

The `status` field indicates whether the operation is `CREATED`, `ACTIVE`, or
`COMPLETE`.

The `product` field provides the details of the created or updated product.

The `userErrors` field provides mutation errors that occurred during the
operation.

Show fields

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
ProductSetOperation.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to product](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-ProductSetOperation.fields.product)product

•[Product](/docs/api/admin-graphql/latest/objects/Product)

    

The product on which the operation is being performed.

Show fields

[Anchor to status](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-ProductSetOperation.fields.status)status

•[ProductOperationStatus!](/docs/api/admin-
graphql/latest/enums/ProductOperationStatus)

non-null

    

The status of this operation.

Show enum values

[Anchor to userErrors](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ProductSetOperation.fields.userErrors)userErrors

•[[ProductSetUserError!]!](/docs/api/admin-
graphql/latest/objects/ProductSetUserError)

non-null

    

Returns mutation errors occurred during background mutation processing.

Show fields

[Anchor to ProductTaxonomyNode](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ProductTaxonomyNode)[ProductTaxonomyNode](/docs/api/admin-
graphql/latest/objects/ProductTaxonomyNode)

•OBJECT

    

Represents a [Shopify product taxonomy](https://shopify.github.io/product-
taxonomy/releases/unstable/?categoryId=sg-4-17-2-17) node.

Show fields

[Anchor to fullName](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-ProductTaxonomyNode.fields.fullName)fullName

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The full name of the product taxonomy node. For example, Animals & Pet
Supplies > Pet Supplies > Dog Supplies > Dog Beds.

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
ProductTaxonomyNode.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

The ID of the product taxonomy node.

[Anchor to isLeaf](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-ProductTaxonomyNode.fields.isLeaf)isLeaf

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether the node is a leaf node.

[Anchor to isRoot](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-ProductTaxonomyNode.fields.isRoot)isRoot

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether the node is a root node.

[Anchor to name](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-ProductTaxonomyNode.fields.name)name

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The name of the product taxonomy node. For example, Dog Beds.

[Anchor to ProductVariant](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ProductVariant)[ProductVariant](/docs/api/admin-
graphql/latest/objects/ProductVariant)

•OBJECT

    

The `ProductVariant` object represents a version of a
[product](https://shopify.dev/docs/api/admin-graphql/latest/objects/Product)
that comes in more than one [option](https://shopify.dev/docs/api/admin-
graphql/latest/objects/ProductOption), such as size or color. For example, if
a merchant sells t-shirts with options for size and color, then a small, blue
t-shirt would be one product variant and a large, blue t-shirt would be
another.

Use the `ProductVariant` object to manage the full lifecycle and configuration
of a product's variants. Common use cases for using the `ProductVariant`
object include:

  * Tracking inventory for each variant
  * Setting unique prices for each variant
  * Assigning barcodes and SKUs to connect variants to fulfillment services
  * Attaching variant-specific images and media
  * Setting delivery and tax requirements
  * Supporting product bundles, subscriptions, and selling plans

A `ProductVariant` is associated with a parent
[`Product`](https://shopify.dev/docs/api/admin-graphql/latest/objects/Product)
object. `ProductVariant` serves as the central link between a product's
merchandising configuration, inventory, pricing, fulfillment, and sales
channels within the GraphQL Admin API schema. Each variant can reference other
GraphQL types such as:

  * [`InventoryItem`](https://shopify.dev/docs/api/admin-graphql/latest/objects/InventoryItem): Used for inventory tracking
  * [`Image`](https://shopify.dev/docs/api/admin-graphql/latest/objects/Image): Used for variant-specific images
  * [`SellingPlanGroup`](https://shopify.dev/docs/api/admin-graphql/latest/objects/SellingPlanGroup): Used for subscriptions and selling plans

Learn more about [Shopify's product
model](https://shopify.dev/docs/apps/build/graphql/migrate/new-product-
model/product-model-components).

Show fields

[Anchor to availableForSale](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ProductVariant.fields.availableForSale)availableForSale

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether the product variant is available for sale.

[Anchor to barcode](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-ProductVariant.fields.barcode)barcode

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The value of the barcode associated with the product.

[Anchor to compareAtPrice](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ProductVariant.fields.compareAtPrice)compareAtPrice

•[Money](/docs/api/admin-graphql/latest/scalars/Money)

    

The compare-at price of the variant in the default shop currency.

[Anchor to contextualPricing](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ProductVariant.fields.contextualPricing)contextualPricing

•[ProductVariantContextualPricing!](/docs/api/admin-
graphql/latest/objects/ProductVariantContextualPricing)

non-null

    

The pricing that applies for a customer in a given context. As of API version
2025-04, only active markets are considered in the price resolution.

Show fields

[Anchor to createdAt](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-ProductVariant.fields.createdAt)createdAt

•[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime)

non-null

    

The date and time when the variant was created.

[Anchor to defaultCursor](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ProductVariant.fields.defaultCursor)defaultCursor

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

A default [cursor](https://shopify.dev/api/usage/pagination-graphql) that
returns the single next record, sorted ascending by ID.

[Anchor to deliveryProfile](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ProductVariant.fields.deliveryProfile)deliveryProfile

•[DeliveryProfile](/docs/api/admin-graphql/latest/objects/DeliveryProfile)

    

The [delivery profile](https://shopify.dev/api/admin-
graphql/latest/objects/DeliveryProfile) for the variant.

Show fields

[Anchor to displayName](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ProductVariant.fields.displayName)displayName

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

Display name of the variant, based on product's title + variant's title.

[Anchor to events](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-ProductVariant.fields.events)events

•[EventConnection!](/docs/api/admin-
graphql/latest/connections/EventConnection)

non-null

    

The paginated list of events associated with the host subject.

Show fields

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
ProductVariant.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to inventoryItem](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ProductVariant.fields.inventoryItem)inventoryItem

•[InventoryItem!](/docs/api/admin-graphql/latest/objects/InventoryItem)

non-null

    

The inventory item, which is used to query for inventory information.

Show fields

[Anchor to inventoryPolicy](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ProductVariant.fields.inventoryPolicy)inventoryPolicy

•[ProductVariantInventoryPolicy!](/docs/api/admin-
graphql/latest/enums/ProductVariantInventoryPolicy)

non-null

    

Whether customers are allowed to place an order for the product variant when
it's out of stock.

Show enum values

[Anchor to inventoryQuantity](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ProductVariant.fields.inventoryQuantity)inventoryQuantity

•[Int](/docs/api/admin-graphql/latest/scalars/Int)

    

The total sellable quantity of the variant.

[Anchor to legacyResourceId](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ProductVariant.fields.legacyResourceId)legacyResourceId

•[UnsignedInt64!](/docs/api/admin-graphql/latest/scalars/UnsignedInt64)

non-null

    

The ID of the corresponding resource in the REST Admin API.

[Anchor to media](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-ProductVariant.fields.media)media

•[MediaConnection!](/docs/api/admin-
graphql/latest/connections/MediaConnection)

non-null

    

The media associated with the product variant.

Show fields

[Anchor to metafield](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-ProductVariant.fields.metafield)metafield

•[Metafield](/docs/api/admin-graphql/latest/objects/Metafield)

    

A [custom field](https://shopify.dev/docs/apps/build/custom-data), including
its `namespace` and `key`, that's associated with a Shopify resource for the
purposes of adding and storing additional information.

Show fields

[Anchor to metafields](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ProductVariant.fields.metafields)metafields

•[MetafieldConnection!](/docs/api/admin-
graphql/latest/connections/MetafieldConnection)

non-null

    

A list of [custom fields](https://shopify.dev/docs/apps/build/custom-data)
that a merchant associates with a Shopify resource.

Show fields

[Anchor to position](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-ProductVariant.fields.position)position

•[Int!](/docs/api/admin-graphql/latest/scalars/Int)

non-null

    

The order of the product variant in the list of product variants. The first
position in the list is 1.

[Anchor to price](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-ProductVariant.fields.price)price

•[Money!](/docs/api/admin-graphql/latest/scalars/Money)

non-null

    

The price of the product variant in the default shop currency.

[Anchor to product](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-ProductVariant.fields.product)product

•[Product!](/docs/api/admin-graphql/latest/objects/Product)

non-null

    

The product that this variant belongs to.

Show fields

[Anchor to productParents](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ProductVariant.fields.productParents)productParents

•[ProductConnection!](/docs/api/admin-
graphql/latest/connections/ProductConnection)

non-null

    

A list of products that have product variants that contain this variant as a
product component.

Show fields

[Anchor to productVariantComponents](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ProductVariant.fields.productVariantComponents)productVariantComponents

•[ProductVariantComponentConnection!](/docs/api/admin-
graphql/latest/connections/ProductVariantComponentConnection)

non-null

    

A list of the product variant components.

Show fields

[Anchor to requiresComponents](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ProductVariant.fields.requiresComponents)requiresComponents

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether a product variant requires components. The default value is `false`.
If `true`, then the product variant can only be purchased as a parent bundle
with components and it will be omitted from channels that don't support
bundles.

[Anchor to selectedOptions](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ProductVariant.fields.selectedOptions)selectedOptions

•[[SelectedOption!]!](/docs/api/admin-graphql/latest/objects/SelectedOption)

non-null

    

List of product options applied to the variant.

Show fields

[Anchor to sellableOnlineQuantity](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ProductVariant.fields.sellableOnlineQuantity)sellableOnlineQuantity

•[Int!](/docs/api/admin-graphql/latest/scalars/Int)

non-null

    

The total sellable quantity of the variant for online channels. This doesn't
represent the total available inventory or capture [limitations based on
customer
location](https://help.shopify.com/manual/markets/inventory_and_fulfillment).

[Anchor to sellingPlanGroups](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ProductVariant.fields.sellingPlanGroups)sellingPlanGroups

•[SellingPlanGroupConnection!](/docs/api/admin-
graphql/latest/connections/SellingPlanGroupConnection)

non-null

    

A list of all selling plan groups defined in the current shop associated with
the product variant.

Show fields

[Anchor to sellingPlanGroupsCount](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ProductVariant.fields.sellingPlanGroupsCount)sellingPlanGroupsCount

•[Count](/docs/api/admin-graphql/latest/objects/Count)

    

Count of selling plan groups associated with the product variant.

Show fields

[Anchor to showUnitPrice](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ProductVariant.fields.showUnitPrice)showUnitPrice

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether to show the unit price for this product variant.

[Anchor to sku](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
ProductVariant.fields.sku)sku

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

A case-sensitive identifier for the product variant in the shop. Required in
order to connect to a fulfillment service.

[Anchor to taxable](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-ProductVariant.fields.taxable)taxable

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether a tax is charged when the product variant is sold.

[Anchor to title](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-ProductVariant.fields.title)title

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The title of the product variant.

[Anchor to translations](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ProductVariant.fields.translations)translations

•[[Translation!]!](/docs/api/admin-graphql/latest/objects/Translation)

non-null

    

The published translations associated with the resource.

Show fields

[Anchor to unitPrice](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-ProductVariant.fields.unitPrice)unitPrice

•[MoneyV2](/docs/api/admin-graphql/latest/objects/MoneyV2)

    

The unit price value for the variant based on the variant measurement.

Show fields

[Anchor to unitPriceMeasurement](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ProductVariant.fields.unitPriceMeasurement)unitPriceMeasurement

•[UnitPriceMeasurement](/docs/api/admin-
graphql/latest/objects/UnitPriceMeasurement)

    

The unit price measurement for the variant.

Show fields

[Anchor to updatedAt](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-ProductVariant.fields.updatedAt)updatedAt

•[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime)

non-null

    

The date and time (ISO 8601 format) when the product variant was last
modified.

[Anchor to image](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-ProductVariant.fields.image)image

•[Image](/docs/api/admin-graphql/latest/objects/Image)

Deprecated

    

Show fields

[Anchor to metafieldDefinitions](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ProductVariant.fields.metafieldDefinitions)metafieldDefinitions

•[MetafieldDefinitionConnection!](/docs/api/admin-
graphql/latest/connections/MetafieldDefinitionConnection)

non-nullDeprecated

    

Show fields

[Anchor to presentmentPrices](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ProductVariant.fields.presentmentPrices)presentmentPrices

•[ProductVariantPricePairConnection!](/docs/api/admin-
graphql/latest/connections/ProductVariantPricePairConnection)

non-nullDeprecated

    

Show fields

[Anchor to sellingPlanGroupCount](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ProductVariant.fields.sellingPlanGroupCount)sellingPlanGroupCount

•[Int!](/docs/api/admin-graphql/latest/scalars/Int)

non-nullDeprecated

    

[Anchor to storefrontId](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ProductVariant.fields.storefrontId)storefrontId

•[StorefrontID!](/docs/api/admin-graphql/latest/scalars/StorefrontID)

non-nullDeprecated

    

[Anchor to taxCode](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-ProductVariant.fields.taxCode)taxCode

•[String](/docs/api/admin-graphql/latest/scalars/String)

Deprecated

    

[Anchor to ProductVariantComponent](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ProductVariantComponent)[ProductVariantComponent](/docs/api/admin-
graphql/latest/objects/ProductVariantComponent)

•OBJECT

    

A product variant component that is included within a bundle.

These are the individual product variants that make up a bundle product, where
each component has a specific required quantity.

Show fields

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
ProductVariantComponent.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to productVariant](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ProductVariantComponent.fields.productVariant)productVariant

•[ProductVariant!](/docs/api/admin-graphql/latest/objects/ProductVariant)

non-null

    

The product variant associated with the component.

Show fields

[Anchor to quantity](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-ProductVariantComponent.fields.quantity)quantity

•[Int!](/docs/api/admin-graphql/latest/scalars/Int)

non-null

    

The required quantity of the component.

[Anchor to Publication](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Publication)[Publication](/docs/api/admin-graphql/latest/objects/Publication)

•OBJECT

    

A publication is a group of products and collections that is published to an
app.

Show fields

[Anchor to autoPublish](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Publication.fields.autoPublish)autoPublish

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether new products are automatically published to this publication.

[Anchor to catalog](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Publication.fields.catalog)catalog

•[Catalog](/docs/api/admin-graphql/latest/interfaces/Catalog)

    

The catalog associated with the publication.

Show fields

[Anchor to collectionPublicationsV3](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Publication.fields.collectionPublicationsV3)collectionPublicationsV3

•[ResourcePublicationConnection!](/docs/api/admin-
graphql/latest/connections/ResourcePublicationConnection)

non-null

    

The list of collection publication records, each representing the publication
status and details for a collection published to this publication (typically
channel).

Show fields

[Anchor to collections](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Publication.fields.collections)collections

•[CollectionConnection!](/docs/api/admin-
graphql/latest/connections/CollectionConnection)

non-null

    

The list of collections published to the publication.

Show fields

[Anchor to hasCollection](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Publication.fields.hasCollection)hasCollection

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether the collection is available to the publication.

Show arguments

### Arguments

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
Publication.fields.hasCollection.arguments.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

required

    

Collection ID to check.

* * *

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
Publication.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to includedProducts](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Publication.fields.includedProducts)includedProducts

•[ProductConnection!](/docs/api/admin-
graphql/latest/connections/ProductConnection)

non-null

    

The list of products included, but not necessarily published, in the
publication.

Show fields

[Anchor to includedProductsCount](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Publication.fields.includedProductsCount)includedProductsCount

•[Count](/docs/api/admin-graphql/latest/objects/Count)

    

The count of products included in the publication. Limited to a maximum of
10000 by default.

Show fields

[Anchor to operation](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Publication.fields.operation)operation

•[PublicationOperation](/docs/api/admin-
graphql/latest/unions/PublicationOperation)

    

A background operation associated with this publication.

Show union types

[Anchor to productPublicationsV3](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Publication.fields.productPublicationsV3)productPublicationsV3

•[ResourcePublicationConnection!](/docs/api/admin-
graphql/latest/connections/ResourcePublicationConnection)

non-null

    

The product publications for the list of products published to the
publication.

Show fields

[Anchor to products](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Publication.fields.products)products

•[ProductConnection!](/docs/api/admin-
graphql/latest/connections/ProductConnection)

non-null

    

The list of products published to the publication.

Show fields

[Anchor to supportsFuturePublishing](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Publication.fields.supportsFuturePublishing)supportsFuturePublishing

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether the publication supports future publishing.

[Anchor to app](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
Publication.fields.app)app

•[App!](/docs/api/admin-graphql/latest/objects/App)

non-nullDeprecated

    

Show fields

[Anchor to name](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Publication.fields.name)name

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-nullDeprecated

    

[Anchor to PublicationResourceOperation](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
PublicationResourceOperation)[PublicationResourceOperation](/docs/api/admin-
graphql/latest/objects/PublicationResourceOperation)

•OBJECT

    

A bulk update operation on a publication.

Show fields

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
PublicationResourceOperation.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to processedRowCount](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
PublicationResourceOperation.fields.processedRowCount)processedRowCount

•[Int](/docs/api/admin-graphql/latest/scalars/Int)

    

The count of processed rows, summing imported, failed, and skipped rows.

[Anchor to rowCount](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-PublicationResourceOperation.fields.rowCount)rowCount

•[RowCount](/docs/api/admin-graphql/latest/objects/RowCount)

    

Represents a rows objects within this background operation.

Show fields

[Anchor to status](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-PublicationResourceOperation.fields.status)status

•[ResourceOperationStatus!](/docs/api/admin-
graphql/latest/enums/ResourceOperationStatus)

non-null

    

The status of this operation.

Show enum values

[Anchor to QuantityPriceBreak](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
QuantityPriceBreak)[QuantityPriceBreak](/docs/api/admin-
graphql/latest/objects/QuantityPriceBreak)

•OBJECT

    

Quantity price breaks lets you offer different rates that are based on the
amount of a specific variant being ordered.

Show fields

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
QuantityPriceBreak.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to minimumQuantity](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
QuantityPriceBreak.fields.minimumQuantity)minimumQuantity

•[Int!](/docs/api/admin-graphql/latest/scalars/Int)

non-null

    

Minimum quantity required to reach new quantity break price.

[Anchor to price](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-QuantityPriceBreak.fields.price)price

•[MoneyV2!](/docs/api/admin-graphql/latest/objects/MoneyV2)

non-null

    

The price of variant after reaching the minimum quanity.

Show fields

[Anchor to priceList](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-QuantityPriceBreak.fields.priceList)priceList

•[PriceList!](/docs/api/admin-graphql/latest/objects/PriceList)

non-null

    

The price list associated with this quantity break.

Show fields

[Anchor to variant](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-QuantityPriceBreak.fields.variant)variant

•[ProductVariant!](/docs/api/admin-graphql/latest/objects/ProductVariant)

non-null

    

The product variant associated with this quantity break.

Show fields

[Anchor to Refund](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Refund)[Refund](/docs/api/admin-graphql/latest/objects/Refund)

•OBJECT

    

The `Refund` object represents a financial record of money returned to a
customer from an order. It provides a comprehensive view of all refunded
amounts, transactions, and restocking instructions associated with returning
products or correcting order issues.

The `Refund` object provides information to:

  * Process customer returns and issue payments back to customers
  * Handle partial or full refunds for line items with optional inventory restocking
  * Refund shipping costs, duties, and additional fees
  * Issue store credit refunds as an alternative to original payment method returns
  * Track and reconcile all financial transactions related to refunds

Each `Refund` object maintains detailed records of what was refunded, how much
was refunded, which payment transactions were involved, and any inventory
restocking that occurred. The refund can include multiple components such as
product line items, shipping charges, taxes, duties, and additional fees, all
calculated with proper currency handling for international orders.

Refunds are always associated with an
[order](https://shopify.dev/docs/api/admin-graphql/latest/objects/Order) and
can optionally be linked to a [return](https://shopify.dev/docs/api/admin-
graphql/latest/objects/Return) if the refund was initiated through the returns
process. The refund tracks both the presentment currency (what the customer
sees) and the shop currency for accurate financial reporting.

* * *

Note

The existence of a `Refund` object doesn't guarantee that the money has been
returned to the customer. The actual financial processing happens through
associated [`OrderTransaction`](https://shopify.dev/docs/api/admin-
graphql/latest/objects/OrderTransaction) objects, which can be in various
states, such as pending, processing, success, or failure. To determine if
money has actually been refunded, check the
[status](https://shopify.dev/docs/api/admin-
graphql/latest/objects/OrderTransaction#field-OrderTransaction.fields.status)
of the associated transactions.

* * *

Learn more about [managing
returns](https://shopify.dev/docs/apps/build/orders-fulfillment/returns-
apps/build-return-management), [refunding
duties](https://shopify.dev/docs/apps/build/orders-fulfillment/returns-
apps/view-and-refund-duties), and [processing
refunds](https://shopify.dev/docs/api/admin-
graphql/latest/mutations/refundCreate).

Show fields

[Anchor to createdAt](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Refund.fields.createdAt)createdAt

•[DateTime](/docs/api/admin-graphql/latest/scalars/DateTime)

    

The date and time when the refund was created.

[Anchor to duties](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Refund.fields.duties)duties

•[[RefundDuty!]](/docs/api/admin-graphql/latest/objects/RefundDuty)

    

A list of the refunded duties as part of this refund.

Show fields

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
Refund.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to legacyResourceId](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Refund.fields.legacyResourceId)legacyResourceId

•[UnsignedInt64!](/docs/api/admin-graphql/latest/scalars/UnsignedInt64)

non-null

    

The ID of the corresponding resource in the REST Admin API.

[Anchor to note](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Refund.fields.note)note

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The optional note associated with the refund.

[Anchor to order](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Refund.fields.order)order

•[Order!](/docs/api/admin-graphql/latest/objects/Order)

non-null

    

The order associated with the refund.

Show fields

[Anchor to orderAdjustments](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Refund.fields.orderAdjustments)orderAdjustments

•[OrderAdjustmentConnection!](/docs/api/admin-
graphql/latest/connections/OrderAdjustmentConnection)

non-null

    

The order adjustments that are attached with the refund.

Show fields

[Anchor to refundLineItems](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Refund.fields.refundLineItems)refundLineItems

•[RefundLineItemConnection!](/docs/api/admin-
graphql/latest/connections/RefundLineItemConnection)

non-null

    

The `RefundLineItem` resources attached to the refund.

Show fields

[Anchor to refundShippingLines](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Refund.fields.refundShippingLines)refundShippingLines

•[RefundShippingLineConnection!](/docs/api/admin-
graphql/latest/connections/RefundShippingLineConnection)

non-null

    

The `RefundShippingLine` resources attached to the refund.

Show fields

[Anchor to return](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Refund.fields.return)return

•[Return](/docs/api/admin-graphql/latest/objects/Return)

    

The return associated with the refund.

Show fields

[Anchor to staffMember](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Refund.fields.staffMember)staffMember

•[StaffMember](/docs/api/admin-graphql/latest/objects/StaffMember)

    

The staff member who created the refund.

Show fields

[Anchor to totalRefundedSet](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Refund.fields.totalRefundedSet)totalRefundedSet

•[MoneyBag!](/docs/api/admin-graphql/latest/objects/MoneyBag)

non-null

    

The total amount across all transactions for the refund, in shop and
presentment currencies.

Show fields

[Anchor to transactions](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Refund.fields.transactions)transactions

•[OrderTransactionConnection!](/docs/api/admin-
graphql/latest/connections/OrderTransactionConnection)

non-null

    

The transactions associated with the refund.

Show fields

[Anchor to updatedAt](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Refund.fields.updatedAt)updatedAt

•[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime)

non-null

    

The date and time when the refund was updated.

[Anchor to totalRefunded](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Refund.fields.totalRefunded)totalRefunded

•[MoneyV2!](/docs/api/admin-graphql/latest/objects/MoneyV2)

non-nullDeprecated

    

Show fields

[Anchor to RefundShippingLine](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
RefundShippingLine)[RefundShippingLine](/docs/api/admin-
graphql/latest/objects/RefundShippingLine)

•OBJECT

    

A shipping line item that's included in a refund.

Show fields

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
RefundShippingLine.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to shippingLine](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
RefundShippingLine.fields.shippingLine)shippingLine

•[ShippingLine!](/docs/api/admin-graphql/latest/objects/ShippingLine)

non-null

    

The `ShippingLine` resource associated to the refunded shipping line item.

Show fields

[Anchor to subtotalAmountSet](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
RefundShippingLine.fields.subtotalAmountSet)subtotalAmountSet

•[MoneyBag!](/docs/api/admin-graphql/latest/objects/MoneyBag)

non-null

    

The subtotal amount of the refund shipping line in shop and presentment
currencies.

Show fields

[Anchor to taxAmountSet](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
RefundShippingLine.fields.taxAmountSet)taxAmountSet

•[MoneyBag!](/docs/api/admin-graphql/latest/objects/MoneyBag)

non-null

    

The tax amount of the refund shipping line in shop and presentment currencies.

Show fields

[Anchor to Return](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Return)[Return](/docs/api/admin-graphql/latest/objects/Return)

•OBJECT

    

The `Return` object represents the intent of a buyer to ship one or more items
from an order back to a merchant or a third-party fulfillment location. A
return is associated with an [order](https://shopify.dev/docs/api/admin-
graphql/latest/objects/Order) and can include multiple return [line
items](https://shopify.dev/docs/api/admin-graphql/latest/objects/LineItem).
Each return has a [status](https://shopify.dev/docs/apps/build/orders-
fulfillment/returns-apps#return-statuses), which indicates the state of the
return.

Use the `Return` object to capture the financial, logistical, and business
intent of a return. For example, you can identify eligible items for a return
and issue customers a refund for returned items on behalf of the merchant.

Learn more about providing a [return management
workflow](https://shopify.dev/docs/apps/build/orders-fulfillment/returns-
apps/build-return-management) for merchants. You can also manage
[exchanges](https://shopify.dev/docs/apps/build/orders-fulfillment/returns-
apps/manage-exchanges), [reverse fulfillment
orders](https://shopify.dev/docs/apps/build/orders-fulfillment/returns-
apps/manage-reverse-fulfillment-orders), and [reverse
deliveries](https://shopify.dev/docs/apps/build/orders-fulfillment/returns-
apps/manage-reverse-deliveries) on behalf of merchants.

Show fields

[Anchor to closedAt](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Return.fields.closedAt)closedAt

•[DateTime](/docs/api/admin-graphql/latest/scalars/DateTime)

    

The date and time when the return was closed.

[Anchor to createdAt](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Return.fields.createdAt)createdAt

•[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime)

non-null

    

The date and time when the return was created.

[Anchor to decline](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Return.fields.decline)decline

•[ReturnDecline](/docs/api/admin-graphql/latest/objects/ReturnDecline)

    

Additional information about the declined return.

Show fields

[Anchor to exchangeLineItems](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Return.fields.exchangeLineItems)exchangeLineItems

•[ExchangeLineItemConnection!](/docs/api/admin-
graphql/latest/connections/ExchangeLineItemConnection)

non-null

    

The exchange line items attached to the return.

Show fields

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
Return.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to name](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Return.fields.name)name

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The name of the return.

[Anchor to order](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Return.fields.order)order

•[Order!](/docs/api/admin-graphql/latest/objects/Order)

non-null

    

The order that the return belongs to.

Show fields

[Anchor to refunds](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Return.fields.refunds)refunds

•[RefundConnection!](/docs/api/admin-
graphql/latest/connections/RefundConnection)

non-null

    

The list of refunds associated with the return.

Show fields

[Anchor to requestApprovedAt](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Return.fields.requestApprovedAt)requestApprovedAt

•[DateTime](/docs/api/admin-graphql/latest/scalars/DateTime)

    

The date and time when the return was approved.

[Anchor to returnLineItems](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Return.fields.returnLineItems)returnLineItems

•[ReturnLineItemTypeConnection!](/docs/api/admin-
graphql/latest/connections/ReturnLineItemTypeConnection)

non-null

    

The return line items attached to the return.

Show fields

[Anchor to returnShippingFees](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Return.fields.returnShippingFees)returnShippingFees

•[[ReturnShippingFee!]!](/docs/api/admin-
graphql/latest/objects/ReturnShippingFee)

non-null

    

The return shipping fees for the return.

Show fields

[Anchor to reverseFulfillmentOrders](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Return.fields.reverseFulfillmentOrders)reverseFulfillmentOrders

•[ReverseFulfillmentOrderConnection!](/docs/api/admin-
graphql/latest/connections/ReverseFulfillmentOrderConnection)

non-null

    

The list of reverse fulfillment orders for the return.

Show fields

[Anchor to status](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Return.fields.status)status

•[ReturnStatus!](/docs/api/admin-graphql/latest/enums/ReturnStatus)

non-null

    

The status of the return.

Show enum values

[Anchor to suggestedFinancialOutcome](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Return.fields.suggestedFinancialOutcome)suggestedFinancialOutcome

•[SuggestedReturnFinancialOutcome](/docs/api/admin-
graphql/latest/objects/SuggestedReturnFinancialOutcome)

    

A suggested financial outcome for the return.

Show fields

[Anchor to totalQuantity](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Return.fields.totalQuantity)totalQuantity

•[Int!](/docs/api/admin-graphql/latest/scalars/Int)

non-null

    

The sum of all return line item quantities for the return.

[Anchor to suggestedRefund](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Return.fields.suggestedRefund)suggestedRefund

•[SuggestedReturnRefund](/docs/api/admin-
graphql/latest/objects/SuggestedReturnRefund)

Deprecated

    

Show fields

[Anchor to ReturnableFulfillment](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ReturnableFulfillment)[ReturnableFulfillment](/docs/api/admin-
graphql/latest/objects/ReturnableFulfillment)

•OBJECT

    

A returnable fulfillment, which is an order that has been delivered and is
eligible to be returned to the merchant.

Show fields

[Anchor to fulfillment](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ReturnableFulfillment.fields.fulfillment)fulfillment

•[Fulfillment!](/docs/api/admin-graphql/latest/objects/Fulfillment)

non-null

    

The fulfillment that the returnable fulfillment refers to.

Show fields

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
ReturnableFulfillment.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

The unique ID of the Returnable Fulfillment.

[Anchor to returnableFulfillmentLineItems](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ReturnableFulfillment.fields.returnableFulfillmentLineItems)returnableFulfillmentLineItems

•[ReturnableFulfillmentLineItemConnection!](/docs/api/admin-
graphql/latest/connections/ReturnableFulfillmentLineItemConnection)

non-null

    

The list of returnable fulfillment line items.

Show fields

[Anchor to ReturnLineItem](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ReturnLineItem)[ReturnLineItem](/docs/api/admin-
graphql/latest/objects/ReturnLineItem)

•OBJECT

    

A return line item.

Show fields

[Anchor to customerNote](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ReturnLineItem.fields.customerNote)customerNote

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

A note from the customer that describes the item to be returned. Maximum
length: 300 characters.

[Anchor to fulfillmentLineItem](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ReturnLineItem.fields.fulfillmentLineItem)fulfillmentLineItem

•[FulfillmentLineItem!](/docs/api/admin-
graphql/latest/objects/FulfillmentLineItem)

non-null

    

The fulfillment line item from which items are returned.

Show fields

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
ReturnLineItem.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to processableQuantity](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ReturnLineItem.fields.processableQuantity)processableQuantity

•[Int!](/docs/api/admin-graphql/latest/scalars/Int)

non-null

    

The quantity that can be processed.

[Anchor to processedQuantity](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ReturnLineItem.fields.processedQuantity)processedQuantity

•[Int!](/docs/api/admin-graphql/latest/scalars/Int)

non-null

    

The quantity that has been processed.

[Anchor to quantity](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-ReturnLineItem.fields.quantity)quantity

•[Int!](/docs/api/admin-graphql/latest/scalars/Int)

non-null

    

The quantity being returned.

[Anchor to refundableQuantity](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ReturnLineItem.fields.refundableQuantity)refundableQuantity

•[Int!](/docs/api/admin-graphql/latest/scalars/Int)

non-null

    

The quantity that can be refunded.

[Anchor to refundedQuantity](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ReturnLineItem.fields.refundedQuantity)refundedQuantity

•[Int!](/docs/api/admin-graphql/latest/scalars/Int)

non-null

    

The quantity that was refunded.

[Anchor to restockingFee](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ReturnLineItem.fields.restockingFee)restockingFee

•[RestockingFee](/docs/api/admin-graphql/latest/objects/RestockingFee)

    

The restocking fee for the return line item.

Show fields

[Anchor to returnReason](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ReturnLineItem.fields.returnReason)returnReason

•[ReturnReason!](/docs/api/admin-graphql/latest/enums/ReturnReason)

non-null

    

The reason for returning the item.

Show enum values

[Anchor to returnReasonNote](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ReturnLineItem.fields.returnReasonNote)returnReasonNote

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

Additional information about the reason for the return. Maximum length: 255
characters.

[Anchor to totalWeight](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ReturnLineItem.fields.totalWeight)totalWeight

•[Weight](/docs/api/admin-graphql/latest/objects/Weight)

    

The total weight of the item.

Show fields

[Anchor to unprocessedQuantity](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ReturnLineItem.fields.unprocessedQuantity)unprocessedQuantity

•[Int!](/docs/api/admin-graphql/latest/scalars/Int)

non-null

    

The quantity that has't been processed.

[Anchor to withCodeDiscountedTotalPriceSet](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ReturnLineItem.fields.withCodeDiscountedTotalPriceSet)withCodeDiscountedTotalPriceSet

•[MoneyBag!](/docs/api/admin-graphql/latest/objects/MoneyBag)

non-null

    

The total line price after all discounts on the line item, including both line
item level discounts and code-based line item discounts, are applied.

Show fields

[Anchor to ReverseDelivery](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ReverseDelivery)[ReverseDelivery](/docs/api/admin-
graphql/latest/objects/ReverseDelivery)

•OBJECT

    

A reverse delivery is a post-fulfillment object that represents a buyer
sending a package to a merchant. For example, a buyer requests a return, and a
merchant sends the buyer a shipping label. The reverse delivery contains the
context of the items sent back, how they're being sent back (for example, a
shipping label), and the current state of the delivery (tracking information).

Show fields

[Anchor to deliverable](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ReverseDelivery.fields.deliverable)deliverable

•[ReverseDeliveryDeliverable](/docs/api/admin-
graphql/latest/unions/ReverseDeliveryDeliverable)

    

The deliverable associated with the reverse delivery.

Show union types

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
ReverseDelivery.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

The ID of the reverse delivery.

[Anchor to reverseDeliveryLineItems](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ReverseDelivery.fields.reverseDeliveryLineItems)reverseDeliveryLineItems

•[ReverseDeliveryLineItemConnection!](/docs/api/admin-
graphql/latest/connections/ReverseDeliveryLineItemConnection)

non-null

    

The reverse delivery line items attached to the reverse delivery.

Show fields

[Anchor to reverseFulfillmentOrder](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ReverseDelivery.fields.reverseFulfillmentOrder)reverseFulfillmentOrder

•[ReverseFulfillmentOrder!](/docs/api/admin-
graphql/latest/objects/ReverseFulfillmentOrder)

non-null

    

The `ReverseFulfillmentOrder` associated with the reverse delivery.

Show fields

[Anchor to ReverseDeliveryLineItem](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ReverseDeliveryLineItem)[ReverseDeliveryLineItem](/docs/api/admin-
graphql/latest/objects/ReverseDeliveryLineItem)

•OBJECT

    

The details about a reverse delivery line item.

Show fields

[Anchor to dispositions](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ReverseDeliveryLineItem.fields.dispositions)dispositions

•[[ReverseFulfillmentOrderDisposition!]!](/docs/api/admin-
graphql/latest/objects/ReverseFulfillmentOrderDisposition)

non-null

    

The dispositions of the item.

Show fields

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
ReverseDeliveryLineItem.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to quantity](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-ReverseDeliveryLineItem.fields.quantity)quantity

•[Int!](/docs/api/admin-graphql/latest/scalars/Int)

non-null

    

The expected number of units.

[Anchor to reverseFulfillmentOrderLineItem](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ReverseDeliveryLineItem.fields.reverseFulfillmentOrderLineItem)reverseFulfillmentOrderLineItem

•[ReverseFulfillmentOrderLineItem!](/docs/api/admin-
graphql/latest/objects/ReverseFulfillmentOrderLineItem)

non-null

    

The corresponding reverse fulfillment order line item.

Show fields

[Anchor to ReverseFulfillmentOrder](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ReverseFulfillmentOrder)[ReverseFulfillmentOrder](/docs/api/admin-
graphql/latest/objects/ReverseFulfillmentOrder)

•OBJECT

    

A group of one or more items in a return that will be processed at a
fulfillment service. There can be more than one reverse fulfillment order for
a return at a given location.

Show fields

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
ReverseFulfillmentOrder.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to lineItems](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-ReverseFulfillmentOrder.fields.lineItems)lineItems

•[ReverseFulfillmentOrderLineItemConnection!](/docs/api/admin-
graphql/latest/connections/ReverseFulfillmentOrderLineItemConnection)

non-null

    

The list of reverse fulfillment order line items for the reverse fulfillment
order.

Show fields

[Anchor to order](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-ReverseFulfillmentOrder.fields.order)order

•[Order](/docs/api/admin-graphql/latest/objects/Order)

    

The order associated with the reverse fulfillment order.

Show fields

[Anchor to reverseDeliveries](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ReverseFulfillmentOrder.fields.reverseDeliveries)reverseDeliveries

•[ReverseDeliveryConnection!](/docs/api/admin-
graphql/latest/connections/ReverseDeliveryConnection)

non-null

    

The list of reverse deliveries for the reverse fulfillment order.

Show fields

[Anchor to status](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-ReverseFulfillmentOrder.fields.status)status

•[ReverseFulfillmentOrderStatus!](/docs/api/admin-
graphql/latest/enums/ReverseFulfillmentOrderStatus)

non-null

    

The status of the reverse fulfillment order.

Show enum values

[Anchor to thirdPartyConfirmation](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ReverseFulfillmentOrder.fields.thirdPartyConfirmation)thirdPartyConfirmation

•[ReverseFulfillmentOrderThirdPartyConfirmation](/docs/api/admin-
graphql/latest/objects/ReverseFulfillmentOrderThirdPartyConfirmation)

    

The current confirmation for the reverse fulfillment order from a third-party
logistics service. If no third-party service is involved, then this value is
`nil`.

Show fields

[Anchor to ReverseFulfillmentOrderDisposition](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ReverseFulfillmentOrderDisposition)[ReverseFulfillmentOrderDisposition](/docs/api/admin-
graphql/latest/objects/ReverseFulfillmentOrderDisposition)

•OBJECT

    

The details of the arrangement of an item.

Show fields

[Anchor to createdAt](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-ReverseFulfillmentOrderDisposition.fields.createdAt)createdAt

•[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime)

non-null

    

The date and time when the disposition was created.

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
ReverseFulfillmentOrderDisposition.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to location](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-ReverseFulfillmentOrderDisposition.fields.location)location

•[Location](/docs/api/admin-graphql/latest/objects/Location)

    

The location where the disposition occurred.

Show fields

[Anchor to quantity](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-ReverseFulfillmentOrderDisposition.fields.quantity)quantity

•[Int!](/docs/api/admin-graphql/latest/scalars/Int)

non-null

    

The number of disposed units.

[Anchor to type](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-ReverseFulfillmentOrderDisposition.fields.type)type

•[ReverseFulfillmentOrderDispositionType!](/docs/api/admin-
graphql/latest/enums/ReverseFulfillmentOrderDispositionType)

non-null

    

The final arrangement of an item.

Show enum values

[Anchor to ReverseFulfillmentOrderLineItem](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ReverseFulfillmentOrderLineItem)[ReverseFulfillmentOrderLineItem](/docs/api/admin-
graphql/latest/objects/ReverseFulfillmentOrderLineItem)

•OBJECT

    

The details about a reverse fulfillment order line item.

Show fields

[Anchor to dispositions](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ReverseFulfillmentOrderLineItem.fields.dispositions)dispositions

•[[ReverseFulfillmentOrderDisposition!]!](/docs/api/admin-
graphql/latest/objects/ReverseFulfillmentOrderDisposition)

non-null

    

The dispositions of the item.

Show fields

[Anchor to fulfillmentLineItem](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ReverseFulfillmentOrderLineItem.fields.fulfillmentLineItem)fulfillmentLineItem

•[FulfillmentLineItem](/docs/api/admin-
graphql/latest/objects/FulfillmentLineItem)

    

The corresponding fulfillment line item for a reverse fulfillment order line
item.

Show fields

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
ReverseFulfillmentOrderLineItem.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to totalQuantity](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ReverseFulfillmentOrderLineItem.fields.totalQuantity)totalQuantity

•[Int!](/docs/api/admin-graphql/latest/scalars/Int)

non-null

    

The total number of units to be processed.

[Anchor to SaleAdditionalFee](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
SaleAdditionalFee)[SaleAdditionalFee](/docs/api/admin-
graphql/latest/objects/SaleAdditionalFee)

•OBJECT

    

The additional fee details for a line item.

Show fields

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
SaleAdditionalFee.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to name](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-SaleAdditionalFee.fields.name)name

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The name of the additional fee.

[Anchor to price](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-SaleAdditionalFee.fields.price)price

•[MoneyBag!](/docs/api/admin-graphql/latest/objects/MoneyBag)

non-null

    

The price of the additional fee.

Show fields

[Anchor to taxLines](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-SaleAdditionalFee.fields.taxLines)taxLines

•[[TaxLine!]!](/docs/api/admin-graphql/latest/objects/TaxLine)

non-null

    

A list of taxes charged on the additional fee.

Show fields

[Anchor to SavedSearch](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
SavedSearch)[SavedSearch](/docs/api/admin-graphql/latest/objects/SavedSearch)

•OBJECT

    

A saved search is a representation of a search query saved in the admin.

Show fields

[Anchor to filters](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-SavedSearch.fields.filters)filters

•[[SearchFilter!]!](/docs/api/admin-graphql/latest/objects/SearchFilter)

non-null

    

The filters of a saved search.

Show fields

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
SavedSearch.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to legacyResourceId](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
SavedSearch.fields.legacyResourceId)legacyResourceId

•[UnsignedInt64!](/docs/api/admin-graphql/latest/scalars/UnsignedInt64)

non-null

    

The ID of the corresponding resource in the REST Admin API.

[Anchor to name](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-SavedSearch.fields.name)name

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The name of a saved search.

[Anchor to query](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-SavedSearch.fields.query)query

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The query string of a saved search. This includes search terms and filters.

[Anchor to resourceType](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
SavedSearch.fields.resourceType)resourceType

•[SearchResultType!](/docs/api/admin-graphql/latest/enums/SearchResultType)

non-null

    

The type of resource this saved search is searching in.

Show enum values

[Anchor to searchTerms](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
SavedSearch.fields.searchTerms)searchTerms

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The search terms of a saved search.

[Anchor to ScriptTag](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-ScriptTag)[ScriptTag](/docs/api/admin-graphql/latest/objects/ScriptTag)

•OBJECT

    

Theme app extensions

If your app integrates with a Shopify theme and you plan to submit it to the
Shopify App Store, you must use theme app extensions instead of Script tags.
Script tags can only be used with vintage themes. [Learn more](/apps/online-
store#what-integration-method-should-i-use).

Script tag deprecation

Script tags will be sunset for the **Order status** page on August 28, 2025.
[Upgrade to Checkout Extensibility](https://www.shopify.com/plus/upgrading-to-
checkout-extensibility) before this date. [Shopify
Scripts](/docs/api/liquid/objects#script) will continue to work alongside
Checkout Extensibility until August 28, 2025.

A script tag represents remote JavaScript code that is loaded into the pages
of a shop's storefront or the **Order status** page of checkout.

Show fields

[Anchor to cache](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-ScriptTag.fields.cache)cache

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether the Shopify CDN can cache and serve the script tag. If `true`, then
the script will be cached and served by the CDN. The cache expires 15 minutes
after the script tag is successfully returned. If `false`, then the script
will be served as is.

[Anchor to createdAt](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-ScriptTag.fields.createdAt)createdAt

•[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime)

non-null

    

The date and time when the script tag was created.

[Anchor to displayScope](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ScriptTag.fields.displayScope)displayScope

•[ScriptTagDisplayScope!](/docs/api/admin-
graphql/latest/enums/ScriptTagDisplayScope)

non-null

    

The page or pages on the online store that the script should be included.

Show enum values

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
ScriptTag.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to legacyResourceId](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ScriptTag.fields.legacyResourceId)legacyResourceId

•[UnsignedInt64!](/docs/api/admin-graphql/latest/scalars/UnsignedInt64)

non-null

    

The ID of the corresponding resource in the REST Admin API.

[Anchor to src](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
ScriptTag.fields.src)src

•[URL!](/docs/api/admin-graphql/latest/scalars/URL)

non-null

    

The URL to the remote script.

[Anchor to updatedAt](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-ScriptTag.fields.updatedAt)updatedAt

•[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime)

non-null

    

The date and time when the script tag was last updated.

[Anchor to Segment](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Segment)[Segment](/docs/api/admin-graphql/latest/objects/Segment)

•OBJECT

    

A dynamic collection of customers based on specific criteria.

Show fields

[Anchor to creationDate](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Segment.fields.creationDate)creationDate

•[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime)

non-null

    

The date and time when the segment was added to the store.

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
Segment.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to lastEditDate](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Segment.fields.lastEditDate)lastEditDate

•[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime)

non-null

    

The date and time when the segment was last updated.

[Anchor to name](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Segment.fields.name)name

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The name of the segment.

[Anchor to query](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Segment.fields.query)query

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

A precise definition of the segment. The definition is composed of a
combination of conditions on facts about customers.

[Anchor to SellingPlan](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
SellingPlan)[SellingPlan](/docs/api/admin-graphql/latest/objects/SellingPlan)

•OBJECT

    

Represents how a product can be sold and purchased. Selling plans and
associated records (selling plan groups and policies) are deleted 48 hours
after a merchant uninstalls their subscriptions app. We recommend backing up
these records if you need to restore them later.

For more information on selling plans, refer to [_Creating and managing
selling plans_](https://shopify.dev/docs/apps/selling-
strategies/subscriptions/selling-plans).

Show fields

[Anchor to billingPolicy](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
SellingPlan.fields.billingPolicy)billingPolicy

•[SellingPlanBillingPolicy!](/docs/api/admin-
graphql/latest/unions/SellingPlanBillingPolicy)

non-null

    

A selling plan policy which describes the recurring billing details.

Show union types

[Anchor to category](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-SellingPlan.fields.category)category

•[SellingPlanCategory](/docs/api/admin-
graphql/latest/enums/SellingPlanCategory)

    

The category used to classify the selling plan for reporting purposes.

Show enum values

[Anchor to createdAt](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-SellingPlan.fields.createdAt)createdAt

•[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime)

non-null

    

The date and time when the selling plan was created.

[Anchor to deliveryPolicy](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
SellingPlan.fields.deliveryPolicy)deliveryPolicy

•[SellingPlanDeliveryPolicy!](/docs/api/admin-
graphql/latest/unions/SellingPlanDeliveryPolicy)

non-null

    

A selling plan policy which describes the delivery details.

Show union types

[Anchor to description](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
SellingPlan.fields.description)description

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

Buyer facing string which describes the selling plan commitment.

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
SellingPlan.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to inventoryPolicy](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
SellingPlan.fields.inventoryPolicy)inventoryPolicy

•[SellingPlanInventoryPolicy](/docs/api/admin-
graphql/latest/objects/SellingPlanInventoryPolicy)

    

When to reserve inventory for a selling plan.

Show fields

[Anchor to metafield](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-SellingPlan.fields.metafield)metafield

•[Metafield](/docs/api/admin-graphql/latest/objects/Metafield)

    

A [custom field](https://shopify.dev/docs/apps/build/custom-data), including
its `namespace` and `key`, that's associated with a Shopify resource for the
purposes of adding and storing additional information.

Show fields

[Anchor to metafields](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
SellingPlan.fields.metafields)metafields

•[MetafieldConnection!](/docs/api/admin-
graphql/latest/connections/MetafieldConnection)

non-null

    

A list of [custom fields](https://shopify.dev/docs/apps/build/custom-data)
that a merchant associates with a Shopify resource.

Show fields

[Anchor to name](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-SellingPlan.fields.name)name

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

A customer-facing description of the selling plan.

If your store supports multiple currencies, then don't include country-
specific pricing content, such as "Buy monthly, get 10$ CAD off". This field
won't be converted to reflect different currencies.

[Anchor to options](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-SellingPlan.fields.options)options

•[[String!]!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The values of all options available on the selling plan. Selling plans are
grouped together in Liquid when they're created by the same app, and have the
same `selling_plan_group.name` and `selling_plan_group.options` values.

[Anchor to position](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-SellingPlan.fields.position)position

•[Int](/docs/api/admin-graphql/latest/scalars/Int)

    

Relative position of the selling plan for display. A lower position will be
displayed before a higher position.

[Anchor to pricingPolicies](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
SellingPlan.fields.pricingPolicies)pricingPolicies

•[[SellingPlanPricingPolicy!]!](/docs/api/admin-
graphql/latest/unions/SellingPlanPricingPolicy)

non-null

    

Selling plan pricing details.

Show union types

[Anchor to translations](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
SellingPlan.fields.translations)translations

•[[Translation!]!](/docs/api/admin-graphql/latest/objects/Translation)

non-null

    

The published translations associated with the resource.

Show fields

[Anchor to metafieldDefinitions](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
SellingPlan.fields.metafieldDefinitions)metafieldDefinitions

•[MetafieldDefinitionConnection!](/docs/api/admin-
graphql/latest/connections/MetafieldDefinitionConnection)

non-nullDeprecated

    

Show fields

[Anchor to SellingPlanGroup](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
SellingPlanGroup)[SellingPlanGroup](/docs/api/admin-
graphql/latest/objects/SellingPlanGroup)

•OBJECT

    

Represents a selling method (for example, "Subscribe and save" or "Pre-paid").
Selling plan groups and associated records (selling plans and policies) are
deleted 48 hours after a merchant uninstalls their subscriptions app. We
recommend backing up these records if you need to restore them later.

Show fields

[Anchor to appId](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-SellingPlanGroup.fields.appId)appId

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The ID for app, exposed in Liquid and product JSON.

[Anchor to appliesToProduct](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
SellingPlanGroup.fields.appliesToProduct)appliesToProduct

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether the given product is directly associated to the selling plan group.

Show arguments

### Arguments

[Anchor to productId](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-SellingPlanGroup.fields.appliesToProduct.arguments.productId)productId

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

required

    

The ID of the product.

* * *

[Anchor to appliesToProductVariant](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
SellingPlanGroup.fields.appliesToProductVariant)appliesToProductVariant

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether the given product variant is directly associated to the selling plan
group.

Show arguments

### Arguments

[Anchor to productVariantId](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
SellingPlanGroup.fields.appliesToProductVariant.arguments.productVariantId)productVariantId

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

required

    

The ID of the product.

* * *

[Anchor to appliesToProductVariants](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
SellingPlanGroup.fields.appliesToProductVariants)appliesToProductVariants

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether any of the product variants of the given product are associated to the
selling plan group.

Show arguments

### Arguments

[Anchor to productId](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-
SellingPlanGroup.fields.appliesToProductVariants.arguments.productId)productId

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

required

    

The ID of the product.

* * *

[Anchor to createdAt](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-SellingPlanGroup.fields.createdAt)createdAt

•[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime)

non-null

    

The date and time when the selling plan group was created.

[Anchor to description](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
SellingPlanGroup.fields.description)description

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The merchant-facing description of the selling plan group.

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
SellingPlanGroup.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to merchantCode](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
SellingPlanGroup.fields.merchantCode)merchantCode

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The merchant-facing label of the selling plan group.

[Anchor to name](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-SellingPlanGroup.fields.name)name

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The buyer-facing label of the selling plan group.

[Anchor to options](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-SellingPlanGroup.fields.options)options

•[[String!]!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The values of all options available on the selling plan group. Selling plans
are grouped together in Liquid when they're created by the same app, and have
the same `selling_plan_group.name` and `selling_plan_group.options` values.

[Anchor to position](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-SellingPlanGroup.fields.position)position

•[Int](/docs/api/admin-graphql/latest/scalars/Int)

    

The relative position of the selling plan group for display.

[Anchor to products](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-SellingPlanGroup.fields.products)products

•[ProductConnection!](/docs/api/admin-
graphql/latest/connections/ProductConnection)

non-null

    

Products associated to the selling plan group.

Show fields

[Anchor to productsCount](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
SellingPlanGroup.fields.productsCount)productsCount

•[Count](/docs/api/admin-graphql/latest/objects/Count)

    

A count of products associated to the selling plan group.

Show fields

[Anchor to productVariants](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
SellingPlanGroup.fields.productVariants)productVariants

•[ProductVariantConnection!](/docs/api/admin-
graphql/latest/connections/ProductVariantConnection)

non-null

    

Product variants associated to the selling plan group.

Show fields

[Anchor to productVariantsCount](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
SellingPlanGroup.fields.productVariantsCount)productVariantsCount

•[Count](/docs/api/admin-graphql/latest/objects/Count)

    

A count of product variants associated to the selling plan group.

Show fields

[Anchor to sellingPlans](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
SellingPlanGroup.fields.sellingPlans)sellingPlans

•[SellingPlanConnection!](/docs/api/admin-
graphql/latest/connections/SellingPlanConnection)

non-null

    

Selling plans associated to the selling plan group.

Show fields

[Anchor to summary](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-SellingPlanGroup.fields.summary)summary

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

A summary of the policies associated to the selling plan group.

[Anchor to translations](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
SellingPlanGroup.fields.translations)translations

•[[Translation!]!](/docs/api/admin-graphql/latest/objects/Translation)

non-null

    

The published translations associated with the resource.

Show fields

[Anchor to ServerPixel](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ServerPixel)[ServerPixel](/docs/api/admin-graphql/latest/objects/ServerPixel)

•OBJECT

    

A server pixel stores configuration for streaming customer interactions to an
EventBridge or PubSub endpoint.

Show fields

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
ServerPixel.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to status](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-ServerPixel.fields.status)status

•[ServerPixelStatus](/docs/api/admin-graphql/latest/enums/ServerPixelStatus)

    

The current state of this server pixel.

Show enum values

[Anchor to webhookEndpointAddress](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ServerPixel.fields.webhookEndpointAddress)webhookEndpointAddress

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

Address of the EventBridge or PubSub endpoint.

[Anchor to Shop](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Shop)[Shop](/docs/api/admin-graphql/latest/objects/Shop)

•OBJECT

    

Represents a collection of general settings and information about the shop.

Show fields

[Anchor to accountOwner](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Shop.fields.accountOwner)accountOwner

•[StaffMember!](/docs/api/admin-graphql/latest/objects/StaffMember)

non-null

    

Account owner information.

Show fields

[Anchor to alerts](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Shop.fields.alerts)alerts

•[[ShopAlert!]!](/docs/api/admin-graphql/latest/objects/ShopAlert)

non-null

    

A list of the shop's active alert messages that appear in the Shopify admin.

Show fields

[Anchor to allProductCategoriesList](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Shop.fields.allProductCategoriesList)allProductCategoriesList

•[[TaxonomyCategory!]!](/docs/api/admin-
graphql/latest/objects/TaxonomyCategory)

non-null

    

A list of the shop's product categories. Limit: 1000 product categories.

Show fields

[Anchor to availableChannelApps](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Shop.fields.availableChannelApps)availableChannelApps

•[AppConnection!](/docs/api/admin-graphql/latest/connections/AppConnection)

non-null

    

The list of sales channels not currently installed on the shop.

Show fields

[Anchor to billingAddress](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Shop.fields.billingAddress)billingAddress

•[ShopAddress!](/docs/api/admin-graphql/latest/objects/ShopAddress)

non-null

    

The shop's billing address information.

Show fields

[Anchor to channelDefinitionsForInstalledChannels](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Shop.fields.channelDefinitionsForInstalledChannels)channelDefinitionsForInstalledChannels

•[[AvailableChannelDefinitionsByChannel!]!](/docs/api/admin-
graphql/latest/objects/AvailableChannelDefinitionsByChannel)

non-null

    

List of all channel definitions associated with a shop.

Show fields

[Anchor to checkoutApiSupported](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Shop.fields.checkoutApiSupported)checkoutApiSupported

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Specifies whether the shop supports checkouts via Checkout API.

[Anchor to contactEmail](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Shop.fields.contactEmail)contactEmail

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The public-facing contact email address for the shop. Customers will use this
email to communicate with the shop owner.

[Anchor to countriesInShippingZones](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Shop.fields.countriesInShippingZones)countriesInShippingZones

•[CountriesInShippingZones!](/docs/api/admin-
graphql/latest/objects/CountriesInShippingZones)

non-null

    

Countries that have been defined in shipping zones for the shop.

Show fields

[Anchor to createdAt](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Shop.fields.createdAt)createdAt

•[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime)

non-null

    

The date and time when the shop was created.

[Anchor to currencyCode](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Shop.fields.currencyCode)currencyCode

•[CurrencyCode!](/docs/api/admin-graphql/latest/enums/CurrencyCode)

non-null

    

The three letter code for the currency that the shop sells in.

Show enum values

[Anchor to currencyFormats](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Shop.fields.currencyFormats)currencyFormats

•[CurrencyFormats!](/docs/api/admin-graphql/latest/objects/CurrencyFormats)

non-null

    

How currencies are displayed on your store.

Show fields

[Anchor to currencySettings](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Shop.fields.currencySettings)currencySettings

•[CurrencySettingConnection!](/docs/api/admin-
graphql/latest/connections/CurrencySettingConnection)

non-null

    

The presentment currency settings for the shop excluding the shop's own
currency.

Show fields

[Anchor to customerAccounts](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Shop.fields.customerAccounts)customerAccounts

•[ShopCustomerAccountsSetting!](/docs/api/admin-
graphql/latest/enums/ShopCustomerAccountsSetting)

non-null

    

Whether customer accounts are required, optional, or disabled for the shop.

Show enum values

[Anchor to customerAccountsV2](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Shop.fields.customerAccountsV2)customerAccountsV2

•[CustomerAccountsV2!](/docs/api/admin-
graphql/latest/objects/CustomerAccountsV2)

non-null

    

Information about the shop's customer accounts.

Show fields

[Anchor to customerTags](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Shop.fields.customerTags)customerTags

•[StringConnection!](/docs/api/admin-
graphql/latest/connections/StringConnection)

non-null

    

A list of tags that have been added to customer accounts.

Show fields

[Anchor to description](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Shop.fields.description)description

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The shop's meta description used in search engine results.

[Anchor to draftOrderTags](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Shop.fields.draftOrderTags)draftOrderTags

•[StringConnection!](/docs/api/admin-
graphql/latest/connections/StringConnection)

non-null

    

A list of tags that have been added to draft orders.

Show fields

[Anchor to email](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Shop.fields.email)email

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The shop owner's email address. Shopify will use this email address to
communicate with the shop owner.

[Anchor to enabledPresentmentCurrencies](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Shop.fields.enabledPresentmentCurrencies)enabledPresentmentCurrencies

•[[CurrencyCode!]!](/docs/api/admin-graphql/latest/enums/CurrencyCode)

non-null

    

The presentment currencies enabled for the shop.

Show enum values

[Anchor to entitlements](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Shop.fields.entitlements)entitlements

•[EntitlementsType!](/docs/api/admin-graphql/latest/objects/EntitlementsType)

non-null

    

The entitlements for a shop.

Show fields

[Anchor to features](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Shop.fields.features)features

•[ShopFeatures!](/docs/api/admin-graphql/latest/objects/ShopFeatures)

non-null

    

The set of features enabled for the shop.

Show fields

[Anchor to fulfillmentServices](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Shop.fields.fulfillmentServices)fulfillmentServices

•[[FulfillmentService!]!](/docs/api/admin-
graphql/latest/objects/FulfillmentService)

non-null

    

List of the shop's installed fulfillment services.

Show fields

[Anchor to ianaTimezone](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Shop.fields.ianaTimezone)ianaTimezone

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The shop's time zone as defined by the IANA.

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
Shop.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to marketingSmsConsentEnabledAtCheckout](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Shop.fields.marketingSmsConsentEnabledAtCheckout)marketingSmsConsentEnabledAtCheckout

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether SMS marketing has been enabled on the shop's checkout configuration
settings.

[Anchor to merchantApprovalSignals](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Shop.fields.merchantApprovalSignals)merchantApprovalSignals

•[MerchantApprovalSignals](/docs/api/admin-
graphql/latest/objects/MerchantApprovalSignals)

    

The approval signals for a shop to support onboarding to channel apps.

Show fields

[Anchor to metafield](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Shop.fields.metafield)metafield

•[Metafield](/docs/api/admin-graphql/latest/objects/Metafield)

    

A [custom field](https://shopify.dev/docs/apps/build/custom-data), including
its `namespace` and `key`, that's associated with a Shopify resource for the
purposes of adding and storing additional information.

Show fields

[Anchor to metafields](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Shop.fields.metafields)metafields

•[MetafieldConnection!](/docs/api/admin-
graphql/latest/connections/MetafieldConnection)

non-null

    

A list of [custom fields](https://shopify.dev/docs/apps/build/custom-data)
that a merchant associates with a Shopify resource.

Show fields

[Anchor to myshopifyDomain](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Shop.fields.myshopifyDomain)myshopifyDomain

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The shop's .myshopify.com domain name.

[Anchor to name](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Shop.fields.name)name

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The shop's name.

[Anchor to navigationSettings](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Shop.fields.navigationSettings)navigationSettings

•[[NavigationItem!]!](/docs/api/admin-graphql/latest/objects/NavigationItem)

non-null

    

The shop's settings related to navigation.

Show fields

[Anchor to orderNumberFormatPrefix](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Shop.fields.orderNumberFormatPrefix)orderNumberFormatPrefix

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The prefix that appears before order numbers.

[Anchor to orderNumberFormatSuffix](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Shop.fields.orderNumberFormatSuffix)orderNumberFormatSuffix

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The suffix that appears after order numbers.

[Anchor to orderTags](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Shop.fields.orderTags)orderTags

•[StringConnection!](/docs/api/admin-
graphql/latest/connections/StringConnection)

non-null

    

A list of tags that have been added to orders.

Show fields

[Anchor to paymentSettings](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Shop.fields.paymentSettings)paymentSettings

•[PaymentSettings!](/docs/api/admin-graphql/latest/objects/PaymentSettings)

non-null

    

The shop's settings related to payments.

Show fields

[Anchor to plan](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Shop.fields.plan)plan

•[ShopPlan!](/docs/api/admin-graphql/latest/objects/ShopPlan)

non-null

    

The shop's billing plan.

Show fields

[Anchor to primaryDomain](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Shop.fields.primaryDomain)primaryDomain

•[Domain!](/docs/api/admin-graphql/latest/objects/Domain)

non-null

    

The primary domain of the shop's online store.

Show fields

[Anchor to resourceLimits](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Shop.fields.resourceLimits)resourceLimits

•[ShopResourceLimits!](/docs/api/admin-
graphql/latest/objects/ShopResourceLimits)

non-null

    

The shop's limits for specific resources. For example, the maximum number
ofvariants allowed per product, or the maximum number of locations allowed.

Show fields

[Anchor to richTextEditorUrl](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Shop.fields.richTextEditorUrl)richTextEditorUrl

•[URL!](/docs/api/admin-graphql/latest/scalars/URL)

non-null

    

The URL of the rich text editor that can be used for mobile devices.

[Anchor to search](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Shop.fields.search)search

•[SearchResultConnection!](/docs/api/admin-
graphql/latest/connections/SearchResultConnection)

non-null

    

Fetches a list of admin search results by a specified query.

Show fields

[Anchor to searchFilters](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Shop.fields.searchFilters)searchFilters

•[SearchFilterOptions!](/docs/api/admin-
graphql/latest/objects/SearchFilterOptions)

non-null

    

The list of search filter options for the shop. These can be used to filter
productvisibility for the shop.

Show fields

[Anchor to setupRequired](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Shop.fields.setupRequired)setupRequired

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether the shop has outstanding setup steps.

[Anchor to shipsToCountries](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Shop.fields.shipsToCountries)shipsToCountries

•[[CountryCode!]!](/docs/api/admin-graphql/latest/enums/CountryCode)

non-null

    

The list of countries that the shop ships to.

Show enum values

[Anchor to shopOwnerName](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Shop.fields.shopOwnerName)shopOwnerName

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The name of the shop owner.

[Anchor to shopPolicies](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Shop.fields.shopPolicies)shopPolicies

•[[ShopPolicy!]!](/docs/api/admin-graphql/latest/objects/ShopPolicy)

non-null

    

The list of all legal policies associated with a shop.

Show fields

[Anchor to storefrontAccessTokens](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Shop.fields.storefrontAccessTokens)storefrontAccessTokens

•[StorefrontAccessTokenConnection!](/docs/api/admin-
graphql/latest/connections/StorefrontAccessTokenConnection)

non-null

    

The storefront access token of a private application. These are scoped per-
application.

Show fields

[Anchor to taxesIncluded](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Shop.fields.taxesIncluded)taxesIncluded

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether applicable taxes are included in the shop's product prices.

[Anchor to taxShipping](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Shop.fields.taxShipping)taxShipping

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether the shop charges taxes for shipping.

[Anchor to timezoneAbbreviation](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Shop.fields.timezoneAbbreviation)timezoneAbbreviation

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The shop's time zone abbreviation.

[Anchor to timezoneOffset](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Shop.fields.timezoneOffset)timezoneOffset

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The shop's time zone offset.

[Anchor to timezoneOffsetMinutes](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Shop.fields.timezoneOffsetMinutes)timezoneOffsetMinutes

•[Int!](/docs/api/admin-graphql/latest/scalars/Int)

non-null

    

The shop's time zone offset expressed as a number of minutes.

[Anchor to transactionalSmsDisabled](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Shop.fields.transactionalSmsDisabled)transactionalSmsDisabled

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether transactional SMS sent by Shopify have been disabled for a shop.

[Anchor to translations](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Shop.fields.translations)translations

•[[Translation!]!](/docs/api/admin-graphql/latest/objects/Translation)

non-null

    

The published translations associated with the resource.

Show fields

[Anchor to unitSystem](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Shop.fields.unitSystem)unitSystem

•[UnitSystem!](/docs/api/admin-graphql/latest/enums/UnitSystem)

non-null

    

The shop's unit system for weights and measures.

Show enum values

[Anchor to updatedAt](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Shop.fields.updatedAt)updatedAt

•[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime)

non-null

    

The date and time when the shop was last updated.

[Anchor to url](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
Shop.fields.url)url

•[URL!](/docs/api/admin-graphql/latest/scalars/URL)

non-null

    

The URL of the shop's online store.

[Anchor to weightUnit](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Shop.fields.weightUnit)weightUnit

•[WeightUnit!](/docs/api/admin-graphql/latest/enums/WeightUnit)

non-null

    

The shop's primary unit of weight for products and shipping.

Show enum values

[Anchor to allProductCategories](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Shop.fields.allProductCategories)allProductCategories

•[[ProductCategory!]!](/docs/api/admin-graphql/latest/objects/ProductCategory)

non-nullDeprecated

    

Show fields

[Anchor to analyticsToken](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Shop.fields.analyticsToken)analyticsToken

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-nullDeprecated

    

[Anchor to assignedFulfillmentOrders](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Shop.fields.assignedFulfillmentOrders)assignedFulfillmentOrders

•[FulfillmentOrderConnection!](/docs/api/admin-
graphql/latest/connections/FulfillmentOrderConnection)

non-nullDeprecated

    

Show fields

[Anchor to channels](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Shop.fields.channels)channels

•[ChannelConnection!](/docs/api/admin-
graphql/latest/connections/ChannelConnection)

non-nullDeprecated

    

Show fields

[Anchor to collections](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Shop.fields.collections)collections

•[CollectionConnection!](/docs/api/admin-
graphql/latest/connections/CollectionConnection)

non-nullDeprecated

    

Show fields

[Anchor to customers](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Shop.fields.customers)customers

•[CustomerConnection!](/docs/api/admin-
graphql/latest/connections/CustomerConnection)

non-nullDeprecated

    

Show fields

[Anchor to domains](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Shop.fields.domains)domains

•[[Domain!]!](/docs/api/admin-graphql/latest/objects/Domain)

non-nullDeprecated

    

Show fields

[Anchor to draftOrders](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Shop.fields.draftOrders)draftOrders

•[DraftOrderConnection!](/docs/api/admin-
graphql/latest/connections/DraftOrderConnection)

non-nullDeprecated (removal date set)

    

Show fields

[Anchor to fulfillmentOrders](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Shop.fields.fulfillmentOrders)fulfillmentOrders

•[FulfillmentOrderConnection!](/docs/api/admin-
graphql/latest/connections/FulfillmentOrderConnection)

non-nullDeprecated

    

Show fields

[Anchor to inventoryItems](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Shop.fields.inventoryItems)inventoryItems

•[InventoryItemConnection!](/docs/api/admin-
graphql/latest/connections/InventoryItemConnection)

non-nullDeprecated

    

Show fields

[Anchor to limitedPendingOrderCount](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Shop.fields.limitedPendingOrderCount)limitedPendingOrderCount

•[LimitedPendingOrderCount!](/docs/api/admin-
graphql/latest/objects/LimitedPendingOrderCount)

non-nullDeprecated

    

Show fields

[Anchor to locations](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Shop.fields.locations)locations

•[LocationConnection!](/docs/api/admin-
graphql/latest/connections/LocationConnection)

non-nullDeprecated

    

Show fields

[Anchor to metafieldDefinitions](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Shop.fields.metafieldDefinitions)metafieldDefinitions

•[MetafieldDefinitionConnection!](/docs/api/admin-
graphql/latest/connections/MetafieldDefinitionConnection)

non-nullDeprecated

    

Show fields

[Anchor to orders](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Shop.fields.orders)orders

•[OrderConnection!](/docs/api/admin-
graphql/latest/connections/OrderConnection)

non-nullDeprecated

    

Show fields

[Anchor to productImages](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Shop.fields.productImages)productImages

•[ImageConnection!](/docs/api/admin-
graphql/latest/connections/ImageConnection)

non-nullDeprecated

    

Show fields

[Anchor to products](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Shop.fields.products)products

•[ProductConnection!](/docs/api/admin-
graphql/latest/connections/ProductConnection)

non-nullDeprecated

    

Show fields

[Anchor to productTags](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Shop.fields.productTags)productTags

•[StringConnection!](/docs/api/admin-
graphql/latest/connections/StringConnection)

non-nullDeprecated

    

Show fields

[Anchor to productTypes](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Shop.fields.productTypes)productTypes

•[StringConnection!](/docs/api/admin-
graphql/latest/connections/StringConnection)

non-nullDeprecated

    

Show fields

[Anchor to productVariants](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Shop.fields.productVariants)productVariants

•[ProductVariantConnection!](/docs/api/admin-
graphql/latest/connections/ProductVariantConnection)

non-nullDeprecated

    

Show fields

[Anchor to productVendors](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Shop.fields.productVendors)productVendors

•[StringConnection!](/docs/api/admin-
graphql/latest/connections/StringConnection)

non-nullDeprecated

    

Show fields

[Anchor to publicationCount](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Shop.fields.publicationCount)publicationCount

•[Int!](/docs/api/admin-graphql/latest/scalars/Int)

non-nullDeprecated

    

[Anchor to staffMembers](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Shop.fields.staffMembers)staffMembers

•[StaffMemberConnection!](/docs/api/admin-
graphql/latest/connections/StaffMemberConnection)

non-nullDeprecated

    

Show fields

[Anchor to storefrontUrl](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Shop.fields.storefrontUrl)storefrontUrl

•[URL!](/docs/api/admin-graphql/latest/scalars/URL)

non-nullDeprecated

    

[Anchor to ShopAddress](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ShopAddress)[ShopAddress](/docs/api/admin-graphql/latest/objects/ShopAddress)

•OBJECT

    

An address for a shop.

Show fields

[Anchor to address1](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-ShopAddress.fields.address1)address1

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The first line of the address. Typically the street address or PO Box number.

[Anchor to address2](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-ShopAddress.fields.address2)address2

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The second line of the address. Typically the number of the apartment, suite,
or unit.

[Anchor to city](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-ShopAddress.fields.city)city

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The name of the city, district, village, or town.

[Anchor to company](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-ShopAddress.fields.company)company

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The name of the company or organization.

[Anchor to coordinatesValidated](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ShopAddress.fields.coordinatesValidated)coordinatesValidated

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether the address coordinates are valid.

[Anchor to country](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-ShopAddress.fields.country)country

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The name of the country.

[Anchor to countryCodeV2](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ShopAddress.fields.countryCodeV2)countryCodeV2

•[CountryCode](/docs/api/admin-graphql/latest/enums/CountryCode)

    

The two-letter code for the country of the address.

For example, US.

Show enum values

[Anchor to formatted](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-ShopAddress.fields.formatted)formatted

•[[String!]!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

A formatted version of the address, customized by the provided arguments.

Show arguments

### Arguments

[Anchor to withCompany](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ShopAddress.fields.formatted.arguments.withCompany)withCompany

•[Boolean](/docs/api/admin-graphql/latest/scalars/Boolean)

Default:true

    

Whether to include the company in the formatted address.

* * *

[Anchor to formattedArea](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ShopAddress.fields.formattedArea)formattedArea

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

A comma-separated list of the values for city, province, and country.

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
ShopAddress.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to latitude](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-ShopAddress.fields.latitude)latitude

•[Float](/docs/api/admin-graphql/latest/scalars/Float)

    

The latitude coordinate of the address.

[Anchor to longitude](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-ShopAddress.fields.longitude)longitude

•[Float](/docs/api/admin-graphql/latest/scalars/Float)

    

The longitude coordinate of the address.

[Anchor to phone](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-ShopAddress.fields.phone)phone

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

A phone number associated with the address.

Formatted using E.164 standard. For example, _+16135551111_.

[Anchor to province](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-ShopAddress.fields.province)province

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The region of the address, such as the province, state, or district.

[Anchor to provinceCode](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ShopAddress.fields.provinceCode)provinceCode

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The alphanumeric code for the region.

For example, ON.

[Anchor to zip](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
ShopAddress.fields.zip)zip

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The zip or postal code of the address.

[Anchor to countryCode](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ShopAddress.fields.countryCode)countryCode

•[String](/docs/api/admin-graphql/latest/scalars/String)

Deprecated

    

[Anchor to firstName](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-ShopAddress.fields.firstName)firstName

•[String](/docs/api/admin-graphql/latest/scalars/String)

Deprecated

    

[Anchor to lastName](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-ShopAddress.fields.lastName)lastName

•[String](/docs/api/admin-graphql/latest/scalars/String)

Deprecated

    

[Anchor to name](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-ShopAddress.fields.name)name

•[String](/docs/api/admin-graphql/latest/scalars/String)

Deprecated

    

[Anchor to ShopifyPaymentsAccount](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ShopifyPaymentsAccount)[ShopifyPaymentsAccount](/docs/api/admin-
graphql/latest/objects/ShopifyPaymentsAccount)

•OBJECT

    

Balance and payout information for a [Shopify
Payments](https://help.shopify.com/manual/payments/shopify-payments/getting-
paid-with-shopify-payments) account. Balance includes all balances for the
currencies supported by the shop. You can also query for a list of payouts,
where each payout includes the corresponding currencyCode field.

Show fields

[Anchor to accountOpenerName](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ShopifyPaymentsAccount.fields.accountOpenerName)accountOpenerName

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The name of the account opener.

[Anchor to activated](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-ShopifyPaymentsAccount.fields.activated)activated

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether the Shopify Payments setup is completed.

[Anchor to balance](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-ShopifyPaymentsAccount.fields.balance)balance

•[[MoneyV2!]!](/docs/api/admin-graphql/latest/objects/MoneyV2)

non-null

    

Current balances in all currencies for the account.

Show fields

[Anchor to balanceTransactions](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ShopifyPaymentsAccount.fields.balanceTransactions)balanceTransactions

•[ShopifyPaymentsBalanceTransactionConnection!](/docs/api/admin-
graphql/latest/connections/ShopifyPaymentsBalanceTransactionConnection)

non-null

    

A list of balance transactions associated with the shop.

Show fields

[Anchor to bankAccounts](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ShopifyPaymentsAccount.fields.bankAccounts)bankAccounts

•[ShopifyPaymentsBankAccountConnection!](/docs/api/admin-
graphql/latest/connections/ShopifyPaymentsBankAccountConnection)

non-null

    

All bank accounts configured for the Shopify Payments account.

Show fields

[Anchor to chargeStatementDescriptors](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ShopifyPaymentsAccount.fields.chargeStatementDescriptors)chargeStatementDescriptors

•[ShopifyPaymentsChargeStatementDescriptor](/docs/api/admin-
graphql/latest/interfaces/ShopifyPaymentsChargeStatementDescriptor)

    

The statement descriptors used for charges.

These descriptors appear on a customer's credit card or bank statement when
they make a purchase.

Show fields

[Anchor to country](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-ShopifyPaymentsAccount.fields.country)country

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The Shopify Payments account country.

[Anchor to defaultCurrency](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ShopifyPaymentsAccount.fields.defaultCurrency)defaultCurrency

•[CurrencyCode!](/docs/api/admin-graphql/latest/enums/CurrencyCode)

non-null

    

The default payout currency for the Shopify Payments account.

Show enum values

[Anchor to disputes](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-ShopifyPaymentsAccount.fields.disputes)disputes

•[ShopifyPaymentsDisputeConnection!](/docs/api/admin-
graphql/latest/connections/ShopifyPaymentsDisputeConnection)

non-null

    

All disputes that originated from a transaction made with the Shopify Payments
account.

Show fields

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
ShopifyPaymentsAccount.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to onboardable](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ShopifyPaymentsAccount.fields.onboardable)onboardable

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether the Shopify Payments account can be onboarded.

[Anchor to payouts](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-ShopifyPaymentsAccount.fields.payouts)payouts

•[ShopifyPaymentsPayoutConnection!](/docs/api/admin-
graphql/latest/connections/ShopifyPaymentsPayoutConnection)

non-null

    

All current and previous payouts made between the account and the bank
account.

Show fields

[Anchor to payoutSchedule](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ShopifyPaymentsAccount.fields.payoutSchedule)payoutSchedule

•[ShopifyPaymentsPayoutSchedule!](/docs/api/admin-
graphql/latest/objects/ShopifyPaymentsPayoutSchedule)

non-null

    

The payout schedule for the account.

Show fields

[Anchor to payoutStatementDescriptor](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ShopifyPaymentsAccount.fields.payoutStatementDescriptor)payoutStatementDescriptor

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The descriptor used for payouts.

The descriptor appears on a merchant's bank statement when they receive a
payout.

[Anchor to chargeStatementDescriptor](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ShopifyPaymentsAccount.fields.chargeStatementDescriptor)chargeStatementDescriptor

•[String](/docs/api/admin-graphql/latest/scalars/String)

Deprecated

    

[Anchor to ShopifyPaymentsBalanceTransaction](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ShopifyPaymentsBalanceTransaction)[ShopifyPaymentsBalanceTransaction](/docs/api/admin-
graphql/latest/objects/ShopifyPaymentsBalanceTransaction)

•OBJECT

    

A transaction that contributes to a Shopify Payments account balance.

Show fields

[Anchor to adjustmentReason](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ShopifyPaymentsBalanceTransaction.fields.adjustmentReason)adjustmentReason

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The reason for the adjustment that's associated with the transaction. If the
source_type isn't an adjustment, the value will be null.

[Anchor to adjustmentsOrders](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ShopifyPaymentsBalanceTransaction.fields.adjustmentsOrders)adjustmentsOrders

•[[ShopifyPaymentsAdjustmentOrder!]!](/docs/api/admin-
graphql/latest/objects/ShopifyPaymentsAdjustmentOrder)

non-null

    

The adjustment orders associated to the transaction.

Show fields

[Anchor to amount](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-ShopifyPaymentsBalanceTransaction.fields.amount)amount

•[MoneyV2!](/docs/api/admin-graphql/latest/objects/MoneyV2)

non-null

    

The amount contributing to the balance transaction.

Show fields

[Anchor to associatedOrder](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ShopifyPaymentsBalanceTransaction.fields.associatedOrder)associatedOrder

•[ShopifyPaymentsAssociatedOrder](/docs/api/admin-
graphql/latest/objects/ShopifyPaymentsAssociatedOrder)

    

The associated order for the balance transaction.

Show fields

[Anchor to associatedPayout](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ShopifyPaymentsBalanceTransaction.fields.associatedPayout)associatedPayout

•[ShopifyPaymentsBalanceTransactionAssociatedPayout!](/docs/api/admin-
graphql/latest/objects/ShopifyPaymentsBalanceTransactionAssociatedPayout)

non-null

    

Payout assoicated with the transaction.

Show fields

[Anchor to fee](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
ShopifyPaymentsBalanceTransaction.fields.fee)fee

•[MoneyV2!](/docs/api/admin-graphql/latest/objects/MoneyV2)

non-null

    

The fee amount contributing to the balance transaction.

Show fields

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
ShopifyPaymentsBalanceTransaction.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to net](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
ShopifyPaymentsBalanceTransaction.fields.net)net

•[MoneyV2!](/docs/api/admin-graphql/latest/objects/MoneyV2)

non-null

    

The net amount contributing to the merchant's balance.

Show fields

[Anchor to sourceId](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-ShopifyPaymentsBalanceTransaction.fields.sourceId)sourceId

•[BigInt](/docs/api/admin-graphql/latest/scalars/BigInt)

    

The ID of the resource leading to the transaction.

[Anchor to sourceOrderTransactionId](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ShopifyPaymentsBalanceTransaction.fields.sourceOrderTransactionId)sourceOrderTransactionId

•[BigInt](/docs/api/admin-graphql/latest/scalars/BigInt)

    

The id of the [Order Transaction](https://shopify.dev/docs/admin-
api/rest/reference/orders/transaction)

that resulted in this balance transaction.

[Anchor to sourceType](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ShopifyPaymentsBalanceTransaction.fields.sourceType)sourceType

•[ShopifyPaymentsSourceType](/docs/api/admin-
graphql/latest/enums/ShopifyPaymentsSourceType)

    

The source type of the balance transaction.

Show enum values

[Anchor to test](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-ShopifyPaymentsBalanceTransaction.fields.test)test

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Wether the tranaction was created in test mode.

[Anchor to transactionDate](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ShopifyPaymentsBalanceTransaction.fields.transactionDate)transactionDate

•[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime)

non-null

    

The date and time when the balance transaction was processed.

[Anchor to type](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-ShopifyPaymentsBalanceTransaction.fields.type)type

•[ShopifyPaymentsTransactionType!](/docs/api/admin-
graphql/latest/enums/ShopifyPaymentsTransactionType)

non-null

    

The type of transaction.

Show enum values

[Anchor to ShopifyPaymentsBankAccount](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ShopifyPaymentsBankAccount)[ShopifyPaymentsBankAccount](/docs/api/admin-
graphql/latest/objects/ShopifyPaymentsBankAccount)

•OBJECT

    

A bank account that can receive payouts.

Show fields

[Anchor to accountNumberLastDigits](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ShopifyPaymentsBankAccount.fields.accountNumberLastDigits)accountNumberLastDigits

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The last digits of the account number (the rest is redacted).

[Anchor to bankName](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-ShopifyPaymentsBankAccount.fields.bankName)bankName

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The name of the bank.

[Anchor to country](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-ShopifyPaymentsBankAccount.fields.country)country

•[CountryCode!](/docs/api/admin-graphql/latest/enums/CountryCode)

non-null

    

The country of the bank.

Show enum values

[Anchor to createdAt](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-ShopifyPaymentsBankAccount.fields.createdAt)createdAt

•[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime)

non-null

    

The date that the bank account was created.

[Anchor to currency](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-ShopifyPaymentsBankAccount.fields.currency)currency

•[CurrencyCode!](/docs/api/admin-graphql/latest/enums/CurrencyCode)

non-null

    

The currency of the bank account.

Show enum values

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
ShopifyPaymentsBankAccount.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to payouts](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-ShopifyPaymentsBankAccount.fields.payouts)payouts

•[ShopifyPaymentsPayoutConnection!](/docs/api/admin-
graphql/latest/connections/ShopifyPaymentsPayoutConnection)

non-null

    

All current and previous payouts made between the account and the bank
account.

Show fields

[Anchor to status](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-ShopifyPaymentsBankAccount.fields.status)status

•[ShopifyPaymentsBankAccountStatus!](/docs/api/admin-
graphql/latest/enums/ShopifyPaymentsBankAccountStatus)

non-null

    

The status of the bank account.

Show enum values

[Anchor to ShopifyPaymentsDispute](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ShopifyPaymentsDispute)[ShopifyPaymentsDispute](/docs/api/admin-
graphql/latest/objects/ShopifyPaymentsDispute)

•OBJECT

    

A dispute occurs when a buyer questions the legitimacy of a charge with their
financial institution.

Show fields

[Anchor to amount](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-ShopifyPaymentsDispute.fields.amount)amount

•[MoneyV2!](/docs/api/admin-graphql/latest/objects/MoneyV2)

non-null

    

The total amount disputed by the cardholder.

Show fields

[Anchor to disputeEvidence](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ShopifyPaymentsDispute.fields.disputeEvidence)disputeEvidence

•[ShopifyPaymentsDisputeEvidence!](/docs/api/admin-
graphql/latest/objects/ShopifyPaymentsDisputeEvidence)

non-null

    

The evidence associated with the dispute.

Show fields

[Anchor to evidenceDueBy](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ShopifyPaymentsDispute.fields.evidenceDueBy)evidenceDueBy

•[Date](/docs/api/admin-graphql/latest/scalars/Date)

    

The deadline for evidence submission.

[Anchor to evidenceSentOn](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ShopifyPaymentsDispute.fields.evidenceSentOn)evidenceSentOn

•[Date](/docs/api/admin-graphql/latest/scalars/Date)

    

The date when evidence was sent. Returns null if evidence hasn't yet been
sent.

[Anchor to finalizedOn](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ShopifyPaymentsDispute.fields.finalizedOn)finalizedOn

•[Date](/docs/api/admin-graphql/latest/scalars/Date)

    

The date when this dispute was resolved. Returns null if the dispute isn't yet
resolved.

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
ShopifyPaymentsDispute.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to initiatedAt](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ShopifyPaymentsDispute.fields.initiatedAt)initiatedAt

•[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime)

non-null

    

The date when this dispute was initiated.

[Anchor to legacyResourceId](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ShopifyPaymentsDispute.fields.legacyResourceId)legacyResourceId

•[UnsignedInt64!](/docs/api/admin-graphql/latest/scalars/UnsignedInt64)

non-null

    

The ID of the corresponding resource in the REST Admin API.

[Anchor to order](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-ShopifyPaymentsDispute.fields.order)order

•[Order](/docs/api/admin-graphql/latest/objects/Order)

    

The order that contains the charge that's under dispute.

Show fields

[Anchor to reasonDetails](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ShopifyPaymentsDispute.fields.reasonDetails)reasonDetails

•[ShopifyPaymentsDisputeReasonDetails!](/docs/api/admin-
graphql/latest/objects/ShopifyPaymentsDisputeReasonDetails)

non-null

    

The reason of the dispute.

Show fields

[Anchor to status](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-ShopifyPaymentsDispute.fields.status)status

•[DisputeStatus!](/docs/api/admin-graphql/latest/enums/DisputeStatus)

non-null

    

The current state of the dispute.

Show enum values

[Anchor to type](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-ShopifyPaymentsDispute.fields.type)type

•[DisputeType!](/docs/api/admin-graphql/latest/enums/DisputeType)

non-null

    

Indicates if this dispute is still in the inquiry phase or has turned into a
chargeback.

Show enum values

[Anchor to ShopifyPaymentsDisputeEvidence](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ShopifyPaymentsDisputeEvidence)[ShopifyPaymentsDisputeEvidence](/docs/api/admin-
graphql/latest/objects/ShopifyPaymentsDisputeEvidence)

•OBJECT

    

The evidence associated with the dispute.

Show fields

[Anchor to accessActivityLog](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ShopifyPaymentsDisputeEvidence.fields.accessActivityLog)accessActivityLog

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The activity logs associated with the dispute evidence.

[Anchor to billingAddress](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ShopifyPaymentsDisputeEvidence.fields.billingAddress)billingAddress

•[MailingAddress](/docs/api/admin-graphql/latest/objects/MailingAddress)

    

The billing address that's provided by the customer.

Show fields

[Anchor to cancellationPolicyDisclosure](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ShopifyPaymentsDisputeEvidence.fields.cancellationPolicyDisclosure)cancellationPolicyDisclosure

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The cancellation policy disclosure associated with the dispute evidence.

[Anchor to cancellationPolicyFile](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ShopifyPaymentsDisputeEvidence.fields.cancellationPolicyFile)cancellationPolicyFile

•[ShopifyPaymentsDisputeFileUpload](/docs/api/admin-
graphql/latest/objects/ShopifyPaymentsDisputeFileUpload)

    

The cancellation policy file associated with the dispute evidence.

Show fields

[Anchor to cancellationRebuttal](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ShopifyPaymentsDisputeEvidence.fields.cancellationRebuttal)cancellationRebuttal

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The cancellation rebuttal associated with the dispute evidence.

[Anchor to customerCommunicationFile](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ShopifyPaymentsDisputeEvidence.fields.customerCommunicationFile)customerCommunicationFile

•[ShopifyPaymentsDisputeFileUpload](/docs/api/admin-
graphql/latest/objects/ShopifyPaymentsDisputeFileUpload)

    

The customer communication file associated with the dispute evidence.

Show fields

[Anchor to customerEmailAddress](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ShopifyPaymentsDisputeEvidence.fields.customerEmailAddress)customerEmailAddress

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The customer's email address.

[Anchor to customerFirstName](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ShopifyPaymentsDisputeEvidence.fields.customerFirstName)customerFirstName

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The customer's first name.

[Anchor to customerLastName](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ShopifyPaymentsDisputeEvidence.fields.customerLastName)customerLastName

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The customer's last name.

[Anchor to customerPurchaseIp](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ShopifyPaymentsDisputeEvidence.fields.customerPurchaseIp)customerPurchaseIp

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The customer purchase ip for this dispute evidence.

[Anchor to dispute](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-ShopifyPaymentsDisputeEvidence.fields.dispute)dispute

•[ShopifyPaymentsDispute!](/docs/api/admin-
graphql/latest/objects/ShopifyPaymentsDispute)

non-null

    

The dispute associated with the evidence.

Show fields

[Anchor to disputeFileUploads](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ShopifyPaymentsDisputeEvidence.fields.disputeFileUploads)disputeFileUploads

•[[ShopifyPaymentsDisputeFileUpload!]!](/docs/api/admin-
graphql/latest/objects/ShopifyPaymentsDisputeFileUpload)

non-null

    

The file uploads associated with the dispute evidence.

Show fields

[Anchor to fulfillments](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ShopifyPaymentsDisputeEvidence.fields.fulfillments)fulfillments

•[[ShopifyPaymentsDisputeFulfillment!]!](/docs/api/admin-
graphql/latest/objects/ShopifyPaymentsDisputeFulfillment)

non-null

    

The fulfillments associated with the dispute evidence.

Show fields

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
ShopifyPaymentsDisputeEvidence.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to productDescription](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ShopifyPaymentsDisputeEvidence.fields.productDescription)productDescription

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The product description for this dispute evidence.

[Anchor to refundPolicyDisclosure](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ShopifyPaymentsDisputeEvidence.fields.refundPolicyDisclosure)refundPolicyDisclosure

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The refund policy disclosure associated with the dispute evidence.

[Anchor to refundPolicyFile](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ShopifyPaymentsDisputeEvidence.fields.refundPolicyFile)refundPolicyFile

•[ShopifyPaymentsDisputeFileUpload](/docs/api/admin-
graphql/latest/objects/ShopifyPaymentsDisputeFileUpload)

    

The refund policy file associated with the dispute evidence.

Show fields

[Anchor to refundRefusalExplanation](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ShopifyPaymentsDisputeEvidence.fields.refundRefusalExplanation)refundRefusalExplanation

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The refund refusal explanation associated with dispute evidence.

[Anchor to serviceDocumentationFile](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ShopifyPaymentsDisputeEvidence.fields.serviceDocumentationFile)serviceDocumentationFile

•[ShopifyPaymentsDisputeFileUpload](/docs/api/admin-
graphql/latest/objects/ShopifyPaymentsDisputeFileUpload)

    

The service documentation file associated with the dispute evidence.

Show fields

[Anchor to shippingAddress](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ShopifyPaymentsDisputeEvidence.fields.shippingAddress)shippingAddress

•[MailingAddress](/docs/api/admin-graphql/latest/objects/MailingAddress)

    

The mailing address for shipping that's provided by the customer.

Show fields

[Anchor to shippingDocumentationFile](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ShopifyPaymentsDisputeEvidence.fields.shippingDocumentationFile)shippingDocumentationFile

•[ShopifyPaymentsDisputeFileUpload](/docs/api/admin-
graphql/latest/objects/ShopifyPaymentsDisputeFileUpload)

    

The shipping documentation file associated with the dispute evidence.

Show fields

[Anchor to submitted](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-ShopifyPaymentsDisputeEvidence.fields.submitted)submitted

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether the dispute evidence is submitted.

[Anchor to uncategorizedFile](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ShopifyPaymentsDisputeEvidence.fields.uncategorizedFile)uncategorizedFile

•[ShopifyPaymentsDisputeFileUpload](/docs/api/admin-
graphql/latest/objects/ShopifyPaymentsDisputeFileUpload)

    

The uncategorized file associated with the dispute evidence.

Show fields

[Anchor to uncategorizedText](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ShopifyPaymentsDisputeEvidence.fields.uncategorizedText)uncategorizedText

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The uncategorized text for the dispute evidence.

[Anchor to ShopifyPaymentsDisputeFileUpload](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ShopifyPaymentsDisputeFileUpload)[ShopifyPaymentsDisputeFileUpload](/docs/api/admin-
graphql/latest/objects/ShopifyPaymentsDisputeFileUpload)

•OBJECT

    

The file upload associated with the dispute evidence.

Show fields

[Anchor to disputeEvidenceType](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ShopifyPaymentsDisputeFileUpload.fields.disputeEvidenceType)disputeEvidenceType

•[ShopifyPaymentsDisputeEvidenceFileType](/docs/api/admin-
graphql/latest/enums/ShopifyPaymentsDisputeEvidenceFileType)

    

The type of the file for the dispute evidence.

Show enum values

[Anchor to fileSize](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-ShopifyPaymentsDisputeFileUpload.fields.fileSize)fileSize

•[Int!](/docs/api/admin-graphql/latest/scalars/Int)

non-null

    

The file size.

[Anchor to fileType](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-ShopifyPaymentsDisputeFileUpload.fields.fileType)fileType

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The file type.

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
ShopifyPaymentsDisputeFileUpload.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to originalFileName](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ShopifyPaymentsDisputeFileUpload.fields.originalFileName)originalFileName

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The original file name.

[Anchor to url](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
ShopifyPaymentsDisputeFileUpload.fields.url)url

•[URL!](/docs/api/admin-graphql/latest/scalars/URL)

non-null

    

The URL for accessing the file.

[Anchor to ShopifyPaymentsDisputeFulfillment](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ShopifyPaymentsDisputeFulfillment)[ShopifyPaymentsDisputeFulfillment](/docs/api/admin-
graphql/latest/objects/ShopifyPaymentsDisputeFulfillment)

•OBJECT

    

The fulfillment associated with dispute evidence.

Show fields

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
ShopifyPaymentsDisputeFulfillment.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to shippingCarrier](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ShopifyPaymentsDisputeFulfillment.fields.shippingCarrier)shippingCarrier

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The shipping carrier for this fulfillment.

[Anchor to shippingDate](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ShopifyPaymentsDisputeFulfillment.fields.shippingDate)shippingDate

•[Date](/docs/api/admin-graphql/latest/scalars/Date)

    

The shipping date for this fulfillment.

[Anchor to shippingTrackingNumber](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ShopifyPaymentsDisputeFulfillment.fields.shippingTrackingNumber)shippingTrackingNumber

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The shipping tracking number for this fulfillment.

[Anchor to ShopifyPaymentsPayout](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ShopifyPaymentsPayout)[ShopifyPaymentsPayout](/docs/api/admin-
graphql/latest/objects/ShopifyPaymentsPayout)

•OBJECT

    

Payouts represent the movement of money between a merchant's Shopify Payments
balance and their bank account.

Show fields

[Anchor to businessEntity](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ShopifyPaymentsPayout.fields.businessEntity)businessEntity

•[BusinessEntity!](/docs/api/admin-graphql/latest/objects/BusinessEntity)

non-null

    

The business entity associated with the payout.

Show fields

[Anchor to externalTraceId](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ShopifyPaymentsPayout.fields.externalTraceId)externalTraceId

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

A unique trace ID from the financial institution. Use this reference number to
track the payout with your provider.

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
ShopifyPaymentsPayout.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to issuedAt](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-ShopifyPaymentsPayout.fields.issuedAt)issuedAt

•[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime)

non-null

    

The exact time when the payout was issued. The payout only contains balance
transactions that were available at this time.

[Anchor to legacyResourceId](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ShopifyPaymentsPayout.fields.legacyResourceId)legacyResourceId

•[UnsignedInt64!](/docs/api/admin-graphql/latest/scalars/UnsignedInt64)

non-null

    

The ID of the corresponding resource in the REST Admin API.

[Anchor to net](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
ShopifyPaymentsPayout.fields.net)net

•[MoneyV2!](/docs/api/admin-graphql/latest/objects/MoneyV2)

non-null

    

The total amount and currency of the payout.

Show fields

[Anchor to status](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-ShopifyPaymentsPayout.fields.status)status

•[ShopifyPaymentsPayoutStatus!](/docs/api/admin-
graphql/latest/enums/ShopifyPaymentsPayoutStatus)

non-null

    

The transfer status of the payout.

Show enum values

[Anchor to summary](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-ShopifyPaymentsPayout.fields.summary)summary

•[ShopifyPaymentsPayoutSummary!](/docs/api/admin-
graphql/latest/objects/ShopifyPaymentsPayoutSummary)

non-null

    

The summary of the payout.

Show fields

[Anchor to transactionType](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ShopifyPaymentsPayout.fields.transactionType)transactionType

•[ShopifyPaymentsPayoutTransactionType!](/docs/api/admin-
graphql/latest/enums/ShopifyPaymentsPayoutTransactionType)

non-null

    

The direction of the payout.

Show enum values

[Anchor to bankAccount](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ShopifyPaymentsPayout.fields.bankAccount)bankAccount

•[ShopifyPaymentsBankAccount](/docs/api/admin-
graphql/latest/objects/ShopifyPaymentsBankAccount)

Deprecated

    

Show fields

[Anchor to gross](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-ShopifyPaymentsPayout.fields.gross)gross

•[MoneyV2!](/docs/api/admin-graphql/latest/objects/MoneyV2)

non-nullDeprecated

    

Show fields

[Anchor to ShopPolicy](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ShopPolicy)[ShopPolicy](/docs/api/admin-graphql/latest/objects/ShopPolicy)

•OBJECT

    

Policy that a merchant has configured for their store, such as their refund or
privacy policy.

Show fields

[Anchor to body](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-ShopPolicy.fields.body)body

•[HTML!](/docs/api/admin-graphql/latest/scalars/HTML)

non-null

    

The text of the policy. The maximum size is 512kb.

[Anchor to createdAt](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-ShopPolicy.fields.createdAt)createdAt

•[Date!](/docs/api/admin-graphql/latest/scalars/Date)

non-null

    

The date and time ([ISO 8601 format](http://en.wikipedia.org/wiki/ISO_8601))
when the policy was created.

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
ShopPolicy.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to title](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-ShopPolicy.fields.title)title

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The translated title of the policy. For example, Refund Policy or Politique de
remboursement.

[Anchor to translations](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
ShopPolicy.fields.translations)translations

•[[Translation!]!](/docs/api/admin-graphql/latest/objects/Translation)

non-null

    

The published translations associated with the resource.

Show fields

[Anchor to type](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-ShopPolicy.fields.type)type

•[ShopPolicyType!](/docs/api/admin-graphql/latest/enums/ShopPolicyType)

non-null

    

The shop policy type.

Show enum values

[Anchor to updatedAt](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-ShopPolicy.fields.updatedAt)updatedAt

•[Date!](/docs/api/admin-graphql/latest/scalars/Date)

non-null

    

The date and time ([ISO 8601 format](http://en.wikipedia.org/wiki/ISO_8601))
when the policy was last modified.

[Anchor to url](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
ShopPolicy.fields.url)url

•[URL!](/docs/api/admin-graphql/latest/scalars/URL)

non-null

    

The public URL of the policy.

[Anchor to StaffMember](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
StaffMember)[StaffMember](/docs/api/admin-graphql/latest/objects/StaffMember)

•OBJECT

    

Represents the data about a staff member's Shopify account. Merchants can use
staff member data to get more information about the staff members in their
store.

Show fields

[Anchor to accountType](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
StaffMember.fields.accountType)accountType

•[AccountType](/docs/api/admin-graphql/latest/enums/AccountType)

    

The type of account the staff member has.

Show enum values

[Anchor to active](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-StaffMember.fields.active)active

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether the staff member is active.

[Anchor to avatar](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-StaffMember.fields.avatar)avatar

•[Image!](/docs/api/admin-graphql/latest/objects/Image)

non-null

    

The image used as the staff member's avatar in the Shopify admin.

Show fields

[Anchor to email](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-StaffMember.fields.email)email

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The staff member's email address.

[Anchor to exists](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-StaffMember.fields.exists)exists

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether the staff member's account exists.

[Anchor to firstName](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-StaffMember.fields.firstName)firstName

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The staff member's first name.

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
StaffMember.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to initials](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-StaffMember.fields.initials)initials

•[[String!]](/docs/api/admin-graphql/latest/scalars/String)

    

The staff member's initials, if available.

[Anchor to isShopOwner](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
StaffMember.fields.isShopOwner)isShopOwner

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether the staff member is the shop owner.

[Anchor to lastName](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-StaffMember.fields.lastName)lastName

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The staff member's last name.

[Anchor to locale](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-StaffMember.fields.locale)locale

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The staff member's preferred locale. Locale values use the format `language`
or `language-COUNTRY`, where `language` is a two-letter language code, and
`COUNTRY` is a two-letter country code. For example: `en` or `en-US`

[Anchor to name](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-StaffMember.fields.name)name

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The staff member's full name.

[Anchor to phone](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-StaffMember.fields.phone)phone

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The staff member's phone number.

[Anchor to privateData](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
StaffMember.fields.privateData)privateData

•[StaffMemberPrivateData!](/docs/api/admin-
graphql/latest/objects/StaffMemberPrivateData)

non-null

    

The data used to customize the Shopify admin experience for the staff member.

Show fields

[Anchor to StandardMetafieldDefinitionTemplate](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
StandardMetafieldDefinitionTemplate)[StandardMetafieldDefinitionTemplate](/docs/api/admin-
graphql/latest/objects/StandardMetafieldDefinitionTemplate)

•OBJECT

    

Standard metafield definition templates provide preset configurations to
create metafield definitions. Each template has a specific namespace and key
that we've reserved to have specific meanings for common use cases.

Refer to the [list of standard metafield
definitions](https://shopify.dev/apps/metafields/definitions/standard-
definitions).

Show fields

[Anchor to description](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
StandardMetafieldDefinitionTemplate.fields.description)description

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The description of the standard metafield definition.

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
StandardMetafieldDefinitionTemplate.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to key](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
StandardMetafieldDefinitionTemplate.fields.key)key

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The key owned by the definition after the definition has been activated.

[Anchor to name](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-StandardMetafieldDefinitionTemplate.fields.name)name

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The human-readable name for the standard metafield definition.

[Anchor to namespace](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-StandardMetafieldDefinitionTemplate.fields.namespace)namespace

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The namespace owned by the definition after the definition has been activated.

[Anchor to ownerTypes](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
StandardMetafieldDefinitionTemplate.fields.ownerTypes)ownerTypes

•[[MetafieldOwnerType!]!](/docs/api/admin-
graphql/latest/enums/MetafieldOwnerType)

non-null

    

The list of resource types that the standard metafield definition can be
applied to.

Show enum values

[Anchor to type](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-StandardMetafieldDefinitionTemplate.fields.type)type

•[MetafieldDefinitionType!](/docs/api/admin-
graphql/latest/objects/MetafieldDefinitionType)

non-null

    

The associated [metafield definition
type](https://shopify.dev/apps/metafields/definitions/types) that the
metafield stores.

Show fields

[Anchor to validations](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
StandardMetafieldDefinitionTemplate.fields.validations)validations

•[[MetafieldDefinitionValidation!]!](/docs/api/admin-
graphql/latest/objects/MetafieldDefinitionValidation)

non-null

    

The configured validations for the standard metafield definition.

Show fields

[Anchor to visibleToStorefrontApi](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
StandardMetafieldDefinitionTemplate.fields.visibleToStorefrontApi)visibleToStorefrontApi

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether metafields for the definition are by default visible using the
Storefront API.

[Anchor to StoreCreditAccount](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
StoreCreditAccount)[StoreCreditAccount](/docs/api/admin-
graphql/latest/objects/StoreCreditAccount)

•OBJECT

    

A store credit account contains a monetary balance that can be redeemed at
checkout for purchases in the shop. The account is held in the specified
currency and has an owner that cannot be transferred.

The account balance is redeemable at checkout only when the owner is
authenticated via [new customer accounts
authentication](https://shopify.dev/docs/api/customer).

Show fields

[Anchor to balance](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-StoreCreditAccount.fields.balance)balance

•[MoneyV2!](/docs/api/admin-graphql/latest/objects/MoneyV2)

non-null

    

The current balance of the store credit account.

Show fields

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
StoreCreditAccount.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to owner](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-StoreCreditAccount.fields.owner)owner

•[HasStoreCreditAccounts!](/docs/api/admin-
graphql/latest/interfaces/HasStoreCreditAccounts)

non-null

    

The owner of the store credit account.

Show fields

[Anchor to transactions](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
StoreCreditAccount.fields.transactions)transactions

•[StoreCreditAccountTransactionConnection!](/docs/api/admin-
graphql/latest/connections/StoreCreditAccountTransactionConnection)

non-null

    

The transaction history of the store credit account.

Show fields

[Anchor to StoreCreditAccountCreditTransaction](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
StoreCreditAccountCreditTransaction)[StoreCreditAccountCreditTransaction](/docs/api/admin-
graphql/latest/objects/StoreCreditAccountCreditTransaction)

•OBJECT

    

A credit transaction which increases the store credit account balance.

Show fields

[Anchor to account](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-StoreCreditAccountCreditTransaction.fields.account)account

•[StoreCreditAccount!](/docs/api/admin-
graphql/latest/objects/StoreCreditAccount)

non-null

    

The store credit account that the transaction belongs to.

Show fields

[Anchor to amount](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-StoreCreditAccountCreditTransaction.fields.amount)amount

•[MoneyV2!](/docs/api/admin-graphql/latest/objects/MoneyV2)

non-null

    

The amount of the transaction.

Show fields

[Anchor to balanceAfterTransaction](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
StoreCreditAccountCreditTransaction.fields.balanceAfterTransaction)balanceAfterTransaction

•[MoneyV2!](/docs/api/admin-graphql/latest/objects/MoneyV2)

non-null

    

The balance of the account after the transaction.

Show fields

[Anchor to createdAt](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-StoreCreditAccountCreditTransaction.fields.createdAt)createdAt

•[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime)

non-null

    

The date and time when the transaction was created.

[Anchor to event](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-StoreCreditAccountCreditTransaction.fields.event)event

•[StoreCreditSystemEvent!](/docs/api/admin-
graphql/latest/enums/StoreCreditSystemEvent)

non-null

    

The event that caused the store credit account transaction.

Show enum values

[Anchor to expiresAt](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-StoreCreditAccountCreditTransaction.fields.expiresAt)expiresAt

•[DateTime](/docs/api/admin-graphql/latest/scalars/DateTime)

    

The time at which the transaction expires. Debit transactions will always
spend the soonest expiring credit first.

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
StoreCreditAccountCreditTransaction.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to origin](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-StoreCreditAccountCreditTransaction.fields.origin)origin

•[StoreCreditAccountTransactionOrigin](/docs/api/admin-
graphql/latest/unions/StoreCreditAccountTransactionOrigin)

    

The origin of the store credit account transaction.

Show union types

[Anchor to remainingAmount](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
StoreCreditAccountCreditTransaction.fields.remainingAmount)remainingAmount

•[MoneyV2!](/docs/api/admin-graphql/latest/objects/MoneyV2)

non-null

    

The remaining amount of the credit. The remaining amount will decrease when a
debit spends this credit. It may also increase if that debit is subsequently
reverted. In the event that the credit expires, the remaining amount will
represent the amount that remained as the expiry ocurred.

Show fields

[Anchor to StoreCreditAccountDebitRevertTransaction](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
StoreCreditAccountDebitRevertTransaction)[StoreCreditAccountDebitRevertTransaction](/docs/api/admin-
graphql/latest/objects/StoreCreditAccountDebitRevertTransaction)

•OBJECT

    

A debit revert transaction which increases the store credit account balance.
Debit revert transactions are created automatically when a [store credit
account debit transaction](https://shopify.dev/api/admin-
graphql/latest/objects/StoreCreditAccountDebitTransaction) is reverted.

Store credit account debit transactions are reverted when an order is
cancelled, refunded or in the event of a payment failure at checkout. The
amount added to the balance is equal to the amount reverted on the original
credit.

Show fields

[Anchor to account](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-StoreCreditAccountDebitRevertTransaction.fields.account)account

•[StoreCreditAccount!](/docs/api/admin-
graphql/latest/objects/StoreCreditAccount)

non-null

    

The store credit account that the transaction belongs to.

Show fields

[Anchor to amount](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-StoreCreditAccountDebitRevertTransaction.fields.amount)amount

•[MoneyV2!](/docs/api/admin-graphql/latest/objects/MoneyV2)

non-null

    

The amount of the transaction.

Show fields

[Anchor to balanceAfterTransaction](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
StoreCreditAccountDebitRevertTransaction.fields.balanceAfterTransaction)balanceAfterTransaction

•[MoneyV2!](/docs/api/admin-graphql/latest/objects/MoneyV2)

non-null

    

The balance of the account after the transaction.

Show fields

[Anchor to createdAt](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-StoreCreditAccountDebitRevertTransaction.fields.createdAt)createdAt

•[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime)

non-null

    

The date and time when the transaction was created.

[Anchor to debitTransaction](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
StoreCreditAccountDebitRevertTransaction.fields.debitTransaction)debitTransaction

•[StoreCreditAccountDebitTransaction!](/docs/api/admin-
graphql/latest/objects/StoreCreditAccountDebitTransaction)

non-null

    

The reverted debit transaction.

Show fields

[Anchor to event](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-StoreCreditAccountDebitRevertTransaction.fields.event)event

•[StoreCreditSystemEvent!](/docs/api/admin-
graphql/latest/enums/StoreCreditSystemEvent)

non-null

    

The event that caused the store credit account transaction.

Show enum values

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
StoreCreditAccountDebitRevertTransaction.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to origin](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-StoreCreditAccountDebitRevertTransaction.fields.origin)origin

•[StoreCreditAccountTransactionOrigin](/docs/api/admin-
graphql/latest/unions/StoreCreditAccountTransactionOrigin)

    

The origin of the store credit account transaction.

Show union types

[Anchor to StoreCreditAccountDebitTransaction](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
StoreCreditAccountDebitTransaction)[StoreCreditAccountDebitTransaction](/docs/api/admin-
graphql/latest/objects/StoreCreditAccountDebitTransaction)

•OBJECT

    

A debit transaction which decreases the store credit account balance.

Show fields

[Anchor to account](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-StoreCreditAccountDebitTransaction.fields.account)account

•[StoreCreditAccount!](/docs/api/admin-
graphql/latest/objects/StoreCreditAccount)

non-null

    

The store credit account that the transaction belongs to.

Show fields

[Anchor to amount](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-StoreCreditAccountDebitTransaction.fields.amount)amount

•[MoneyV2!](/docs/api/admin-graphql/latest/objects/MoneyV2)

non-null

    

The amount of the transaction.

Show fields

[Anchor to balanceAfterTransaction](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
StoreCreditAccountDebitTransaction.fields.balanceAfterTransaction)balanceAfterTransaction

•[MoneyV2!](/docs/api/admin-graphql/latest/objects/MoneyV2)

non-null

    

The balance of the account after the transaction.

Show fields

[Anchor to createdAt](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-StoreCreditAccountDebitTransaction.fields.createdAt)createdAt

•[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime)

non-null

    

The date and time when the transaction was created.

[Anchor to event](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-StoreCreditAccountDebitTransaction.fields.event)event

•[StoreCreditSystemEvent!](/docs/api/admin-
graphql/latest/enums/StoreCreditSystemEvent)

non-null

    

The event that caused the store credit account transaction.

Show enum values

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
StoreCreditAccountDebitTransaction.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to origin](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-StoreCreditAccountDebitTransaction.fields.origin)origin

•[StoreCreditAccountTransactionOrigin](/docs/api/admin-
graphql/latest/unions/StoreCreditAccountTransactionOrigin)

    

The origin of the store credit account transaction.

Show union types

[Anchor to StorefrontAccessToken](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
StorefrontAccessToken)[StorefrontAccessToken](/docs/api/admin-
graphql/latest/objects/StorefrontAccessToken)

•OBJECT

    

A token that's used to delegate unauthenticated access scopes to clients that
need to access the unauthenticated [Storefront
API](https://shopify.dev/docs/api/storefront).

An app can have a maximum of 100 active storefront access tokens for each
shop.

[Get started with the Storefront
API](https://shopify.dev/docs/storefronts/headless/building-with-the-
storefront-api/getting-started).

Show fields

[Anchor to accessScopes](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
StorefrontAccessToken.fields.accessScopes)accessScopes

•[[AccessScope!]!](/docs/api/admin-graphql/latest/objects/AccessScope)

non-null

    

List of permissions associated with the token.

Show fields

[Anchor to accessToken](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
StorefrontAccessToken.fields.accessToken)accessToken

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The issued public access token.

[Anchor to createdAt](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-StorefrontAccessToken.fields.createdAt)createdAt

•[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime)

non-null

    

The date and time when the public access token was created.

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
StorefrontAccessToken.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to title](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-StorefrontAccessToken.fields.title)title

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

An arbitrary title for each token determined by the developer, used for
reference purposes.

[Anchor to updatedAt](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-StorefrontAccessToken.fields.updatedAt)updatedAt

•[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime)

non-null

    

The date and time when the storefront access token was updated.

[Anchor to SubscriptionBillingAttempt](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
SubscriptionBillingAttempt)[SubscriptionBillingAttempt](/docs/api/admin-
graphql/latest/objects/SubscriptionBillingAttempt)

•OBJECT

    

A record of an execution of the subscription billing process. Billing attempts
use idempotency keys to avoid duplicate order creation. A successful billing
attempt will create an order.

Show fields

[Anchor to completedAt](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
SubscriptionBillingAttempt.fields.completedAt)completedAt

•[DateTime](/docs/api/admin-graphql/latest/scalars/DateTime)

    

The date and time when the billing attempt was completed.

[Anchor to createdAt](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-SubscriptionBillingAttempt.fields.createdAt)createdAt

•[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime)

non-null

    

The date and time when the billing attempt was created.

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
SubscriptionBillingAttempt.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to idempotencyKey](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
SubscriptionBillingAttempt.fields.idempotencyKey)idempotencyKey

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

A unique key generated by the client to avoid duplicate payments.

[Anchor to nextActionUrl](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
SubscriptionBillingAttempt.fields.nextActionUrl)nextActionUrl

•[URL](/docs/api/admin-graphql/latest/scalars/URL)

    

The URL where the customer needs to be redirected so they can complete the 3D
Secure payment flow.

[Anchor to order](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-SubscriptionBillingAttempt.fields.order)order

•[Order](/docs/api/admin-graphql/latest/objects/Order)

    

The result of this billing attempt if completed successfully.

Show fields

[Anchor to originTime](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
SubscriptionBillingAttempt.fields.originTime)originTime

•[DateTime](/docs/api/admin-graphql/latest/scalars/DateTime)

    

The date and time used to calculate fulfillment intervals for a billing
attempt that successfully completed after the current anchor date. To prevent
fulfillment from being pushed to the next anchor date, this field can override
the billing attempt date.

[Anchor to paymentGroupId](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
SubscriptionBillingAttempt.fields.paymentGroupId)paymentGroupId

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The reference shared between retried payment attempts.

[Anchor to paymentSessionId](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
SubscriptionBillingAttempt.fields.paymentSessionId)paymentSessionId

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The reference shared between payment attempts with similar payment details.

[Anchor to processingError](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
SubscriptionBillingAttempt.fields.processingError)processingError

•[SubscriptionBillingAttemptProcessingError](/docs/api/admin-
graphql/latest/interfaces/SubscriptionBillingAttemptProcessingError)

    

Error information from processing the billing attempt.

Show fields

[Anchor to ready](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-SubscriptionBillingAttempt.fields.ready)ready

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether the billing attempt is still processing.

[Anchor to respectInventoryPolicy](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
SubscriptionBillingAttempt.fields.respectInventoryPolicy)respectInventoryPolicy

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether the billing attempt respects the merchant's inventory policy.

[Anchor to subscriptionContract](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
SubscriptionBillingAttempt.fields.subscriptionContract)subscriptionContract

•[SubscriptionContract!](/docs/api/admin-
graphql/latest/objects/SubscriptionContract)

non-null

    

The subscription contract.

Show fields

[Anchor to transactions](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
SubscriptionBillingAttempt.fields.transactions)transactions

•[OrderTransactionConnection!](/docs/api/admin-
graphql/latest/connections/OrderTransactionConnection)

non-null

    

The transactions created by the billing attempt.

Show fields

[Anchor to errorCode](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-SubscriptionBillingAttempt.fields.errorCode)errorCode

•[SubscriptionBillingAttemptErrorCode](/docs/api/admin-
graphql/latest/enums/SubscriptionBillingAttemptErrorCode)

Deprecated

    

Show enum values

[Anchor to errorMessage](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
SubscriptionBillingAttempt.fields.errorMessage)errorMessage

•[String](/docs/api/admin-graphql/latest/scalars/String)

Deprecated

    

[Anchor to SubscriptionContract](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
SubscriptionContract)[SubscriptionContract](/docs/api/admin-
graphql/latest/objects/SubscriptionContract)

•OBJECT

    

Represents a Subscription Contract.

Show fields

[Anchor to app](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
SubscriptionContract.fields.app)app

•[App](/docs/api/admin-graphql/latest/objects/App)

    

The subscription app that the subscription contract is registered to.

Show fields

[Anchor to appAdminUrl](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
SubscriptionContract.fields.appAdminUrl)appAdminUrl

•[URL](/docs/api/admin-graphql/latest/scalars/URL)

    

The URL of the subscription contract page on the subscription app.

[Anchor to billingAttempts](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
SubscriptionContract.fields.billingAttempts)billingAttempts

•[SubscriptionBillingAttemptConnection!](/docs/api/admin-
graphql/latest/connections/SubscriptionBillingAttemptConnection)

non-null

    

The list of billing attempts associated with the subscription contract.

Show fields

[Anchor to billingPolicy](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
SubscriptionContract.fields.billingPolicy)billingPolicy

•[SubscriptionBillingPolicy!](/docs/api/admin-
graphql/latest/objects/SubscriptionBillingPolicy)

non-null

    

The billing policy associated with the subscription contract.

Show fields

[Anchor to createdAt](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-SubscriptionContract.fields.createdAt)createdAt

•[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime)

non-null

    

The date and time when the subscription contract was created.

[Anchor to currencyCode](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
SubscriptionContract.fields.currencyCode)currencyCode

•[CurrencyCode!](/docs/api/admin-graphql/latest/enums/CurrencyCode)

non-null

    

The currency that's used for the subscription contract.

Show enum values

[Anchor to customAttributes](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
SubscriptionContract.fields.customAttributes)customAttributes

•[[Attribute!]!](/docs/api/admin-graphql/latest/objects/Attribute)

non-null

    

A list of the custom attributes to be added to the generated orders.

Show fields

[Anchor to customer](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-SubscriptionContract.fields.customer)customer

•[Customer](/docs/api/admin-graphql/latest/objects/Customer)

    

The customer to whom the subscription contract belongs.

Show fields

[Anchor to customerPaymentMethod](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
SubscriptionContract.fields.customerPaymentMethod)customerPaymentMethod

•[CustomerPaymentMethod](/docs/api/admin-
graphql/latest/objects/CustomerPaymentMethod)

    

The customer payment method that's used for the subscription contract.

Show fields

[Anchor to deliveryMethod](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
SubscriptionContract.fields.deliveryMethod)deliveryMethod

•[SubscriptionDeliveryMethod](/docs/api/admin-
graphql/latest/unions/SubscriptionDeliveryMethod)

    

The delivery method for each billing of the subscription contract.

Show union types

[Anchor to deliveryPolicy](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
SubscriptionContract.fields.deliveryPolicy)deliveryPolicy

•[SubscriptionDeliveryPolicy!](/docs/api/admin-
graphql/latest/objects/SubscriptionDeliveryPolicy)

non-null

    

The delivery policy associated with the subscription contract.

Show fields

[Anchor to deliveryPrice](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
SubscriptionContract.fields.deliveryPrice)deliveryPrice

•[MoneyV2!](/docs/api/admin-graphql/latest/objects/MoneyV2)

non-null

    

The delivery price for each billing of the subscription contract.

Show fields

[Anchor to discounts](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-SubscriptionContract.fields.discounts)discounts

•[SubscriptionManualDiscountConnection!](/docs/api/admin-
graphql/latest/connections/SubscriptionManualDiscountConnection)

non-null

    

The list of subscription discounts associated with the subscription contract.

Show fields

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
SubscriptionContract.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to lastBillingAttemptErrorType](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
SubscriptionContract.fields.lastBillingAttemptErrorType)lastBillingAttemptErrorType

•[SubscriptionContractLastBillingErrorType](/docs/api/admin-
graphql/latest/enums/SubscriptionContractLastBillingErrorType)

    

The last billing error type of the contract.

Show enum values

[Anchor to lastPaymentStatus](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
SubscriptionContract.fields.lastPaymentStatus)lastPaymentStatus

•[SubscriptionContractLastPaymentStatus](/docs/api/admin-
graphql/latest/enums/SubscriptionContractLastPaymentStatus)

    

The current status of the last payment.

Show enum values

[Anchor to lines](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-SubscriptionContract.fields.lines)lines

•[SubscriptionLineConnection!](/docs/api/admin-
graphql/latest/connections/SubscriptionLineConnection)

non-null

    

The list of subscription lines associated with the subscription contract.

Show fields

[Anchor to linesCount](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
SubscriptionContract.fields.linesCount)linesCount

•[Count](/docs/api/admin-graphql/latest/objects/Count)

    

The number of lines associated with the subscription contract.

Show fields

[Anchor to nextBillingDate](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
SubscriptionContract.fields.nextBillingDate)nextBillingDate

•[DateTime](/docs/api/admin-graphql/latest/scalars/DateTime)

    

The next billing date for the subscription contract. This field is managed by
the apps. Alternatively you can utilize our [Billing Cycles
APIs](https://shopify.dev/docs/apps/selling-strategies/subscriptions/billing-
cycles), which provide auto-computed billing dates and additional
functionalities.

[Anchor to note](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-SubscriptionContract.fields.note)note

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The note field that will be applied to the generated orders.

[Anchor to orders](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-SubscriptionContract.fields.orders)orders

•[OrderConnection!](/docs/api/admin-
graphql/latest/connections/OrderConnection)

non-null

    

A list of the subscription contract's orders.

Show fields

[Anchor to originOrder](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
SubscriptionContract.fields.originOrder)originOrder

•[Order](/docs/api/admin-graphql/latest/objects/Order)

    

The order from which this contract originated.

Show fields

[Anchor to revisionId](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
SubscriptionContract.fields.revisionId)revisionId

•[UnsignedInt64!](/docs/api/admin-graphql/latest/scalars/UnsignedInt64)

non-null

    

The revision id of the contract.

[Anchor to status](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-SubscriptionContract.fields.status)status

•[SubscriptionContractSubscriptionStatus!](/docs/api/admin-
graphql/latest/enums/SubscriptionContractSubscriptionStatus)

non-null

    

The current status of the subscription contract.

Show enum values

[Anchor to updatedAt](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-SubscriptionContract.fields.updatedAt)updatedAt

•[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime)

non-null

    

The date and time when the subscription contract was updated.

[Anchor to lineCount](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-SubscriptionContract.fields.lineCount)lineCount

•[Int!](/docs/api/admin-graphql/latest/scalars/Int)

non-nullDeprecated

    

[Anchor to SubscriptionDraft](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
SubscriptionDraft)[SubscriptionDraft](/docs/api/admin-
graphql/latest/objects/SubscriptionDraft)

•OBJECT

    

The `SubscriptionDraft` object represents a draft version of a [subscription
contract](https://shopify.dev/docs/api/admin-
graphql/latest/objects/SubscriptionContract) before it's committed. It serves
as a staging area for making changes to an existing subscription or creating a
new one. The draft allows you to preview and modify various aspects of a
subscription before applying the changes.

Use the `SubscriptionDraft` object to:

  * Add, remove, or modify subscription lines and their quantities
  * Manage discounts (add, remove, or update manual and code-based discounts)
  * Configure delivery options and shipping methods
  * Set up billing and delivery policies
  * Manage customer payment methods
  * Add custom attributes and notes to generated orders
  * Configure billing cycles and next billing dates
  * Preview the projected state of the subscription

Each `SubscriptionDraft` object maintains a projected state that shows how the
subscription will look after the changes are committed. This allows you to
preview the impact of your modifications before applying them. The draft can
be associated with an existing subscription contract (for modifications) or
used to create a new subscription.

The draft remains in a draft state until it's committed, at which point the
changes are applied to the subscription contract and the draft is no longer
accessible.

Learn more about [how subscription contracts
work](https://shopify.dev/docs/apps/build/purchase-
options/subscriptions/contracts) and how to
[build](https://shopify.dev/docs/apps/build/purchase-
options/subscriptions/contracts/build-a-subscription-contract),
[update](https://shopify.dev/docs/apps/build/purchase-
options/subscriptions/contracts/update-a-subscription-contract), and
[combine](https://shopify.dev/docs/apps/build/purchase-
options/subscriptions/contracts/combine-subscription-contracts) subscription
contracts.

Show fields

[Anchor to billingCycle](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
SubscriptionDraft.fields.billingCycle)billingCycle

•[SubscriptionBillingCycle](/docs/api/admin-
graphql/latest/objects/SubscriptionBillingCycle)

    

The billing cycle that the subscription contract will be associated with.

Show fields

[Anchor to billingPolicy](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
SubscriptionDraft.fields.billingPolicy)billingPolicy

•[SubscriptionBillingPolicy!](/docs/api/admin-
graphql/latest/objects/SubscriptionBillingPolicy)

non-null

    

The billing policy for the subscription contract.

Show fields

[Anchor to concatenatedBillingCycles](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
SubscriptionDraft.fields.concatenatedBillingCycles)concatenatedBillingCycles

•[SubscriptionBillingCycleConnection!](/docs/api/admin-
graphql/latest/connections/SubscriptionBillingCycleConnection)

non-null

    

The billing cycles of the contracts that will be concatenated to the
subscription contract.

Show fields

[Anchor to currencyCode](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
SubscriptionDraft.fields.currencyCode)currencyCode

•[CurrencyCode!](/docs/api/admin-graphql/latest/enums/CurrencyCode)

non-null

    

The currency used for the subscription contract.

Show enum values

[Anchor to customAttributes](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
SubscriptionDraft.fields.customAttributes)customAttributes

•[[Attribute!]!](/docs/api/admin-graphql/latest/objects/Attribute)

non-null

    

A list of the custom attributes to be added to the generated orders.

Show fields

[Anchor to customer](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-SubscriptionDraft.fields.customer)customer

•[Customer!](/docs/api/admin-graphql/latest/objects/Customer)

non-null

    

The customer to whom the subscription contract belongs.

Show fields

[Anchor to customerPaymentMethod](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
SubscriptionDraft.fields.customerPaymentMethod)customerPaymentMethod

•[CustomerPaymentMethod](/docs/api/admin-
graphql/latest/objects/CustomerPaymentMethod)

    

The customer payment method used for the subscription contract.

Show fields

[Anchor to deliveryMethod](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
SubscriptionDraft.fields.deliveryMethod)deliveryMethod

•[SubscriptionDeliveryMethod](/docs/api/admin-
graphql/latest/unions/SubscriptionDeliveryMethod)

    

The delivery method for each billing of the subscription contract.

Show union types

[Anchor to deliveryOptions](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
SubscriptionDraft.fields.deliveryOptions)deliveryOptions

•[SubscriptionDeliveryOptionResult](/docs/api/admin-
graphql/latest/unions/SubscriptionDeliveryOptionResult)

    

The available delivery options for a given delivery address. Returns `null`
for pending requests.

Show union types

[Anchor to deliveryPolicy](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
SubscriptionDraft.fields.deliveryPolicy)deliveryPolicy

•[SubscriptionDeliveryPolicy!](/docs/api/admin-
graphql/latest/objects/SubscriptionDeliveryPolicy)

non-null

    

The delivery policy for the subscription contract.

Show fields

[Anchor to deliveryPrice](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
SubscriptionDraft.fields.deliveryPrice)deliveryPrice

•[MoneyV2](/docs/api/admin-graphql/latest/objects/MoneyV2)

    

The delivery price for each billing the subscription contract.

Show fields

[Anchor to discounts](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-SubscriptionDraft.fields.discounts)discounts

•[SubscriptionDiscountConnection!](/docs/api/admin-
graphql/latest/connections/SubscriptionDiscountConnection)

non-null

    

The list of subscription discounts which will be associated with the
subscription contract.

Show fields

[Anchor to discountsAdded](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
SubscriptionDraft.fields.discountsAdded)discountsAdded

•[SubscriptionDiscountConnection!](/docs/api/admin-
graphql/latest/connections/SubscriptionDiscountConnection)

non-null

    

The list of subscription discounts to be added to the subscription contract.

Show fields

[Anchor to discountsRemoved](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
SubscriptionDraft.fields.discountsRemoved)discountsRemoved

•[SubscriptionDiscountConnection!](/docs/api/admin-
graphql/latest/connections/SubscriptionDiscountConnection)

non-null

    

The list of subscription discounts to be removed from the subscription
contract.

Show fields

[Anchor to discountsUpdated](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
SubscriptionDraft.fields.discountsUpdated)discountsUpdated

•[SubscriptionDiscountConnection!](/docs/api/admin-
graphql/latest/connections/SubscriptionDiscountConnection)

non-null

    

The list of subscription discounts to be updated on the subscription contract.

Show fields

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
SubscriptionDraft.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to lines](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-SubscriptionDraft.fields.lines)lines

•[SubscriptionLineConnection!](/docs/api/admin-
graphql/latest/connections/SubscriptionLineConnection)

non-null

    

The list of subscription lines which will be associated with the subscription
contract.

Show fields

[Anchor to linesAdded](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
SubscriptionDraft.fields.linesAdded)linesAdded

•[SubscriptionLineConnection!](/docs/api/admin-
graphql/latest/connections/SubscriptionLineConnection)

non-null

    

The list of subscription lines to be added to the subscription contract.

Show fields

[Anchor to linesRemoved](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
SubscriptionDraft.fields.linesRemoved)linesRemoved

•[SubscriptionLineConnection!](/docs/api/admin-
graphql/latest/connections/SubscriptionLineConnection)

non-null

    

The list of subscription lines to be removed from the subscription contract.

Show fields

[Anchor to nextBillingDate](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
SubscriptionDraft.fields.nextBillingDate)nextBillingDate

•[DateTime](/docs/api/admin-graphql/latest/scalars/DateTime)

    

The next billing date for the subscription contract.

[Anchor to note](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-SubscriptionDraft.fields.note)note

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The note field that will be applied to the generated orders.

[Anchor to originalContract](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
SubscriptionDraft.fields.originalContract)originalContract

•[SubscriptionContract](/docs/api/admin-
graphql/latest/objects/SubscriptionContract)

    

The original subscription contract.

Show fields

[Anchor to status](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-SubscriptionDraft.fields.status)status

•[SubscriptionContractSubscriptionStatus](/docs/api/admin-
graphql/latest/enums/SubscriptionContractSubscriptionStatus)

    

The current status of the subscription contract.

Show enum values

[Anchor to shippingOptions](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
SubscriptionDraft.fields.shippingOptions)shippingOptions

•[SubscriptionShippingOptionResult](/docs/api/admin-
graphql/latest/unions/SubscriptionShippingOptionResult)

Deprecated

    

Show union types

[Anchor to TaxonomyAttribute](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
TaxonomyAttribute)[TaxonomyAttribute](/docs/api/admin-
graphql/latest/objects/TaxonomyAttribute)

•OBJECT

    

A Shopify product taxonomy attribute.

Show fields

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
TaxonomyAttribute.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to TaxonomyCategory](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
TaxonomyCategory)[TaxonomyCategory](/docs/api/admin-
graphql/latest/objects/TaxonomyCategory)

•OBJECT

    

The details of a specific product category within the [Shopify product
taxonomy](https://shopify.github.io/product-
taxonomy/releases/unstable/?categoryId=sg-4-17-2-17).

Show fields

[Anchor to ancestorIds](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
TaxonomyCategory.fields.ancestorIds)ancestorIds

•[[ID!]!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

The IDs of the category's ancestor categories.

[Anchor to attributes](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
TaxonomyCategory.fields.attributes)attributes

•[TaxonomyCategoryAttributeConnection!](/docs/api/admin-
graphql/latest/connections/TaxonomyCategoryAttributeConnection)

non-null

    

The attributes of the taxonomy category.

Show fields

[Anchor to childrenIds](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
TaxonomyCategory.fields.childrenIds)childrenIds

•[[ID!]!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

The IDs of the category's child categories.

[Anchor to fullName](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-TaxonomyCategory.fields.fullName)fullName

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The full name of the taxonomy category. For example, Animals & Pet Supplies >
Pet Supplies > Dog Supplies > Dog Beds.

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
TaxonomyCategory.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

The globally-unique ID of the TaxonomyCategory.

[Anchor to isArchived](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
TaxonomyCategory.fields.isArchived)isArchived

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether the category is archived. The default value is `false`.

[Anchor to isLeaf](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-TaxonomyCategory.fields.isLeaf)isLeaf

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether the category is a leaf category. A leaf category doesn't have any
subcategories beneath it. For example, in Animals & Pet Supplies > Pet
Supplies > Dog Supplies > Dog Treadmills, Dog Treadmills is a leaf category.
The value is `true` when there are no `childrenIds` specified.

[Anchor to isRoot](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-TaxonomyCategory.fields.isRoot)isRoot

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether the category is a root category. A root category is at the top level
of the category hierarchy and doesn't have a parent category. For example,
Animals & Pet Supplies. The value is `true` when there's no `parentId`
specified.

[Anchor to level](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-TaxonomyCategory.fields.level)level

•[Int!](/docs/api/admin-graphql/latest/scalars/Int)

non-null

    

The level of the category in the taxonomy tree. Levels indicate the depth of
the category from the root. For example, in Animals & Pet Supplies > Pet
Supplies > Dog Supplies, Animals & Pet Supplies is at level 1, Animals & Pet
Supplies > Pet Supplies is at level 2, and Animals & Pet Supplies > Pet
Supplies > Dog Supplies is at level 3.

[Anchor to name](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-TaxonomyCategory.fields.name)name

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The name of the taxonomy category. For example, Dog Beds.

[Anchor to parentId](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-TaxonomyCategory.fields.parentId)parentId

•[ID](/docs/api/admin-graphql/latest/scalars/ID)

    

The ID of the category's parent category.

[Anchor to TaxonomyChoiceListAttribute](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
TaxonomyChoiceListAttribute)[TaxonomyChoiceListAttribute](/docs/api/admin-
graphql/latest/objects/TaxonomyChoiceListAttribute)

•OBJECT

    

A Shopify product taxonomy choice list attribute.

Show fields

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
TaxonomyChoiceListAttribute.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

The unique ID of the TaxonomyAttribute.

[Anchor to name](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-TaxonomyChoiceListAttribute.fields.name)name

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The name of the product taxonomy attribute. For example, Color.

[Anchor to values](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-TaxonomyChoiceListAttribute.fields.values)values

•[TaxonomyValueConnection!](/docs/api/admin-
graphql/latest/connections/TaxonomyValueConnection)

non-null

    

A list of values on the choice list attribute.

Show fields

[Anchor to TaxonomyMeasurementAttribute](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
TaxonomyMeasurementAttribute)[TaxonomyMeasurementAttribute](/docs/api/admin-
graphql/latest/objects/TaxonomyMeasurementAttribute)

•OBJECT

    

A Shopify product taxonomy measurement attribute.

Show fields

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
TaxonomyMeasurementAttribute.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

The unique ID of the TaxonomyAttribute.

[Anchor to name](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-TaxonomyMeasurementAttribute.fields.name)name

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The name of the product taxonomy attribute. For example, Color.

[Anchor to options](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-TaxonomyMeasurementAttribute.fields.options)options

•[[Attribute!]!](/docs/api/admin-graphql/latest/objects/Attribute)

non-null

    

The product taxonomy attribute options.

Show fields

[Anchor to TaxonomyValue](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
TaxonomyValue)[TaxonomyValue](/docs/api/admin-
graphql/latest/objects/TaxonomyValue)

•OBJECT

    

Represents a Shopify product taxonomy value.

Show fields

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
TaxonomyValue.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to name](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-TaxonomyValue.fields.name)name

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The name of the product taxonomy value. For example, Red.

[Anchor to TenderTransaction](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
TenderTransaction)[TenderTransaction](/docs/api/admin-
graphql/latest/objects/TenderTransaction)

•OBJECT

    

A TenderTransaction represents a transaction with financial impact on a shop's
balance sheet. A tender transaction always represents actual money movement
between a buyer and a shop. TenderTransactions can be used instead of
OrderTransactions for reconciling a shop's cash flow. A TenderTransaction is
immutable once created.

Show fields

[Anchor to amount](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-TenderTransaction.fields.amount)amount

•[MoneyV2!](/docs/api/admin-graphql/latest/objects/MoneyV2)

non-null

    

The amount and currency of the tender transaction.

Show fields

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
TenderTransaction.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to order](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-TenderTransaction.fields.order)order

•[Order](/docs/api/admin-graphql/latest/objects/Order)

    

The order that's related to the tender transaction. This value is null if the
order has been deleted.

Show fields

[Anchor to paymentMethod](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
TenderTransaction.fields.paymentMethod)paymentMethod

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

Information about the payment method used for the transaction.

[Anchor to processedAt](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
TenderTransaction.fields.processedAt)processedAt

•[DateTime](/docs/api/admin-graphql/latest/scalars/DateTime)

    

Date and time when the transaction was processed.

[Anchor to remoteReference](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
TenderTransaction.fields.remoteReference)remoteReference

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The remote gateway reference associated with the tender transaction.

[Anchor to test](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-TenderTransaction.fields.test)test

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether the transaction is a test transaction.

[Anchor to transactionDetails](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
TenderTransaction.fields.transactionDetails)transactionDetails

•[TenderTransactionDetails](/docs/api/admin-
graphql/latest/unions/TenderTransactionDetails)

    

Information about the payment instrument used for the transaction.

Show union types

[Anchor to user](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-TenderTransaction.fields.user)user

•[StaffMember](/docs/api/admin-graphql/latest/objects/StaffMember)

    

The staff member who performed the transaction.

Show fields

[Anchor to TransactionFee](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
TransactionFee)[TransactionFee](/docs/api/admin-
graphql/latest/objects/TransactionFee)

•OBJECT

    

Transaction fee related to an order transaction.

Show fields

[Anchor to amount](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-TransactionFee.fields.amount)amount

•[MoneyV2!](/docs/api/admin-graphql/latest/objects/MoneyV2)

non-null

    

Amount of the fee.

Show fields

[Anchor to flatFee](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-TransactionFee.fields.flatFee)flatFee

•[MoneyV2!](/docs/api/admin-graphql/latest/objects/MoneyV2)

non-null

    

Flat rate charge for a transaction.

Show fields

[Anchor to flatFeeName](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
TransactionFee.fields.flatFeeName)flatFeeName

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

Name of the credit card flat fee.

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
TransactionFee.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to rate](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-TransactionFee.fields.rate)rate

•[Decimal!](/docs/api/admin-graphql/latest/scalars/Decimal)

non-null

    

Percentage charge.

[Anchor to rateName](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-TransactionFee.fields.rateName)rateName

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

Name of the credit card rate.

[Anchor to taxAmount](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-TransactionFee.fields.taxAmount)taxAmount

•[MoneyV2!](/docs/api/admin-graphql/latest/objects/MoneyV2)

non-null

    

Tax amount charged on the fee.

Show fields

[Anchor to type](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-TransactionFee.fields.type)type

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

Name of the type of fee.

[Anchor to UnverifiedReturnLineItem](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
UnverifiedReturnLineItem)[UnverifiedReturnLineItem](/docs/api/admin-
graphql/latest/objects/UnverifiedReturnLineItem)

•OBJECT

    

An unverified return line item.

Show fields

[Anchor to customerNote](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
UnverifiedReturnLineItem.fields.customerNote)customerNote

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

A note from the customer that describes the item to be returned. Maximum
length: 300 characters.

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
UnverifiedReturnLineItem.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to processableQuantity](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
UnverifiedReturnLineItem.fields.processableQuantity)processableQuantity

•[Int!](/docs/api/admin-graphql/latest/scalars/Int)

non-null

    

The quantity that can be processed.

[Anchor to processedQuantity](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
UnverifiedReturnLineItem.fields.processedQuantity)processedQuantity

•[Int!](/docs/api/admin-graphql/latest/scalars/Int)

non-null

    

The quantity that has been processed.

[Anchor to quantity](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-UnverifiedReturnLineItem.fields.quantity)quantity

•[Int!](/docs/api/admin-graphql/latest/scalars/Int)

non-null

    

The quantity being returned.

[Anchor to refundableQuantity](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
UnverifiedReturnLineItem.fields.refundableQuantity)refundableQuantity

•[Int!](/docs/api/admin-graphql/latest/scalars/Int)

non-null

    

The quantity that can be refunded.

[Anchor to refundedQuantity](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
UnverifiedReturnLineItem.fields.refundedQuantity)refundedQuantity

•[Int!](/docs/api/admin-graphql/latest/scalars/Int)

non-null

    

The quantity that was refunded.

[Anchor to returnReason](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
UnverifiedReturnLineItem.fields.returnReason)returnReason

•[ReturnReason!](/docs/api/admin-graphql/latest/enums/ReturnReason)

non-null

    

The reason for returning the item.

Show enum values

[Anchor to returnReasonNote](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
UnverifiedReturnLineItem.fields.returnReasonNote)returnReasonNote

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

Additional information about the reason for the return. Maximum length: 255
characters.

[Anchor to unitPrice](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-UnverifiedReturnLineItem.fields.unitPrice)unitPrice

•[MoneyV2!](/docs/api/admin-graphql/latest/objects/MoneyV2)

non-null

    

The unit price of the unverified return line item.

Show fields

[Anchor to unprocessedQuantity](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
UnverifiedReturnLineItem.fields.unprocessedQuantity)unprocessedQuantity

•[Int!](/docs/api/admin-graphql/latest/scalars/Int)

non-null

    

The quantity that has't been processed.

[Anchor to UrlRedirect](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
UrlRedirect)[UrlRedirect](/docs/api/admin-graphql/latest/objects/UrlRedirect)

•OBJECT

    

The URL redirect for the online store.

Show fields

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
UrlRedirect.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

The ID of the URL redirect.

[Anchor to path](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-UrlRedirect.fields.path)path

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The old path to be redirected from. When the user visits this path, they will
be redirected to the target location.

[Anchor to target](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-UrlRedirect.fields.target)target

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The target location where the user will be redirected to.

[Anchor to UrlRedirectImport](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
UrlRedirectImport)[UrlRedirectImport](/docs/api/admin-
graphql/latest/objects/UrlRedirectImport)

•OBJECT

    

A request to import a [`URLRedirect`](https://shopify.dev/api/admin-
graphql/latest/objects/UrlRedirect) object into the Online Store channel. Apps
can use this to query the state of an `UrlRedirectImport` request.

For more information, see [`url-
redirect`](https://help.shopify.com/en/manual/online-store/menus-and-
links/url-redirect)s.

Show fields

[Anchor to count](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-UrlRedirectImport.fields.count)count

•[Int](/docs/api/admin-graphql/latest/scalars/Int)

    

The number of rows in the file.

[Anchor to createdCount](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
UrlRedirectImport.fields.createdCount)createdCount

•[Int](/docs/api/admin-graphql/latest/scalars/Int)

    

The number of redirects created from the import.

[Anchor to failedCount](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
UrlRedirectImport.fields.failedCount)failedCount

•[Int](/docs/api/admin-graphql/latest/scalars/Int)

    

The number of redirects that failed to be imported.

[Anchor to finished](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-UrlRedirectImport.fields.finished)finished

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether the import is finished.

[Anchor to finishedAt](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
UrlRedirectImport.fields.finishedAt)finishedAt

•[DateTime](/docs/api/admin-graphql/latest/scalars/DateTime)

    

The date and time when the import finished.

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
UrlRedirectImport.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

The ID of the `UrlRedirectImport` object.

[Anchor to previewRedirects](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
UrlRedirectImport.fields.previewRedirects)previewRedirects

•[[UrlRedirectImportPreview!]!](/docs/api/admin-
graphql/latest/objects/UrlRedirectImportPreview)

non-null

    

A list of up to three previews of the URL redirects to be imported.

Show fields

[Anchor to updatedCount](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
UrlRedirectImport.fields.updatedCount)updatedCount

•[Int](/docs/api/admin-graphql/latest/scalars/Int)

    

The number of redirects updated during the import.

[Anchor to Validation](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Validation)[Validation](/docs/api/admin-graphql/latest/objects/Validation)

•OBJECT

    

A checkout server side validation installed on the shop.

Show fields

[Anchor to blockOnFailure](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Validation.fields.blockOnFailure)blockOnFailure

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether the validation should block on failures other than expected
violations.

[Anchor to enabled](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Validation.fields.enabled)enabled

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether the validation is enabled on the merchant checkout.

[Anchor to errorHistory](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Validation.fields.errorHistory)errorHistory

•[FunctionsErrorHistory](/docs/api/admin-
graphql/latest/objects/FunctionsErrorHistory)

    

The error history on the most recent version of the validation function.

Show fields

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
Validation.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

Global ID for the validation.

[Anchor to metafield](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Validation.fields.metafield)metafield

•[Metafield](/docs/api/admin-graphql/latest/objects/Metafield)

    

A [custom field](https://shopify.dev/docs/apps/build/custom-data), including
its `namespace` and `key`, that's associated with a Shopify resource for the
purposes of adding and storing additional information.

Show fields

[Anchor to metafields](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Validation.fields.metafields)metafields

•[MetafieldConnection!](/docs/api/admin-
graphql/latest/connections/MetafieldConnection)

non-null

    

A list of [custom fields](https://shopify.dev/docs/apps/build/custom-data)
that a merchant associates with a Shopify resource.

Show fields

[Anchor to shopifyFunction](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Validation.fields.shopifyFunction)shopifyFunction

•[ShopifyFunction!](/docs/api/admin-graphql/latest/objects/ShopifyFunction)

non-null

    

The Shopify Function implementing the validation.

Show fields

[Anchor to title](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Validation.fields.title)title

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The merchant-facing validation name.

[Anchor to metafieldDefinitions](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Validation.fields.metafieldDefinitions)metafieldDefinitions

•[MetafieldDefinitionConnection!](/docs/api/admin-
graphql/latest/connections/MetafieldDefinitionConnection)

non-nullDeprecated

    

Show fields

[Anchor to Video](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Video)[Video](/docs/api/admin-graphql/latest/objects/Video)

•OBJECT

    

Represents a Shopify hosted video.

Show fields

[Anchor to alt](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
Video.fields.alt)alt

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

A word or phrase to share the nature or contents of a media.

[Anchor to createdAt](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Video.fields.createdAt)createdAt

•[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime)

non-null

    

The date and time ([ISO 8601 format](http://en.wikipedia.org/wiki/ISO_8601))
when the file was created.

[Anchor to duration](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Video.fields.duration)duration

•[Int](/docs/api/admin-graphql/latest/scalars/Int)

    

The video's duration in milliseconds. This value is `null` unless the video's
status field is [READY](https://shopify.dev/api/admin-
graphql/latest/enums/MediaStatus#value-ready).

[Anchor to fileErrors](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Video.fields.fileErrors)fileErrors

•[[FileError!]!](/docs/api/admin-graphql/latest/objects/FileError)

non-null

    

Any errors that have occurred on the file.

Show fields

[Anchor to filename](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Video.fields.filename)filename

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The video's filename.

[Anchor to fileStatus](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Video.fields.fileStatus)fileStatus

•[FileStatus!](/docs/api/admin-graphql/latest/enums/FileStatus)

non-null

    

The status of the file.

Show enum values

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
Video.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to mediaContentType](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Video.fields.mediaContentType)mediaContentType

•[MediaContentType!](/docs/api/admin-graphql/latest/enums/MediaContentType)

non-null

    

The media content type.

Show enum values

[Anchor to mediaErrors](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Video.fields.mediaErrors)mediaErrors

•[[MediaError!]!](/docs/api/admin-graphql/latest/objects/MediaError)

non-null

    

Any errors which have occurred on the media.

Show fields

[Anchor to mediaWarnings](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Video.fields.mediaWarnings)mediaWarnings

•[[MediaWarning!]!](/docs/api/admin-graphql/latest/objects/MediaWarning)

non-null

    

The warnings attached to the media.

Show fields

[Anchor to originalSource](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
Video.fields.originalSource)originalSource

•[VideoSource](/docs/api/admin-graphql/latest/objects/VideoSource)

    

The video's original source. This value is `null` unless the video's status
field is [READY](https://shopify.dev/api/admin-
graphql/latest/enums/MediaStatus#value-ready).

Show fields

[Anchor to preview](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Video.fields.preview)preview

•[MediaPreviewImage](/docs/api/admin-graphql/latest/objects/MediaPreviewImage)

    

The preview image for the media.

Show fields

[Anchor to sources](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Video.fields.sources)sources

•[[VideoSource!]!](/docs/api/admin-graphql/latest/objects/VideoSource)

non-null

    

The video's sources. This value is empty unless the video's status field is
[READY](https://shopify.dev/api/admin-graphql/latest/enums/MediaStatus#value-
ready).

Show fields

[Anchor to status](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Video.fields.status)status

•[MediaStatus!](/docs/api/admin-graphql/latest/enums/MediaStatus)

non-null

    

Current status of the media.

Show enum values

[Anchor to updatedAt](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-Video.fields.updatedAt)updatedAt

•[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime)

non-null

    

The date and time ([ISO 8601 format](http://en.wikipedia.org/wiki/ISO_8601))
when the file was last updated.

[Anchor to WebhookSubscription](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
WebhookSubscription)[WebhookSubscription](/docs/api/admin-
graphql/latest/objects/WebhookSubscription)

•OBJECT

    

A webhook subscription is a persisted data object created by an app using the
REST Admin API or GraphQL Admin API. It describes the topic that the app wants
to receive, and a destination where Shopify should send webhooks of the
specified topic. When an event for a given topic occurs, the webhook
subscription sends a relevant payload to the destination. Learn more about the
[webhooks system](https://shopify.dev/apps/webhooks).

Show fields

[Anchor to apiVersion](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
WebhookSubscription.fields.apiVersion)apiVersion

•[ApiVersion!](/docs/api/admin-graphql/latest/objects/ApiVersion)

non-null

    

The Admin API version that Shopify uses to serialize webhook events. This
value is inherited from the app that created the webhook subscription.

Show fields

[Anchor to createdAt](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-WebhookSubscription.fields.createdAt)createdAt

•[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime)

non-null

    

The date and time when the webhook subscription was created.

[Anchor to filter](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-WebhookSubscription.fields.filter)filter

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

A constraint specified using search syntax that ensures only webhooks that
match the specified filter are emitted. See our [guide on
filters](https://shopify.dev/docs/apps/build/webhooks/customize/filters) for
more details.

[Anchor to format](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-WebhookSubscription.fields.format)format

•[WebhookSubscriptionFormat!](/docs/api/admin-
graphql/latest/enums/WebhookSubscriptionFormat)

non-null

    

The format in which the webhook subscription should send the data.

Show enum values

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
WebhookSubscription.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to includeFields](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
WebhookSubscription.fields.includeFields)includeFields

•[[String!]!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The list of fields to be included in the webhook subscription. Only the fields
specified will be included in the webhook payload. If null, then all fields
will be included. Learn more about [modifying webhook
payloads](https://shopify.dev/docs/apps/build/webhooks/customize/modify_payloads).

[Anchor to legacyResourceId](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
WebhookSubscription.fields.legacyResourceId)legacyResourceId

•[UnsignedInt64!](/docs/api/admin-graphql/latest/scalars/UnsignedInt64)

non-null

    

The ID of the corresponding resource in the REST Admin API.

[Anchor to metafieldNamespaces](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
WebhookSubscription.fields.metafieldNamespaces)metafieldNamespaces

•[[String!]!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The list of namespaces for any metafields that should be included in the
webhook subscription.

[Anchor to metafields](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
WebhookSubscription.fields.metafields)metafields

•[[WebhookSubscriptionMetafieldIdentifier!]!](/docs/api/admin-
graphql/latest/objects/WebhookSubscriptionMetafieldIdentifier)

non-null

    

The list of identifiers specifying metafields to include in the webhook
subscription.

Show fields

[Anchor to topic](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-WebhookSubscription.fields.topic)topic

•[WebhookSubscriptionTopic!](/docs/api/admin-
graphql/latest/enums/WebhookSubscriptionTopic)

non-null

    

The type of event that triggers the webhook. The topic determines when the
webhook subscription sends a webhook, as well as what class of data object
that webhook contains.

Show enum values

[Anchor to updatedAt](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-WebhookSubscription.fields.updatedAt)updatedAt

•[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime)

non-null

    

The date and time when the webhook subscription was updated.

[Anchor to uri](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
WebhookSubscription.fields.uri)uri

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The URI to which the webhook subscription will send events.

[Anchor to callbackUrl](/docs/api/admin-
graphql/latest/interfaces/Node#possible-types-
WebhookSubscription.fields.callbackUrl)callbackUrl

•[URL!](/docs/api/admin-graphql/latest/scalars/URL)

non-nullDeprecated

    

[Anchor to endpoint](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-WebhookSubscription.fields.endpoint)endpoint

•[WebhookSubscriptionEndpoint!](/docs/api/admin-
graphql/latest/unions/WebhookSubscriptionEndpoint)

non-nullDeprecated

    

Show union types

[Anchor to WebPixel](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-WebPixel)[WebPixel](/docs/api/admin-graphql/latest/objects/WebPixel)

•OBJECT

    

The `WebPixel` object enables you to manage JavaScript code snippets that run
on an online store and collect [behavioral
data](https://shopify.dev/docs/api/web-pixels-api/standard-events) for
marketing campaign optimization and analytics.

Learn how to create a [web pixel
extension](https://shopify.dev/docs/apps/build/marketing-analytics/build-web-
pixels) to subscribe your app to events that are emitted by Shopify.

Show fields

[Anchor to id](/docs/api/admin-graphql/latest/interfaces/Node#possible-types-
WebPixel.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to settings](/docs/api/admin-graphql/latest/interfaces/Node#possible-
types-WebPixel.fields.settings)settings

•[JSON!](/docs/api/admin-graphql/latest/scalars/JSON)

non-null

    

The [settings object](https://shopify.dev/docs/apps/build/marketing-
analytics/build-web-pixels#step-2-define-your-web-pixel-settings) for the web
pixel. This object specifies configuration options that control the web
pixel's functionality and behavior. You can find the settings for a web pixel
in `extensions/<your_extension_name>/shopify.extension.toml`.

* * *

Was this section helpful?

YesNo

CodeMap

VariablesSchema

Copy

9

1

2

3

{

"id": ""

}

##### Variables

    
    
    {
    	"id": ""
    }

##### Schema

    
    
    interface Node {
      id: ID!
    }

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

