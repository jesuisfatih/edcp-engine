# Source: https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/unique-doc-param-names

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

    * [Overview](/docs/storefronts/themes)
    * Quick start

  * ### Key concepts

    * [Architecture](/docs/storefronts/themes/architecture)
    * Layouts

    * Templates

    * Sections

    * Section groups

    * Blocks

    * [Snippets](/docs/storefronts/themes/architecture/snippets)
    * Settings

    * Config

    * Locales

  * ### Best practices

    * [Overview](/docs/storefronts/themes/best-practices)
    * [Sections and blocks](/docs/storefronts/themes/best-practices/templates-sections-blocks)
    * [JavaScript and stylesheet tags](/docs/storefronts/themes/best-practices/javascript-and-stylesheet-tags)
    * Performance

    * [Accessibility](/docs/storefronts/themes/best-practices/accessibility)
    * Theme editor

    * Design

    * [Merchant stores](/docs/storefronts/themes/best-practices/merchant-stores)
    * [Version control](/docs/storefronts/themes/best-practices/version-control)
    * [File transformation](/docs/storefronts/themes/best-practices/file-transformation)
    * [Deceptive code](/docs/storefronts/themes/best-practices/deceptive-code)
  * ### Developer Tools

    * [Overview](/docs/storefronts/themes/tools)
    * CLI

    * [GitHub integration](/docs/storefronts/themes/tools/github)
    * [VS Code extension](/docs/storefronts/themes/tools/shopify-liquid-vscode)
    * [Prettier plugin](/docs/storefronts/themes/tools/liquid-prettier-plugin)
    * [LiquidDoc](/docs/storefronts/themes/tools/liquid-doc)
    * Theme Check

    * [Theme editor](/docs/storefronts/themes/tools/online-editor)
    * [Code editor](/docs/storefronts/themes/tools/code-editor)
    * [Theme Access app](/docs/storefronts/themes/tools/theme-access)
    * Development stores

    * [Collaborator accounts](/docs/storefronts/themes/tools/collaborator-accounts)
    * Theme Inspector

    * [Lighthouse CI](/docs/storefronts/themes/tools/lighthouse-ci)
  * ### Theme features

    * [Overview](/docs/storefronts/themes/theme-features)
    * [Integrating apps](/docs/apps/online-store)
    * Product merchandising

    * Pricing and payments

    * Delivery and fulfillment

    * Customer engagement

    * Markets

    * Site navigation and search

    * SEO

    * Trust and security

    * Migrating to Online Store 2.

    * [Login redirects](/docs/storefronts/themes/login)
    * [Troubleshooting](/docs/storefronts/themes/troubleshooting)
  * ### Sell themes

    * Theme Store

Full index

ExpandOn this page

  * [Examples](/docs/storefronts/themes/tools/theme-check/checks/unique-doc-param-names#examples)
  * [Options](/docs/storefronts/themes/tools/theme-check/checks/unique-doc-param-names#options)
  * [Disabling this check](/docs/storefronts/themes/tools/theme-check/checks/unique-doc-param-names#disabling-this-check)

# UniqueDocParamNames

Copy page MD

Each parameter defined in [LiquidDoc](/docs/storefronts/themes/tools/liquid-
doc) needs to have a unique name.

* * *

##

[Anchor to Examples](/docs/storefronts/themes/tools/theme-check/checks/unique-
doc-param-names#examples)Examples

The following examples contain code snippets that either fail or pass this
check.

###

[Anchor to ✗ Fail](/docs/storefronts/themes/tools/theme-check/checks/unique-
doc-param-names#-fail)✗ Fail

In the following example, there are two parameters defined in LiquidDoc with
the same name:

Copy

9

1

2

3

4

{% doc %}

@param {string} some_input

@param {number} some_input

{% enddoc %}

###

[Anchor to ✓ Pass](/docs/storefronts/themes/tools/theme-check/checks/unique-
doc-param-names#-pass)✓ Pass

In the following example, all the parameters in LiquidDoc have different
names:

Copy

9

1

2

3

4

{% doc %}

@param {string} some_str

@param {number} some_num

{% enddoc %}

* * *

##

[Anchor to Options](/docs/storefronts/themes/tools/theme-check/checks/unique-
doc-param-names#options)Options

The following example contains the default configuration for this check:

Copy

9

1

2

3

UniqueDocParamNames:

enabled: true

severity: error

Parameter| Description  
---|---  
`enabled`| Whether this check is enabled.  
`severity`| The [severity](/docs/storefronts/themes/tools/theme-
check/configuration#check-severity) of the check.  
  
* * *

##

[Anchor to Disabling this check](/docs/storefronts/themes/tools/theme-
check/checks/unique-doc-param-names#disabling-this-check)Disabling this check

Disabling this check isn't recommended.

* * *

Was this page helpful?

YesNo

  * [Examples](/docs/storefronts/themes/tools/theme-check/checks/unique-doc-param-names#examples)
  * [Options](/docs/storefronts/themes/tools/theme-check/checks/unique-doc-param-names#options)
  * [Disabling this check](/docs/storefronts/themes/tools/theme-check/checks/unique-doc-param-names#disabling-this-check)

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

