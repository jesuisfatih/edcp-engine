# Source: https://shopify.dev/docs/apps/build/localize-your-app

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

Apps

  * [Build](/docs/apps/build)
  * [Design](/docs/apps/design)
  * [Launch](/docs/apps/launch)

Collapse sidebar

  * ### Getting started

    * [Shopify app platform](/docs/apps/build)
    * [App surfaces](/docs/apps/build/app-surfaces)
    * [Scaffold an app](/docs/apps/build/scaffold-app)
    * [Build an app](/docs/apps/build/build)
  * ### Dev tools

    * [Dev MCP server](/docs/apps/build/devmcp)
    * Shopify CLI for apps

    * Dev Dashboard

  * ### Extending Shopify

    * Admin

    * Checkout

    * Customer accounts

    * Flow

    * Online store

    * Point of Sale

  * ### Building blocks

    * GraphQL

    * Extensions

    * Shopify Functions

    * Storefront MCP

    * Webhooks

    * Custom data

    * Authentication

  * ### Use cases

    * Marketing and analytics

    * Discounts

    * Product merchandising

    * Purchase options

    * Global markets

    * Orders and fulfillment

    * Payments

    * Sales channels

    * B2B

    * Shopify Collective

    * Blockchain

  * ### Best practices

    * Performance

    * [Accessibility](/docs/apps/build/accessibility)
    * [Localize your app](/docs/apps/build/localize-your-app)
    * [Integrating with Shopify](/docs/apps/build/integrating-with-shopify)
    * [Mobile support](/docs/apps/build/mobile-support)
    * [Non-deceptive code](/docs/apps/build/non-deceptive-code)
    * Compliance

    * Security

Full index

