# Source: https://shopify.dev/docs/storefronts/themes/tools/liquid-doc

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

  * [Why use LiquidDoc?](/docs/storefronts/themes/tools/liquid-doc#why-use-liquiddoc)
  * [Syntax reference](/docs/storefronts/themes/tools/liquid-doc#syntax-reference)
  * [Editor features](/docs/storefronts/themes/tools/liquid-doc#editor-features)
  * [Next steps](/docs/storefronts/themes/tools/liquid-doc#next-steps)

# LiquidDoc

Copy page MD

LiquidDoc gives you a way to create a structured interface for Liquid snippets
and blocks, allowing you to specify input parameters, add descriptions, and
provide usage examples. These details are exposed through theme checks, code
completions, and hover information, making development faster and more
reliable.

* * *

##

[Anchor to Why use LiquidDoc?](/docs/storefronts/themes/tools/liquid-doc#why-
use-liquiddoc)Why use LiquidDoc?

It can be easy to make a small mistake when writing Liquid code:

  * Missing required parameters don't trigger warnings

  * Unrecognized parameters pass through silently

  * No type checking ensures values match expected formats

  * Parameter discovery requires reading the code

For example, these misspelled parameters won't trigger errors:

## sections/broken-section.liquid

Copy

9

1

{% render 'loading-spinner', produt: product, show_vendorr: true %}

LiquidDoc solves these problems by providing structured documentation that
development tools can recognize, offering real-time feedback during
development.

* * *

##

[Anchor to Syntax reference](/docs/storefronts/themes/tools/liquid-doc#syntax-
reference)Syntax reference

LiquidDoc uses a JSDoc-inspired syntax to document snippets and blocks. The
following tags are supported:

  * @description \- explains the purpose
  * @param \- documents expected parameters
  * @example \- shows usage examples

###

[Anchor to Basic structure](/docs/storefronts/themes/tools/liquid-doc#basic-
structure)Basic structure

Place LiquidDoc content at the top of a snippet or a block file inside a `doc`
tag:

## snippets/example-snippet.liquid

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

{% doc %}

Provides an example of a snippet description.

  

@param {string} title - The title to display

@param {number} [max_items] - Optional maximum number of items to show

  

@example

{% render 'example-snippet', title: 'Featured Products', max_items: 3 %}

{% enddoc %}

###

[Anchor to Descriptions (,[object
Object],)](/docs/storefronts/themes/tools/liquid-doc#descriptions-
description)Descriptions (`@description`)

You can document your snippet's or block's purpose in two ways:

## snippets/example-snippet.liquid

Copy

9

1

2

3

4

5

{% doc %}

The description can be placed before any @ annotations without needing a tag.

  

@description You can also use this tag to place a description anywhere.

{% enddoc %}

####

[Anchor to Usage notes](/docs/storefronts/themes/tools/liquid-doc#usage-
notes)Usage notes

  * You can omit the `@description` tag by providing a description before any `@` annotations.
  * If you provide multiple descriptions, then only the first one will appear when hovering over a render tag.
  * Multi-line descriptions are automatically formatted to start on a new line.

###

[Anchor to Parameters (,[object
Object],)](/docs/storefronts/themes/tools/liquid-doc#parameters-
param)Parameters (`@param`)

Parameters define the inputs accepted by a snippet or a static block with the
following format:

`@param {type} name - description`

Component| Required| Description  
---|---|---  
**Type**|  Optional| A data type in curly braces `{}`. Must be one of the
supported types.  
**Name**|  Required| A parameter identifier. For optional parameters, wrap in
`[]`. For example, `[max_items]`.  
**Description**|  Optional| An explanation of the parameter's purpose.  
  
The following example shows how to use parameters:

## snippets/param-examples.liquid

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

{% doc %}

Product card snippet

  

@param {string} title - Main product title

@param {number} price - Product price value

@param {boolean} show_vendor - Whether to display vendor name

@param {object} product - Product object

@param {string} [subtitle] - Optional secondary text

{% enddoc %}

####

[Anchor to Supported parameter types](/docs/storefronts/themes/tools/liquid-
doc#supported-parameter-types)Supported parameter types

Type| Description  
---|---  
`string`| Text values  
`number`| Numeric values  
`boolean`| True/false values. All values in Liquid have truthy or falsy
evaluation.  
`object`| Complex Liquid types or anything that's not a primitive  
  
###

[Anchor to Examples (,[object
Object],)](/docs/storefronts/themes/tools/liquid-doc#examples-example)Examples
(`@example`)

Examples demonstrate how a snippet or a static block should be used:

## snippets/example-snippet.liquid

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

{% doc %}

Price display snippet

  

@param {number} price - Price value

@param {boolean} [show_compare_at] - Whether to show compare-at price

  

@example

{% render 'price', price: product.price, show_compare_at: true %}

  

@example

{% render 'price',

price: variant.price,

show_compare_at: false

%}

{% enddoc %}

####

[Anchor to Usage notes](/docs/storefronts/themes/tools/liquid-doc#usage-
notes)Usage notes

  * Multiple examples help demonstrate different usage patterns.
  * Multi-line examples are automatically formatted to start on a new line.

* * *

##

[Anchor to Editor features](/docs/storefronts/themes/tools/liquid-doc#editor-
features)Editor features

LiquidDoc speeds up development while catching parameter errors, typos, and
type mismatches in real-time.

###

[Anchor to Hover documentation](/docs/storefronts/themes/tools/liquid-
doc#hover-documentation)Hover documentation

See comprehensive information when hovering over a name in a render tag:

![Hovering over 'product-card' to see LiquidDoc
documentation](https://cdn.shopify.com/shopifycloud/shopify-
dev/production/assets/assets/images/themes/liquid-doc/hover-jU4oseCi.gif)

###

[Anchor to Code completion](/docs/storefronts/themes/tools/liquid-doc#code-
completion)Code completion

Get smart suggestions for parameter names when using documented snippets or
static blocks:

![Code completion showing available LiquidDoc
snippets](https://cdn.shopify.com/shopifycloud/shopify-
dev/production/assets/assets/images/themes/liquid-doc/completion-DBdYxY6A.gif)

###

[Anchor to Parameter validation](/docs/storefronts/themes/tools/liquid-
doc#parameter-validation)Parameter validation

Receive warnings when required parameters are missing:

![Parameter validation showing required parameters for a
snippet](https://cdn.shopify.com/shopifycloud/shopify-
dev/production/assets/assets/images/themes/liquid-doc/param-check-
_bna6YbN.gif)

###

[Anchor to Type checking](/docs/storefronts/themes/tools/liquid-doc#type-
checking)Type checking

Get appropriate suggestions and validation based on type annotations in
`@param` tags.

![Type checking showing proper value types for
parameters](https://cdn.shopify.com/shopifycloud/shopify-
dev/production/assets/assets/images/themes/liquid-doc/type-check-C57Q9wYS.gif)

When a type mismatch is detected, the editor suggests converting to these
fallback values:

Type| Fallback value  
---|---  
`string`| `''`  
`number`| `0`  
`boolean`| `false`  
`object`| `N/A`  
  
###

[Anchor to Theme Check](/docs/storefronts/themes/tools/liquid-doc#theme-
check)Theme Check

LiquidDoc integrates with [Theme Check](/docs/storefronts/themes/tools/theme-
check) to validate your snippets and blocks through:

  * **Documentation checks** \- Validate syntax and structure inside `{% doc %}` blocks
  * **Usage checks** \- Ensure `{% render %}` tags properly use documented parameters

####

[Anchor to Documentation checks](/docs/storefronts/themes/tools/liquid-
doc#documentation-checks)Documentation checks

Check| Description  
---|---  
[UniqueDocParamNames](/docs/storefronts/themes/tools/theme-
check/checks/unique-doc-param-names)| Each parameter defined in LiquidDoc
needs to have a unique name.  
[UnsupportedDocTag](/docs/storefronts/themes/tools/theme-
check/checks/unsupported-doc-tag)| The `doc` tag can only be used within a
liquid snippet file.  
[ValidDocParamTypes](/docs/storefronts/themes/tools/theme-check/checks/valid-
doc-param-types)| Each parameter defined in LiquidDoc should be `string`,
`number`, `boolean`, `object`, or any [liquid
object](https://shopify.dev/docs/api/liquid/objects) that isn't exclusively a
global object.  
[UnusedDocParam](/docs/storefronts/themes/tools/theme-check/checks/unused-doc-
param)| The parameters defined within the `doc` tag must be used within the
scope of the variable.  
  
####

[Anchor to Usage checks](/docs/storefronts/themes/tools/liquid-doc#usage-
checks)Usage checks

Check| Description  
---|---  
[DuplicateContentForArguments](/docs/storefronts/themes/tools/theme-
check/checks/duplicate-content-for-arguments)| Each named argument should be
passed into the `content_for` tag only once.  
[DuplicateRenderSnippetArguments](/docs/storefronts/themes/tools/theme-
check/checks/duplicate-render-snippet-arguments)| Each named argument should
be passed into the `render` tag only once.  
[MissingContentForArguments](/docs/storefronts/themes/tools/theme-
check/checks/missing-content-for-arguments)| When you render a static block,
you must provide all required arguments defined in that block file's
LiquidDoc.  
[MissingRenderSnippetArguments](/docs/storefronts/themes/tools/theme-
check/checks/missing-render-snippet-arguments)| When you render a snippet, you
must provide all required arguments defined in that snippet file's LiquidDoc.  
[UnrecognizedContentForArguments](/docs/storefronts/themes/tools/theme-
check/checks/unrecognized-content-for-arguments)| All arguments provided when
rendering a static block must match the arguments defined in that block's
LiquidDoc.  
[UnrecognizedRenderSnippetArguments](/docs/storefronts/themes/tools/theme-
check/checks/unrecognized-render-snippet-arguments)| All arguments provided
when rendering a snippet must match the arguments defined in that snippet's
LiquidDoc.  
[ValidContentForArgumentTypes](/docs/storefronts/themes/tools/theme-
check/checks/valid-content-for-argument-types)| All arguments provided when
rendering a static block must match the respective parameter's type defined in
that block's LiquidDoc.  
[ValidRenderSnippetArgumentTypes](/docs/storefronts/themes/tools/theme-
check/checks/valid-render-snippet-argument-types)| All arguments provided when
rendering a snippet must match the respective parameter's type defined in that
snippet's LiquidDoc.  
  
###

[Anchor to Limitations](/docs/storefronts/themes/tools/liquid-
doc#limitations)Limitations

####

[Anchor to Dynamic validation](/docs/storefronts/themes/tools/liquid-
doc#dynamic-validation)Dynamic validation

Usage checks are disabled when the name is a variable:

#####

[Anchor to ✗ Disabled](/docs/storefronts/themes/tools/liquid-doc#-disabled)✗
Disabled

## section-example.liquid

Copy

9

1

2

{% assign snippetName = 'price' %}

{% render snippetName %}

#####

[Anchor to ✓ Enabled](/docs/storefronts/themes/tools/liquid-doc#-enabled)✓
Enabled

## section-example.liquid

Copy

9

1

{% render 'price' %}

####

[Anchor to Dynamic type validation](/docs/storefronts/themes/tools/liquid-
doc#dynamic-type-validation)Dynamic type validation

We don't currently validate the types of objects or variables passed as
parameters:

#####

[Anchor to ✗ Disabled](/docs/storefronts/themes/tools/liquid-doc#-disabled)✗
Disabled

## section-example.liquid

Copy

9

1

{% render 'price', price: product.price %}

#####

[Anchor to ✓ Enabled](/docs/storefronts/themes/tools/liquid-doc#-enabled)✓
Enabled

## section-example.liquid

Copy

9

1

{% render 'price', price: 100 %}

* * *

##

[Anchor to Next steps](/docs/storefronts/themes/tools/liquid-doc#next-
steps)Next steps

  * [Learn more about Liquid syntax](/docs/api/liquid).
  * [Explore theme development best practices](/docs/storefronts/themes/best-practices).

* * *

Was this page helpful?

YesNo

  * [Why use LiquidDoc?](/docs/storefronts/themes/tools/liquid-doc#why-use-liquiddoc)
  * [Syntax reference](/docs/storefronts/themes/tools/liquid-doc#syntax-reference)
  * [Editor features](/docs/storefronts/themes/tools/liquid-doc#editor-features)
  * [Next steps](/docs/storefronts/themes/tools/liquid-doc#next-steps)

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

