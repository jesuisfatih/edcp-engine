# Source: https://shopify.dev/docs/api/admin-graphql/2025-10#endpoints-and-queries

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

  * [Overview](/docs/api/admin-graphql/latest)
  * [Client libraries](/docs/api/admin-graphql/latest#client-libraries)
  * [Authentication](/docs/api/admin-graphql/latest#authentication)
  * [Endpoints and queries](/docs/api/admin-graphql/latest#endpoints-and-queries)
  * [Rate limits](/docs/api/admin-graphql/latest#rate-limits)
  * [Status and error codes](/docs/api/admin-graphql/latest#status-and-error-codes)

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

# GraphQL Admin API reference

The Admin API lets you build apps and integrations that extend and enhance the
Shopify admin.

This page will help you get up and running with Shopify’s GraphQL API.

Copy page MD

Choose a version:

unstable 2026-01 release candidate2025-10 latest2025-07 2025-04 2025-01

2025-10latest

##

[Anchor to Client libraries](/docs/api/admin-graphql/latest#client-
libraries)Client libraries

Use Shopify’s officially supported libraries to build fast, reliable apps with
the programming languages and frameworks you already know.

![](/images/logos/ReactRouter.svg)![](/images/logos/ReactRouter-dark.svg)

React Router

The official package for React Router applications.

  * [Docs](/docs/api/shopify-app-react-router)
  * [npm package](https://www.npmjs.com/package/@shopify/shopify-app-react-router)
  * [GitHub repo](https://github.com/Shopify/shopify-app-js/tree/main/packages/apps/shopify-app-react-router#readme)

![](/images/logos/Nodejs.svg)![](/images/logos/Nodejs-dark.svg)

Node.js

The official client library for Node.js apps. No framework dependencies—works
with any Node.js app.

  * [Docs](https://github.com/Shopify/shopify-app-js/tree/main/packages/apps/shopify-api#readme)
  * [npm package](https://www.npmjs.com/package/@shopify/shopify-api)
  * [GitHub repo](https://github.com/Shopify/shopify-app-js/tree/main/packages/apps/shopify-api)

![](/images/logos/Ruby.svg)![](/images/logos/Ruby-dark.svg)

Ruby

The official client library for Ruby apps.

  * [Docs](https://shopify.github.io/shopify-api-ruby/)

  * [Ruby gem](https://rubygems.org/gems/shopify_api)

  * [GitHub repo](https://github.com/Shopify/shopify-api-ruby)

![](/images/logos/CURL.svg)![](/images/logos/CURL-dark.svg)

cURL

Use the [curl utility](https://curl.se/) to make API queries directly from the
command line.

Other

Need a different language? Check the list of [community-supported
libraries](/apps/tools/api-libraries#third-party-admin-api-libraries).

React RouterNode.jsRubycURL

Copy

9

1

2

npm install -g @shopify/cli@latest

shopify app init

9

1

2

3

npm install \--save @shopify/shopify-api

# or

yarn add @shopify/shopify-api

9

1

bundle add shopify_api

9

1

2

# cURL is often available by default on macOS and Linux.

# See http://curl.se/docs/install.html for more details.

##### React Router

    
    
    npm install -g @shopify/cli@latest
    shopify app init

##### Node.js

    
    
    npm install --save @shopify/shopify-api
    # or
    yarn add @shopify/shopify-api

##### Ruby

    
    
    bundle add shopify_api

##### cURL

    
    
    # cURL is often available by default on macOS and Linux.
    # See http://curl.se/docs/install.html for more details.

* * *

##

[Anchor to Authentication](/docs/api/admin-
graphql/latest#authentication)Authentication

All GraphQL Admin API requests require a valid Shopify access token. If you
use Shopify’s [client libraries](/apps/tools/api-libraries), then this will be
done for you. Otherwise, you should include your token as a `X-Shopify-Access-
Token` header on all GraphQL requests.

Public and custom apps created in the Dev Dashboard generate tokens using
[OAuth](/apps/auth/oauth), and custom apps made in the Shopify admin are
[authenticated in the Shopify admin](/apps/auth/admin-app-access-tokens).

To keep the platform secure, apps need to request specific [access
scopes](/api/usage/access-scopes) during the install process. Only request as
much data access as your app needs to work.

Learn more about [getting started with authentication](/apps/auth) and
[building apps](/apps/getting-started).

React RouterNode.jsRubycURL

Copy

9

1

2

3

4

5

6

7

8

import { authenticate } from "../shopify.server";

  

export async function loader({request}) {

const { admin } = await authenticate.admin(request);

const response = await admin.graphql(

`query { shop { name } }`,

);

}

9

1

2

const client = new shopify.clients.Graphql({session});

const response = await client.query({data: 'query { shop { name } }'});

9

1

2

3

4

5

6

7

8

session = ShopifyAPI::Auth::Session.new(

shop: 'your-development-store.myshopify.com',

access_token: access_token,

)

client = ShopifyAPI::Clients::Graphql::Admin.new(

session: session,

)

response = client.query(query: 'query { shop { name } }')

9

1

2

3

4

5

6

7

8

# Replace {SHOPIFY_ACCESS_TOKEN} with your actual access token

curl -X POST \

https://{shop}.myshopify.com/admin/api/2025-10/graphql.json \

-H 'Content-Type: application/json' \

-H 'X-Shopify-Access-Token: {SHOPIFY_ACCESS_TOKEN}' \

-d '{

"query": "query { shop { name } }"

}'

##### React Router

    
    
    import { authenticate } from "../shopify.server";
    
    export async function loader({request}) {
      const { admin } = await authenticate.admin(request);
      const response = await admin.graphql(
        `query { shop { name } }`,
      );
    }

##### Node.js

    
    
    const client = new shopify.clients.Graphql({session});
    const response = await client.query({data: 'query { shop { name } }'});

##### Ruby

    
    
    session = ShopifyAPI::Auth::Session.new(
      shop: 'your-development-store.myshopify.com',
      access_token: access_token,
    )
    client = ShopifyAPI::Clients::Graphql::Admin.new(
      session: session,
    )
    response = client.query(query: 'query { shop { name } }')

##### cURL

    
    
    # Replace {SHOPIFY_ACCESS_TOKEN} with your actual access token
      curl -X POST \
      https://{shop}.myshopify.com/admin/api/2025-10/graphql.json \
      -H 'Content-Type: application/json' \
      -H 'X-Shopify-Access-Token: {SHOPIFY_ACCESS_TOKEN}' \
      -d '{
      "query": "query { shop { name } }"
      }'

* * *

##

[Anchor to Endpoints and queries](/docs/api/admin-graphql/latest#endpoints-
and-queries)Endpoints and queries

GraphQL queries are executed by sending `POST` HTTP requests to the endpoint:

`https://{store_name}.myshopify.com/admin/api/2025-10/graphql.json`

Queries begin with one of the objects listed under [QueryRoot](/api/admin-
graphql/2025-10/objects/queryroot). The QueryRoot is the schema’s entry-point
for queries.

Queries are equivalent to making a `GET` request in REST. The example shown is
a query to get the ID and title of the first three products.

Learn more about [API usage](/api/usage).

* * *

Note

Explore and learn Shopify's Admin API using [GraphiQL
Explorer](/apps/tools/graphiql-admin-api). To build queries and mutations with
shop data, install [Shopify’s GraphiQL app](https://shopify-graphiql-
app.shopifycloud.com/).

POST

## https://{store_name}.myshopify.com/admin/api/2025-10/graphql.json

React RouterNode.jsRubycURL

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

import { authenticate } from "../shopify.server";

  

export async function loader({request}) {

const { admin } = await authenticate.admin(request);

const response = await admin.graphql(

`#graphql

query getProducts {

products (first: 3) {

edges {

node {

id

title

}

}

}

}`,

);

const json = await response.json();

return { products: json?.data?.products?.edges };

}

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

const queryString = `{

products (first: 3) {

edges {

node {

id

title

}

}

}

}`

  

// `session` is built as part of the OAuth process

const client = new shopify.clients.Graphql({session});

const products = await client.query({

data: queryString,

});

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

query = <<~GQL

{

products (first: 3) {

edges {

node {

id

title

}

}

}

}

GQL

  

# session is built as part of the OAuth process

client = ShopifyAPI::Clients::Graphql::Admin.new(

session: session

)

products = client.query(

query: query,

)

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

# Get the ID and title of the three most recently added products

curl -X POST https://{store_name}.myshopify.com/admin/api/2025-10/graphql.json
\

-H 'Content-Type: application/json' \

-H 'X-Shopify-Access-Token: {access_token}' \

-d '{

"query": "{

products(first: 3) {

edges {

node {

id

title

}

}

}

}"

}'

##### React Router

    
    
    import { authenticate } from "../shopify.server";
    
    export async function loader({request}) {
      const { admin } = await authenticate.admin(request);
      const response = await admin.graphql(
        `#graphql
        query getProducts {
          products (first: 3) {
            edges {
              node {
                id
                title
              }
            }
          }
        }`,
      );
      const json = await response.json();
      return { products: json?.data?.products?.edges };
    }

##### Node.js

    
    
    const queryString = `{
      products (first: 3) {
        edges {
          node {
            id
            title
          }
        }
      }
    }`
    
    // `session` is built as part of the OAuth process
    const client = new shopify.clients.Graphql({session});
    const products = await client.query({
      data: queryString,
    });

##### Ruby

    
    
    query = <<~GQL
      {
        products (first: 3) {
          edges {
            node {
              id
              title
            }
          }
        }
      }
    GQL
    
    # session is built as part of the OAuth process
    client = ShopifyAPI::Clients::Graphql::Admin.new(
      session: session
    )
    products = client.query(
      query: query,
    )

##### cURL

    
    
    # Get the ID and title of the three most recently added products
    curl -X POST   https://{store_name}.myshopify.com/admin/api/2025-10/graphql.json \
      -H 'Content-Type: application/json' \
      -H 'X-Shopify-Access-Token: {access_token}' \
      -d '{
      "query": "{
        products(first: 3) {
          edges {
            node {
              id
              title
            }
          }
        }
      }"
    }'

* * *

##

[Anchor to Rate limits](/docs/api/admin-graphql/latest#rate-limits)Rate limits

The GraphQL Admin API is rate-limited using calculated query costs, measured
in cost points. Each field returned by a query costs a set number of points.
The total cost of a query is the maximum of possible fields selected, so more
complex queries cost more to run.

Learn more about [rate limits](/api/usage/limits#graphql-admin-api-rate-
limits).

{}

## Request

Copy

9

1

2

3

4

5

6

7

8

9

{

products(first: 1) {

edges {

node {

title

}

}

}

}

{}

## Response

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

{

"data": {

"products": {

"edges": [

{

"node": {

"title": "Hiking backpack"

}

}

]

}

},

"extensions": {

"cost": {

"requestedQueryCost": 3,

"actualQueryCost": 3,

"throttleStatus": {

"maximumAvailable": 1000.0,

"currentlyAvailable": 997,

"restoreRate": 50.0

}

}

}

}

* * *

##

[Anchor to Status and error codes](/docs/api/admin-graphql/latest#status-and-
error-codes)Status and error codes

All API queries return HTTP status codes that contain more information about
the response.

###

[Anchor to 200 OK](/docs/api/admin-graphql/latest#200-ok)200 OK

GraphQL HTTP status codes are different from REST API status codes. Most
importantly, the GraphQL API can return a `200 OK` response code in cases that
would typically produce 4xx or 5xx errors in REST.

###

[Anchor to Error handling](/docs/api/admin-graphql/latest#error-handling)Error
handling

The response for the errors object contains additional detail to help you
debug your operation.

The response for mutations contains additional detail to help debug your
query. To access this, you must request `userErrors`.

#### Properties

errors•array

A list of all errors returned

Show error item properties

errors[n].message•string

Contains details about the error(s).

errors[n].extensions•object

Provides more information about the error(s) including properties and
metadata.

Show extensions properties

errors[n].extensions.code•string

Shows error codes common to Shopify. Additional error codes may also be shown.

Show common error codes

THROTTLED

The client has exceeded the rate limit. Similar to 429 Too Many Requests.

ACCESS_DENIED

The client doesn’t have correct authentication credentials. Similar to 401
Unauthorized.

SHOP_INACTIVE

The shop is not active. This can happen when stores repeatedly exceed API rate
limits or due to fraud risk.

INTERNAL_SERVER_ERROR

Shopify experienced an internal error while processing the request. This error
is returned instead of 500 Internal Server Error in most circumstances.

* * *

###

[Anchor to 4xx and 5xx status codes](/docs/api/admin-graphql/latest#4xx-
and-5xx-status-codes)4xx and 5xx status codes

The 4xx and 5xx errors occur infrequently. They are often related to network
communications, your account, or an issue with Shopify’s services.

Many errors that would typically return a 4xx or 5xx status code, return an
HTTP 200 errors response instead. Refer to the 200 OK section above for
details.

{}

## Sample 200 error responses

ThrottledInternal

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

{

"errors": [

{

"message": "Query cost is 2003, which exceeds the single query max cost limit
(1000).

  

See https://shopify.dev/concepts/about-apis/rate-limits for more information
on how the

cost of a query is calculated.

  

To query larger amounts of data with fewer limits, bulk operations should be
used instead.

See https://shopify.dev/tutorials/perform-bulk-operations-with-admin-api for
usage details.

",

"extensions": {

"code": "MAX_COST_EXCEEDED",

"cost": 2003,

"maxCost": 1000,

"documentation": "https://shopify.dev/api/usage/limits#rate-limits"

}

}

]

}

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

{

"errors": [

{

"message": "Internal error. Looks like something went wrong on our end.

Request ID: 1b355a21-7117-44c5-8d8b-8948082f40a8 (include this in support
requests).",

"extensions": {

"code": "INTERNAL_SERVER_ERROR",

"requestId": "1b355a21-7117-44c5-8d8b-8948082f40a8"

}

}

]

}

##### Throttled

    
    
    {
    "errors": [
      {
        "message": "Query cost is 2003, which exceeds the single query max cost limit (1000).
    
    See https://shopify.dev/concepts/about-apis/rate-limits for more information on how the
    cost of a query is calculated.
    
    To query larger amounts of data with fewer limits, bulk operations should be used instead.
    See https://shopify.dev/tutorials/perform-bulk-operations-with-admin-api for usage details.
    ",
        "extensions": {
          "code": "MAX_COST_EXCEEDED",
          "cost": 2003,
          "maxCost": 1000,
          "documentation": "https://shopify.dev/api/usage/limits#rate-limits"
        }
      }
    ]
    }

##### Internal

    
    
    {
    "errors": [
      {
        "message": "Internal error. Looks like something went wrong on our end.
    Request ID: 1b355a21-7117-44c5-8d8b-8948082f40a8 (include this in support requests).",
        "extensions": {
          "code": "INTERNAL_SERVER_ERROR",
          "requestId": "1b355a21-7117-44c5-8d8b-8948082f40a8"
        }
      }
    ]
    }

###

[Anchor to 4xx and 5xx status codes](/docs/api/admin-graphql/latest#4xx-
and-5xx-status-codes)4xx and 5xx status codes

The 4xx and 5xx errors occur infrequently. They are often related to network
communications, your account, or an issue with Shopify’s services.

Many errors that would typically return a 4xx or 5xx status code, return an
HTTP 200 errors response instead. Refer to the 200 OK section above for
details.

* * *

####

[Anchor to [object Object]](/docs/api/admin-graphql/latest#400-bad-request)400
Bad Request

The server will not process the request.

* * *

####

[Anchor to [object Object]](/docs/api/admin-graphql/latest#402-payment-
required)402 Payment Required

The shop is frozen. The shop owner will need to pay the outstanding balance to
[unfreeze](https://help.shopify.com/en/manual/your-account/pause-close-
store#unfreeze-your-shopify-store) the shop.

* * *

####

[Anchor to [object Object]](/docs/api/admin-graphql/latest#403-forbidden)403
Forbidden

The shop is forbidden. Returned if the store has been marked as fraudulent.

* * *

####

[Anchor to [object Object]](/docs/api/admin-graphql/latest#404-not-found)404
Not Found

The resource isn’t available. This is often caused by querying for something
that’s been deleted.

* * *

####

[Anchor to [object Object]](/docs/api/admin-graphql/latest#423-locked)423
Locked

The shop isn’t available. This can happen when stores repeatedly exceed API
rate limits or due to fraud risk.

* * *

####

[Anchor to [object Object]](/docs/api/admin-graphql/latest#5xx-errors)5xx
Errors

An internal error occurred in Shopify. Check out the [Shopify status
page](https://www.shopifystatus.com) for more information.

* * *

Info

Didn’t find the status code you’re looking for? View the complete list of [API
status response and error codes](/api/usage/response-codes).

{}

## Sample error codes

400402403404423500

9

1

2

3

4

5

6

HTTP/1.1 400 Bad Request

{

"errors": {

"query": "Required parameter missing or invalid"

}

}

9

1

2

3

4

HTTP/1.1 402 Payment Required

{

"errors": "This shop's plan does not have access to this feature"

}

9

1

2

3

4

HTTP/1.1 403 Access Denied

{

"errors": "User does not have access"

}

9

1

2

3

4

HTTP/1.1 404 Not Found

{

"errors": "Not Found"

}

9

1

2

3

4

HTTP/1.1 423 Locked

{

"errors": "This shop is unavailable"

}

9

1

2

3

4

HTTP/1.1 500 Internal Server Error

{

"errors": "An unexpected error occurred"

}

##### 400

    
    
    HTTP/1.1 400 Bad Request
    {
      "errors": {
        "query": "Required parameter missing or invalid"
      }
    }

##### 402

    
    
    HTTP/1.1 402 Payment Required
    {
      "errors": "This shop's plan does not have access to this feature"
    }

##### 403

    
    
    HTTP/1.1 403 Access Denied
    {
      "errors": "User does not have access"
    }

##### 404

    
    
    HTTP/1.1 404 Not Found
    {
      "errors": "Not Found"
    }

##### 423

    
    
    HTTP/1.1 423 Locked
    {
      "errors": "This shop is unavailable"
    }

##### 500

    
    
    HTTP/1.1 500 Internal Server Error
    {
      "errors": "An unexpected error occurred"
    }

* * *

Was this page helpful?

YesNo

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

