# Source: https://shopify.dev/docs/api/admin-graphql/latest/mutations/customerPaymentMethodSendUpdateEmail#returns

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

[Anchor to customerPaymentMethodSendUpdateEmail](/docs/api/admin-
graphql/latest/mutations/customerPaymentMethodSendUpdateEmail#top)

# customerPaymentMethodSendUpdateEmail

mutation

Copy page MD

Requires `write_customers` access scope.

Sends a link to the customer so they can update a specific payment method.

[Anchor to Arguments](/docs/api/admin-
graphql/latest/mutations/customerPaymentMethodSendUpdateEmail#arguments)

## Arguments

[Anchor to customerPaymentMethodId](/docs/api/admin-
graphql/latest/mutations/customerPaymentMethodSendUpdateEmail#arguments-
customerPaymentMethodId)customerPaymentMethodId

•[ID!](/docs/api/admin-graphql/latest/scalars/ID)

required

    

The payment method to be updated.

[Anchor to email](/docs/api/admin-
graphql/latest/mutations/customerPaymentMethodSendUpdateEmail#arguments-
email)email

•[EmailInput](/docs/api/admin-graphql/latest/input-objects/EmailInput)

    

Specifies the payment method update email fields. Only the 'from' and 'bcc'
fields are accepted for input.

Show input fields

* * *

Was this section helpful?

YesNo

##

[Anchor to CustomerPaymentMethodSendUpdateEmailPayload
returns](/docs/api/admin-
graphql/latest/mutations/customerPaymentMethodSendUpdateEmail#returns)CustomerPaymentMethodSendUpdateEmailPayload
returns

[Anchor to customer](/docs/api/admin-
graphql/latest/mutations/customerPaymentMethodSendUpdateEmail#returns-
customer)customer

•[Customer](/docs/api/admin-graphql/latest/objects/Customer)

    

The customer to whom an update payment method email was sent.

Show fields

[Anchor to userErrors](/docs/api/admin-
graphql/latest/mutations/customerPaymentMethodSendUpdateEmail#returns-
userErrors)userErrors

•[[UserError!]!](/docs/api/admin-graphql/latest/objects/UserError)

non-null

    

The list of errors that occurred from executing the mutation.

Show fields

* * *

Was this section helpful?

YesNo

## Examples

  * ### Send an email with only the customer payment method id

#### Query

        
        mutation sendCustomerPaymentUpdateEmail($customerPaymentMethodId: ID!) {
          customerPaymentMethodSendUpdateEmail(customerPaymentMethodId: $customerPaymentMethodId) {
            customer {
              id
            }
            userErrors {
              field
              message
            }
          }
        }

#### Variables

        
        {
          "customerPaymentMethodId": "gid://shopify/CustomerPaymentMethod/b7cc6e3267aace169e516ed48be72dff"
        }

#### cURL

        
        curl -X POST \
        https://your-development-store.myshopify.com/admin/api/2025-10/graphql.json \
        -H 'Content-Type: application/json' \
        -H 'X-Shopify-Access-Token: {access_token}' \
        -d '{
        "query": "mutation sendCustomerPaymentUpdateEmail($customerPaymentMethodId: ID!) { customerPaymentMethodSendUpdateEmail(customerPaymentMethodId: $customerPaymentMethodId) { customer { id } userErrors { field message } } }",
         "variables": {
            "customerPaymentMethodId": "gid://shopify/CustomerPaymentMethod/b7cc6e3267aace169e516ed48be72dff"
          }
        }'

#### React Router

        
        import { authenticate } from "../shopify.server";
        
        export const loader = async ({request}) => {
          const { admin } = await authenticate.admin(request);
          const response = await admin.graphql(
            `#graphql
          mutation sendCustomerPaymentUpdateEmail($customerPaymentMethodId: ID!) {
            customerPaymentMethodSendUpdateEmail(customerPaymentMethodId: $customerPaymentMethodId) {
              customer {
                id
              }
              userErrors {
                field
                message
              }
            }
          }`,
          {
            variables: {
                "customerPaymentMethodId": "gid://shopify/CustomerPaymentMethod/b7cc6e3267aace169e516ed48be72dff"
            },
          },
          );
          const json = await response.json();
          return json.data;
        }

#### Ruby

        
        session = ShopifyAPI::Auth::Session.new(
          shop: "your-development-store.myshopify.com",
          access_token: access_token
        )
        client = ShopifyAPI::Clients::Graphql::Admin.new(
          session: session
        )
        
        query = <<~QUERY
          mutation sendCustomerPaymentUpdateEmail($customerPaymentMethodId: ID!) {
            customerPaymentMethodSendUpdateEmail(customerPaymentMethodId: $customerPaymentMethodId) {
              customer {
                id
              }
              userErrors {
                field
                message
              }
            }
          }
        QUERY
        
        variables = {
          "customerPaymentMethodId": "gid://shopify/CustomerPaymentMethod/b7cc6e3267aace169e516ed48be72dff"
        }
        
        response = client.query(query: query, variables: variables)

#### Node.js

        
        const client = new shopify.clients.Graphql({session});
        const data = await client.query({
          data: {
            "query": `mutation sendCustomerPaymentUpdateEmail($customerPaymentMethodId: ID!) {
              customerPaymentMethodSendUpdateEmail(customerPaymentMethodId: $customerPaymentMethodId) {
                customer {
                  id
                }
                userErrors {
                  field
                  message
                }
              }
            }`,
            "variables": {
                "customerPaymentMethodId": "gid://shopify/CustomerPaymentMethod/b7cc6e3267aace169e516ed48be72dff"
            },
          },
        });

#### Response

        
        {
          "customerPaymentMethodSendUpdateEmail": {
            "customer": {
              "id": "gid://shopify/Customer/544365967"
            },
            "userErrors": []
          }
        }

  * ### customerPaymentMethodSendUpdateEmail reference

## Examples

Send an email with only the customer payment method id

Hide content

GQLcURLReact RouterNode.jsRuby

[Open in
GraphiQL](http://localhost:3457/graphiql?query=mutation%20sendCustomerPaymentUpdateEmail\(%24customerPaymentMethodId%3A%20ID!\)%20%7B%0A%20%20customerPaymentMethodSendUpdateEmail\(customerPaymentMethodId%3A%20%24customerPaymentMethodId\)%20%7B%0A%20%20%20%20customer%20%7B%0A%20%20%20%20%20%20id%0A%20%20%20%20%7D%0A%20%20%20%20userErrors%20%7B%0A%20%20%20%20%20%20field%0A%20%20%20%20%20%20message%0A%20%20%20%20%7D%0A%20%20%7D%0A%7D&variables=%7B%0A%20%20%22customerPaymentMethodId%22%3A%20%22gid%3A%2F%2Fshopify%2FCustomerPaymentMethod%2Fb7cc6e3267aace169e516ed48be72dff%22%0A%7D)Copy

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

›

⌄

⌄

⌄

import { authenticate } from "../shopify.server";

  

export const loader = async ({request}) => {

const { admin } = await authenticate.admin(request);

const response = await admin.graphql(

`#graphql

mutation sendCustomerPaymentUpdateEmail($customerPaymentMethodId: ID!) {

customerPaymentMethodSendUpdateEmail(customerPaymentMethodId:
$customerPaymentMethodId) {

customer {

id

}

userErrors {

field

message

}

}

}`,

{

variables: {

"customerPaymentMethodId":
"gid://shopify/CustomerPaymentMethod/b7cc6e3267aace169e516ed48be72dff"

},

},

);

const json = await response.json();

return json.data;

}

##### GQL

    
    
    mutation sendCustomerPaymentUpdateEmail($customerPaymentMethodId: ID!) {
      customerPaymentMethodSendUpdateEmail(customerPaymentMethodId: $customerPaymentMethodId) {
        customer {
          id
        }
        userErrors {
          field
          message
        }
      }
    }

##### cURL

    
    
    curl -X POST \
    https://your-development-store.myshopify.com/admin/api/2025-10/graphql.json \
    -H 'Content-Type: application/json' \
    -H 'X-Shopify-Access-Token: {access_token}' \
    -d '{
    "query": "mutation sendCustomerPaymentUpdateEmail($customerPaymentMethodId: ID!) { customerPaymentMethodSendUpdateEmail(customerPaymentMethodId: $customerPaymentMethodId) { customer { id } userErrors { field message } } }",
     "variables": {
        "customerPaymentMethodId": "gid://shopify/CustomerPaymentMethod/b7cc6e3267aace169e516ed48be72dff"
      }
    }'

##### React Router

    
    
    import { authenticate } from "../shopify.server";
    
    export const loader = async ({request}) => {
      const { admin } = await authenticate.admin(request);
      const response = await admin.graphql(
        `#graphql
      mutation sendCustomerPaymentUpdateEmail($customerPaymentMethodId: ID!) {
        customerPaymentMethodSendUpdateEmail(customerPaymentMethodId: $customerPaymentMethodId) {
          customer {
            id
          }
          userErrors {
            field
            message
          }
        }
      }`,
      {
        variables: {
            "customerPaymentMethodId": "gid://shopify/CustomerPaymentMethod/b7cc6e3267aace169e516ed48be72dff"
        },
      },
      );
      const json = await response.json();
      return json.data;
    }

##### Node.js

    
    
    const client = new shopify.clients.Graphql({session});
    const data = await client.query({
      data: {
        "query": `mutation sendCustomerPaymentUpdateEmail($customerPaymentMethodId: ID!) {
          customerPaymentMethodSendUpdateEmail(customerPaymentMethodId: $customerPaymentMethodId) {
            customer {
              id
            }
            userErrors {
              field
              message
            }
          }
        }`,
        "variables": {
            "customerPaymentMethodId": "gid://shopify/CustomerPaymentMethod/b7cc6e3267aace169e516ed48be72dff"
        },
      },
    });

##### Ruby

    
    
    session = ShopifyAPI::Auth::Session.new(
      shop: "your-development-store.myshopify.com",
      access_token: access_token
    )
    client = ShopifyAPI::Clients::Graphql::Admin.new(
      session: session
    )
    
    query = <<~QUERY
      mutation sendCustomerPaymentUpdateEmail($customerPaymentMethodId: ID!) {
        customerPaymentMethodSendUpdateEmail(customerPaymentMethodId: $customerPaymentMethodId) {
          customer {
            id
          }
          userErrors {
            field
            message
          }
        }
      }
    QUERY
    
    variables = {
      "customerPaymentMethodId": "gid://shopify/CustomerPaymentMethod/b7cc6e3267aace169e516ed48be72dff"
    }
    
    response = client.query(query: query, variables: variables)

Hide content

## Input variables

JSON

Copy

9

1

2

3

›

⌄

{

"customerPaymentMethodId":
"gid://shopify/CustomerPaymentMethod/b7cc6e3267aace169e516ed48be72dff"

}

Hide content

## Response

JSON

9

1

2

3

4

5

6

7

8

›

⌄

⌄

⌄

{

"customerPaymentMethodSendUpdateEmail": {

"customer": {

"id": "gid://shopify/Customer/544365967"

},

"userErrors": []

}

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

