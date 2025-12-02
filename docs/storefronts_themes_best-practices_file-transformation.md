# Source: https://shopify.dev/docs/storefronts/themes/best-practices/file-transformation

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

  * [Compiled code and merchant or app customizations](/docs/storefronts/themes/best-practices/file-transformation#compiled-code-and-merchant-or-app-customizations)
  * [Just-in-time file transformations](/docs/storefronts/themes/best-practices/file-transformation#just-in-time-file-transformations)

# File transformation best practices for Shopify themes

Copy page MD

File transformations improve the developer experience by letting you write and
maintain code using your preferred strategies and build tools, and ship
compiled code that is optimized for browser runtime.

For example, you might want to divide your stylesheets into multiple files,
each scoped to a particular UI element, which makes them easier to maintain.
However, loading a large number of small stylesheets is slower than loading
one or two larger stylesheets. You can use file transformations to automate
the process of combining these smaller, scoped stylesheets into fewer, larger
bundles.

You can transform files as part of a build process, and then upload your
compiled code as a theme that can be accessed in the Shopify admin.

Below are some examples of file transformations that theme developers might
want to perform:

File transformation| Benefit  
---|---  
Custom file structure > Shopify theme file structure| Code maintenance
flexibility  
SCSS > CSS| Write in SCSS, output Shopify-compatible CSS  
SVG > snippet| Include SVGs inline in HTML  
[PostCSS](https://github.com/postcss/postcss) transformations (e.g.
Autoprefixer, cssnano, tailwindcss)| Linting, variables, transpiling, browser
compatibility  
Section folders > section files| Build sections in separate Liquid, JS, CSS,
and JSON files  
Automated calculation and inlining of critical styles| Avoid load-blocking CSS
resources  
Optimized JavaScript bundles| Reduced load times, smaller file sizes  
JavaScript, CSS, and HTML minification| Reduced load times, smaller file sizes  
  
If you want to perform transformations on your files, then you need to decide
how you want to manage both the source code and the transformed, or compiled,
code. To learn about the options, and which options can be used with Shopify
tools, refer to [Version control best practices for Shopify
themes](/docs/storefronts/themes/best-practices/version-control).

You can also consider using just-in-time (JIT) file transformations to reduce
the need to track changes to compiled code. JIT transformations can deliver
optimized dependencies and resources at runtime, allowing for a unified code
base that doesn't need to be backfilled.

* * *

##

[Anchor to Compiled code and merchant or app
customizations](/docs/storefronts/themes/best-practices/file-
transformation#compiled-code-and-merchant-or-app-customizations)Compiled code
and merchant or app customizations

After a theme is uploaded to Shopify, merchants can customize it using the
[theme editor](/docs/storefronts/themes/tools/online-editor) or the [code
editor](/docs/storefronts/themes/tools/code-editor). [Apps](/docs/apps/build)
might also change the theme code through the `Asset` [REST Admin API
resource](/docs/apps/build/online-store/asset-legacy). This can lead to
situations where compiled code has been altered, but source code hasn't been
updated.

You might need to identify changes to the compiled code, and then manually
backfill those changes into your source code so the changes persist the next
time the code is compiled. This is a particular risk if you are a Partner or
merchant developer who performs ongoing customizations to a merchant's theme.
You should consider the impact of merchant or app customizations when planning
your file transformation and [version control](/docs/storefronts/themes/best-
practices/version-control) strategy.

Tip

If you perform file transformations using Just-in-time services, then you
don't need to backfill changes.

###

[Anchor to Backfilling changes to compiled
code](/docs/storefronts/themes/best-practices/file-transformation#backfilling-
changes-to-compiled-code)Backfilling changes to compiled code

When a change is made to a compiled file and the theme is [connected to
GitHub](/docs/storefronts/themes/tools/github), then the change is added to
the theme's GitHub repo as a commit. You can use this commit to identify and
backfill merchant changes.

The following is an example of identifying and backfilling a change to a theme
that's connected to version control using [the Shopify GitHub
integration](/docs/storefronts/themes/tools/github).

####

[Anchor to Step 1: The developer writes source code and compiles
it](/docs/storefronts/themes/best-practices/file-transformation#step-1-the-
developer-writes-source-code-and-compiles-it)Step 1: The developer writes
source code and compiles it

You create the following scoped JavaScript resources for a theme.

## /assets/scopeA.js

Copy

9

1

export console.log('ScopeA JS is running!');

## /assets/scopeB.js

Copy

9

1

export console.log('ScopeB JS is running!');

## /assets/index.js

Copy

9

1

2

import './scopeA.js'

import './scopeB.js'

These three files are bundled for optimized delivery, resulting in the
following file:

## /assets/index.bundle.js

Copy

9

1

2

console.log('ScopeA JS is running!');

console.log('ScopeB JS is running!');

These files are all committed to the GitHub repo, and then `index.bundle.js`
is synced with the store using [the Shopify GitHub
integration](/docs/storefronts/themes/tools/github).

`index.bundle.js` is called inside of a Liquid template:

## templates/index.liquid

Copy

9

1

<script src="{{ 'index.bundle.js' | asset_url }}"></script>

This store or theme is handed off to the merchant.

####

[Anchor to Step 2: The merchant edits compiled
code](/docs/storefronts/themes/best-practices/file-transformation#step-2-the-
merchant-edits-compiled-code)Step 2: The merchant edits compiled code

When the merchant starts using the theme, they need to make a change to the
compiled JS bundle using the code editor in the Shopify admin:

## assets/index.bundle.js

Copy

9

1

2

3

console.log('ScopeA JS is running!');

console.log('ScopeB JS is running!');

+ console.log('ScopeB is way cooler than ScopeA');

This change is synced to the theme's associated GitHub repo as a commit.

####

[Anchor to Step 3: The developer identifies changes to compiled code and
backfills them](/docs/storefronts/themes/best-practices/file-
transformation#step-3-the-developer-identifies-changes-to-compiled-code-and-
backfills-them)Step 3: The developer identifies changes to compiled code and
backfills them

When the merchant contacts you to add another feature to your theme, you can
see the commit from the Shopify admin in the repo.

Because the change was made to the compiled `index.bundle.js`, this change
will disappear when the file is recompiled, unless a corresponding change is
made to the source files.

To make sure changes made to compiled code persist after the code is
recompiled, you can manually backport the change into the source code. In this
case, you can modify `index.js`:

## assets/index.js

Copy

9

1

2

3

import './scopeA.js'

import './scopeB.js'

+ console.log('ScopeB is way cooler than ScopeA');

* * *

##

[Anchor to Just-in-time file transformations](/docs/storefronts/themes/best-
practices/file-transformation#just-in-time-file-transformations)Just-in-time
file transformations

Many transformations are one-way: you can transform source code into compiled
code, but you can't transform compiled code into source code. Most code
management strategies for Shopify themes involve tracking changes to compiled
code and backfilling source code. This is because the code a merchant sees is
often the result of a file transformation, and a merchant might edit the code
or install code-injecting apps as a part of running a store.

You can use just-in-time (JIT) file transformations for some of your common
file transformation tasks. JIT transformations move the functionality of
installed developer tools to on-demand services that can generate an optimized
runtime file from source code.

When you remove the need to perform certain types of file transformations, you
can further reduce or even eliminate the number of compiled files that you
need to create, track and maintain. Merchants can edit source code rather than
compiled code, allowing for a unified code base that doesn't need to be
backfilled.

Common uses for JIT transformations include JavaScript minification, CSS
optimization and minification, and third-party dependency management.

###

[Anchor to Advantages](/docs/storefronts/themes/best-practices/file-
transformation#advantages)Advantages

  * This method is compatible with the [Shopify GitHub integration](/docs/storefronts/themes/tools/github).
  * Maintenance is performed by service owners.
  * This method works within Shopify's supported [theme file structure](/docs/storefronts/themes/architecture).
  * Merchants can work on source files, resulting in reduced backfilling.

###

[Anchor to Shopify minification](/docs/storefronts/themes/best-practices/file-
transformation#shopify-minification)Shopify minification

Shopify automatically minifies CSS and JavaScript files. For instance, you can
include a CSS file such as `main.css` in your asset folder. Shopify compiles
and sends a minified version of it, which updates every time the source file
changes.

* * *

Was this page helpful?

YesNo

  * [Compiled code and merchant or app customizations](/docs/storefronts/themes/best-practices/file-transformation#compiled-code-and-merchant-or-app-customizations)
  * [Just-in-time file transformations](/docs/storefronts/themes/best-practices/file-transformation#just-in-time-file-transformations)

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

