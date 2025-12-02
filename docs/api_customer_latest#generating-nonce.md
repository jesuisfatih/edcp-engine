# Source: https://shopify.dev/docs/api/customer/latest#generating-nonce

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

  * [Overview](/docs/api/customer/latest)
  * [Authentication](/docs/api/customer/latest#authentication)
  * [Endpoints and queries](/docs/api/customer/latest#endpoints-and-queries)
  * [Directives](/docs/api/customer/latest#directives)
  * [Rate limits](/docs/api/customer/latest#rate-limits)
  * [Status and error codes](/docs/api/customer/latest#status-and-error-codes)

* * *

  * Common objects

  * * * *

  * GraphQL Types

[Full index](/docs/api/customer/2025-10/full-index)

Choose a version:

unstable 2026-01 release candidate2025-10 latest2025-07 2025-04 2025-01

2025-10latest

# GraphQL Customer Account API

Create personalized, customer authenticated experiences with the Customer
Account API. The API offers a full range of options making it possible for
customers to view their orders, manage their profile and much more.

Copy page MD

Choose a version:

unstable 2026-01 release candidate2025-10 latest2025-07 2025-04 2025-01

2025-10latest

##

[Anchor to
Authentication](/docs/api/customer/latest#authentication)Authentication

This guide will provide an overview of the new authentication system for the
Customer Account API and help developers understand how to use it effectively.

###

[Anchor to Overview](/docs/api/customer/latest#overview)Overview

The Customer Account API is designed to serve as the primary source for
customer-scoped data and authenticated customer actions. To ensure secure
access to this data, a robust authentication system is in place for
developers.

###

[Anchor to Authentication process](/docs/api/customer/latest#authentication-
process)Authentication process

We support two types of clients:

  * **Confidential** \- A client capable of keeping a client secret confidential. This type is typically used for server-side applications.
  * **Public** \- A client unable to keep a client secret confidential. This type is typically used for client-side applications, including web and mobile clients.

For **public clients** , we use [Proof Key for Code
Exchange](https://datatracker.ietf.org/doc/html/rfc7636) or PKCE to mitigate
the risk of authorization code interception.

In order to authenticate and utilize the Customer Account API, the sections
below outline the necessary steps required by the [OAuth 2.0 authorization
specification](https://datatracker.ietf.org/doc/html/rfc6749).

###

[Anchor to Discovery endpoints](/docs/api/customer/latest#discovery-
endpoints)Discovery endpoints

Discovery endpoints are standardized URLs that return configuration data about
a shop's authentication and API endpoints. Use these endpoints whenever you
need to authenticate customers or make API requests to ensure your application
works with any shop's configuration.

Using discovery endpoints automatically provides authentication and API URLs
rather than hardcoding URLs. This keeps your integration working as Shopify's
infrastructure evolves and automatically resolves the correct URLs for any
shop, removing the need for hardcoded domain dependencies.

Your app can use the following discovery endpoints on the storefront domain:

  * **OpenID configuration**
    * **Endpoint** : `GET /.well-known/openid-configuration`
    * **Returns** :
      * Authentication endpoints (authorization, token, logout URLs)
      * Standard OpenID Connect discovery format
  * **Customer Account API configuration** :
    * **Endpoint** : `GET /.well-known/customer-account-api`
    * **Returns** :
      * Customer Account API endpoints (GraphQL API, MCP API)
      * Shopify-specific discovery format

## Authorization request

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

// First, discover the authentication endpoints

const discoveryResponse = await fetch(`https://${shopDomain}/.well-
known/openid-configuration`);

const authConfig = await discoveryResponse.json();

  

// Now build the authorization request using the discovered endpoint

const clientId = process.env.CLIENT_ID;

const authorizationRequestUrl = new URL(authConfig.authorization_endpoint);

  

authorizationRequestUrl.searchParams.append(

'scope',

'openid email customer-account-api:full'

);

authorizationRequestUrl.searchParams.append(

'client_id',

clientId

);

authorizationRequestUrl.searchParams.append(

'response_type',

'code'

);

authorizationRequestUrl.searchParams.append(

'redirect_uri',

`<redirect_uri>`

);

authorizationRequestUrl.searchParams.append(

'state',

'<state>'

);

authorizationRequestUrl.searchParams.append(

'nonce',

'<nonce>'

);

  

// Public client

const verifier = await generateCodeVerifier();

const challenge = await generateCodeChallenge(verifier);

localStorage.setItem('code-verifier', verifier);

  

authorizationRequestUrl.searchParams.append(

'code_challenge',

challenge

);

authorizationRequestUrl.searchParams.append(

'code_challenge_method',

'S256'

);

  

window.location.href = authorizationRequestUrl.toString()

###

[Anchor to Discover authentication
endpoints](/docs/api/customer/latest#discover-authentication-
endpoints)Discover authentication endpoints

Before initiating the authorization flow, discover the authentication
endpoints from the shop's storefront domain. The response contains
`authorization_endpoint`, `token_endpoint`, `end_session_endpoint`, and
`jwks_uri`.

The example code demonstrates how to:

  1. Make a request to the discovery endpoint.
  2. Parse the JSON response to access the authentication URLs.
  3. Use these discovered endpoints in your OAuth flow.

You should include this discovery step once, at the beginning of your
authentication flow. Then you can reuse the discovered endpoints throughout
your application.

## Discover Authentication Endpoints

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

const discoveryUrl = `https://${shopDomain}/.well-known/openid-configuration`;

  

const response = await fetch(discoveryUrl);

const config = await response.json();

  

// config contains:

// {

// "authorization_endpoint":
"https://{shopDomain}/authentication/oauth/authorize",

// "token_endpoint": "https://{shopDomain}/authentication/oauth/token",

// "end_session_endpoint": "https://{shopDomain}/authentication/logout",

// "jwks_uri": "https://{shopDomain}/authentication/.well-known/jwks.json",

// "issuer": "https://shopify.com/authentication/{shopId}"

// }

###

[Anchor to
Authorization](/docs/api/customer/latest#authorization)Authorization

To redirect a customer to the login page, use the `authorization_endpoint`
from the discovery response with the following parameters:

* * *

scope•openid email customer-account-api:fullrequired

A list of scope names separated by space. Scopes are attached to all access
tokens issued from this authorization request and determine what data these
access token will be able to retrieve from API endpoints.

* * *

client_id•<client_id>required

Unique UUID associated with the application. This should be visible in the
Customer Account API settings of the given application / storefront.

* * *

response_type•coderequired

Implies that authorization code flow will be used.

* * *

redirect_uri•<redirect_uri>required

URL to redirect with `authorization code` after successful authentication.
This has to be one of the redirect URIs defined in the customer account api
settings of the given application/storefront. For public mobile applications,
the scheme must be "shop.{shop_id}.*."

* * *

state•<state>required

A string of characters which will be returned along with the `code` during
callback/redirect. This is used to prevent CSRF/XSRF. See Generating state for
more details on usage.

* * *

nonce•<nonce>

This is used to mitigate replay attacks. The `nonce` will be returned in the
`id_token` as part of the Obtain access code step. See Generating nonce and
Retrieving Nonce for more details on usage.

* * *

prompt•none

Specifies that no login screen should be shown to the user. If a session is
present, a `code` is returned that can be used in the Obtain access token
step. If no session is present, a login_required error is returned to your
redirect_uri endpoint.

* * *

locale•en

Specifies the the language for the login screen. Supported Locales: `en`,
`fr`, `cs`, `da`, `de`, `el`, `es`, `fi`, `hi`, `hr`, `hu`, `id`, `it`, `ja`,
`ko`, `lt`, `ms`, `nb`, `nl`, `pl`, `pt-BR`, `pt-PT`, `ro`, `ru`, `sk`, `sl`,
`sv`, `th`, `tr`, `vi`, `zh-CN`, `zh-TW`

* * *

###

[Anchor to Public client](/docs/api/customer/latest#public-client)Public
client

In addition to the parameters above, public clients (web or mobile) need to
provide the parameters outlined below.

Info

An example implementing a code challenge and verifier can be seen in the Code
challenge and verifier section

* * *

code_challenge•<code_verifier>required

A string that is derived from the `code_verifier` using a hashing algorithm.
The `code_verifier` is a string that is randomly generated by the client.

* * *

code_challenge_method•S256required

The code challenge method.

* * *

## Authorization Request

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

// First, discover the authentication endpoints

const discoveryResponse = await fetch(`https://${shopDomain}/.well-
known/openid-configuration`);

const config = await discoveryResponse.json();

  

const clientId = process.env.CLIENT_ID;

const authorizationRequestUrl = new URL(config.authorization_endpoint);

  

authorizationRequestUrl.searchParams.append(

'scope',

'openid email customer-account-api:full'

);

authorizationRequestUrl.searchParams.append(

'client_id',

clientId

);

authorizationRequestUrl.searchParams.append(

'response_type',

'code'

);

authorizationRequestUrl.searchParams.append(

'redirect_uri',

`<redirect_uri>`

);

authorizationRequestUrl.searchParams.append(

'state',

'<state>'

);

authorizationRequestUrl.searchParams.append(

'nonce',

'<nonce>'

);

  

// Public client

const verifier = await generateCodeVerifier();

const challenge = await generateCodeChallenge(verifier);

localStorage.setItem('code-verifier', verifier);

  

authorizationRequestUrl.searchParams.append(

'code_challenge',

challenge

);

authorizationRequestUrl.searchParams.append(

'code_challenge_method',

'S256'

);

  

window.location.href = authorizationRequestUrl.toString()

###

[Anchor to Retrieve code to get access
token](/docs/api/customer/latest#retrieve-code-to-get-access-token)Retrieve
code to get access token

When a customer successfully completes a login and is redirected to the uri
specified in the parameters above, a `code` is received as a query parameter.
The code will be utilized in the Obtain access token step and enables you to
make requests to the Customer Account API.

The optional `state` parameter will also be returned if it was part of the
original Authorization step above.

###

[Anchor to Obtain access token](/docs/api/customer/latest#obtain-access-
token)Obtain access token

To authenticate with the Customer Account API, your application needs to
obtain an access token. You can request an access token by sending a `POST`
request to the `token_endpoint` discovered from the OpenID configuration:

If in the Authorization step a `nonce` was passed, it can be validated using
the Retrieving nonce step.

This will return a json result that contains the `access_token`,
`refresh_token`, `id_token` and `expires_in` (in seconds) of the access token.

**Confidential client only**

Headers containing authorization credentials are required in order to get an
access token. Check out the Authorization header section for more details.

If a response code of `301` is returned, ensure the correct `shop_id` is
specified in the `POST` request.

If a response code of `400` with a message of `invalid_grant` is returned,
then ensure that padding is removed (for example, `=`) from your
base64-encoded code challenge in the Authorization step. Additionally, make
sure to replace “+” with “-” and “/” with “_” to ensure compatibility with URL
encoding.

If a response code of `401` with a message of `invalid_client` is returned,
then verify that the `client_id` is correct.

If a response code of `401` with a message of `invalid_token` in the `www-
authenticate` header is returned, then ensure that an `origin` header is
specified in the request. Verify that the `origin` header specified is set in
the list of Javascript Origin(s) in the Customer Account API settings page.

If a response code of `403` with a message of `You do not have permission to
access this website` is returned, then ensure that a `user-agent` header is
specified in the request.

With this access token, you can now make requests to the Customer Account API.

* * *

grant_type•authorization_coderequired

Must be set to `authorization_code`.

* * *

client_id•<client_id>required

Same client_id used in the `authorize` request.

* * *

redirect_uri•<redirect_uri>required

Same redirect_uri specified in the first `/authorize` request.

* * *

code•<code>required

The `code` received as a parameter as part of the Retrieve code section.

* * *

###

[Anchor to Public Client](/docs/api/customer/latest#public-client)Public
Client

In addition to the parameters above, public clients (web or mobile) need to
provide the following parameters.

* * *

code_verifier•<code_verifier>required

The `code_verifier` used to generate the `code_challenge` in the Authorization
section.

* * *

## Obtain Access Token

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

// First, discover the authentication endpoints

const discoveryResponse = await fetch(`https://${shopDomain}/.well-
known/openid-configuration`);

const config = await discoveryResponse.json();

  

const clientId = process.env.CLIENT_ID;

const body = new URLSearchParams();

  

body.append('grant_type', 'authorization_code');

body.append('client_id', clientId);

body.append(

'redirect_uri',

`<redirect_uri>`,

);

body.append('code', code);

  

// Public Client

const codeVerifier = localStorage.getItem('code-verifier');

body.append('code_verifier', codeVerifier);

  

const headers = {

'content-type': 'application/x-www-form-urlencoded',

// Confidential Client

'Authorization': 'Basic `<credentials>`'

}

  

// Use the discovered token_endpoint

const response = await fetch(config.token_endpoint, {

method: 'POST',

headers: headers,

body,

});

  

interface AccessTokenResponse {

access_token: string;

expires_in: number;

id_token: string;

refresh_token: string;

}

  

const {access_token, expires_in, id_token, refresh_token} =

await response.json<AccessTokenResponse>();

###

[Anchor to Use refresh token](/docs/api/customer/latest#use-refresh-token)Use
refresh token

The access token retrieved in the previous step has an associated `expires_in`
property (in seconds). Once that has passed, the access token is invalid and
needs to be refreshed.

The procedure to refresh the token is very similar to the Obtain access token
step except different parameters are passed.

To refresh your token, make a `POST` request to the `token_endpoint` from the
discovery response:

* * *

grant_type•refresh_tokenrequired

Must be set to `refresh_token`.

* * *

client_id•<client_id>required

Same client_id used in the `authorize` request.

* * *

refresh_token•<refresh_token>required

The `refresh_token` received as part of the Obtain access token step.

* * *

## Refresh Token

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

// First, discover the authentication endpoints

const discoveryResponse = await fetch(`https://${shopDomain}/.well-
known/openid-configuration`);

const config = await discoveryResponse.json();

  

const clientId = process.env.CLIENT_ID;

const body = new URLSearchParams();

  

body.append('grant_type', 'refresh_token');

body.append('client_id', clientId);

body.append('refresh_token', refresh_token);

  

const headers = {

'content-type': 'application/x-www-form-urlencoded',

// Confidential Client

'Authorization': 'Basic `<credentials>`'

}

  

// Use the discovered token_endpoint

const response = await fetch(config.token_endpoint, {

method: 'POST',

headers: headers,

body,

});

  

interface AccessTokenResponse {

access_token: string;

expires_in: number;

id_token: string;

refresh_token: string;

}

  

const {access_token, expires_in, refresh_token} =

await response.json<Omit<AccessTokenResponse, 'id_token'>>();

###

[Anchor to Authorization header (confidential client
only)](/docs/api/customer/latest#authorization-header-confidential-client-
only)Authorization header (confidential client only)

An Authorization Header is a Base64 encode of the `client_id` and
`client_secret` and is required for certain requests.

## Authorization Header

Copy

9

1

2

3

4

const clientId = process.env.CLIENT_ID;

const clientSecret = process.env.CLIENT_SECRET;

  

const credentials = btoa(`${clientId}:${clientSecret}`);

###

[Anchor to Code challenge and verifier (public client
only)](/docs/api/customer/latest#code-challenge-and-verifier-public-client-
only)Code challenge and verifier (public client only)

A code challenge and verifier are needed when doing requests from a public
client in order to verify that the client is the same client that initiated
the authorization request.

## Code Challenge and Verifier

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

export async function generateCodeVerifier() {

const rando = generateRandomCode();

return base64UrlEncode(rando);

}

  

export async function generateCodeChallenge(codeVerifier: string) {

const digestOp = await crypto.subtle.digest(

{ name: "SHA-256" },

new TextEncoder().encode(codeVerifier)

);

const hash = convertBufferToString(digestOp);

return base64UrlEncode(hash);

}

  

function generateRandomCode() {

const array = new Uint8Array(32);

crypto.getRandomValues(array);

return String.fromCharCode.apply(null, Array.from(array));

}

  

function base64UrlEncode(str: string) {

const base64 = btoa(str);

// This is to ensure that the encoding does not have +, /, or = characters in
it.

return base64.replace(/\\+/g, "-").replace(/\//g, "_").replace(/=/g, "");

}

  

function convertBufferToString(hash: ArrayBuffer) {

const uintArray = new Uint8Array(hash);

const numberArray = Array.from(uintArray);

return String.fromCharCode(...numberArray);

}

###

[Anchor to Generating state](/docs/api/customer/latest#generating-
state)Generating state

The state parameter is used to maintain the state of the client application
during the Authorization step. It acts as a security measure to prevent cross-
site request forgery (CSRF) attacks.

This `state` is then returned as a parameter in addition to the `code` in the
Retrieve code to get access token and can be used to verify that the response
matches the request.

## Generating State

Copy

9

1

2

3

4

5

export async function generateState(): Promise<string> {

const timestamp = Date.now().toString();

const randomString = Math.random().toString(36).substring(2);

return timestamp + randomString;

}

###

[Anchor to Generating nonce](/docs/api/customer/latest#generating-
nonce)Generating nonce

A nonce (number used once) is a random or unique value used to prevent replay
attacks. It can be provided in the Authorization step to ensure the freshness
and integrity of the communication.

Nonces help protect against unauthorized reuse of captured messages by
verifying that they are recent and have not been tampered with.

Once passed as part of the Authorization step, it can be verified in the
Obtain access token step. See Retrieving nonce for more information.

## Generating Nonce

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

export async function generateNonce(length: number) {

const characters =
'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';

let nonce = '';

  

for (let i = 0; i < length; i++) {

const randomIndex = Math.floor(Math.random() * characters.length);

nonce += characters.charAt(randomIndex);

}

  

return nonce;

}

###

[Anchor to Retrieving nonce](/docs/api/customer/latest#retrieving-
nonce)Retrieving nonce

In the Obtain access token step an `id_token` is returned, this is an encoded
JWT token that once decoded contains the nonce that was passed in the
Authorization step.

## Retrieving Nonce

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

export async function getNonce(token: string) {

return decodeJwt(token).payload.nonce;

}

  

export function decodeJwt(token: string) {

const [header, payload, signature] = token.split('.');

  

const decodedHeader = JSON.parse(atob(header));

const decodedPayload = JSON.parse(atob(payload));

  

return {

header: decodedHeader,

payload: decodedPayload,

signature,

};

}

###

[Anchor to Logging out](/docs/api/customer/latest#logging-out)Logging out

To log out a customer, redirect them to the `end_session_endpoint` discovered
from the OpenID configuration:

* * *

id_token_hint•<id_token>required

The `id_token` received as part of the Obtain access code step

* * *

post_logout_redirect_uri•<post_logout_redirect_uri>required

The URI to redirect to after logging out. If this isn't specified, then the
uri to redirect to will to one of the URIs in the Logout URI setting.

* * *

####

[Anchor to Mobile client](/docs/api/customer/latest#mobile-client)Mobile
client

For mobile clients, the logout uri can be called as an API endpoint that
returns a `200 OK` status code on successful logout, rather than performing a
redirect. `id_token_hint` is still required.

###

[Anchor to Stay authenticated from Headless storefront to
Checkout](/docs/api/customer/latest#stay-authenticated-from-headless-
storefront-to-checkout)Stay authenticated from Headless storefront to Checkout

In order to stay authenticated from the headless storefront to checkout, you
need to add a query parameter `logged_in=true` to the end of the checkout url.

For example, if the checkout url is `https://<shop-
domain>/checkouts/<checkout_id>`, then the URL should look like this:

`https://<shop-domain>/checkouts/<checkout_id>?logged_in=true`

###

[Anchor to Stay authenticated from Checkout to Headless storefront via
Cart](/docs/api/customer/latest#stay-authenticated-from-checkout-to-headless-
storefront-via-cart)Stay authenticated from Checkout to Headless storefront
via Cart

Info

Customer Accounts must be enabled.

There are situations where a customer can be authenticated in checkout but not
in the headless storefront. This can be addressed with the following steps.

During the Authorization step detailed above, include the optional `prompt`
parameter with a value of `none`. This performs a silent check with the
authorization server and will not prompt the customer to log in again. If the
customer's session has expired, the `redirect_uri` will receive code parameter
set to `login_required`.

* * *

##

[Anchor to Endpoints and queries](/docs/api/customer/latest#endpoints-and-
queries)Endpoints and queries

The Customer Account API is available only in GraphQL.

###

[Anchor to Discover API endpoints](/docs/api/customer/latest#discover-api-
endpoints)Discover API endpoints

Before making API requests, discover the GraphQL endpoint dynamically from the
shop's storefront domain. The response contains `graphql_api` and `mcp_api`
endpoints with the current API version already included.

The example code demonstrates how to:

  1. Make a request to the Customer Account API discovery endpoint.
  2. Parse the JSON response to get the GraphQL and MCP API URLs.
  3. Use the discovered `graphql_api` endpoint for your API requests.

The discovered endpoint already includes the latest stable API version, so you
can use it directly without appending version numbers.

## Discover API Endpoints

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

const apiDiscoveryUrl = `https://${shopDomain}/.well-known/customer-account-
api`;

  

const response = await fetch(apiDiscoveryUrl);

const apiConfig = await response.json();

  

// apiConfig contains:

// {

// "graphql_api":
"https://{shopDomain}/customer/api/{LATEST_API_VERSION}/graphql",

// "mcp_api": "https://{shopDomain}/customer/api/mcp"

// }

// Note: URLs will use the shop's configured customer accounts domain,

// which may be a custom vanity domain instead of myshopify.com

  

// Use the discovered GraphQL endpoint directly (already includes version)

const graphqlEndpoint = apiConfig.graphql_api;

Like other Shopify APIs, the Customer Account API releases once a quarter. If
you need a specific API version, then construct the [versioned
URL](/docs/api/usage/versioning) from the discovered URL.

`https://{shop-domain}/customer/api/2025-10/graphql`

If this request responds with a `500`, then verify you don't have any
misspelled parameters when obtaining the access token.

POST

## Dynamic GraphQL Endpoint

Node.jscURL

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

// First discover the API endpoints

const apiDiscoveryResponse = await fetch(`https://${shopDomain}/.well-
known/customer-account-api`);

const apiConfig = await apiDiscoveryResponse.json();

  

// Use the discovered endpoint directly

const graphqlEndpoint = apiConfig.graphql_api;

  

const response = await fetch(graphqlEndpoint, {

method: 'POST',

headers: {

'Content-Type': 'application/json',

Authorization: {access_token},

},

body: JSON.stringify({

operationName: 'SomeQuery',

query: 'query { customer { emailAddress { emailAddress }}}',

variables: {},

}),

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

# First discover the API endpoint

API_CONFIG=$(curl -s https://{shopDomain}/.well-known/customer-account-api)

GRAPHQL_ENDPOINT=$(echo $API_CONFIG | jq -r '.graphql_api')

  

# Use the discovered endpoint to make API calls (version already included)

curl -X POST \

"${GRAPHQL_ENDPOINT}" \

-H 'Content-Type: application/json' \

-H 'Authorization: {access_token}' \

-d '

query {

customer {

emailAddress {

emailAddress

}

}

}

'

##### Node.js

    
    
    // First discover the API endpoints
    const apiDiscoveryResponse = await fetch(`https://${shopDomain}/.well-known/customer-account-api`);
    const apiConfig = await apiDiscoveryResponse.json();
    
    // Use the discovered endpoint directly
    const graphqlEndpoint = apiConfig.graphql_api;
    
    const response = await fetch(graphqlEndpoint, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        Authorization: {access_token},
      },
      body: JSON.stringify({
        operationName: 'SomeQuery',
        query: 'query { customer { emailAddress { emailAddress }}}',
        variables: {},
      }),
    });

##### cURL

    
    
    # First discover the API endpoint
    API_CONFIG=$(curl -s https://{shopDomain}/.well-known/customer-account-api)
    GRAPHQL_ENDPOINT=$(echo $API_CONFIG | jq -r '.graphql_api')
    
    # Use the discovered endpoint to make API calls (version already included)
    curl -X POST \
      "${GRAPHQL_ENDPOINT}" \
      -H 'Content-Type: application/json' \
      -H 'Authorization: {access_token}' \
      -d '
      query {
        customer {
          emailAddress {
            emailAddress
          }
        }
      }
      '

* * *

##

[Anchor to Directives](/docs/api/customer/latest#directives)Directives

A directive provides a way for apps to describe additional options to the
GraphQL executor. It lets GraphQL change the result of the query or mutation
based on the additional information provided by the directive.

###

[Anchor to Customer Account API
Directives](/docs/api/customer/latest#customer-account-api-directives)Customer
Account API Directives

* * *

####

[Anchor to @inContext (Language)](/docs/api/customer/latest#incontext-
language)@inContext (Language)

In Customer Account API versions higher than 2025-04, the `@incontext`
directive takes an optional [language code
argument](/api/customer/2025-10/enums/LanguageCode) and applies this to the
query or mutation.

This example shows how to return user errors that are translated into French
`@incontext(language: FR)`.

* * *

## @inContext (Country Code)

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

mutation customerAddressUpdate @inContext(language: FR){

customerAddressUpdate(address: {phoneNumber: "invalid123"}, addressId:
"gid://shopify/CustomerAddress/123456" ) {

userErrors {

code

field

message

}

}

}

## Response

JSON

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

{

"data": {

"customerAddressUpdate": {

"userErrors": [

{

"code": "PHONE_NUMBER_NOT_VALID",

"field": null,

"message": "Le numéro de téléphone n'est pas valide."

}

]

}

},

"extensions": {

"context": {

"country": "CA",

"language": "FR"

},

"cost": {

"requestedQueryCost": 10,

"actualQueryCost": 10

}

}

}

* * *

##

[Anchor to Rate limits](/docs/api/customer/latest#rate-limits)Rate limits

The Customer Account API is rate-limited using calculated query costs,
measured in cost points. Each field returned by a query costs a set number of
points. The total cost of a query is the sum of all the fields it returns, so
more complex queries cost more to run.

This API limits each app to 7500 cost points per store and customer. This
quota replenishes at a rate of either 100.0 or 200.0 cost points per second,
depending on your plan.

Most fields cost 1 point. Most mutations cost 10 points. The best way to
determine the true cost of a query is to run it. The API response includes
information about the total query cost and the client's current quota under
the extensions key. Include a `Shopify-GraphQL-Cost-Debug=1` header to receive
a more detailed breakdown of the query cost.

Learn more about [rate limits](https://shopify.dev/api/usage/limits#rate-
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

{

customer {

firstName

lastName

}

}

{}

## Response

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

"errors": [{

"message": "Throttled",

"extensions": {

"code": "THROTTLED",

"documentation": "https://shopify.dev/api/usage/limits#rate-limits"

}

}]

}

* * *

##

[Anchor to Status and error codes](/docs/api/customer/latest#status-and-error-
codes)Status and error codes

All API queries return HTTP status codes that contain more information about
the response.

###

[Anchor to 200 OK](/docs/api/customer/latest#200-ok)200 OK

GraphQL HTTP status codes are different from REST API status codes. Most
importantly, the GraphQL API can return a `200 OK` response code in cases that
would typically produce 4xx or 5xx errors in REST.

###

[Anchor to Error handling](/docs/api/customer/latest#error-handling)Error
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

extensions.code•string

Shows error codes common to Shopify. Additional error codes may also be shown.

Show common error codes

THROTTLED

The client has exceeded the rate limit. Similar to 429 Too Many Requests.

SHOP_INACTIVE

The shop is not active. This can happen when stores repeatedly exceed API rate
limits or due to fraud risk.

INTERNAL_SERVER_ERROR

Shopify experienced an internal error while processing the request. This error
is returned instead of 500 Internal Server Error in most circumstances.

* * *

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

{

"errors": [

{

"message": "Throttled",

"extensions": {

"code": "THROTTLED",

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

{

"errors": [

{

"message": "Internal error. Looks like something went wrong on our end.

Request ID: 1b355a21-7117-44c5-8d8b-8948082f40a8 (include this in support
requests).",

"extensions": {

"code": "INTERNAL_SERVER_ERROR",

}

}

]

}

##### Throttled

    
    
    {
      "errors": [
        {
          "message": "Throttled",
          "extensions": {
            "code": "THROTTLED",
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
          }
        }
      ]
    }

###

[Anchor to 4xx and 5xx status codes](/docs/api/customer/latest#4xx-and-5xx-
status-codes)4xx and 5xx status codes

The 4xx and 5xx errors occur infrequently. They are often related to network
communications, your account, or an issue with Shopify’s services.

Many errors that would typically return a 4xx or 5xx status code, return an
HTTP 200 errors response instead. Refer to the 200 OK section above for
details.

* * *

####

[Anchor to [object Object]](/docs/api/customer/latest#400-bad-request)400 Bad
Request

The server will not process the request.

* * *

####

[Anchor to [object Object]](/docs/api/customer/latest#401-bad-request)401 Bad
Request

The client does not have correct authentication credentials.

* * *

####

[Anchor to [object Object]](/docs/api/customer/latest#402-payment-required)402
Payment Required

The shop is frozen. The shop owner will need to pay the outstanding balance to
[unfreeze](https://help.shopify.com/en/manual/your-account/pause-close-
store#unfreeze-your-shopify-store) the shop.

* * *

####

[Anchor to [object Object]](/docs/api/customer/latest#403-forbidden)403
Forbidden

The shop is forbidden. Returned if the store has been marked as fraudulent.

* * *

####

[Anchor to [object Object]](/docs/api/customer/latest#404-not-found)404 Not
Found

The resource isn’t available. This is often caused by querying for something
that’s been deleted.

* * *

####

[Anchor to [object Object]](/docs/api/customer/latest#423-locked)423 Locked

The shop isn’t available. This can happen when stores repeatedly exceed API
rate limits or due to fraud risk.

* * *

####

[Anchor to [object Object]](/docs/api/customer/latest#5xx-errors)5xx Errors

An internal error occurred in Shopify. Check out the [Shopify status
page](https://www.shopifystatus.com) for more information.

* * *

Info

Didn’t find the status code you’re looking for? View the complete list of [API
status response and error codes](/api/usage/response-codes).

{}

## Sample error codes

400401402403404423500

Copy

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

HTTP/1.1 401 Unauthorized

{

"errors": "User does not have access"

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

##### 401

    
    
    HTTP/1.1 401 Unauthorized
    {
      "errors": "User does not have access"
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

