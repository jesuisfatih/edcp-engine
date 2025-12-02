# Source: https://shopify.dev/docs/storefronts/headless/building-with-the-storefront-api/cart

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

  * ### Getting started

    * [Overview](/docs/storefronts/headless)
    * Getting started

  * ### Hydrogen and Oxygen

    * [Getting started](/docs/storefronts/headless/hydrogen/getting-started)
    * [Fundamentals](/docs/storefronts/headless/hydrogen/fundamentals)
    * Analytics

    * Cart

    * [Content security policy](/docs/storefronts/headless/hydrogen/content-security-policy)
    * Data fetching

    * Caching

    * Markets

    * [SEO](/docs/storefronts/headless/hydrogen/seo)
    * [Storefronts](/docs/storefronts/headless/hydrogen/storefronts)
    * [Environments](/docs/storefronts/headless/hydrogen/environments)
    * Deployments

    * Debugging and testing

    * Performance

    * Migrate and upgrade

    * [Production checklist](/docs/storefronts/headless/hydrogen/production-checklist)
    * [Hydrogen CLI commands](/docs/api/shopify-cli/hydrogen)
    * [Hydrogen API reference](/docs/api/hydrogen)
    * Cookbook

  * ### Bring your own stack

    * [Overview](/docs/storefronts/headless/bring-your-own-stack)
    * [Headless with B2B](/docs/storefronts/headless/bring-your-own-stack/b2b)
    * Shopify Plugin for WordPress

    * [Storefront Web Components](/docs/api/storefront-web-components)
  * ### Headless APIs

    * Building with the Storefront API

    * Building with the Customer Account API

    * Additional SDKs

Full index

