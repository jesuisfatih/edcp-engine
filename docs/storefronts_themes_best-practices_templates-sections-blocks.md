# Source: https://shopify.dev/docs/storefronts/themes/best-practices/templates-sections-blocks

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

  * [Sections](/docs/storefronts/themes/best-practices/templates-sections-blocks#sections)
  * [Blocks](/docs/storefronts/themes/best-practices/templates-sections-blocks#blocks)
  * [Theme settings](/docs/storefronts/themes/best-practices/templates-sections-blocks#theme-settings)

# Building with sections and blocks

Copy page MD

When you're designing a theme, you should consider when to provide
functionality in a section or a block. Sections and blocks are modular
components that give merchants the opportunity to customize and extend their
theme. Merchants can add and remove sections and theme blocks, adjust section
and block settings, and introduce [app
blocks](/docs/storefronts/themes/architecture/blocks/app-blocks) and
[metafields](/docs/api/liquid/objects/metafield).

These guidelines apply to [Online Store 2.0](/docs/storefronts/themes/best-
practices/version-control) themes, which use [JSON
templates](/docs/storefronts/themes/architecture/templates) and [section
groups](/docs/storefronts/themes/architecture/section-groups). You can't add
or remove [static
sections](/docs/storefronts/themes/architecture/sections#statically-render-a-
section) from Liquid templates or layouts.

* * *

##

[Anchor to Sections](/docs/storefronts/themes/best-practices/templates-
sections-blocks#sections)Sections

[Sections](/docs/storefronts/themes/architecture/sections) are available on
all pages.

When building theme templates, you should ensure that your template's default
content is available in a main template section, and that sections can be
added, removed, and reordered. You can use sections to do the following:

  * To add, remove, or reorder content at the template or section group level
  * To control theme settings that are scoped to the entire section's layout and content

![Merchants can stack multiple sections together to populate a
template.](https://cdn.shopify.com/shopifycloud/shopify-
dev/production/assets/assets/images/themes/templates-tutorial/modularity-by-
stacking-5gFGCzIW.png)

* * *

##

[Anchor to Blocks](/docs/storefronts/themes/best-practices/templates-sections-
blocks#blocks)Blocks

You should provide
[blocks](/docs/storefronts/themes/architecture/sections/section-schema#blocks)
to add, remove, or reorder content at the section level, or when it enhances
the usability of a section.

![A section can contain multiple blocks to make it more
customizable.](https://cdn.shopify.com/shopifycloud/shopify-
dev/production/assets/assets/images/themes/templates-tutorial/modularity-by-
blocks-BUDRfOCt.png)

Keep the following principles in mind when developing blocks:

  * Ensure that the [theme settings](/docs/storefronts/themes/architecture/settings) are scoped to the block.
  * Choose a block layout that is appropriate for the content, and ensure that your blocks flow logically regardless of block type or sequence.
  * Select an appropriate flexibility level to introduce using blocks.

###

[Anchor to Block layouts](/docs/storefronts/themes/best-practices/templates-
sections-blocks#block-layouts)Block layouts

When designing the grid layout for your section, ensure that your blocks
follow a logical and intuitive reading flow regardless of the block types and
block sequence.

Consider the following when determining how blocks should flow in a section:

  * Stack blocks vertically for text-based content that requires hierarchy.

![Blocks can be stacked vertically to indicate content
hierarchy.](https://cdn.shopify.com/shopifycloud/shopify-
dev/production/assets/assets/images/themes/templates-tutorial/vertical-stack-
DrK5v4bY.png)

  * If you don't need to show hierarchy, then either stack blocks horizontally or create a grid that adapts to the block types that are available in the section.

![Blocks can be stacked horizontally and wrap on multiple
lines.](https://cdn.shopify.com/shopifycloud/shopify-
dev/production/assets/assets/images/themes/templates-tutorial/horizontal-
stack-riYZEfrE.png)

![You can create a grid that adapts to the block types that are available in
the section.](https://cdn.shopify.com/shopifycloud/shopify-
dev/production/assets/assets/images/themes/templates-tutorial/adaptive-stack-
ZK6Kco0d.png)

  * When stacking blocks horizontally, either ensure that the section grid can wrap on several lines or offer horizontal sliding controls to maintain a comfortable block width. Ensure your section grid is responsive and that blocks can reflow depending on screen size.

![do](https://cdn.shopify.com/shopifycloud/shopify-
dev/production/assets/assets/images/themes/templates-
tutorial/check-D2CvX7Jo.png)| ![Blocks wrap on several
lines.](https://cdn.shopify.com/shopifycloud/shopify-
dev/production/assets/assets/images/themes/templates-tutorial/wrap-blocks-
DYpFcjuK.png)  
---|---  
![do](https://cdn.shopify.com/shopifycloud/shopify-
dev/production/assets/assets/images/themes/templates-
tutorial/check-D2CvX7Jo.png)| ![Add sliding controls to move between blocks in
narrow viewports.](https://cdn.shopify.com/shopifycloud/shopify-
dev/production/assets/assets/images/themes/templates-tutorial/sliding-
controls-rDOa6xzI.png)  
![don't](https://cdn.shopify.com/shopifycloud/shopify-
dev/production/assets/assets/images/themes/templates-tutorial/x-BmGlFLqe.png)|
![Avoid squeezing blocks to fit in narrow
viewports.](https://cdn.shopify.com/shopifycloud/shopify-
dev/production/assets/assets/images/themes/templates-tutorial/blocks-no-wrap-
DJnUj9Oz.png)  
  
  * Don't rely on a specific block type or sequence to design a layout, and don't use a specific block order to change the grid layout.

![do](https://cdn.shopify.com/shopifycloud/shopify-
dev/production/assets/assets/images/themes/templates-
tutorial/check-D2CvX7Jo.png)| ![Enforce expected layouts by grouping settings
into a single block.](https://cdn.shopify.com/shopifycloud/shopify-
dev/production/assets/assets/images/themes/templates-tutorial/three-col-
layout-B853kCkv.png)  
---|---  
![don't](https://cdn.shopify.com/shopifycloud/shopify-
dev/production/assets/assets/images/themes/templates-tutorial/x-BmGlFLqe.png)|
![Don't rely on a specific block type or sequence to design a section
layout.](https://cdn.shopify.com/shopifycloud/shopify-
dev/production/assets/assets/images/themes/templates-tutorial/reliance-on-
block-sequence-CQazdG62.png)  
  
![do](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/themes/templates-tutorial/check-D2CvX7Jo.png)| | ![don't](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/themes/templates-tutorial/x-BmGlFLqe.png)  
---|---|---  
![Don't use a specific block order to change the grid
layout.](https://cdn.shopify.com/shopifycloud/shopify-
dev/production/assets/assets/images/themes/templates-tutorial/block-order-and-
layout-kZlNYnf2.png)  
  
###

[Anchor to Blocks and flexibility](/docs/storefronts/themes/best-
practices/templates-sections-blocks#blocks-and-flexibility)Blocks and
flexibility

To balance simplicity and flexibility, you should carefully consider when to
add blocks and what each block should contain. Too many blocks creates clutter
and complexity. You can use the following principles to understand how to
define your blocks.

  * Group settings into blocks to simplify the editing experience and declutter the editor sidebar. For example, you can nest theme settings to customize an image block inside of the block.
  * When elements follow a specific hierarchy, group elements together and optionally allow block insertion points before and after. For example, you might create a single block that controls cart page line items.
  * Avoid providing blocks that are too granular. Granularity adds complexity to the theme code and to the merchant editing experience. For example, you should group the author, date, and comments into a single block or into settings, rather than introducing these attributes as three separate blocks.

![do](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/themes/templates-tutorial/check-D2CvX7Jo.png)| | ![don't](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/themes/templates-tutorial/x-BmGlFLqe.png)  
---|---|---  
![Choose the right level of granularity for blocks in your
sections.](https://cdn.shopify.com/shopifycloud/shopify-
dev/production/assets/assets/images/themes/templates-tutorial/granularity-
DRtrNmcu.png)  
  
###

[Anchor to Considerations for app blocks](/docs/storefronts/themes/best-
practices/templates-sections-blocks#considerations-for-app-
blocks)Considerations for app blocks

Merchants can add [app-provided blocks](/docs/apps/build/online-store/theme-
app-extensions) to their themes. As a theme developer, you need to [add
support](/docs/storefronts/themes/architecture/blocks/app-blocks) for these
types of blocks to your sections. Consider the following when deciding whether
to support app blocks in a section:

  * Provide app blocks in sections that have clear use cases for layering additional conversion tools, or purchase decision factors. For example, you might want to include an app block with the product information on the product page, or in the cart template.
  * Always consider antifragility and the section's purpose when considering extending a theme using app blocks. Would the layout break easily when inserting unexpected block types? Would it require adding edge-case CSS styles to handle those blocks? Would it make the section's purpose vague, or inconsistent? If the answer is yes to these questions, then avoid app blocks.

* * *

##

[Anchor to Theme settings](/docs/storefronts/themes/best-practices/templates-
sections-blocks#theme-settings)Theme settings

Use [theme settings](/docs/storefronts/themes/architecture/settings) to
provide different look and feel options. Theme settings can be applied at the
section, block, and theme levels.

![Settings can provide different look and feel
options.](https://cdn.shopify.com/shopifycloud/shopify-
dev/production/assets/assets/images/themes/templates-tutorial/settings-
flexibility-BllwmWff.png)

###

[Anchor to Metafields](/docs/storefronts/themes/best-practices/templates-
sections-blocks#metafields)Metafields

Shopify provides various standard
[metafields](/docs/api/liquid/objects/metafield) that can fit your target
segment. Review what's available and consider which use cases make sense for
the theme. For example, you might include either sections or blocks for a care
guide or size chart metafield. These metafields, when referenced as [dynamic
sources](/docs/storefronts/themes/architecture/settings/dynamic-sources),
update to reflect their context, such as the product that is being rendered.

![Use metafields to add dynamic information to your
theme.](https://cdn.shopify.com/shopifycloud/shopify-
dev/production/assets/assets/images/themes/templates-tutorial/block-settings-
and-metafields-CqFzxwoI.png)

When building metafields into your theme, consider building specific blocks
for metafields. You can also audit ecommerce websites for your target segment,
and analyze how content is presented to identify opportunities to design
specific components. For example, you might want to use metafields to create a
well-formatted information list for electronic products, or to add information
about a coffee blend and origin.

* * *

Was this page helpful?

YesNo

  * [Sections](/docs/storefronts/themes/best-practices/templates-sections-blocks#sections)
  * [Blocks](/docs/storefronts/themes/best-practices/templates-sections-blocks#blocks)
  * [Theme settings](/docs/storefronts/themes/best-practices/templates-sections-blocks#theme-settings)

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

