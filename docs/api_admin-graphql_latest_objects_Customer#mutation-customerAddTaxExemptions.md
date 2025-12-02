# Source: https://shopify.dev/docs/api/admin-graphql/latest/objects/Customer#mutation-customerAddTaxExemptions

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

[Anchor to Customer](/docs/api/admin-graphql/latest/objects/Customer#top)

# Customer

object

Copy page MD

Requires `read_customers` access scope.

Represents information about a customer of the shop, such as the customer's
contact details, their order history, and whether they've agreed to receive
marketing material by email.

**Caution:** Only use this data if it's required for your app's functionality.
Shopify will restrict [access to scopes](https://shopify.dev/api/usage/access-
scopes) for apps that don't have a legitimate use for the associated data.

##

[Anchor to Fields](/docs/api/admin-
graphql/latest/objects/Customer#fields)Fields

[Anchor to addresses](/docs/api/admin-graphql/latest/objects/Customer#field-
Customer.fields.addresses)addresses

•[[MailingAddress!]!](/docs/api/admin-graphql/latest/objects/MailingAddress)

non-null

    

A list of addresses associated with the customer.

Show fields

[Anchor to addressesV2](/docs/api/admin-graphql/latest/objects/Customer#field-
Customer.fields.addressesV2)addressesV2

•[MailingAddressConnection!](/docs/api/admin-
graphql/latest/connections/MailingAddressConnection)

non-null

    

The addresses associated with the customer.

Show fields

[Anchor to amountSpent](/docs/api/admin-graphql/latest/objects/Customer#field-
Customer.fields.amountSpent)amountSpent

•[MoneyV2!](/docs/api/admin-graphql/latest/objects/MoneyV2)

non-null

    

The total amount that the customer has spent on orders in their lifetime.

Show fields

[Anchor to canDelete](/docs/api/admin-graphql/latest/objects/Customer#field-
Customer.fields.canDelete)canDelete

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether the merchant can delete the customer from their store.

A customer can be deleted from a store only if they haven't yet made an order.
After a customer makes an order, they can't be deleted from a store.

[Anchor to companyContactProfiles](/docs/api/admin-
graphql/latest/objects/Customer#field-
Customer.fields.companyContactProfiles)companyContactProfiles

•[[CompanyContact!]!](/docs/api/admin-graphql/latest/objects/CompanyContact)

non-null

    

A list of the customer's company contact profiles.

Show fields

[Anchor to createdAt](/docs/api/admin-graphql/latest/objects/Customer#field-
Customer.fields.createdAt)createdAt

•[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime)

non-null

    

The date and time when the customer was added to the store.

[Anchor to dataSaleOptOut](/docs/api/admin-
graphql/latest/objects/Customer#field-
Customer.fields.dataSaleOptOut)dataSaleOptOut

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether the customer has opted out of having their data sold.

[Anchor to defaultAddress](/docs/api/admin-
graphql/latest/objects/Customer#field-
Customer.fields.defaultAddress)defaultAddress

•[MailingAddress](/docs/api/admin-graphql/latest/objects/MailingAddress)

    

The default address associated with the customer.

Show fields

[Anchor to defaultEmailAddress](/docs/api/admin-
graphql/latest/objects/Customer#field-
Customer.fields.defaultEmailAddress)defaultEmailAddress

•[CustomerEmailAddress](/docs/api/admin-
graphql/latest/objects/CustomerEmailAddress)

    

The customer's default email address.

Show fields

[Anchor to defaultPhoneNumber](/docs/api/admin-
graphql/latest/objects/Customer#field-
Customer.fields.defaultPhoneNumber)defaultPhoneNumber

•[CustomerPhoneNumber](/docs/api/admin-
graphql/latest/objects/CustomerPhoneNumber)

    

The customer's default phone number.

Show fields

[Anchor to displayName](/docs/api/admin-graphql/latest/objects/Customer#field-
Customer.fields.displayName)displayName

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The full name of the customer, based on the values for first_name and
last_name. If the first_name and last_name are not available, then this falls
back to the customer's email address, and if that is not available, the
customer's phone number.

[Anchor to events](/docs/api/admin-graphql/latest/objects/Customer#field-
Customer.fields.events)events

•[EventConnection!](/docs/api/admin-
graphql/latest/connections/EventConnection)

non-null

    

A list of events associated with the customer.

Show fields

[Anchor to firstName](/docs/api/admin-graphql/latest/objects/Customer#field-
Customer.fields.firstName)firstName

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The customer's first name.

[Anchor to id](/docs/api/admin-graphql/latest/objects/Customer#field-
Customer.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to image](/docs/api/admin-graphql/latest/objects/Customer#field-
Customer.fields.image)image

•[Image!](/docs/api/admin-graphql/latest/objects/Image)

non-null

    

The image associated with the customer.

Show fields

[Anchor to lastName](/docs/api/admin-graphql/latest/objects/Customer#field-
Customer.fields.lastName)lastName

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The customer's last name.

[Anchor to lastOrder](/docs/api/admin-graphql/latest/objects/Customer#field-
Customer.fields.lastOrder)lastOrder

•[Order](/docs/api/admin-graphql/latest/objects/Order)

    

The customer's last order.

Show fields

[Anchor to legacyResourceId](/docs/api/admin-
graphql/latest/objects/Customer#field-
Customer.fields.legacyResourceId)legacyResourceId

•[UnsignedInt64!](/docs/api/admin-graphql/latest/scalars/UnsignedInt64)

non-null

    

The ID of the corresponding resource in the REST Admin API.

[Anchor to lifetimeDuration](/docs/api/admin-
graphql/latest/objects/Customer#field-
Customer.fields.lifetimeDuration)lifetimeDuration

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The amount of time since the customer was first added to the store.

Example: 'about 12 years'.

[Anchor to locale](/docs/api/admin-graphql/latest/objects/Customer#field-
Customer.fields.locale)locale

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The customer's locale.

[Anchor to mergeable](/docs/api/admin-graphql/latest/objects/Customer#field-
Customer.fields.mergeable)mergeable

•[CustomerMergeable!](/docs/api/admin-
graphql/latest/objects/CustomerMergeable)

non-null

    

Whether the customer can be merged with another customer.

Show fields

[Anchor to metafield](/docs/api/admin-graphql/latest/objects/Customer#field-
Customer.fields.metafield)metafield

•[Metafield](/docs/api/admin-graphql/latest/objects/Metafield)

    

A [custom field](https://shopify.dev/docs/apps/build/custom-data), including
its `namespace` and `key`, that's associated with a Shopify resource for the
purposes of adding and storing additional information.

Show fields

[Anchor to metafields](/docs/api/admin-graphql/latest/objects/Customer#field-
Customer.fields.metafields)metafields

•[MetafieldConnection!](/docs/api/admin-
graphql/latest/connections/MetafieldConnection)

non-null

    

A list of [custom fields](https://shopify.dev/docs/apps/build/custom-data)
that a merchant associates with a Shopify resource.

Show fields

[Anchor to multipassIdentifier](/docs/api/admin-
graphql/latest/objects/Customer#field-
Customer.fields.multipassIdentifier)multipassIdentifier

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

A unique identifier for the customer that's used with Multipass login.

[Anchor to note](/docs/api/admin-graphql/latest/objects/Customer#field-
Customer.fields.note)note

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

A note about the customer.

[Anchor to numberOfOrders](/docs/api/admin-
graphql/latest/objects/Customer#field-
Customer.fields.numberOfOrders)numberOfOrders

•[UnsignedInt64!](/docs/api/admin-graphql/latest/scalars/UnsignedInt64)

non-null

    

The number of orders that the customer has made at the store in their
lifetime.

[Anchor to orders](/docs/api/admin-graphql/latest/objects/Customer#field-
Customer.fields.orders)orders

•[OrderConnection!](/docs/api/admin-
graphql/latest/connections/OrderConnection)

non-null

    

A list of the customer's orders.

Show fields

[Anchor to paymentMethods](/docs/api/admin-
graphql/latest/objects/Customer#field-
Customer.fields.paymentMethods)paymentMethods

•[CustomerPaymentMethodConnection!](/docs/api/admin-
graphql/latest/connections/CustomerPaymentMethodConnection)

non-null

    

A list of the customer's payment methods.

Show fields

[Anchor to productSubscriberStatus](/docs/api/admin-
graphql/latest/objects/Customer#field-
Customer.fields.productSubscriberStatus)productSubscriberStatus

•[CustomerProductSubscriberStatus!](/docs/api/admin-
graphql/latest/enums/CustomerProductSubscriberStatus)

non-null

    

Possible subscriber states of a customer defined by their subscription
contracts.

Show enum values

[Anchor to state](/docs/api/admin-graphql/latest/objects/Customer#field-
Customer.fields.state)state

•[CustomerState!](/docs/api/admin-graphql/latest/enums/CustomerState)

non-null

    

The state of the customer's account with the shop.

Please note that this only meaningful when Classic Customer Accounts is
active.

Show enum values

[Anchor to statistics](/docs/api/admin-graphql/latest/objects/Customer#field-
Customer.fields.statistics)statistics

•[CustomerStatistics!](/docs/api/admin-
graphql/latest/objects/CustomerStatistics)

non-null

    

The statistics for a given customer.

Show fields

[Anchor to storeCreditAccounts](/docs/api/admin-
graphql/latest/objects/Customer#field-
Customer.fields.storeCreditAccounts)storeCreditAccounts

•[StoreCreditAccountConnection!](/docs/api/admin-
graphql/latest/connections/StoreCreditAccountConnection)

non-null

    

Returns a list of store credit accounts that belong to the owner resource. A
store credit account owner can hold multiple accounts each with a different
currency.

Show fields

[Anchor to subscriptionContracts](/docs/api/admin-
graphql/latest/objects/Customer#field-
Customer.fields.subscriptionContracts)subscriptionContracts

•[SubscriptionContractConnection!](/docs/api/admin-
graphql/latest/connections/SubscriptionContractConnection)

non-null

    

A list of the customer's subscription contracts.

Show fields

[Anchor to tags](/docs/api/admin-graphql/latest/objects/Customer#field-
Customer.fields.tags)tags

•[[String!]!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

A comma separated list of tags that have been added to the customer.

[Anchor to taxExempt](/docs/api/admin-graphql/latest/objects/Customer#field-
Customer.fields.taxExempt)taxExempt

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether the customer is exempt from being charged taxes on their orders.

[Anchor to taxExemptions](/docs/api/admin-
graphql/latest/objects/Customer#field-
Customer.fields.taxExemptions)taxExemptions

•[[TaxExemption!]!](/docs/api/admin-graphql/latest/enums/TaxExemption)

non-null

    

The list of tax exemptions applied to the customer.

Show enum values

[Anchor to updatedAt](/docs/api/admin-graphql/latest/objects/Customer#field-
Customer.fields.updatedAt)updatedAt

•[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime)

non-null

    

The date and time when the customer was last updated.

[Anchor to verifiedEmail](/docs/api/admin-
graphql/latest/objects/Customer#field-
Customer.fields.verifiedEmail)verifiedEmail

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether the customer has verified their email address. Defaults to `true` if
the customer is created through the Shopify admin or API.

### Deprecated fields

[Anchor to email](/docs/api/admin-graphql/latest/objects/Customer#field-
Customer.fields.email)email

•[String](/docs/api/admin-graphql/latest/scalars/String)

Deprecated

    

[Anchor to emailMarketingConsent](/docs/api/admin-
graphql/latest/objects/Customer#field-
Customer.fields.emailMarketingConsent)emailMarketingConsent

•[CustomerEmailMarketingConsentState](/docs/api/admin-
graphql/latest/objects/CustomerEmailMarketingConsentState)

Deprecated

    

Show fields

[Anchor to hasTimelineComment](/docs/api/admin-
graphql/latest/objects/Customer#field-
Customer.fields.hasTimelineComment)hasTimelineComment

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-nullDeprecated

    

[Anchor to market](/docs/api/admin-graphql/latest/objects/Customer#field-
Customer.fields.market)market

•[Market](/docs/api/admin-graphql/latest/objects/Market)

Deprecated

    

Show fields

[Anchor to metafieldDefinitions](/docs/api/admin-
graphql/latest/objects/Customer#field-
Customer.fields.metafieldDefinitions)metafieldDefinitions

•[MetafieldDefinitionConnection!](/docs/api/admin-
graphql/latest/connections/MetafieldDefinitionConnection)

non-nullDeprecated

    

Show fields

[Anchor to phone](/docs/api/admin-graphql/latest/objects/Customer#field-
Customer.fields.phone)phone

•[String](/docs/api/admin-graphql/latest/scalars/String)

Deprecated

    

[Anchor to smsMarketingConsent](/docs/api/admin-
graphql/latest/objects/Customer#field-
Customer.fields.smsMarketingConsent)smsMarketingConsent

•[CustomerSmsMarketingConsentState](/docs/api/admin-
graphql/latest/objects/CustomerSmsMarketingConsentState)

Deprecated

    

Show fields

[Anchor to unsubscribeUrl](/docs/api/admin-
graphql/latest/objects/Customer#field-
Customer.fields.unsubscribeUrl)unsubscribeUrl

•[URL!](/docs/api/admin-graphql/latest/scalars/URL)

non-nullDeprecated

    

[Anchor to validEmailAddress](/docs/api/admin-
graphql/latest/objects/Customer#field-
Customer.fields.validEmailAddress)validEmailAddress

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-nullDeprecated

    

* * *

Was this section helpful?

YesNo

## Map

### Fields and connections with this object

  * {}[AbandonedCheckout.customer](/docs/api/admin-graphql/latest/objects/AbandonedCheckout#field-AbandonedCheckout.fields.customer)
  * {}[Abandonment.customer](/docs/api/admin-graphql/latest/objects/Abandonment#field-Abandonment.fields.customer)
  * {}[CalculatedDraftOrder.customer](/docs/api/admin-graphql/latest/objects/CalculatedDraftOrder#field-CalculatedDraftOrder.fields.customer)
  * {}[CompanyContact.customer](/docs/api/admin-graphql/latest/objects/CompanyContact#field-CompanyContact.fields.customer)
  * <->[CustomerConnection.nodes](/docs/api/admin-graphql/latest/connections/CustomerConnection#returns-nodes)
  * {}[CustomerEdge.node](/docs/api/admin-graphql/latest/objects/CustomerEdge#field-CustomerEdge.fields.node)
  * {}[CustomerPaymentMethod.customer](/docs/api/admin-graphql/latest/objects/CustomerPaymentMethod#field-CustomerPaymentMethod.fields.customer)
  * {}[DiscountCustomers.customers](/docs/api/admin-graphql/latest/objects/DiscountCustomers#field-DiscountCustomers.fields.customers)
  * {}[DraftOrder.customer](/docs/api/admin-graphql/latest/objects/DraftOrder#field-DraftOrder.fields.customer)
  * {}[GiftCard.customer](/docs/api/admin-graphql/latest/objects/GiftCard#field-GiftCard.fields.customer)
  * {}[GiftCardRecipient.recipient](/docs/api/admin-graphql/latest/objects/GiftCardRecipient#field-GiftCardRecipient.fields.recipient)
  * {}[Order.customer](/docs/api/admin-graphql/latest/objects/Order#field-Order.fields.customer)
  * {}[PriceRuleCustomerSelection.customers](/docs/api/admin-graphql/latest/objects/PriceRuleCustomerSelection#field-PriceRuleCustomerSelection.fields.customers)
  * {}[SubscriptionBillingCycleEditedContract.customer](/docs/api/admin-graphql/latest/objects/SubscriptionBillingCycleEditedContract#field-SubscriptionBillingCycleEditedContract.fields.customer)
  * {}[SubscriptionContract.customer](/docs/api/admin-graphql/latest/objects/SubscriptionContract#field-SubscriptionContract.fields.customer)
  * ||-[SubscriptionContractBase.customer](/docs/api/admin-graphql/latest/interfaces/SubscriptionContractBase#fields-customer)
  * {}[SubscriptionDraft.customer](/docs/api/admin-graphql/latest/objects/SubscriptionDraft#field-SubscriptionDraft.fields.customer)

Show deprecations

### Possible type in

  * [CommentEventEmbed](/docs/api/admin-graphql/latest/unions/CommentEventEmbed)
  * [MetafieldReference](/docs/api/admin-graphql/latest/unions/MetafieldReference)
  * [MetafieldReferencer](/docs/api/admin-graphql/latest/unions/MetafieldReferencer)
  * [PurchasingEntity](/docs/api/admin-graphql/latest/unions/PurchasingEntity)

* * *

##

[Anchor to Queries](/docs/api/admin-
graphql/latest/objects/Customer#queries)Queries

[Anchor to customer](/docs/api/admin-graphql/latest/objects/Customer#query-
customer)[customer](/docs/api/admin-graphql/latest/queries/customer)

•query

    

Returns a `Customer` resource by ID.

Show fields

[Anchor to customerByIdentifier](/docs/api/admin-
graphql/latest/objects/Customer#query-
customerByIdentifier)[customerByIdentifier](/docs/api/admin-
graphql/latest/queries/customerByIdentifier)

•query

    

Return a customer by an identifier.

Show fields

[Anchor to customers](/docs/api/admin-graphql/latest/objects/Customer#query-
customers)[customers](/docs/api/admin-graphql/latest/queries/customers)

•query

    

Returns a list of [customers](https://shopify.dev/api/admin-
graphql/latest/objects/Customer) in your Shopify store, including key
information such as name, email, location, and purchase history. Use this
query to segment your audience, personalize marketing campaigns, or analyze
customer behavior by applying filters based on location, order history,
marketing preferences and tags. The `customers` query supports
[pagination](https://shopify.dev/api/usage/pagination-graphql) and
[sorting](https://shopify.dev/api/admin-
graphql/latest/enums/CustomerSortKeys).

Show fields

* * *

Was this section helpful?

YesNo

## <?>Customer Queries

### Queried by

  * <?>[customer](/docs/api/admin-graphql/latest/queries/customer)
  * <?>[customerByIdentifier](/docs/api/admin-graphql/latest/queries/customerByIdentifier)
  * <?>[customers](/docs/api/admin-graphql/latest/queries/customers)

* * *

##

[Anchor to Mutations](/docs/api/admin-
graphql/latest/objects/Customer#mutations)Mutations

[Anchor to customerAddTaxExemptions](/docs/api/admin-
graphql/latest/objects/Customer#mutation-
customerAddTaxExemptions)[customerAddTaxExemptions](/docs/api/admin-
graphql/latest/mutations/customerAddTaxExemptions)

•mutation

    

Add tax exemptions for the customer.

Show payload

[Anchor to customerCreate](/docs/api/admin-
graphql/latest/objects/Customer#mutation-
customerCreate)[customerCreate](/docs/api/admin-
graphql/latest/mutations/customerCreate)

•mutation

    

Create a new customer. As of API version 2022-10, apps using protected
customer data must meet the protected customer data
[requirements](https://shopify.dev/apps/store/data-protection/protected-
customer-data).

Show payload

[Anchor to customerEmailMarketingConsentUpdate](/docs/api/admin-
graphql/latest/objects/Customer#mutation-
customerEmailMarketingConsentUpdate)[customerEmailMarketingConsentUpdate](/docs/api/admin-
graphql/latest/mutations/customerEmailMarketingConsentUpdate)

•mutation

    

Update a customer's email marketing information information.

Show payload

[Anchor to customerPaymentMethodSendUpdateEmail](/docs/api/admin-
graphql/latest/objects/Customer#mutation-
customerPaymentMethodSendUpdateEmail)[customerPaymentMethodSendUpdateEmail](/docs/api/admin-
graphql/latest/mutations/customerPaymentMethodSendUpdateEmail)

•mutation

    

Sends a link to the customer so they can update a specific payment method.

Show payload

[Anchor to customerRemoveTaxExemptions](/docs/api/admin-
graphql/latest/objects/Customer#mutation-
customerRemoveTaxExemptions)[customerRemoveTaxExemptions](/docs/api/admin-
graphql/latest/mutations/customerRemoveTaxExemptions)

•mutation

    

Remove tax exemptions from a customer.

Show payload

[Anchor to customerReplaceTaxExemptions](/docs/api/admin-
graphql/latest/objects/Customer#mutation-
customerReplaceTaxExemptions)[customerReplaceTaxExemptions](/docs/api/admin-
graphql/latest/mutations/customerReplaceTaxExemptions)

•mutation

    

Replace tax exemptions for a customer.

Show payload

[Anchor to customerSendAccountInviteEmail](/docs/api/admin-
graphql/latest/objects/Customer#mutation-
customerSendAccountInviteEmail)[customerSendAccountInviteEmail](/docs/api/admin-
graphql/latest/mutations/customerSendAccountInviteEmail)

•mutation

    

Sends the customer an account invite email.

Show payload

[Anchor to customerSet](/docs/api/admin-
graphql/latest/objects/Customer#mutation-
customerSet)[customerSet](/docs/api/admin-
graphql/latest/mutations/customerSet)

•mutation

    

Creates or updates a customer in a single mutation.

Use this mutation when syncing information from an external data source into
Shopify.

This mutation can be used to create a new customer, update an existing
customer by id, or upsert a customer by a unique key (email or phone).

To create a new customer omit the `identifier` argument. To update an existing
customer, include the `identifier` with the id of the customer to update.

To perform an 'upsert' by unique key (email or phone) use the `identifier`
argument to upsert a customer by a unique key (email or phone). If a customer
with the specified unique key exists, it will be updated. If not, a new
customer will be created with that unique key.

As of API version 2022-10, apps using protected customer data must meet the
protected customer data [requirements](https://shopify.dev/apps/store/data-
protection/protected-customer-data)

Any list field (e.g. [addresses](https://shopify.dev/api/admin-
graphql/unstable/input-objects/MailingAddressInput), will be updated so that
all included entries are either created or updated, and all existing entries
not included will be deleted.

All other fields will be updated to the value passed. Omitted fields will not
be updated.

Show payload

[Anchor to customerSmsMarketingConsentUpdate](/docs/api/admin-
graphql/latest/objects/Customer#mutation-
customerSmsMarketingConsentUpdate)[customerSmsMarketingConsentUpdate](/docs/api/admin-
graphql/latest/mutations/customerSmsMarketingConsentUpdate)

•mutation

    

Update a customer's SMS marketing consent information.

Show payload

[Anchor to customerUpdate](/docs/api/admin-
graphql/latest/objects/Customer#mutation-
customerUpdate)[customerUpdate](/docs/api/admin-
graphql/latest/mutations/customerUpdate)

•mutation

    

Update a customer's attributes. As of API version 2022-10, apps using
protected customer data must meet the protected customer data
[requirements](https://shopify.dev/apps/store/data-protection/protected-
customer-data).

Show payload

[Anchor to customerUpdateDefaultAddress](/docs/api/admin-
graphql/latest/objects/Customer#mutation-
customerUpdateDefaultAddress)[customerUpdateDefaultAddress](/docs/api/admin-
graphql/latest/mutations/customerUpdateDefaultAddress)

•mutation

    

Updates a customer's default address.

Show payload

* * *

Was this section helpful?

YesNo

## <~> Customer Mutations

### Mutated by

  * <~>[customerAddTaxExemptions](/docs/api/admin-graphql/latest/mutations/customerAddTaxExemptions)
  * <~>[customerCreate](/docs/api/admin-graphql/latest/mutations/customerCreate)
  * <~>[customerEmailMarketingConsentUpdate](/docs/api/admin-graphql/latest/mutations/customerEmailMarketingConsentUpdate)
  * <~>[customerPaymentMethodSendUpdateEmail](/docs/api/admin-graphql/latest/mutations/customerPaymentMethodSendUpdateEmail)
  * <~>[customerRemoveTaxExemptions](/docs/api/admin-graphql/latest/mutations/customerRemoveTaxExemptions)
  * <~>[customerReplaceTaxExemptions](/docs/api/admin-graphql/latest/mutations/customerReplaceTaxExemptions)
  * <~>[customerSendAccountInviteEmail](/docs/api/admin-graphql/latest/mutations/customerSendAccountInviteEmail)
  * <~>[customerSet](/docs/api/admin-graphql/latest/mutations/customerSet)
  * <~>[customerSmsMarketingConsentUpdate](/docs/api/admin-graphql/latest/mutations/customerSmsMarketingConsentUpdate)
  * <~>[customerUpdate](/docs/api/admin-graphql/latest/mutations/customerUpdate)
  * <~>[customerUpdateDefaultAddress](/docs/api/admin-graphql/latest/mutations/customerUpdateDefaultAddress)

* * *

##

[Anchor to Interfaces](/docs/api/admin-
graphql/latest/objects/Customer#interfaces)Interfaces

[Anchor to CommentEventSubject](/docs/api/admin-
graphql/latest/objects/Customer#interface-
CommentEventSubject)[CommentEventSubject](/docs/api/admin-
graphql/latest/interfaces/CommentEventSubject)

•interface

[Anchor to HasEvents](/docs/api/admin-
graphql/latest/objects/Customer#interface-
HasEvents)[HasEvents](/docs/api/admin-graphql/latest/interfaces/HasEvents)

•interface

[Anchor to HasMetafieldDefinitions](/docs/api/admin-
graphql/latest/objects/Customer#interface-
HasMetafieldDefinitions)[HasMetafieldDefinitions](/docs/api/admin-
graphql/latest/interfaces/HasMetafieldDefinitions)

•interface

[Anchor to HasMetafields](/docs/api/admin-
graphql/latest/objects/Customer#interface-
HasMetafields)[HasMetafields](/docs/api/admin-
graphql/latest/interfaces/HasMetafields)

•interface

[Anchor to HasStoreCreditAccounts](/docs/api/admin-
graphql/latest/objects/Customer#interface-
HasStoreCreditAccounts)[HasStoreCreditAccounts](/docs/api/admin-
graphql/latest/interfaces/HasStoreCreditAccounts)

•interface

[Anchor to LegacyInteroperability](/docs/api/admin-
graphql/latest/objects/Customer#interface-
LegacyInteroperability)[LegacyInteroperability](/docs/api/admin-
graphql/latest/interfaces/LegacyInteroperability)

•interface

[Anchor to Node](/docs/api/admin-graphql/latest/objects/Customer#interface-
Node)[Node](/docs/api/admin-graphql/latest/interfaces/Node)

•interface

* * *

Was this section helpful?

YesNo

## ||-Customer Implements

### Implements

  * ||-[CommentEventSubject](/docs/api/admin-graphql/latest/interfaces/CommentEventSubject)
  * ||-[HasEvents](/docs/api/admin-graphql/latest/interfaces/HasEvents)
  * ||-[HasMetafieldDefinitions](/docs/api/admin-graphql/latest/interfaces/HasMetafieldDefinitions)
  * ||-[HasMetafields](/docs/api/admin-graphql/latest/interfaces/HasMetafields)
  * ||-[HasStoreCreditAccounts](/docs/api/admin-graphql/latest/interfaces/HasStoreCreditAccounts)
  * ||-[LegacyInteroperability](/docs/api/admin-graphql/latest/interfaces/LegacyInteroperability)
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

