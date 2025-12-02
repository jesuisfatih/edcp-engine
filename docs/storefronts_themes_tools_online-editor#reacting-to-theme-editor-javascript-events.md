# Source: https://shopify.dev/docs/storefronts/themes/tools/online-editor#reacting-to-theme-editor-javascript-events

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

  * [Accessing the theme editor through the Shopify admin](/docs/storefronts/themes/tools/online-editor#accessing-the-theme-editor-through-the-shopify-admin)
  * [Accessing the theme editor during development](/docs/storefronts/themes/tools/online-editor#accessing-the-theme-editor-during-development)
  * [Allowing for customization through the theme editor](/docs/storefronts/themes/tools/online-editor#allowing-for-customization-through-the-theme-editor)
  * [Live preview](/docs/storefronts/themes/tools/online-editor#live-preview)
  * [Integrating your theme with the theme editor](/docs/storefronts/themes/tools/online-editor#integrating-your-theme-with-the-theme-editor)

# The theme editor

Copy page MD

The [theme editor](https://shopify.com/admin/themes/current/editor) is a tool
that lets merchants customize the content and appearance of their store, and
preview changes to their theme in real time.

As a theme developer, you can allow merchants to customize their theme in the
theme editor by introducing settings, and by dividing your theme functionality
into [modular sections and blocks](/docs/storefronts/themes/best-
practices/templates-sections-blocks).

You need to integrate your theme with the theme editor to create a seamless
editing experience for merchants. In the theme editor preview, the merchant
should see exactly what will appear in the storefront when the theme is live.

![The theme editor in the Shopify
admin](https://cdn.shopify.com/shopifycloud/shopify-
dev/production/assets/assets/images/themes/theme_editor-fhUF7rbL.png)

* * *

##

[Anchor to Accessing the theme editor through the Shopify
admin](/docs/storefronts/themes/tools/online-editor#accessing-the-theme-
editor-through-the-shopify-admin)Accessing the theme editor through the
Shopify admin

Merchants can access the theme editor in the Shopify admin.

  1. From the Shopify admin, go to **Online Store** > **Themes**.
  2. Find the theme that you want to edit, and then click **Customize**.

* * *

##

[Anchor to Accessing the theme editor during
development](/docs/storefronts/themes/tools/online-editor#accessing-the-theme-
editor-during-development)Accessing the theme editor during development

To understand how your theme settings appear to merchants, you can preview
your theme in the theme editor. You can access the theme editor during
development by using the following methods:

  * Run your theme as a [development theme](/docs/storefronts/themes/tools/cli#development-themes) or [push your theme to a store](/docs/api/shopify-cli/theme/theme-push) using [Shopify CLI](/docs/api/shopify-cli/theme)
  * Connect a GitHub branch to your store using the [Shopify GitHub integration](/docs/storefronts/themes/tools/github)
  * Upload your theme as a ZIP to a Shopify store

You should choose the preview method that makes the most sense for your
current development process.

* * *

##

[Anchor to Allowing for customization through the theme
editor](/docs/storefronts/themes/tools/online-editor#allowing-for-
customization-through-the-theme-editor)Allowing for customization through the
theme editor

The settings that a merchant can access in the theme editor are controlled by
the theme. Settings can be specified in the following places:

  * The theme's [config/settings_schema.json](/docs/storefronts/themes/architecture/settings) file
  * The setting attributes for each [section](/docs/storefronts/themes/architecture/sections/section-schema#settings) that's included in the theme.

When a merchant configures these settings using the theme editor, their
configurations are saved. Learn more about [theme settings, and the types of
settings that you can add to your
theme](/docs/storefronts/themes/architecture/settings).

* * *

##

[Anchor to Live preview](/docs/storefronts/themes/tools/online-editor#live-
preview)Live preview

The theme editor can preview certain input settings as merchants interact with
them, instead of refreshing the entire storefront preview after the merchant
makes a selection.

The following input setting categories support live preview:

  * Color settings
  * Text settings

###

[Anchor to Color settings](/docs/storefronts/themes/tools/online-editor#color-
settings)Color settings

The theme editor can show a live preview of input settings that return a
[`color` object](/docs/api/liquid/objects/color), including
[color](/docs/storefronts/themes/architecture/settings/input-settings#color)
and [color_background](/docs/themes/architecture/settings/input-
settings#color_background).

To allow the theme editor to preview color setting changes live, reference the
setting in a `{% style %}` tag in a Liquid template, a section, or a snippet.
You can reference the `color` object directly, or the one of the following
properties of the object:

  * `red`
  * `green`
  * `blue`
  * `rgb`

####

[Anchor to Limitations](/docs/storefronts/themes/tools/online-
editor#limitations)Limitations

The theme editor can't provide a live preview for color settings in the
following cases:

  * **Filtered settings** : The theme editor can't provide a live preview for color settings that have Liquid filters applied. For example, `{{ settings.colors_accent_2.rgb | replace ' ', ',' }}` can't be previewed live.
  * **Stylesheets** : The theme editor can't provide a live preview for color settings that are referenced in stylesheets that are stored in the `/assets` directory of a theme. Instead, we recommend declaring a CSS variable in your `theme.liquid` layout file and referencing it in your theme's CSS files.

Refer to
[theme.liquid](https://github.com/Shopify/dawn/blob/d902375db0a71d5d2d6091eea242b71a42aa16ad/layout/theme.liquid#L67)
and
[base.css](https://github.com/Shopify/dawn/blob/d902375db0a71d5d2d6091eea242b71a42aa16ad/assets/base.css#L5)
in Dawn for an example implementation.

###

[Anchor to Text settings](/docs/storefronts/themes/tools/online-editor#text-
settings)Text settings

The theme editor can show a live preview of plain or rich text settings. This
includes the following settings:

  * [text](/docs/storefronts/themes/architecture/settings/input-settings#text)
  * [textarea](/docs/storefronts/themes/architecture/settings/input-settings#textarea)
  * [inline_richtext](/docs/themes/architecture/settings/input-settings#inline_richtext)
  * [richtext](/docs/storefronts/themes/architecture/settings/input-settings#richtext)

To allow the theme editor to preview text settings live, the code where the
setting is referenced must meet the following criteria:

  * The setting value must be the only child of its parent HTML element:

![do](https://cdn.shopify.com/shopifycloud/shopify-
dev/production/assets/assets/images/themes/templates-
tutorial/check-D2CvX7Jo.png)| 91<h1>{{ section.settings.title }}</h1>  
---|---  
![do](https://cdn.shopify.com/shopifycloud/shopify-
dev/production/assets/assets/images/themes/templates-
tutorial/check-D2CvX7Jo.png)| 91<h1><span className="icon">...</span> <span>{{
section.settings.title }}</span></h1>  
![don't](https://cdn.shopify.com/shopifycloud/shopify-
dev/production/assets/assets/images/themes/templates-tutorial/x-BmGlFLqe.png)|
91<h1><span className="icon">...</span> {{ section.settings.title }}</h1>  
  
  * There must be no Liquid filters applied to the setting value, other than the [`escape` filter](/docs/api/liquid/filters/escape):

![do](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/themes/templates-tutorial/check-D2CvX7Jo.png)| 91<h1>{{ section.settings.title | escape }}</h1>  
---|---  
![don't](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/themes/templates-tutorial/x-BmGlFLqe.png)| 91<h1>{{ section.settings.title | replace: ' ', '-' }}</h1>  
  
  * The setting must not be preceded by, followed by, or wrapped by other Liquid markup inside of the parent HTML element:

![do](https://cdn.shopify.com/shopifycloud/shopify-
dev/production/assets/assets/images/themes/templates-
tutorial/check-D2CvX7Jo.png)| 9123{%- when 'heading' -%} <h1>{{
block.settings.title }}</h1>{%- endwhen -%}  
---|---  
![don't](https://cdn.shopify.com/shopifycloud/shopify-
dev/production/assets/assets/images/themes/templates-tutorial/x-BmGlFLqe.png)|
91234<h1> {%- assign title = block.settings.title -%} {{ title }}</h1>  
![don't](https://cdn.shopify.com/shopifycloud/shopify-
dev/production/assets/assets/images/themes/templates-tutorial/x-BmGlFLqe.png)|
912345<h1> {%- when 'heading' -%} {{ block.settings.title }} {%- endwhen
-%}</h1>  
  
  * The element must not be hidden when the page loads:

![don't](https://cdn.shopify.com/shopifycloud/shopify-
dev/production/assets/assets/images/themes/templates-tutorial/x-BmGlFLqe.png)|
9123{%- unless block.settings.title == blank -%} <h1>{{ block.settings.title
}}</h1>{%- endunless -%}  
---|---  
  
* * *

##

[Anchor to Integrating your theme with the theme
editor](/docs/storefronts/themes/tools/online-editor#integrating-your-theme-
with-the-theme-editor)Integrating your theme with the theme editor

You need to make sure that your theme behaves in the editor the same way it
would in the storefront. In some cases, you need to adjust your theme's
behavior when it's being previewed in the theme editor to give merchants this
experience.

To make your theme context-aware, you need to integrate with the theme editor.

Integrating with the theme editor allows you to do the following:

  * Disable any code that should be run only when the theme is viewed by a customer
  * Enable or disable any code that should be run only when the theme is being edited
  * Make sure that any necessary code is run or cleaned up when a section is added, removed, customized, or moved

###

[Anchor to Detecting the theme editor](/docs/storefronts/themes/tools/online-
editor#detecting-the-theme-editor)Detecting the theme editor

Caution

You shouldn't use these methods to change the storefront preview that's
displayed in the theme editor. In most cases, the preview that merchants see
in the theme editor should match what their customers see on the live store.

A use case for this variable is to prevent theme editor session data from
being included in any page tracking scripts. Another use case is working with
a third-party API that returns and outputs any errors to the theme editor but
never to the live store.

####

[Anchor to Using Liquid](/docs/storefronts/themes/tools/online-editor#using-
liquid)Using Liquid

The
[`request.design_mode`](/docs/themes/liquid/reference/objects/request#request-
design_mode) global variable can be used in your theme's Liquid files to
detect whether the storefront is being viewed in the theme editor. The value
of the variable is set to `true` when viewing the theme editor. Otherwise,
it's set to `false`.

Copy

9

1

2

3

{% if request.design_mode %}

<!-- This will only render in the theme editor -->

{% endif %}

####

[Anchor to Using JavaScript](/docs/storefronts/themes/tools/online-
editor#using-javascript)Using JavaScript

The `Shopify.designMode` global variable can be used in your theme's
JavaScript files to detect whether the storefront is being viewed in the theme
editor. The value of the variable is set to `true` when viewing the theme
editor. Otherwise, it's set to `undefined`.

Copy

9

1

2

3

if (Shopify.designMode) {

// This will only happen in the theme editor

}

###

[Anchor to Reacting to theme editor JavaScript
events](/docs/storefronts/themes/tools/online-editor#reacting-to-theme-editor-
javascript-events)Reacting to theme editor JavaScript events

When a merchant interacts with a section or block in the theme editor, or
activates or deactivates the [theme editor preview
inspector](https://help.shopify.com/manual/online-store/themes/customizing-
themes/edit#preview-inspector), the theme editor emits JavaScript events. To
learn about the actions that your code should take to account for these
events, refer to [Integrate sections with the theme
editor](/docs/storefronts/themes/best-practices/editor/integrate-sections-and-
blocks).

* * *

Was this page helpful?

YesNo

  * [Accessing the theme editor through the Shopify admin](/docs/storefronts/themes/tools/online-editor#accessing-the-theme-editor-through-the-shopify-admin)
  * [Accessing the theme editor during development](/docs/storefronts/themes/tools/online-editor#accessing-the-theme-editor-during-development)
  * [Allowing for customization through the theme editor](/docs/storefronts/themes/tools/online-editor#allowing-for-customization-through-the-theme-editor)
  * [Live preview](/docs/storefronts/themes/tools/online-editor#live-preview)
  * [Integrating your theme with the theme editor](/docs/storefronts/themes/tools/online-editor#integrating-your-theme-with-the-theme-editor)

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