ExpandOn this page

  * [How it works](/docs/storefronts/headless/building-with-the-storefront-api/cart#how-it-works)
  * [Benefits](/docs/storefronts/headless/building-with-the-storefront-api/cart#benefits)
  * [Extension options](/docs/storefronts/headless/building-with-the-storefront-api/cart#extension-options)
  * [International pricing](/docs/storefronts/headless/building-with-the-storefront-api/cart#international-pricing)
  * [Speed and scale](/docs/storefronts/headless/building-with-the-storefront-api/cart#speed-and-scale)
  * [Limitations](/docs/storefronts/headless/building-with-the-storefront-api/cart#limitations)
  * [Developer tools and resources](/docs/storefronts/headless/building-with-the-storefront-api/cart#developer-tools-and-resources)
  * [Product Roadmap](/docs/storefronts/headless/building-with-the-storefront-api/cart#product-roadmap)
  * [Next steps](/docs/storefronts/headless/building-with-the-storefront-api/cart#next-steps)

# Cart

Copy page MD

Carts are smart buyer assistants that contain the merchandise that a buyer
intends to purchase and information about the buyer.

This guide introduces carts within the context of the buying journey, ways
that you can extend a cart's functionality, and some considerations before you
get started with building carts.

* * *

##

[Anchor to How it works](/docs/storefronts/headless/building-with-the-
storefront-api/cart#how-it-works)How it works

The following components form a part of every buying journey:

  * A **storefront** is where merchants tell their brand story, and where customers browse available products.

  * A **cart** is where customers add products that they're interested in buying, and remove products that they no longer want to buy. A customer might visit their cart multiple times to renegotiate with themselves before they make a final purchase.

  * A **checkout** is where a customer makes their final decision to purchase products, and completes a transaction.

![A diagram showing the components that form a part of every buying
journey](https://cdn.shopify.com/shopifycloud/shopify-
dev/production/assets/assets/images/apps/storefront-cart-
checkout-C8xXF93e.png)

* * *

##

[Anchor to Benefits](/docs/storefronts/headless/building-with-the-storefront-
api/cart#benefits)Benefits

The carts that most buyers encounter are simple baskets that are only used to
collect products. They lack functionality and context, and typically lead to
buyer frustration at checkout.

Shopify-powered carts provide the following benefits:

  * Display accurate and personalized discounts, tax, and shipping estimates.
  * Provide price transparency in real time, and at each new step of the purchase journey.
  * Run brand-provided custom business logic.
  * Shortcut buyers through checkout by providing known buyer preferences, such as payment methods or shipping details.
  * Offer fast and predictable performance no matter the size of the store or the sale.

* * *

##

[Anchor to Extension options](/docs/storefronts/headless/building-with-the-
storefront-api/cart#extension-options)Extension options

Many merchants have unique business requirements. You can extend the
functionality of a cart, while ensuring it's performant, reliable, and
scalable in checkout, in the following ways:

Feature| Description| Example use cases  
---|---|---  
[Shopify Functions](/docs/apps/build/functions)| Extend and customize
Shopify's default logic and provide consistency throughout the buyer journey.|
Create a custom validation function that can be executed by Shopify on every
cart update to do the following:  

  * Validate or limit the number of items a buyer can add to their cart.
  * Validate an address or check for a PO box.

  
[Metafields](/docs/storefronts/headless/building-with-the-storefront-
api/cart/manage#step-4-set-metafields-on-a-cart)| Create metafields to extend
the cart schema with custom values and logic at checkout.| Attach custom
structured metadata on a cart, and read it from a checkout extension to
deliver a customized end-to-end buyer experience.  
[Preferences](/docs/storefronts/headless/building-with-the-storefront-
api/cart/manage#step-5-update-customer-information-and-customer-preferences-
for-guest-checkout-journeys)| Set customer preferences to provide a
personalized cart and checkout experience.| Provide a list of preferred
delivery addresses to accelerate the checkout flow, and best optimize
conversion.  
  
* * *

##

[Anchor to International pricing](/docs/storefronts/headless/building-with-
the-storefront-api/cart#international-pricing)International pricing

Carts offer [contextual experiences](/docs/storefronts/headless/building-with-
the-storefront-api/markets/international-pricing#step-2-create-a-cart) based
on location, language, and pricing. You can query international prices for
products and orders, and explicitly set the context of a cart.

Users can configure the prices of products on a per country basis in their
Shopify admin. For example, a storefront might have default prices for
products set in USD, and price adjustments configured for Canada (CAD),
Australia (AUD), and France (EUR).

The following diagram shows the different prices of the same product based on
customer location:

![A diagram showing different prices of the same product based on customer
location](https://cdn.shopify.com/shopifycloud/shopify-
dev/production/assets/assets/images/apps/contextual-pricing-storefront-api-
DhwWaJ-O.png)

* * *

##

[Anchor to Speed and scale](/docs/storefronts/headless/building-with-the-
storefront-api/cart#speed-and-scale)Speed and scale

Shopify's cart functionality is built on the same infrastructure as our
storefronts. Carts are deployed globally and deliver a low-latency experience
to buyers around the world.

  * **Rate limits:** Carts don't have any global API rate limits. This means that merchants can confidently launch their biggest flash sale, or absorb an unexpected wave of buyers.
  * **Cart limits:** A shop or customer can create an unlimited number of carts.
  * **Abandonded carts:** Unused and abandoned carts automatically expire within 10 days of creation.
  * **Completed carts:** Shopify automatically deletes the cart when the customer completes their checkout.
  * **Bot Protection:** Shopify Plus [bot protection](https://help.shopify.com/manual/checkout-settings/bot-protection) is available for cart.

Note

Shopify continues to optimize every aspect of cart execution, including
delivering reliable sub-100 millisecond response times for every cart
operation.

* * *

##

[Anchor to Limitations](/docs/storefronts/headless/building-with-the-
storefront-api/cart#limitations)Limitations

  * The cart is subject to the [same throttling restrictions](/docs/api/usage/limits#rate-limits#storefront-api-rate-limits) as the Storefront API.
  * The cart supports a maximum of 500 line items.

* * *

##

[Anchor to Developer tools and resources](/docs/storefronts/headless/building-
with-the-storefront-api/cart#developer-tools-and-resources)Developer tools and
resources

Explore the following developer tools and resources to learn more about
working with carts.

[![](/images/icons/48/growth.png)![](/images/icons/48/growth-dark.png)Create
and update a cart with the Storefront APILearn how to manage a cart in Shopify
with the Storefront API.Create and update a cart with the Storefront APILearn
how to manage a cart in Shopify with the Storefront
API.](/docs/storefronts/headless/building-with-the-storefront-api/cart/manage)

[Create and update a cart with the Storefront API  
  
Learn how to manage a cart in Shopify with the Storefront
API.](/docs/storefronts/headless/building-with-the-storefront-api/cart/manage)

[![](/images/icons/48/globe.png)![](/images/icons/48/globe-dark.png)Support
international pricing on storefrontsLearn how to create a cart or checkout in
the context of a specific country.Support international pricing on
storefrontsLearn how to create a cart or checkout in the context of a specific
country.](/docs/storefronts/headless/building-with-the-storefront-
api/markets/international-pricing)

[Support international pricing on storefronts  
  
Learn how to create a cart or checkout in the context of a specific
country.](/docs/storefronts/headless/building-with-the-storefront-
api/markets/international-pricing)

[![](/images/icons/48/graphql.png)![](/images/icons/48/graphql-dark.png)Cart
objectConsult the GraphQL Storefront API reference to learn more about the
Cart object.Cart objectConsult the GraphQL Storefront API reference to learn
more about the Cart object.](/docs/api/storefront/latest/objects/Cart)

[Cart object  
  
Consult the GraphQL Storefront API reference to learn more about the Cart
object.](/docs/api/storefront/latest/objects/Cart)

[![](/images/icons/48/graphql.png)![](/images/icons/48/graphql-
dark.png)CartBuyerIdentity objectConsult the GraphQL Storefront API reference
to learn more about the CartBuyerIdentity object.CartBuyerIdentity
objectConsult the GraphQL Storefront API reference to learn more about the
CartBuyerIdentity
object.](/docs/api/storefront/latest/objects/CartBuyerIdentity)

[CartBuyerIdentity object  
  
Consult the GraphQL Storefront API reference to learn more about the
CartBuyerIdentity
object.](/docs/api/storefront/latest/objects/CartBuyerIdentity)

* * *

##

[Anchor to Product Roadmap](/docs/storefronts/headless/building-with-the-
storefront-api/cart#product-roadmap)Product Roadmap

Note

This roadmap is being shared for informational purposes and is subject to
change. Share your feedback on what future features you'd like to see in our
[community discussion board](https://github.com/Shopify/storefront-api-
feedback/discussions).

Feature| Release Target  
---|---  
[Cart API Migration Guide](/docs/storefronts/headless/building-with-the-
storefront-api/cart/migrate-to-cart-api)| 2024-04 (Shipped)  
[Append Gift Card to
Cart](/docs/api/storefront/latest/mutations/cartGiftCardCodesUpdate)| 2024-07
(Shipped)  
[Query and Set Carrier Calculated Shipping
Rates](/docs/storefronts/headless/building-with-the-storefront-
api/defer#fetching-carrier-calculated-rates-for-the-cart-using-defer)| 2024-07
(Shipped)  
[Support Asynchronous Calls with `@defer`
Directive](/docs/storefronts/headless/building-with-the-storefront-
api/defer#optimize-a-query-using-defer)| 2024-07 (Shipped)  
[`Cart.buyerIdentity` Authentication Carried Through to
Checkout](/docs/storefronts/headless/building-with-the-storefront-
api/cart/manage#step-6-authenticate-customer-for-logged-in-checkouts)| 2024-07
(Shipped)  
[Support for Native Wallets (Apple Pay, Google Pay) in Mobile Apps on
Cart](https://docs.google.com/forms/d/e/1FAIpQLSfZrQpQUfm5UiTCufo_YH4RcCipJDxjK0Dl_CS5uOIgJn-67w/viewform)|
2025-01 (Shipped)  
  
* * *

##

[Anchor to Next steps](/docs/storefronts/headless/building-with-the-
storefront-api/cart#next-steps)Next steps

  * Learn how to [create and update a cart](/docs/storefronts/headless/building-with-the-storefront-api/cart/manage) in Shopify with the Storefront API.
  * Learn how to [migrate to the Cart API](/docs/storefronts/headless/building-with-the-storefront-api/cart/migrate-to-cart-api)

* * *

Was this page helpful?

YesNo

  * [How it works](/docs/storefronts/headless/building-with-the-storefront-api/cart#how-it-works)
  * [Benefits](/docs/storefronts/headless/building-with-the-storefront-api/cart#benefits)
  * [Extension options](/docs/storefronts/headless/building-with-the-storefront-api/cart#extension-options)
  * [International pricing](/docs/storefronts/headless/building-with-the-storefront-api/cart#international-pricing)
  * [Speed and scale](/docs/storefronts/headless/building-with-the-storefront-api/cart#speed-and-scale)
  * [Limitations](/docs/storefronts/headless/building-with-the-storefront-api/cart#limitations)
  * [Developer tools and resources](/docs/storefronts/headless/building-with-the-storefront-api/cart#developer-tools-and-resources)
  * [Product Roadmap](/docs/storefronts/headless/building-with-the-storefront-api/cart#product-roadmap)
  * [Next steps](/docs/storefronts/headless/building-with-the-storefront-api/cart#next-steps)

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

