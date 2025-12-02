# Source: https://shopify.dev/docs/api/customer/latest/objects/Order

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

[Anchor to Order](/docs/api/customer/latest/objects/Order#top)

# Order

object

Copy page MD

A customer’s completed request to purchase one or more products from a shop.
Apps using the Customer Account API must meet the protected customer data
[requirements](https://shopify.dev/docs/apps/launch/protected-customer-data).

##

[Anchor to Fields](/docs/api/customer/latest/objects/Order#fields)Fields

[Anchor to agreements](/docs/api/customer/latest/objects/Order#field-
Order.fields.agreements)agreements

•[SalesAgreementConnection!](/docs/api/customer/latest/connections/SalesAgreementConnection)

non-null[Pre-auth accessible](/docs/apps/build/customer-accounts/order-status-
page#customer-account-api)

    

A list of sales agreements associated with the order.

Show fields

[Anchor to billingAddress](/docs/api/customer/latest/objects/Order#field-
Order.fields.billingAddress)billingAddress

•[CustomerAddress](/docs/api/customer/latest/objects/CustomerAddress)

[Pre-auth accessible](/docs/apps/build/customer-accounts/order-status-
page#customer-account-api)

    

The mailing address provided by the customer. Not all orders have a mailing
address.

Show fields

[Anchor to cancelledAt](/docs/api/customer/latest/objects/Order#field-
Order.fields.cancelledAt)cancelledAt

•[DateTime](/docs/api/customer/latest/scalars/DateTime)

[Pre-auth accessible](/docs/apps/build/customer-accounts/order-status-
page#customer-account-api)

    

The date and time when the order was canceled. Returns `null` if the order
wasn't canceled.

[Anchor to cancelReason](/docs/api/customer/latest/objects/Order#field-
Order.fields.cancelReason)cancelReason

•[OrderCancelReason](/docs/api/customer/latest/enums/OrderCancelReason)

[Pre-auth accessible](/docs/apps/build/customer-accounts/order-status-
page#customer-account-api)

    

The reason for the cancellation of the order. Returns `null` if the order
wasn't canceled.

Show enum values

[Anchor to confirmationNumber](/docs/api/customer/latest/objects/Order#field-
Order.fields.confirmationNumber)confirmationNumber

•[String](/docs/api/customer/latest/scalars/String)

[Pre-auth accessible](/docs/apps/build/customer-accounts/order-status-
page#customer-account-api)

    

A randomly generated alpha-numeric identifier for the order that may be shown
to the customer instead of the sequential order name. For example,
"XPAV284CT", "R50KELTJP" or "35PKUN0UJ". This value isn't guaranteed to be
unique.

[Anchor to createdAt](/docs/api/customer/latest/objects/Order#field-
Order.fields.createdAt)createdAt

•[DateTime!](/docs/api/customer/latest/scalars/DateTime)

non-null[Pre-auth accessible](/docs/apps/build/customer-accounts/order-status-
page#customer-account-api)

    

The date and time when the order was created.

[Anchor to currencyCode](/docs/api/customer/latest/objects/Order#field-
Order.fields.currencyCode)currencyCode

•[CurrencyCode!](/docs/api/customer/latest/enums/CurrencyCode)

non-null[Pre-auth accessible](/docs/apps/build/customer-accounts/order-status-
page#customer-account-api)

    

The shop currency when the order was placed.

Show enum values

[Anchor to customer](/docs/api/customer/latest/objects/Order#field-
Order.fields.customer)customer

•[Customer](/docs/api/customer/latest/objects/Customer)

[Pre-auth accessible](/docs/apps/build/customer-accounts/order-status-
page#customer-account-api)

    

The customer who placed the order.

Show fields

[Anchor to customerLocale](/docs/api/customer/latest/objects/Order#field-
Order.fields.customerLocale)customerLocale

•[String](/docs/api/customer/latest/scalars/String)

[Pre-auth accessible](/docs/apps/build/customer-accounts/order-status-
page#customer-account-api)

    

The locale code representing the region where this specific order was placed.

[Anchor to
discountApplications](/docs/api/customer/latest/objects/Order#field-
Order.fields.discountApplications)discountApplications

•[DiscountApplicationConnection!](/docs/api/customer/latest/connections/DiscountApplicationConnection)

non-null[Pre-auth accessible](/docs/apps/build/customer-accounts/order-status-
page#customer-account-api)

    

The discounts that have been applied to the order.

Show fields

[Anchor to draftOrder](/docs/api/customer/latest/objects/Order#field-
Order.fields.draftOrder)draftOrder

•[DraftOrder](/docs/api/customer/latest/objects/DraftOrder)

[Pre-auth accessible](/docs/apps/build/customer-accounts/order-status-
page#customer-account-api)

    

The draft order associated with the order.

Show fields

[Anchor to edited](/docs/api/customer/latest/objects/Order#field-
Order.fields.edited)edited

•[Boolean!](/docs/api/customer/latest/scalars/Boolean)

non-null[Pre-auth accessible](/docs/apps/build/customer-accounts/order-status-
page#customer-account-api)

    

Whether the order has been edited or not.

[Anchor to email](/docs/api/customer/latest/objects/Order#field-
Order.fields.email)email

•[String](/docs/api/customer/latest/scalars/String)

[Pre-auth accessible](/docs/apps/build/customer-accounts/order-status-
page#customer-account-api)

    

The email address of the customer.

[Anchor to financialStatus](/docs/api/customer/latest/objects/Order#field-
Order.fields.financialStatus)financialStatus

•[OrderFinancialStatus](/docs/api/customer/latest/enums/OrderFinancialStatus)

[Pre-auth accessible](/docs/apps/build/customer-accounts/order-status-
page#customer-account-api)

    

The financial status of the order.

Show enum values

[Anchor to fulfillments](/docs/api/customer/latest/objects/Order#field-
Order.fields.fulfillments)fulfillments

•[FulfillmentConnection!](/docs/api/customer/latest/connections/FulfillmentConnection)

non-null[Pre-auth accessible](/docs/apps/build/customer-accounts/order-status-
page#customer-account-api)

    

The fulfillments associated with the order.

Show fields

[Anchor to fulfillmentStatus](/docs/api/customer/latest/objects/Order#field-
Order.fields.fulfillmentStatus)fulfillmentStatus

•[OrderFulfillmentStatus!](/docs/api/customer/latest/enums/OrderFulfillmentStatus)

non-null[Pre-auth accessible](/docs/apps/build/customer-accounts/order-status-
page#customer-account-api)

    

The fulfillment status of the order.

Show enum values

[Anchor to id](/docs/api/customer/latest/objects/Order#field-
Order.fields.id)id

•[ID!](/docs/api/customer/latest/scalars/ID)

non-null[Pre-auth accessible](/docs/apps/build/customer-accounts/order-status-
page#customer-account-api)

    

A globally-unique ID.

[Anchor to lineItems](/docs/api/customer/latest/objects/Order#field-
Order.fields.lineItems)lineItems

•[LineItemConnection!](/docs/api/customer/latest/connections/LineItemConnection)

non-null[Pre-auth accessible](/docs/apps/build/customer-accounts/order-status-
page#customer-account-api)

    

The list of line items of the order.

Show fields

[Anchor to locationName](/docs/api/customer/latest/objects/Order#field-
Order.fields.locationName)locationName

•[String](/docs/api/customer/latest/scalars/String)

[Pre-auth accessible](/docs/apps/build/customer-accounts/order-status-
page#customer-account-api)

    

The name of the fulfillment location assigned at the time of order creation.

[Anchor to metafield](/docs/api/customer/latest/objects/Order#field-
Order.fields.metafield)metafield

•[Metafield](/docs/api/customer/latest/objects/Metafield)

[Pre-auth accessible](/docs/apps/build/customer-accounts/order-status-
page#customer-account-api)

    

A metafield found by namespace and key.

Show fields

[Anchor to metafields](/docs/api/customer/latest/objects/Order#field-
Order.fields.metafields)metafields

•[[Metafield]!](/docs/api/customer/latest/objects/Metafield)

non-null[Pre-auth accessible](/docs/apps/build/customer-accounts/order-status-
page#customer-account-api)

    

The metafields associated with the resource matching the supplied list of
namespaces and keys.

Show fields

[Anchor to name](/docs/api/customer/latest/objects/Order#field-
Order.fields.name)name

•[String!](/docs/api/customer/latest/scalars/String)

non-null[Pre-auth accessible](/docs/apps/build/customer-accounts/order-status-
page#customer-account-api)

    

The identifier for the order that appears on the order. For example, _#1000_
or _Store1001.

[Anchor to note](/docs/api/customer/latest/objects/Order#field-
Order.fields.note)note

•[String](/docs/api/customer/latest/scalars/String)

[Pre-auth accessible](/docs/apps/build/customer-accounts/order-status-
page#customer-account-api)

    

The order's notes.

[Anchor to number](/docs/api/customer/latest/objects/Order#field-
Order.fields.number)number

•[Int!](/docs/api/customer/latest/scalars/Int)

non-null[Pre-auth accessible](/docs/apps/build/customer-accounts/order-status-
page#customer-account-api)

    

A unique numeric identifier for the order, used by both the shop owner and
customer.

[Anchor to paymentInformation](/docs/api/customer/latest/objects/Order#field-
Order.fields.paymentInformation)paymentInformation

•[OrderPaymentInformation](/docs/api/customer/latest/objects/OrderPaymentInformation)

[Pre-auth accessible](/docs/apps/build/customer-accounts/order-status-
page#customer-account-api)

    

The payment information for the order.

Show fields

[Anchor to phone](/docs/api/customer/latest/objects/Order#field-
Order.fields.phone)phone

•[String](/docs/api/customer/latest/scalars/String)

    

The phone number of the customer for SMS notifications.

[Anchor to poNumber](/docs/api/customer/latest/objects/Order#field-
Order.fields.poNumber)poNumber

•[String](/docs/api/customer/latest/scalars/String)

[Pre-auth accessible](/docs/apps/build/customer-accounts/order-status-
page#customer-account-api)

    

The purchase order number of the order.

[Anchor to processedAt](/docs/api/customer/latest/objects/Order#field-
Order.fields.processedAt)processedAt

•[DateTime!](/docs/api/customer/latest/scalars/DateTime)

non-null[Pre-auth accessible](/docs/apps/build/customer-accounts/order-status-
page#customer-account-api)

    

The date and time when the order was processed. This value can be set to dates
in the past when importing from other systems. If no value is provided, it
will be auto-generated based on current date and time.

[Anchor to purchasingEntity](/docs/api/customer/latest/objects/Order#field-
Order.fields.purchasingEntity)purchasingEntity

•[PurchasingEntity](/docs/api/customer/latest/unions/PurchasingEntity)

[Pre-auth accessible](/docs/apps/build/customer-accounts/order-status-
page#customer-account-api)

    

The purchasing entity for the order.

Show union types

[Anchor to refunds](/docs/api/customer/latest/objects/Order#field-
Order.fields.refunds)refunds

•[[Refund!]!](/docs/api/customer/latest/objects/Refund)

non-null[Pre-auth accessible](/docs/apps/build/customer-accounts/order-status-
page#customer-account-api)

    

A list of refunds associated with the order.

Show fields

[Anchor to requiresShipping](/docs/api/customer/latest/objects/Order#field-
Order.fields.requiresShipping)requiresShipping

•[Boolean!](/docs/api/customer/latest/scalars/Boolean)

non-null[Pre-auth accessible](/docs/apps/build/customer-accounts/order-status-
page#customer-account-api)

    

Whether the order requires shipping.

[Anchor to returnInformation](/docs/api/customer/latest/objects/Order#field-
Order.fields.returnInformation)returnInformation

•[OrderReturnInformation!](/docs/api/customer/latest/objects/OrderReturnInformation)

non-null[Pre-auth accessible](/docs/apps/build/customer-accounts/order-status-
page#customer-account-api)

    

The return information for the order.

Show fields

[Anchor to returns](/docs/api/customer/latest/objects/Order#field-
Order.fields.returns)returns

•[ReturnConnection!](/docs/api/customer/latest/connections/ReturnConnection)

non-null[Pre-auth accessible](/docs/apps/build/customer-accounts/order-status-
page#customer-account-api)

    

The list of returns for the order with pagination.

Show fields

[Anchor to shippingAddress](/docs/api/customer/latest/objects/Order#field-
Order.fields.shippingAddress)shippingAddress

•[CustomerAddress](/docs/api/customer/latest/objects/CustomerAddress)

[Pre-auth accessible](/docs/apps/build/customer-accounts/order-status-
page#customer-account-api)

    

The mailing address to which the order items are shipped.

Show fields

[Anchor to
shippingDiscountAllocations](/docs/api/customer/latest/objects/Order#field-
Order.fields.shippingDiscountAllocations)shippingDiscountAllocations

•[[DiscountAllocation!]!](/docs/api/customer/latest/objects/DiscountAllocation)

non-null[Pre-auth accessible](/docs/apps/build/customer-accounts/order-status-
page#customer-account-api)

    

The discounts that have been allocated onto the shipping line by discount
applications.

Show fields

[Anchor to shippingLine](/docs/api/customer/latest/objects/Order#field-
Order.fields.shippingLine)shippingLine

•[ShippingLine](/docs/api/customer/latest/objects/ShippingLine)

[Pre-auth accessible](/docs/apps/build/customer-accounts/order-status-
page#customer-account-api)

    

A summary of all shipping costs on the order.

Show fields

[Anchor to statusPageUrl](/docs/api/customer/latest/objects/Order#field-
Order.fields.statusPageUrl)statusPageUrl

•[URL!](/docs/api/customer/latest/scalars/URL)

non-null[Pre-auth accessible](/docs/apps/build/customer-accounts/order-status-
page#customer-account-api)

    

The unique URL for the status page of the order.

[Anchor to
subscriptionContracts](/docs/api/customer/latest/objects/Order#field-
Order.fields.subscriptionContracts)subscriptionContracts

•[SubscriptionContractConnection](/docs/api/customer/latest/connections/SubscriptionContractConnection)

    

The customer Subscription Contracts associated with the order.

Show fields

[Anchor to subtotal](/docs/api/customer/latest/objects/Order#field-
Order.fields.subtotal)subtotal

•[MoneyV2](/docs/api/customer/latest/objects/MoneyV2)

[Pre-auth accessible](/docs/apps/build/customer-accounts/order-status-
page#customer-account-api)

    

The price of the order before duties, shipping, and taxes.

Show fields

[Anchor to totalDuties](/docs/api/customer/latest/objects/Order#field-
Order.fields.totalDuties)totalDuties

•[MoneyV2](/docs/api/customer/latest/objects/MoneyV2)

[Pre-auth accessible](/docs/apps/build/customer-accounts/order-status-
page#customer-account-api)

    

The total amount of duties after returns.

Show fields

[Anchor to totalPrice](/docs/api/customer/latest/objects/Order#field-
Order.fields.totalPrice)totalPrice

•[MoneyV2!](/docs/api/customer/latest/objects/MoneyV2)

non-null[Pre-auth accessible](/docs/apps/build/customer-accounts/order-status-
page#customer-account-api)

    

The total amount of the order (including taxes and discounts) minus the
amounts for line items that have been returned.

Show fields

[Anchor to totalRefunded](/docs/api/customer/latest/objects/Order#field-
Order.fields.totalRefunded)totalRefunded

•[MoneyV2!](/docs/api/customer/latest/objects/MoneyV2)

non-null[Pre-auth accessible](/docs/apps/build/customer-accounts/order-status-
page#customer-account-api)

    

The total amount refunded.

Show fields

[Anchor to totalShipping](/docs/api/customer/latest/objects/Order#field-
Order.fields.totalShipping)totalShipping

•[MoneyV2!](/docs/api/customer/latest/objects/MoneyV2)

non-null[Pre-auth accessible](/docs/apps/build/customer-accounts/order-status-
page#customer-account-api)

    

The total cost of shipping.

Show fields

[Anchor to totalTax](/docs/api/customer/latest/objects/Order#field-
Order.fields.totalTax)totalTax

•[MoneyV2](/docs/api/customer/latest/objects/MoneyV2)

[Pre-auth accessible](/docs/apps/build/customer-accounts/order-status-
page#customer-account-api)

    

The total cost of taxes.

Show fields

[Anchor to totalTip](/docs/api/customer/latest/objects/Order#field-
Order.fields.totalTip)totalTip

•[MoneyV2](/docs/api/customer/latest/objects/MoneyV2)

[Pre-auth accessible](/docs/apps/build/customer-accounts/order-status-
page#customer-account-api)

    

The total value of tips.

Show fields

[Anchor to transactions](/docs/api/customer/latest/objects/Order#field-
Order.fields.transactions)transactions

•[[OrderTransaction!]!](/docs/api/customer/latest/objects/OrderTransaction)

non-null[Pre-auth accessible](/docs/apps/build/customer-accounts/order-status-
page#customer-account-api)

    

A list of transactions associated with the order.

Show fields

[Anchor to updatedAt](/docs/api/customer/latest/objects/Order#field-
Order.fields.updatedAt)updatedAt

•[DateTime!](/docs/api/customer/latest/scalars/DateTime)

non-null

    

The date and time when the order was last updated.

* * *

Was this section helpful?

YesNo

## Map

### Fields and connections with this object

  * {}[Company.orders](/docs/api/customer/latest/objects/Company#field-Company.fields.orders)
  * {}[CompanyContact.orders](/docs/api/customer/latest/objects/CompanyContact#field-CompanyContact.fields.orders)
  * {}[CompanyLocation.orders](/docs/api/customer/latest/objects/CompanyLocation#field-CompanyLocation.fields.orders)
  * {}[Customer.orders](/docs/api/customer/latest/objects/Customer#field-Customer.fields.orders)
  * {}[DraftOrder.order](/docs/api/customer/latest/objects/DraftOrder#field-DraftOrder.fields.order)
  * {}[OrderAgreement.order](/docs/api/customer/latest/objects/OrderAgreement#field-OrderAgreement.fields.order)
  * <->[OrderConnection.nodes](/docs/api/customer/latest/connections/OrderConnection#returns-nodes)
  * {}[OrderEdge.node](/docs/api/customer/latest/objects/OrderEdge#field-OrderEdge.fields.node)
  * {}[OrderTransaction.order](/docs/api/customer/latest/objects/OrderTransaction#field-OrderTransaction.fields.order)
  * {}[SubscriptionContract.orders](/docs/api/customer/latest/objects/SubscriptionContract#field-SubscriptionContract.fields.orders)
  * {}[SubscriptionContract.originOrder](/docs/api/customer/latest/objects/SubscriptionContract#field-SubscriptionContract.fields.originOrder)
  * ||-[SubscriptionContractBase.orders](/docs/api/customer/latest/interfaces/SubscriptionContractBase#fields-orders)

* * *

##

[Anchor to Queries](/docs/api/customer/latest/objects/Order#queries)Queries

[Anchor to order](/docs/api/customer/latest/objects/Order#query-
order)[order](/docs/api/customer/latest/queries/order)

•query

    

Returns an Order resource by ID. Apps using the Customer Account API must meet
the protected customer data
[requirements](https://shopify.dev/docs/apps/launch/protected-customer-data).

Show fields

* * *

Was this section helpful?

YesNo

## <?>Order Queries

### Queried by

  * <?>[order](/docs/api/customer/latest/queries/order)

* * *

##

[Anchor to
Interfaces](/docs/api/customer/latest/objects/Order#interfaces)Interfaces

[Anchor to HasMetafields](/docs/api/customer/latest/objects/Order#interface-
HasMetafields)[HasMetafields](/docs/api/customer/latest/interfaces/HasMetafields)

•interface

[Anchor to Node](/docs/api/customer/latest/objects/Order#interface-
Node)[Node](/docs/api/customer/latest/interfaces/Node)

•interface

* * *

Was this section helpful?

YesNo

## ||-Order Implements

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

