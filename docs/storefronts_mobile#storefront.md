# Source: https://shopify.dev/docs/storefronts/mobile#storefront

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

Storefronts

  * [Overview](/docs/storefronts)
  * [Themes](/docs/storefronts/themes)
  * [Web API / Headless](/docs/storefronts/headless)
  * [Mobile](/docs/storefronts/mobile)

Collapse sidebar

  * ### Mobile commerce

    * [Overview](/docs/storefronts/mobile)
    * [Android Buy SDK](/docs/storefronts/mobile/buy-sdk-android)
    * [iOS Buy SDK](/docs/storefronts/mobile/buy-sdk-ios)
  * ### Checkout Kit

    * [Overview](/docs/storefronts/mobile/checkout-kit)
    * Getting Started

    * [Authentication](/docs/storefronts/mobile/checkout-kit/authenticate-checkouts)
    * [Branding](/docs/storefronts/mobile/checkout-kit/configuration)
    * [Lifecycle management](/docs/storefronts/mobile/checkout-kit/monitor-checkout-lifecycle)
    * [Performance](/docs/storefronts/mobile/checkout-kit/preloading)
    * [Offsite payments](/docs/storefronts/mobile/checkout-kit/offsite-payments)
    * [Privacy compliance](/docs/storefronts/mobile/checkout-kit/privacy-compliance)
    * Accelerated checkouts

Full index

ExpandOn this page

  * [How it works](/docs/storefronts/mobile#how-it-works)
  * [Storefront](/docs/storefronts/mobile#storefront)
  * [Buyer identity](/docs/storefronts/mobile#buyer-identity)
  * [Checkout Kit](/docs/storefronts/mobile#checkout-kit)

# Building a mobile app for your Shopify store

Copy page MD

![Diagram showing how storefront, buyer identity and checkout can be combined
when building a mobile app](https://cdn.shopify.com/shopifycloud/shopify-
dev/production/assets/assets/images/custom-storefronts/mobile-sdk-overview-Bc-
bSrFY.png)

* * *

##

[Anchor to How it works](/docs/storefronts/mobile#how-it-works)How it works

Shopify provides a suite of libraries that enable developers to deliver best-
in-class, mobile app commerce experiences for buyers: build custom storefront
and product discovery flows, integrate identity with sign-in and account
management, and accelerate buyers through a contextual and personalized
checkout process.

* * *

##

[Anchor to Storefront](/docs/storefronts/mobile#storefront)Storefront

Shopify’s Mobile Buy SDK’s enable you to create and embed custom storefront
and product discovery experiences within your mobile app. The SDK’s interface
with the [GraphQL Storefront API](/docs/api/storefront) to fetch information
about products and collections, and to assemble a personalized buyer cart with
contextual buyer information.

[![](/images/icons/48/custom-storefronts.png)![](/images/icons/48/custom-
storefronts-dark.png)iOS Buy SDKCreate custom storefronts and assemble carts
within an iOS app.iOS Buy SDKCreate custom storefronts and assemble carts
within an iOS app.](/docs/storefronts/mobile/buy-sdk-ios)

[iOS Buy SDK  
  
Create custom storefronts and assemble carts within an iOS
app.](/docs/storefronts/mobile/buy-sdk-ios)

[![](/images/icons/48/custom-storefronts.png)![](/images/icons/48/custom-
storefronts-dark.png)Android Buy SDKCreate custom storefronts and assemble
carts within an Android app.Android Buy SDKCreate custom storefronts and
assemble carts within an Android app.](/docs/storefronts/mobile/buy-sdk-
android)

[Android Buy SDK  
  
Create custom storefronts and assemble carts within an Android
app.](/docs/storefronts/mobile/buy-sdk-android)

* * *

##

[Anchor to Buyer identity](/docs/storefronts/mobile#buyer-identity)Buyer
identity

The best shopping experiences are buyer and context aware, enabling relevant
personalization of product, payment, and other preferences in product
discovery, checkout, and post-purchase workflows. Shopify provides support for
built-in identity solutions, integrations with third-party identity providers,
and cart-driven workflows for optimizing guest and new buyer checkout
journeys.

[![](/images/icons/48/graphql.png)![](/images/icons/48/graphql-
dark.png)Customer AccountsAuthenticate buyers with a secure one-time code sent
to an email address, with built-in support for Shop sign-in. Integrate into
your app using the Customer Account API.Customer AccountsAuthenticate buyers
with a secure one-time code sent to an email address, with built-in support
for Shop sign-in. Integrate into your app using the Customer Account
API.](/docs/api/customer)

[Customer Accounts  
  
Authenticate buyers with a secure one-time code sent to an email address, with
built-in support for Shop sign-in. Integrate into your app using the Customer
Account API.](/docs/api/customer)

[![](/images/icons/48/custom-storefronts.png)![](/images/icons/48/custom-
storefronts-dark.png)Legacy Customer AccountsAuthenticate buyers with legacy
customer account via username and password. Integrate via Storefront API or
Buy SDK.Legacy Customer AccountsAuthenticate buyers with legacy customer
account via username and password. Integrate via Storefront API or Buy
SDK.](/docs/api/storefront/latest/queries/customer)

[Legacy Customer Accounts  
  
Authenticate buyers with legacy customer account via username and password.
Integrate via Storefront API or Buy
SDK.](/docs/api/storefront/latest/queries/customer)

[![](/images/icons/48/tutorial.png)![](/images/icons/48/tutorial-
dark.png)MultipassAuthenticate buyers with third-party identity and
authentication system via Multipass protocol.MultipassAuthenticate buyers with
third-party identity and authentication system via Multipass
protocol.](/docs/api/multipass)

[Multipass  
  
Authenticate buyers with third-party identity and authentication system via
Multipass protocol.](/docs/api/multipass)

[![](/images/icons/48/custom-storefronts.png)![](/images/icons/48/custom-
storefronts-dark.png)Cart Buyer IdentityAssociate known identity and buyer
preferences via cart to prefill and accelerate checkout.Cart Buyer
IdentityAssociate known identity and buyer preferences via cart to prefill and
accelerate
checkout.](/docs/api/storefront/latest/mutations/cartBuyerIdentityUpdate)

[Cart Buyer Identity  
  
Associate known identity and buyer preferences via cart to prefill and
accelerate
checkout.](/docs/api/storefront/latest/mutations/cartBuyerIdentityUpdate)

* * *

##

[Anchor to Checkout Kit](/docs/storefronts/mobile#checkout-kit)Checkout Kit

Shopify’s Checkout Kit enables you to provide the world’s highest converting,
customizable, one-page checkout directly within the native app. The experience
is a fully-featured checkout that preserves all of the store
customizations—e.g. branding settings, UI extensions, Functions, and more. It
also provides platform idiomatic defaults such as support for light and dark
mode, and developer APIs to embed, customize, and follow the lifecycle of the
checkout experience.

[![](/images/icons/48/cart.png)![](/images/icons/48/cart-dark.png)Checkout
KitA library for presenting the Shopify checkout experience.Checkout KitA
library for presenting the Shopify checkout
experience.](/docs/storefronts/mobile/checkout-kit)

[Checkout Kit  
  
A library for presenting the Shopify checkout
experience.](/docs/storefronts/mobile/checkout-kit)

* * *

Was this page helpful?

YesNo

  * [How it works](/docs/storefronts/mobile#how-it-works)
  * [Storefront](/docs/storefronts/mobile#storefront)
  * [Buyer identity](/docs/storefronts/mobile#buyer-identity)
  * [Checkout Kit](/docs/storefronts/mobile#checkout-kit)

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

