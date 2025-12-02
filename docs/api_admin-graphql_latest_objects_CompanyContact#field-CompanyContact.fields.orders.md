# Source: https://shopify.dev/docs/api/admin-graphql/latest/objects/CompanyContact#field-CompanyContact.fields.orders

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

[Anchor to CompanyContact](/docs/api/admin-
graphql/latest/objects/CompanyContact#top)

# CompanyContact

object

Copy page MD

Requires `read_customers` access scope or `read_companies` access scope. Also:
The API client must be installed on a Shopify Plus store.

A person that acts on behalf of company associated to [a
customer](https://shopify.dev/api/admin-graphql/latest/objects/customer).

##

[Anchor to Fields](/docs/api/admin-
graphql/latest/objects/CompanyContact#fields)Fields

[Anchor to company](/docs/api/admin-
graphql/latest/objects/CompanyContact#field-
CompanyContact.fields.company)company

•[Company!](/docs/api/admin-graphql/latest/objects/Company)

non-null

    

The company to which the contact belongs.

Show fields

[Anchor to createdAt](/docs/api/admin-
graphql/latest/objects/CompanyContact#field-
CompanyContact.fields.createdAt)createdAt

•[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime)

non-null

    

The date and time ([ISO 8601 format](http://en.wikipedia.org/wiki/ISO_8601))
at which the company contact was created at Shopify.

[Anchor to customer](/docs/api/admin-
graphql/latest/objects/CompanyContact#field-
CompanyContact.fields.customer)customer

•[Customer!](/docs/api/admin-graphql/latest/objects/Customer)

non-null

    

The customer associated to this contact.

Show fields

[Anchor to draftOrders](/docs/api/admin-
graphql/latest/objects/CompanyContact#field-
CompanyContact.fields.draftOrders)draftOrders

•[DraftOrderConnection!](/docs/api/admin-
graphql/latest/connections/DraftOrderConnection)

non-null

    

The list of draft orders for the company contact.

Show fields

[Anchor to id](/docs/api/admin-graphql/latest/objects/CompanyContact#field-
CompanyContact.fields.id)id

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

non-null

    

A globally-unique ID.

[Anchor to isMainContact](/docs/api/admin-
graphql/latest/objects/CompanyContact#field-
CompanyContact.fields.isMainContact)isMainContact

•[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean)

non-null

    

Whether the contact is the main contact of the company.

[Anchor to lifetimeDuration](/docs/api/admin-
graphql/latest/objects/CompanyContact#field-
CompanyContact.fields.lifetimeDuration)lifetimeDuration

•[String!](/docs/api/admin-graphql/latest/scalars/String)

non-null

    

The lifetime duration of the company contact, since its creation date on
Shopify. Examples: `1 year`, `2 months`, `3 days`.

[Anchor to locale](/docs/api/admin-
graphql/latest/objects/CompanyContact#field-
CompanyContact.fields.locale)locale

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The company contact's locale (language).

[Anchor to orders](/docs/api/admin-
graphql/latest/objects/CompanyContact#field-
CompanyContact.fields.orders)orders

•[OrderConnection!](/docs/api/admin-
graphql/latest/connections/OrderConnection)

non-null

    

The list of orders for the company contact.

Show fields

[Anchor to roleAssignments](/docs/api/admin-
graphql/latest/objects/CompanyContact#field-
CompanyContact.fields.roleAssignments)roleAssignments

•[CompanyContactRoleAssignmentConnection!](/docs/api/admin-
graphql/latest/connections/CompanyContactRoleAssignmentConnection)

non-null

    

The list of roles assigned to this company contact.

Show fields

[Anchor to title](/docs/api/admin-graphql/latest/objects/CompanyContact#field-
CompanyContact.fields.title)title

•[String](/docs/api/admin-graphql/latest/scalars/String)

    

The company contact's job title.

[Anchor to updatedAt](/docs/api/admin-
graphql/latest/objects/CompanyContact#field-
CompanyContact.fields.updatedAt)updatedAt

•[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime)

non-null

    

The date and time ([ISO 8601 format](http://en.wikipedia.org/wiki/ISO_8601))
at which the company contact was last updated.

* * *

Was this section helpful?

YesNo

## Map

### Fields and connections with this object

  * {}[Company.contacts](/docs/api/admin-graphql/latest/objects/Company#field-Company.fields.contacts)
  * {}[Company.mainContact](/docs/api/admin-graphql/latest/objects/Company#field-Company.fields.mainContact)
  * <->[CompanyContactConnection.nodes](/docs/api/admin-graphql/latest/connections/CompanyContactConnection#returns-nodes)
  * {}[CompanyContactEdge.node](/docs/api/admin-graphql/latest/objects/CompanyContactEdge#field-CompanyContactEdge.fields.node)
  * {}[CompanyContactRoleAssignment.companyContact](/docs/api/admin-graphql/latest/objects/CompanyContactRoleAssignment#field-CompanyContactRoleAssignment.fields.companyContact)
  * {}[Customer.companyContactProfiles](/docs/api/admin-graphql/latest/objects/Customer#field-Customer.fields.companyContactProfiles)
  * {}[PurchasingCompany.contact](/docs/api/admin-graphql/latest/objects/PurchasingCompany#field-PurchasingCompany.fields.contact)

* * *

##

[Anchor to Queries](/docs/api/admin-
graphql/latest/objects/CompanyContact#queries)Queries

[Anchor to companyContact](/docs/api/admin-
graphql/latest/objects/CompanyContact#query-
companyContact)[companyContact](/docs/api/admin-
graphql/latest/queries/companyContact)

•query

    

Returns a `CompanyContact` resource by ID.

Show fields

* * *

Was this section helpful?

YesNo

## <?>CompanyContact Queries

### Queried by

  * <?>[companyContact](/docs/api/admin-graphql/latest/queries/companyContact)

* * *

##

[Anchor to Mutations](/docs/api/admin-
graphql/latest/objects/CompanyContact#mutations)Mutations

[Anchor to companyAssignCustomerAsContact](/docs/api/admin-
graphql/latest/objects/CompanyContact#mutation-
companyAssignCustomerAsContact)[companyAssignCustomerAsContact](/docs/api/admin-
graphql/latest/mutations/companyAssignCustomerAsContact)

•mutation

    

Assigns the customer as a company contact.

Show payload

[Anchor to companyContactCreate](/docs/api/admin-
graphql/latest/objects/CompanyContact#mutation-
companyContactCreate)[companyContactCreate](/docs/api/admin-
graphql/latest/mutations/companyContactCreate)

•mutation

    

Creates a company contact and the associated customer.

Show payload

[Anchor to companyContactUpdate](/docs/api/admin-
graphql/latest/objects/CompanyContact#mutation-
companyContactUpdate)[companyContactUpdate](/docs/api/admin-
graphql/latest/mutations/companyContactUpdate)

•mutation

    

Updates a company contact.

Show payload

* * *

Was this section helpful?

YesNo

## <~> CompanyContact Mutations

### Mutated by

  * <~>[companyAssignCustomerAsContact](/docs/api/admin-graphql/latest/mutations/companyAssignCustomerAsContact)
  * <~>[companyContactCreate](/docs/api/admin-graphql/latest/mutations/companyContactCreate)
  * <~>[companyContactUpdate](/docs/api/admin-graphql/latest/mutations/companyContactUpdate)

* * *

##

[Anchor to Interfaces](/docs/api/admin-
graphql/latest/objects/CompanyContact#interfaces)Interfaces

[Anchor to Node](/docs/api/admin-
graphql/latest/objects/CompanyContact#interface-Node)[Node](/docs/api/admin-
graphql/latest/interfaces/Node)

•interface

* * *

Was this section helpful?

YesNo

## ||-CompanyContact Implements

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

