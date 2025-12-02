# Source: https://shopify.dev/docs/storefronts/themes/tools/theme-check/configuration

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

# Theme Check configuration

Copy page MD

You can configure Theme Check to override default check options, enable or
disable specific checks, or point to your own custom checks. You can make
these changes using a config file, disable checks using comments, or
selectively run checks using command line flags. To learn more about theme
check command line flags, refer to [Theme Check
commands](/docs/storefronts/themes/tools/theme-check/commands).

* * *

##

[Anchor to Config file](/docs/storefronts/themes/tools/theme-
check/configuration#config-file)Config file

Add a `.theme-check.yml` file to the root of your theme to override check
defaults.

You can generate a new `.theme-check.yml` file using the command `shopify
theme check --init`.

You can adjust the following settings:

Setting| Type| Description  
---|---|---  
`root`| `string`| If your theme isn't using the standard theme directory
structure, you can provide root path for finding the `templates`, `sections`,
and `snippets` directories. For example, If you generate code from a `src`
directory, then you should point your Theme Check configuration at your
corresponding `dist` directory.  
`extends`| `string or string[]`| If you want to compose configuration files,
or start off the recommended one, you can use the `extends` setting to
reference a configuration file. Also supports the following magic settings:
`theme-check:all`, `theme-check:recommended`, `theme-check:theme-app-
extension`. When multiple configurations are extended; objects are deep
merged, arrays are concatenated, and the latest one in the list takes
priority.  
`require`| `string or string[]`| If you want to use a [custom or third party
set of checks](/docs/storefronts/themes/tools/theme-check#creating-your-own-
checks), then add a CommonJS import path.  
`ignore`| `string[]`| Exclude directories in the theme from Theme Check.  
Check settings| `object`| For each check, set `enabled` to `true` or `false`,
set the check severity, set specific `ignore` files and paths for the check,
and configure any other check options. If you created a custom check, then you
need to enable it using this method.  
You can view the default values of check options in the [checks
reference](/docs/storefronts/themes/tools/theme-check/checks).  
  
All settings are optional.

## .theme-check.yml

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

# The directory where theme folders are located (optional)

root: dist

  

# Configuration files are extensible

extends:

\- theme-check:recommended # or theme-check:all, theme-check:theme-app-
extension

\- '@acme/my-custom-checks/recommended.yml'

\- '../configs/.theme-check.yml'

  

# Paths to custom checks

require:

\- ./path/to/my_custom_check.js # path to file or module

\- '@acme/my-custom-checks' # for node_modules checks

  

# Paths to ignore (don't lint those!)

ignore:

\- 'node_modules/**'

\- 'snippets/*-icon.liquid' # minimatch globs are supported

  

# Disable a check

TemplateLength:

enabled: false

severity: warning

ignore:

\- templates/index.liquid

# Configure options for a check

max_length: 300

  

# Enable a custom check

MyCustomCheck:

enabled: true

severity: error

###

[Anchor to Check severity](/docs/storefronts/themes/tools/theme-
check/configuration#check-severity)Check severity

The check severity indicates the relative importance of a check to the
functionality and optimization of your theme. Severity levels include `error`,
`warning`, and `info`. You can change the severity of a check in your config
file.

If you're running theme check as a part of your CI process, the severity
levels of the failed checks can determine the exit code that you receive. By
default, Theme Check fails, or returns an exit code of 1, when one or more
issues with severity `error` are detected. You can configure the severity that
causes a run of theme check to fail using the [`--fail-
level`](/docs/storefronts/themes/tools/theme-check/commands) flag.

###

[Anchor to Disable checks using Liquid
comments](/docs/storefronts/themes/tools/theme-check/configuration#disable-
checks-using-liquid-comments)Disable checks using Liquid comments

You can disable all checks or specific checks using comments. You can disable
checks for a specific section of your theme code, or for an entire file.

Disable all checks for a section of code:

Copy

9

1

2

3

{% # theme-check-disable %}

{% assign x = 1 %}

{% # theme-check-enable %}

Disable all checks for the next line:

Copy

9

1

2

{% # theme-check-disable-next-line %}

{% assign x = 1 %}

Disable a specific check for a section of code:

Copy

9

1

2

3

{% # theme-check-disable UnusedAssign %}

{% assign x = 1 %}

{% # theme-check-enable UnusedAssign %}

Disable a specific check for the next line:

Copy

9

1

2

{% # theme-check-disable-next-line UnusedAssign %}

{% assign x = 1 %}

Disable multiple checks for a section of code by including checks in a comma-
separated list:

Copy

9

1

2

3

4

{% # theme-check-disable UnusedAssign, UndefinedObject %}

{% assign x = 1 %}

{% echo y %}

{% # theme-check-enable UnusedAssign, UndefinedObject %}

Disable multiple checks for the next line by including checks in a comma-
separated list:

Copy

9

1

2

{% # theme-check-disable-next-line UnusedAssign, UndefinedObject %}

{% assign x = y %}

Disable checks for the entire document by placing the comment on the first
line:

Copy

9

1

2

3

{% # theme-check-disable UnusedAssign %}

  

{% assign x = 1 %}

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