ExpandOn this page

  * [Why internationalize your app?](/docs/apps/build/localize-your-app#why-internationalize-your-app)
  * [Internationalize your app](/docs/apps/build/localize-your-app#internationalize-your-app)

# Localize your app

Copy page MD

Shopify helps merchants expand their business to a global audience, sell to
multiple countries, and scale internationally. This means that many merchants
need to sell in multiple languages and currencies.

This guide explains how internationalization works, and provides key terms and
example use cases for internationalization.

You'll also learn how to begin internationalizing your app by externalizing,
formatting, and translating strings.

* * *

##

[Anchor to Why internationalize your app?](/docs/apps/build/localize-your-
app#why-internationalize-your-app)Why internationalize your app?

###

[Anchor to Market opportunity](/docs/apps/build/localize-your-app#market-
opportunity)Market opportunity

Shopify’s priority European markets are growing rapidly—at nearly 3x the rate
of the US. Yet only 5–7% of all public apps are available in these priority
markets. Merchants typically experience Shopify as a combination of Shopify
itself and apps: 82% of active merchants have at least one app installed, and
virtually all merchants with sales use apps. This gap between international
merchant adoption and localized app availability represents a significant
opportunity for developers who localize their apps.

Additionally, different markets have unique needs, presenting specific
opportunities for app developers:

European markets:

  * **Payment solutions** : Cash on delivery is especially important in Spain and Italy, where trust concerns make this payment method essential.

  * **Compliance** : Features related to invoice formatting, tax reporting, and product reviews are highly sought-after due to complex regional regulations.

  * **Ad measurement** : European merchants invest more in advertising tools and require improved measurement solutions to address GDPR-related challenges.

Japan:

  * **Messaging integrations** : LINE messaging support is critical for Japanese merchants, who use it for marketing and customer support.

  * **Loyalty programs** : Reward systems are culturally important and expected by Japanese customers.

  * **Page customization** : Japanese merchants show higher demand for store customization tools to make their storefronts stand out.

Cross-market:

  * **Shipping integrations** : Merchants in France, Italy, and Japan require solutions that support key local shipping carriers.

  * Features developed for one international market often apply to others, enabling you to scale your solution across multiple regions.

###

[Anchor to Business impact](/docs/apps/build/localize-your-app#business-
impact)Business impact

Internationalization can deliver measurable benefits for your app:

  * **Reduced churn rates** : Localized apps have demonstrated lower user churn in non-English markets.
  * **Increased visibility** : Well-localized apps are more likely to be featured prominently in the Shopify App Store and admin.
  * **Expanded user base** : Localization helps you reach merchants who prefer or require apps in their native language.
  * **Competitive advantage** : Localizing your app lets you stand out in markets where merchants have limited localized options.

###

[Anchor to Merchant experience](/docs/apps/build/localize-your-app#merchant-
experience)Merchant experience

Without localized apps, international merchants face several challenges:

  * **Inaccurate translations** : Merchants must rely on browser-based translation tools, which are often inaccurate and disruptive.
  * **Dependence on third-party solutions** : They may need external tools or specialized support to understand and use English-only apps.
  * **Disjointed workflows** : Switching between the localized Shopify admin and non-localized apps creates a fragmented user experience.
  * **App abandonment** : Merchants may stop using apps entirely if they're not available in their native language.

* * *

##

[Anchor to Internationalize your app](/docs/apps/build/localize-your-
app#internationalize-your-app)Internationalize your app

###

[Anchor to How it works](/docs/apps/build/localize-your-app#how-it-works)How
it works

Internationalization helps merchants expand their business to a global
audience by creating shopping experiences in local languages and currencies.

Tip

You can speed up internationalizing new and existing apps by using
[i18n-ally](https://marketplace.visualstudio.com/items?itemName=Lokalise.i18n-ally),
an open source Visual Studio Code extension that makes it easier to
externalize strings, view and navigate to translation strings from code, and
perform machine translation.

The following diagram illustrates the different stages in the process of
internationalizing your app:

![Stages in the process of internationalizing your
app](https://cdn.shopify.com/shopifycloud/shopify-
dev/production/assets/assets/images/apps/internationalization/stages-B-
brMiH_.png)

####

[Anchor to Definitions](/docs/apps/build/localize-your-
app#definitions)Definitions

The following definitions provide a starting point for understanding key terms
associated with internationalizing your app:

Term| Definition  
---|---  
Internationalization| Building your app and interface so it can be used in
different locales. This includes creating flexible interfaces that allow for
text expansion and changes to word order.  
Localization| Adapting your app and interface for different locales to make
them a good cultural fit. This includes adapting features, changing visuals,
and translating text.  
Translation| Converting text from one language to another. Not to be confused
with localization, translation is just one part of localizing a product.  
  
####

[Anchor to Use cases](/docs/apps/build/localize-your-app#use-cases)Use cases

  * The app user is going global as their addressable market is growing, and their buyers live in different parts of the world.
  * The app user has staff that use the Shopify admin in multiple languages.
  * You want to promote your app in the Shopify community. Shopify promotes localized apps in the App Store over apps that aren’t localized.
  * You want to sell your app cross-border in other markets.

###

[Anchor to What you'll learn](/docs/apps/build/localize-your-app#what-youll-
learn)What you'll learn

In this guide, you'll learn how to do the following tasks:

  * Externalize strings so that they're available for localization
  * Format strings, including names and lists to support regional variation
  * Translate strings and test your UI

###

[Anchor to Requirements](/docs/apps/build/localize-your-
app#requirements)Requirements

  * You're a [user with app development permissions](/docs/apps/build/dev-dashboard/user-permissions) and have created [a dev store](/docs/apps/build/dev-dashboard/development-stores).
  * You understand the different ways of [distributing your app](/docs/apps/launch/distribution).

###

[Anchor to Step 1: Externalize strings](/docs/apps/build/localize-your-
app#step-1-externalize-strings)Step 1: Externalize strings

Translation is foundational to localization. The first step of translation
involves externalizing any hard-coded strings from your app into translation
files.

When your app renders its UI, it looks up the corresponding strings from the
translation file that's associated with the requested locale.

####

[Anchor to Source files](/docs/apps/build/localize-your-app#source-
files)Source files

The following example shows a hard-coded `greeting` string from an app:

## Hard-coded string

Copy

9

1

2

3

function greeting(casual_name) {

return `Hello ${casual_name}`;

}

The following example shows how to externalize the hard-coded `greeting`
string in a translation file:

## translations/en.json

Copy

9

1

2

3

{

"greeting": "Hello {casual_name}"

}

## Looking up externalized string

Copy

9

1

2

3

function greeting(casual_name) {

return i18n.translate("greeting", { casual_name: casual_name });

}

Tip

Even if you don't intend to initially translate your app, you should still
externalize strings in your app during initial development. It can be
difficult to externalize strings in an existing app that wasn't originally
structured with externalized strings.

####

[Anchor to Graphics](/docs/apps/build/localize-your-app#graphics)Graphics

Text within graphics and images should also be externalized for translation.

Instead of having flat graphics that include text, externalize the text and
overlay it on the graphic. Alternatively, you can generate flat graphics for
each locale, and switch between them based on the requested locale.

###

[Anchor to Step 2: Get access to the user's locale](/docs/apps/build/localize-
your-app#step-2-get-access-to-the-users-locale)Step 2: Get access to the
user's locale

Depending on the audience, the lookup of a translation string uses the
preferred locale of either an app user or a buyer.

The mechanism for receiving the locale depends on the type of app or app
extension being developed.

For example, embedded apps receive the app user's chosen locale in the
`locale` request parameter in Shopify's `GET` requests to the app.

Refer to the documentation for your [type of app
extension](/docs/apps/build/app-extensions/list-of-app-extensions) for more
information.

###

[Anchor to Step 3: Format strings](/docs/apps/build/localize-your-
app#step-3-format-strings)Step 3: Format strings

Beyond language translation, parts of your app's strings should adapt
dynamically to different locales.

For example, dates and times, names, numbers, prices, and lists are elements
that should be formatted differently based not on language, but on the user's
region or preferences.

Remove these elements from your app's strings, use a localization library to
generate the formatted versions, and inject the formatted versions dynamically
using string interpolation. The following sections describe how to format the
following parts of strings:

  * Dates and times
  * Numbers
  * Prices
  * Lists
  * Names

####

[Anchor to Format dates and times](/docs/apps/build/localize-your-app#format-
dates-and-times)Format dates and times

The format of dates and times varies by region, not by language. As a result,
dates and times, such as the following examples, don't belong in translation
strings:

Locale| Formatted datetime  
---|---  
`en-US`| `12/19/2020, 10:23 PM`  
`en-GB`| `19/12/2020, 22:23`  
`en-CA`| `2020-12-19, 10:23 p.m.`  
  
Use an API or library to format dates and times. For example, you can use
[`Intl.DateTimeFormat`](https://developer.mozilla.org/en-
US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat) and
inject the formatted dates and times into your translations using string
interpolation:

## Non-localized en.json

Copy

9

1

2

3

{

"last_sale_day": "All orders must be placed by 2022-10-30"

}

## Localized en.json

Copy

9

1

2

3

{

"last_sale_day": "All orders must be placed by {date}" // 2022-10-30,
10/30/2022, 30/10/2022

}

####

[Anchor to Format numbers](/docs/apps/build/localize-your-app#format-
numbers)Format numbers

The format of numbers varies by region, not by language. As a result, numbers,
such as the following examples, don't belong in translation strings:

Locale| Formatted number  
---|---  
`en-US`| `123,000`  
`en-NL`| `123.000`  
`en-IN`| `1,23,000`  
  
Use an API or library to format numbers. For example, you can use
[`Intl.NumberFormat`](https://developer.mozilla.org/en-
US/docs/Web/JavaScript/Reference/Global_Objects/Intl/NumberFormat) and inject
the formatted numbers into your translations using string interpolation:

## Non-localized en.json

Copy

9

1

2

3

{

"congrats": "Congratulations on 100,000 orders"

}

## Localized en.json

Copy

9

1

2

3

{

"congrats": "Congratulations on {formatted_number} orders" // 100,000,
100.000, 1,00,000

}

Note

If the number is a variable, then you should also make use of pluralization
features to make sure that the correct grammar can be used for each number.

####

[Anchor to Format prices](/docs/apps/build/localize-your-app#format-
prices)Format prices

The format of prices varies by currency and region, not by language. As a
result, prices, such as the following examples, don't belong in translation
strings:

Locale| Currency| Formatted price  
---|---|---  
`en-US`| `USD`| `$123,456.00`  
`en-CH`| `USD`| `US$ 123’456.00`  
`en-IN`| `USD`| `$1,23,456.00`  
  
Use an API or library to format prices. For example, you can use
[`Intl.NumberFormat`](https://developer.mozilla.org/en-
US/docs/Web/JavaScript/Reference/Global_Objects/Intl/NumberFormat) and inject
the formatted prices into your translations using string interpolation:

## Non-localized en.json

Copy

9

1

2

3

{

"order_total": "Your total order is ${price}"

}

## Localized en.json

Copy

9

1

2

3

{

"order_total": "Your total order is {formatted_price}", // $15.50, USD 15.5,
15,50 $US

}

####

[Anchor to Format lists](/docs/apps/build/localize-your-app#format-
lists)Format lists

The way that items are combined into lists varies by region, not by language.
As a result, lists, such as the following examples, don't belong in
translation strings:

Locale| Formatted list  
---|---  
`en-US`| `User, Product, or Variant`  
`en-GB`| `User, Product or Variant`  
  
Use an API or library to format lists of items. For example, you can use
[`Intl.ListFormat`](https://developer.mozilla.org/en-
US/docs/Web/JavaScript/Reference/Global_Objects/Intl/ListFormat) and inject
the formatted lists into your translations using string interpolation:

## en.json

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

"prompt": "Please select one of: {nouns}",

"nouns": {

"user": "User",

"product": "Product",

"variant": "Variant",

...

}

}

## File

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

function selection_prompt() {

nouns = fetch_nouns().map(function (noun) {

return i18n.translate(`nouns.${noun}`);

});

return i18n.translate("prompt", {

nouns: new Intl.ListFormat(locale, {

style: "long",

type: "disjunction",

}).format(nouns),

});

}

####

[Anchor to Format names](/docs/apps/build/localize-your-app#format-
names)Format names

The way that you address a person varies by context and region.

For example, for a person with the given name "Quinn" and surname "Ishida"
might be addressed in the following ways:

Locale| Formatted full name| Formatted casual name  
---|---|---  
`en-US`| `Quinn Ishida`| `Quinn`  
`en-JP`| `IshidaQuinn-sama`| `Ishida-sama`  
  
Don't encode the name formatting conventions of North American English.
Instead, use an API or library to format a person's name based on the context,
and inject the formatted name into your translations using string
interpolation:

## Non-localized en.json

Copy

9

1

2

3

4

{

"greeting": "Hello {first_name} {last_name}",

"casual_greeting": "Hey {first_name}!"

}

## Localized en.json

Copy

9

1

2

3

4

{

"greeting": "Hello {full_name}", // Quinn Ishida, IshidaQuinn-sama

"casual_greeting": "Hey {casual_name}!" // Quinn, Ishida-sama

}

###

[Anchor to Example prompt](/docs/apps/build/localize-your-app#example-
prompt)Example prompt

LLMs can significantly streamline internationalization efforts by
automatically handling many of the steps described above. Here's a sample
prompt to help you get started:

## example-externalize-strings

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

You are an expert software developer, specializing in software localization,
specifically for Shopify Apps. You possess a deep understanding of
localization tooling and how to build software to work across languages and
locales. I have a Shopify app that needs to be localized. It currently has no
localization middleware installed and all UIs have hardcoded english strings.

  

Your primary goal is to localize this app so that it can work seamlessly for
users in different languages and regions. Approach this translation as an
expert software developer would, following these steps:

  

1\. Install the i18n-next localization middleware

2\. Extract hardcoded strings from all UIs to public/locales/en.json. Don't
translate them into any other languages yet. Give each hardcoded string an
descriptive key.

3\. Localize the display of numbers. For example, 1,000 in English is written
as 1.000 in Spanish. Extract them from UIs and apply the intlNumber method for
that.

4\. Localize any displays of currency using the i18n-next library.

5\. Localize dates using the i18n-next helpers, so we get the correct dates in
every language. For example, Spanish uses DD/MM/YYY and US English uses
MM/DD/YYY.

6\. Configure this app to use the value of the 'locale' request parameter as
the current user's preferred locale.

  

As you make changes, log actions to a file called 'i18nupdates.md' that
includes one row for each file updated with internationalized strings. Include
the folder, filename and the count of strings internationalized.

###

[Anchor to Step 4: Translate strings](/docs/apps/build/localize-your-
app#step-4-translate-strings)Step 4: Translate strings

Translating strings involves accounting for text expansion in different
languages, and providing your source strings to someone that can translate the
content.

####

[Anchor to Step 4.1: Use pseudolocalization
(Optional)](/docs/apps/build/localize-your-app#step-41-use-pseudolocalization-
optional)Step 4.1: Use pseudolocalization (Optional)

When interfaces are localized, the content often expands in length. In most
languages, text is up to 50% longer on average than English. Some non-Latin
languages, such as Japanese, take up more vertical space. For character-based
languages, text wrapping and line breaking can’t always rely on spaces to
separate words. Your interface needs to be flexible enough to accommodate
language formatting and text expansion without changing its context of use.

The [Polaris i18n
documentation](https://polaris.shopify.com/foundations/internationalization)
has more information about, and examples of, text expansion issues.

You can use pseudolocalization tools
([example](https://github.com/Shopify/pseudolocalization)) to simulate text
expansion before translation is completed. This enables you to test your app's
UI for common text expansion issues. For example, you might want to test for
overflowing strings or word wrapping.

####

[Anchor to Step 4.2: Choose the languages to translate
into](/docs/apps/build/localize-your-app#step-42-choose-the-languages-to-
translate-into)Step 4.2: Choose the languages to translate into

The Shopify admin can be used in any of the [supported
languages](https://help.shopify.com/en/manual/your-account/languages).

Shopify also translates some buyer-facing strings (first-party themes,
checkout, and system messages) into additional languages (for example, refer
to the [language list in the Dawn
theme](https://github.com/Shopify/dawn/blob/0ea3e2780876ff81d599bffac5f6c790dac567b0/translation.yml#LL2)).

When deciding on which languages to translate into, consider starting with
those most common in the regions or markets that your app supports.

####

[Anchor to Step 4.3: Translate content](/docs/apps/build/localize-your-
app#step-43-translate-content)Step 4.3: Translate content

Translating content involves providing your source strings to someone that can
translate the content into each language.

Note

Because you'll need to make changes to translations as you develop new
features, you should expect the relationship with the provider of your
translations to be a continuous partnership.

There are several options for getting translations. The options vary on cost,
turn-around time, and quality.

#####

[Anchor to Third party translation service](/docs/apps/build/localize-your-
app#third-party-translation-service)Third party translation service

The highest quality, but often most costly, option is to engage a third party
translation service to manage the work of providing translations for your app.

Translation providers manage the relationships with the translators so that
you can have confidence in the quality and turnaround time of the
translations.

Shopify recommends using one of the following translation providers:

  * [Blend](https://www.getblend.com/)
  * [Crowdin](https://crowdin.com/)
  * [TranslateCI](https://translateci.com/)

#####

[Anchor to Machine translation](/docs/apps/build/localize-your-app#machine-
translation)Machine translation

Machine translation, such as [Google Translate](https://translate.google.com),
is artificial intelligence software that can generate translations on-demand.

Machine translation can be quick and cost-effective, but the quality of the
translations can vary because strings are often translated without context
about your app or business.

#####

[Anchor to Crowdsourced translation](/docs/apps/build/localize-your-
app#crowdsourced-translation)Crowdsourced translation

If your app already has a large community, then sometimes community members
are willing to contribute translations.

This method relies on managing and engaging your app's community in an ongoing
manner, which can be time-consuming. Depending on the diversity of your
community, it might be difficult to find enough people with fluency in the
languages that you're translating your content into.

#####

[Anchor to Do it yourself](/docs/apps/build/localize-your-app#do-it-
yourself)Do it yourself

If you or an acquaintance knows another language, then translations for that
language can be manually provided.

###

[Anchor to Next steps](/docs/apps/build/localize-your-app#next-steps)Next
steps

  * Promote your app to a global audience by [writing](/docs/apps/launch/app-requirements-checklist#writing-a-shopify-app-store-listing) and [translating](/docs/apps/launch/app-requirements-checklist#translate-your-app-listing) an app listing.

* * *

Was this page helpful?

YesNo

  * [Why internationalize your app?](/docs/apps/build/localize-your-app#why-internationalize-your-app)
  * [Internationalize your app](/docs/apps/build/localize-your-app#internationalize-your-app)

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

