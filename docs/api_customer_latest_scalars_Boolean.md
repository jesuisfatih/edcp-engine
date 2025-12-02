# Source: https://shopify.dev/docs/api/customer/latest/scalars/Boolean

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

[Anchor to Boolean](/docs/api/customer/latest/scalars/Boolean#top)

# Boolean

scalar

Copy page MD

Represents `true` or `false` values.

## Map

### Fields with this scalar

  * <-|[AvailableShippingRates.ready](/docs/api/customer/latest/objects/AvailableShippingRates#field-AvailableShippingRates.fields.ready)
  * <-|[BuyerExperienceConfiguration.payNowOnly](/docs/api/customer/latest/objects/BuyerExperienceConfiguration#field-BuyerExperienceConfiguration.fields.payNowOnly)
  * <-|[Checkout.ready](/docs/api/customer/latest/objects/Checkout#field-Checkout.fields.ready)
  * <-|[Checkout.requiresShipping](/docs/api/customer/latest/objects/Checkout#field-Checkout.fields.requiresShipping)
  * <-|[Checkout.taxExempt](/docs/api/customer/latest/objects/Checkout#field-Checkout.fields.taxExempt)
  * <-|[Checkout.taxesIncluded](/docs/api/customer/latest/objects/Checkout#field-Checkout.fields.taxesIncluded)
  * <-|[DraftOrder.inReview](/docs/api/customer/latest/objects/DraftOrder#field-DraftOrder.fields.inReview)
  * <-|[DraftOrder.requiresShipping](/docs/api/customer/latest/objects/DraftOrder#field-DraftOrder.fields.requiresShipping)
  * <-|[DraftOrder.taxExempt](/docs/api/customer/latest/objects/DraftOrder#field-DraftOrder.fields.taxExempt)
  * <-|[DraftOrder.taxesIncluded](/docs/api/customer/latest/objects/DraftOrder#field-DraftOrder.fields.taxesIncluded)
  * <-|[DraftOrderLineItem.requiresShipping](/docs/api/customer/latest/objects/DraftOrderLineItem#field-DraftOrderLineItem.fields.requiresShipping)
  * <-|[DraftOrderLineItem.taxable](/docs/api/customer/latest/objects/DraftOrderLineItem#field-DraftOrderLineItem.fields.taxable)
  * <-|[ExchangeLineItem.productHasOnlyDefaultVariant](/docs/api/customer/latest/objects/ExchangeLineItem#field-ExchangeLineItem.fields.productHasOnlyDefaultVariant)
  * <-|[Fulfillment.isPickedUp](/docs/api/customer/latest/objects/Fulfillment#field-Fulfillment.fields.isPickedUp)
  * <-|[Fulfillment.requiresShipping](/docs/api/customer/latest/objects/Fulfillment#field-Fulfillment.fields.requiresShipping)
  * <-|[LineItem.giftCard](/docs/api/customer/latest/objects/LineItem#field-LineItem.fields.giftCard)
  * <-|[LineItem.requiresShipping](/docs/api/customer/latest/objects/LineItem#field-LineItem.fields.requiresShipping)
  * <-|[Order.edited](/docs/api/customer/latest/objects/Order#field-Order.fields.edited)
  * <-|[Order.requiresShipping](/docs/api/customer/latest/objects/Order#field-Order.fields.requiresShipping)
  * <-|[OrderReturnInformation.hasRestockingFee](/docs/api/customer/latest/objects/OrderReturnInformation#field-OrderReturnInformation.fields.hasRestockingFee)
  * <-|[OrderReturnInformation.hasReturnShippingFee](/docs/api/customer/latest/objects/OrderReturnInformation#field-OrderReturnInformation.fields.hasReturnShippingFee)
  * <-|[PageInfo.hasNextPage](/docs/api/customer/latest/objects/PageInfo#field-PageInfo.fields.hasNextPage)
  * <-|[PageInfo.hasPreviousPage](/docs/api/customer/latest/objects/PageInfo#field-PageInfo.fields.hasPreviousPage)
  * <-|[PaymentSchedule.completed](/docs/api/customer/latest/objects/PaymentSchedule#field-PaymentSchedule.fields.completed)
  * <-|[PaymentTerms.overdue](/docs/api/customer/latest/objects/PaymentTerms#field-PaymentTerms.fields.overdue)
  * <-|[ReverseDelivery.customerGeneratedLabel](/docs/api/customer/latest/objects/ReverseDelivery#field-ReverseDelivery.fields.customerGeneratedLabel)
  * <-|[SubscriptionBillingCycle.edited](/docs/api/customer/latest/objects/SubscriptionBillingCycle#field-SubscriptionBillingCycle.fields.edited)
  * <-|[SubscriptionBillingCycle.skipped](/docs/api/customer/latest/objects/SubscriptionBillingCycle#field-SubscriptionBillingCycle.fields.skipped)
  * <-|[SubscriptionDiscount.appliesToAllLines](/docs/api/customer/latest/objects/SubscriptionDiscount#field-SubscriptionDiscount.fields.appliesToAllLines)
  * <-|[SubscriptionDiscountFixedAmountValue.appliesOnEachItem](/docs/api/customer/latest/objects/SubscriptionDiscountFixedAmountValue#field-SubscriptionDiscountFixedAmountValue.fields.appliesOnEachItem)

Show hidden

### Arguments with this scalar

  * <-|[CalculatedReturn.returnLineItems(reverse)](/docs/api/customer/latest/objects/CalculatedReturn#field-CalculatedReturn.fields.returnLineItems.arguments.reverse)
  * <-|[Checkout.discountApplications(reverse)](/docs/api/customer/latest/objects/Checkout#field-Checkout.fields.discountApplications.arguments.reverse)
  * <-|[Checkout.lineItems(reverse)](/docs/api/customer/latest/objects/Checkout#field-Checkout.fields.lineItems.arguments.reverse)
  * <-|[Company.draftOrders(reverse)](/docs/api/customer/latest/objects/Company#field-Company.fields.draftOrders.arguments.reverse)
  * <-|[Company.locations(reverse)](/docs/api/customer/latest/objects/Company#field-Company.fields.locations.arguments.reverse)
  * <-|[Company.orders(reverse)](/docs/api/customer/latest/objects/Company#field-Company.fields.orders.arguments.reverse)
  * <-|[CompanyAddress.formattedAddress(withName)](/docs/api/customer/latest/objects/CompanyAddress#field-CompanyAddress.fields.formattedAddress.arguments.withName)
  * <-|[CompanyAddress.formattedAddress(withCompanyName)](/docs/api/customer/latest/objects/CompanyAddress#field-CompanyAddress.fields.formattedAddress.arguments.withCompanyName)
  * <-|[CompanyContact.draftOrders(reverse)](/docs/api/customer/latest/objects/CompanyContact#field-CompanyContact.fields.draftOrders.arguments.reverse)
  * <-|[CompanyContact.locations(reverse)](/docs/api/customer/latest/objects/CompanyContact#field-CompanyContact.fields.locations.arguments.reverse)
  * <-|[CompanyContact.orders(reverse)](/docs/api/customer/latest/objects/CompanyContact#field-CompanyContact.fields.orders.arguments.reverse)
  * <-|[CompanyLocation.contacts(reverse)](/docs/api/customer/latest/objects/CompanyLocation#field-CompanyLocation.fields.contacts.arguments.reverse)
  * <-|[CompanyLocation.draftOrders(reverse)](/docs/api/customer/latest/objects/CompanyLocation#field-CompanyLocation.fields.draftOrders.arguments.reverse)
  * <-|[CompanyLocation.orders(reverse)](/docs/api/customer/latest/objects/CompanyLocation#field-CompanyLocation.fields.orders.arguments.reverse)
  * <-|[CompanyLocation.roleAssignments(reverse)](/docs/api/customer/latest/objects/CompanyLocation#field-CompanyLocation.fields.roleAssignments.arguments.reverse)
  * <-|[Customer.addresses(skipDefault)](/docs/api/customer/latest/objects/Customer#field-Customer.fields.addresses.arguments.skipDefault)
  * <-|[Customer.addresses(reverse)](/docs/api/customer/latest/objects/Customer#field-Customer.fields.addresses.arguments.reverse)
  * <-|[Customer.companyContacts(reverse)](/docs/api/customer/latest/objects/Customer#field-Customer.fields.companyContacts.arguments.reverse)
  * <-|[Customer.draftOrders(reverse)](/docs/api/customer/latest/objects/Customer#field-Customer.fields.draftOrders.arguments.reverse)
  * <-|[Customer.orders(reverse)](/docs/api/customer/latest/objects/Customer#field-Customer.fields.orders.arguments.reverse)
  * <-|[Customer.subscriptionContracts(reverse)](/docs/api/customer/latest/objects/Customer#field-Customer.fields.subscriptionContracts.arguments.reverse)
  * <-|[CustomerAddress.formatted(withName)](/docs/api/customer/latest/objects/CustomerAddress#field-CustomerAddress.fields.formatted.arguments.withName)
  * <-|[CustomerAddress.formatted(withCompany)](/docs/api/customer/latest/objects/CustomerAddress#field-CustomerAddress.fields.formatted.arguments.withCompany)
  * <-|[DraftOrder.lineItems(reverse)](/docs/api/customer/latest/objects/DraftOrder#field-DraftOrder.fields.lineItems.arguments.reverse)
  * <-|[Fulfillment.events(reverse)](/docs/api/customer/latest/objects/Fulfillment#field-Fulfillment.fields.events.arguments.reverse)
  * <-|[Fulfillment.fulfillmentLineItems(reverse)](/docs/api/customer/latest/objects/Fulfillment#field-Fulfillment.fields.fulfillmentLineItems.arguments.reverse)
  * <-|[Order.agreements(reverse)](/docs/api/customer/latest/objects/Order#field-Order.fields.agreements.arguments.reverse)
  * <-|[Order.discountApplications(reverse)](/docs/api/customer/latest/objects/Order#field-Order.fields.discountApplications.arguments.reverse)
  * <-|[Order.fulfillments(reverse)](/docs/api/customer/latest/objects/Order#field-Order.fields.fulfillments.arguments.reverse)
  * <-|[Order.lineItems(reverse)](/docs/api/customer/latest/objects/Order#field-Order.fields.lineItems.arguments.reverse)

Show hidden

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

