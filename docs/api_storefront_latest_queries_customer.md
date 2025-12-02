# Source: https://shopify.dev/docs/api/storefront/latest/queries/customer

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

Storefront API

Choose a version:

unstable 2026-01 release candidate2025-10 latest2025-07 2025-04 2025-01

2025-10latest

  * [Overview](/docs/api/storefront/2025-10)
  * [Development frameworks and SDKs](/docs/api/storefront/2025-10#development-frameworks-and-sdks)
  * [Authentication](/docs/api/storefront/2025-10#authentication)
  * [Endpoints and queries](/docs/api/storefront/2025-10#endpoints-and-queries)
  * [Directives](/docs/api/storefront/2025-10#directives)
  * [Rate limits](/docs/api/storefront/2025-10#rate-limits)
  * [Status and error codes](/docs/api/storefront/2025-10#status-and-error-codes)
  * [Resources](/docs/api/storefront/2025-10#resources)

* * *

  * Cart

  * Checkouts

  * Common objects

  * Customers

  * Metaobjects

  * Search

  * * * *

  * GraphQL Types

[Full index](/docs/api/storefront/2025-10/full-index)

Choose a version:

unstable 2026-01 release candidate2025-10 latest2025-07 2025-04 2025-01

2025-10latest

[Anchor to customer](/docs/api/storefront/latest/queries/customer#top)

# customer

query

Copy page MD

The customer associated with the given access token. Tokens are obtained by
using the [`customerAccessTokenCreate`
mutation](https://shopify.dev/docs/api/storefront/latest/mutations/customerAccessTokenCreate).

[Anchor to Arguments](/docs/api/storefront/latest/queries/customer#arguments)

## Arguments

[Anchor to
customerAccessToken](/docs/api/storefront/latest/queries/customer#arguments-
customerAccessToken)customerAccessToken

•[String!](/docs/api/storefront/latest/scalars/String)

required

    

The customer access token.

* * *

Was this section helpful?

YesNo

##

[Anchor to Possible
returns](/docs/api/storefront/latest/queries/customer#possible-
returns)Possible returns

[Anchor to Customer](/docs/api/storefront/latest/queries/customer#returns-
Customer)Customer

•[Customer](/docs/api/storefront/latest/objects/Customer)

    

A customer represents a customer account with the shop. Customer accounts
store contact information for the customer, saving logged-in customers the
trouble of having to provide it at every checkout.

Show fields

* * *

Was this section helpful?

YesNo

## Examples

  * ### Get a customer by access token

#### Description

The following query retrieves the customer with the associated access token.
It returns the customer fields specified in the query.

#### Query

        
        query {
          customer(customerAccessToken: "bobs_token") {
            id
            firstName
            lastName
            acceptsMarketing
            email
            phone
          }
        }

#### cURL

        
        curl -X POST \
        https://your-development-store.myshopify.com/api/2025-10/graphql.json \
        -H 'Content-Type: application/json' \
        -H 'X-Shopify-Storefront-Access-Token: {storefront_access_token}' \
        -d '{
        "query": "query { customer(customerAccessToken: \"bobs_token\") { id firstName lastName acceptsMarketing email phone } }"
        }'

#### React Router

        
        import { unauthenticated } from "../shopify.server";
        
        export const loader = async () => {
          const { storefront } = await unauthenticated.storefront(
            'your-development-store.myshopify.com'
          );
          const response = await storefront.graphql(
            `#graphql
          query {
            customer(customerAccessToken: "bobs_token") {
              id
              firstName
              lastName
              acceptsMarketing
              email
              phone
            }
          }`,
          );
          const json = await response.json();
          return json.data;
        }

#### Node.js

        
        const client = new shopify.clients.Storefront({
          domain: 'your-development-store.myshopify.com',
          storefrontAccessToken,
        });
        const data = await client.query({
          data: `query {
            customer(customerAccessToken: "bobs_token") {
              id
              firstName
              lastName
              acceptsMarketing
              email
              phone
            }
          }`,
        });

#### Response

        
        {
          "customer": {
            "id": "gid://shopify/Customer/410535040",
            "firstName": "John",
            "lastName": "Smith",
            "acceptsMarketing": false,
            "email": "johnsmith@example.com",
            "phone": "+16134504533"
          }
        }

## Get a customer by access token

Hide content

GQLcURLReact RouterNode.js

Show description[Open in
GraphiQL](http://localhost:3457/graphiql?query=query%20%7B%0A%20%20customer\(customerAccessToken%3A%20%22bobs_token%22\)%20%7B%0A%20%20%20%20id%0A%20%20%20%20firstName%0A%20%20%20%20lastName%0A%20%20%20%20acceptsMarketing%0A%20%20%20%20email%0A%20%20%20%20phone%0A%20%20%7D%0A%7D)Copy

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

›

⌄

import { unauthenticated } from "../shopify.server";

  

export const loader = async () => {

const { storefront } = await unauthenticated.storefront(

'your-development-store.myshopify.com'

);

const response = await storefront.graphql(

`#graphql

query {

customer(customerAccessToken: "bobs_token") {

id

firstName

lastName

acceptsMarketing

email

phone

}

}`,

);

const json = await response.json();

return json.data;

}

##### GQL

    
    
    query {
      customer(customerAccessToken: "bobs_token") {
        id
        firstName
        lastName
        acceptsMarketing
        email
        phone
      }
    }

##### cURL

    
    
    curl -X POST \
    https://your-development-store.myshopify.com/api/2025-10/graphql.json \
    -H 'Content-Type: application/json' \
    -H 'X-Shopify-Storefront-Access-Token: {storefront_access_token}' \
    -d '{
    "query": "query { customer(customerAccessToken: \"bobs_token\") { id firstName lastName acceptsMarketing email phone } }"
    }'

##### React Router

    
    
    import { unauthenticated } from "../shopify.server";
    
    export const loader = async () => {
      const { storefront } = await unauthenticated.storefront(
        'your-development-store.myshopify.com'
      );
      const response = await storefront.graphql(
        `#graphql
      query {
        customer(customerAccessToken: "bobs_token") {
          id
          firstName
          lastName
          acceptsMarketing
          email
          phone
        }
      }`,
      );
      const json = await response.json();
      return json.data;
    }

##### Node.js

    
    
    const client = new shopify.clients.Storefront({
      domain: 'your-development-store.myshopify.com',
      storefrontAccessToken,
    });
    const data = await client.query({
      data: `query {
        customer(customerAccessToken: "bobs_token") {
          id
          firstName
          lastName
          acceptsMarketing
          email
          phone
        }
      }`,
    });

Hide content

## Response

JSON

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

›

⌄

⌄

{

"customer": {

"id": "gid://shopify/Customer/410535040",

"firstName": "John",

"lastName": "Smith",

"acceptsMarketing": false,

"email": "johnsmith@example.com",

"phone": "+16134504533"

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

