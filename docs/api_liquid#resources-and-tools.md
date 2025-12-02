# Source: https://shopify.dev/docs/api/liquid#resources-and-tools

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

Liquid

  * [Overview](/docs/api/liquid)
  * [What is a template language?](/docs/api/liquid#what-is-a-template-language)
  * [Variations of Liquid](/docs/api/liquid#variations-of-liquid)
  * [Liquid basics](/docs/api/liquid#liquid-basics)
  * [Defining logic with tags](/docs/api/liquid#defining-logic-with-tags)
  * [Modifying output with filters](/docs/api/liquid#modifying-output-with-filters)
  * [Referencing objects](/docs/api/liquid#referencing-objects)
  * [Resources & tools](/docs/api/liquid#resources-and-tools)

* * *

  * [Basics](/docs/api/liquid/basics)
  * Tags

  * Filters

  * Objects

Full index

# Liquid reference

Liquid is a template language created by Shopify. It's available as an [open
source project](https://shopify.github.io/liquid/) on GitHub, and is used by
many different software projects and companies.

This reference documents the Liquid tags, filters, and objects that you can
use to build [Shopify Themes](/themes).

Copy page MD

##

[Anchor to What is a template language?](/docs/api/liquid#what-is-a-template-
language)What is a template language?

A template language allows you to create a single template to host static
content, and dynamically insert information depending on where the template is
rendered. For example, you can create a product template that hosts all of
your standard product attributes, such as the product image, title, and price.
That template can then dynamically render those attributes with the
appropriate content, depending on the current product being viewed.

* * *

##

[Anchor to Variations of Liquid](/docs/api/liquid#variations-of-
liquid)Variations of Liquid

The variation of Liquid in this reference extends the open-source version of
Liquid for use with [Shopify themes](/themes). It includes tags, filters, and
objects that can be used to render objects specific to Shopify stores and
storefront functionality.

Shopify also uses slightly different versions of Liquid to render dynamic
content for the following features. These variations aren’t included in this
reference.

[![](/images/icons/32/liquidnotificationstemplate.png)![](/images/icons/32/liquidnotificationstemplate-
dark.png)Notification templatesNotification
templates](https://help.shopify.com/en/manual/orders/notifications/email-
variables)

[Notification
templates](https://help.shopify.com/en/manual/orders/notifications/email-
variables)

[![](/images/icons/32/flow.png)![](/images/icons/32/flow-dark.png)Shopify
FlowShopify Flow](https://help.shopify.com/en/manual/shopify-
flow/reference/variables#liquid-variables)

[Shopify Flow](https://help.shopify.com/en/manual/shopify-
flow/reference/variables#liquid-variables)

[![](/images/icons/32/liquidordertemplate.png)![](/images/icons/32/liquidordertemplate-
dark.png)Order printer templatesOrder printer
templates](https://help.shopify.com/en/manual/fulfillment/managing-
orders/printing-orders/shopify-order-printer/liquid-variables-and-filters-
reference)

[Order printer
templates](https://help.shopify.com/en/manual/fulfillment/managing-
orders/printing-orders/shopify-order-printer/liquid-variables-and-filters-
reference)

[![](/images/icons/32/liquidpackingsliptemplate.png)![](/images/icons/32/liquidpackingsliptemplate-
dark.png)Packing slip templatesPacking slip
templates](https://help.shopify.com/en/manual/orders/packing-slips-variable-
list)

[Packing slip templates](https://help.shopify.com/en/manual/orders/packing-
slips-variable-list)

* * *

##

[Anchor to Liquid basics](/docs/api/liquid#liquid-basics)Liquid basics

Liquid is used to dynamically output objects and their properties. You can
further modify that output by creating logic with tags, or directly altering
it with a filter. Objects and object properties are output using one of six
basic data types. Liquid also includes basic logical and comparison operators
for use with tags.

[![](/images/icons/32/liquid.png)![](/images/icons/32/liquid-dark.png)Navigate
toBasicsNavigate toBasics](/docs/api/liquid/basics)

[Navigate to \- Basics](/docs/api/liquid/basics)

Code

Reset Code

9

1

2

3

4

5

6

<title>

{{ page_title }}

</title>

{% if page_description -%}

<meta name="description" content="{{ page_description | truncate: 150 }}">

{%- endif %}

##### Code

    
    
    <title>
      {{ page_title }}
    </title>
    {% if page_description -%}
      <meta name="description" content="{{ page_description | truncate: 150 }}">
    {%- endif %}

## Output

9

1

2

3

4

<title>

Health potion

</title>

<meta name="description" content="Are you low on health? Well we've got the
potion just for you! Just need a top up? Almost dead? In between? No need to
worry because we have a ...">

##### Output

    
    
    <title>
      Health potion
    </title>
    <meta name="description" content="Are you low on health? Well we've got the potion just for you! Just need a top up? Almost dead? In between? No need to worry because we have a ...">

* * *

##

[Anchor to Defining logic with tags](/docs/api/liquid#defining-logic-with-
tags)Defining logic with tags

Liquid tags are used to define logic that tells templates what to do.

Tags are wrapped with curly brace percentage delimiters `{% %}`. The text
within the delimiters is an instruction, not content to render.

In the example to the right, the `if` tag defines the condition to be met. If
`product.available` returns `true`, then the price is displayed. Otherwise,
the “sold out” message is shown.

`

{% %}

`

To nest multiple tags inside one set of delimiters, use the
[`liquid`](/docs/api/liquid/tags/liquid) tag.

CodeData

Reset Code

9

1

2

3

4

5

{% if product.available %}

Price: $99.99

{% else %}

Sorry, this product is sold out.

{% endif %}

##### Code

    
    
    {% if product.available %}
      Price: $99.99
    {% else %}
      Sorry, this product is sold out.
    {% endif %}

##### Data

    
    
    {
      "product": {
        "available": true
      }
    }

## Output

9

1

Price: $99.99

##### Output

    
    
    Price: $99.99

###

[Anchor to Tags with parameters](/docs/api/liquid#tags-with-parameters)Tags
with parameters

Some tags accept parameters: either required or optional. For example, the
`for` tag takes an optional `limit` parameter to stop the loop at a specific
index.

Code

Reset Code

9

1

2

3

4

5

{% assign numbers = '1,2,3,4,5' | split: ',' %}

  

{% for item in numbers limit:2 -%}

{{ item }}

{% endfor %}

##### Code

    
    
    {% assign numbers = '1,2,3,4,5' | split: ',' %}
    
    {% for item in numbers limit:2 -%}
      {{ item }}
    {% endfor %}

## Output

9

1

2

1

2

##### Output

    
    
    1
    2

* * *

##

[Anchor to Modifying output with filters](/docs/api/liquid#modifying-output-
with-filters)Modifying output with filters

Liquid filters modify the output of variables and objects.

To filter the output of a tag, use the pipe character `|`, followed by the
filter. In this example, `product` is the object, `title` is its property, and
`upcase` is the filter.

CodeData

Reset Code

9

1

2

3

{% # product.title -> Health potion %}

  

{{ product.title | upcase }}

##### Code

    
    
    {% # product.title -> Health potion %}
    
    {{ product.title | upcase }}

##### Data

    
    
    {
      "product": {
        "title": "Health potion"
      }
    }

## Output

9

1

HEALTH POTION

##### Output

    
    
    HEALTH POTION

###

[Anchor to Filters with parameters](/docs/api/liquid#filters-with-
parameters)Filters with parameters

Many filters accept parameters that adjust their output. Some parameters are
required, others are optional.

CodeData

Reset Code

9

1

2

3

{% # product.title -> Health potion %}

  

{{ product.title | remove: 'Health' }}

##### Code

    
    
    {% # product.title -> Health potion %}
    
    {{ product.title | remove: 'Health' }}

##### Data

    
    
    {
      "product": {
        "title": "Health potion"
      }
    }

## Output

9

1

potion

##### Output

    
    
    potion

###

[Anchor to Using multiple filters](/docs/api/liquid#using-multiple-
filters)Using multiple filters

Multiple filters can be used on one output. They're applied from left to
right.

CodeData

Reset Code

9

1

2

3

{% # product.title -> Health potion %}

  

{{ product.title | upcase | remove: 'HEALTH' }}

##### Code

    
    
    {% # product.title -> Health potion %}
    
    {{ product.title | upcase | remove: 'HEALTH' }}

##### Data

    
    
    {
      "product": {
        "title": "Health potion"
      }
    }

## Output

9

1

POTION

##### Output

    
    
    POTION

* * *

##

[Anchor to Referencing objects](/docs/api/liquid#referencing-
objects)Referencing objects

Liquid objects represent variables that you can use to build your theme.
Object types include, but aren't limited to:

  * Store resources, such as a collection or product and its properties
  * Standard content that is used to power Shopify themes, such as `content_for_header`
  * Functional elements that can be used to build interactivity, such as `paginate` and `search`

Objects might represent a single data point, or contain multiple properties.
Some products might represent a related object, such as a product in a
collection.

`

{{ }}

`

Double curly brace delimiters denote an output.

###

[Anchor to Usage](/docs/api/liquid#usage)Usage

To output an object, wrap it in curly brace delimiters `{{ }}`.

To output an object's property, use dot notation. This example outputs the
`product` object's `title` property.

CodeData

Reset Code

9

1

{{ product.title }}

##### Code

    
    
    {{ product.title }}

##### Data

    
    
    {
      "product": {
        "title": "Health potion"
      }
    }

## Output

9

1

Health potion

##### Output

    
    
    Health potion

###

[Anchor to Object access](/docs/api/liquid#object-access)Object access

Objects can be accessed in three ways:

  * **Globally** : Available in any Liquid file, excluding [checkout.liquid](/themes/architecture/layouts/checkout-liquid) and [Liquid asset files](/themes/architecture#assets)
  * **In templates** : Available in specific templates and their sections or blocks. For example, the [`product`](/docs/api/liquid/objects/product) object in a [product template](/themes/architecture/templates/product)
  * **Through parent objects** : Returned as properties of other objects. For example, [`article`](/docs/api/liquid/objects/article) objects through [`articles`](/docs/api/liquid/objects/articles) or [`blog`](/docs/api/liquid/objects/blog)

Check each object's documentation to see how it can be accessed.

###

[Anchor to Creating variables](/docs/api/liquid#creating-variables)Creating
variables

To create your own variables, use variable tags like
[`assign`](/docs/api/liquid/tags/assign) or
[`capture`](/docs/api/liquid/tags/capture). Syntactically, Liquid treats
variables the same as objects.

Code

Reset Code

9

1

2

{% assign my_variable = 'My custom string.' %}

{{ my_variable }}

##### Code

    
    
    {% assign my_variable = 'My custom string.' %}
    {{ my_variable }}

## Output

9

1

My custom string.

##### Output

    
    
    My custom string.

* * *

##

[Anchor to Resources & tools](/docs/api/liquid#resources-and-tools)Resources &
tools

[![](/images/icons/48/cheatsheet.png)![](/images/icons/48/cheatsheet-
dark.png)Liquid Cheat SheetA simple reference guide to the Liquid
language.Liquid Cheat SheetA simple reference guide to the Liquid
language.](https://www.shopify.com/partners/shopify-cheat-sheet)

[Liquid Cheat Sheet  
  
A simple reference guide to the Liquid
language.](https://www.shopify.com/partners/shopify-cheat-sheet)

[![](/images/icons/48/themecheck.png)![](/images/icons/48/themecheck-
dark.png)Theme CheckCommand line-based linter for themes. Also comes as an
official Visual Studio Code extension.Theme CheckCommand line-based linter for
themes. Also comes as an official Visual Studio Code
extension.](/themes/tools/theme-check)

[Theme Check  
  
Command line-based linter for themes. Also comes as an official Visual Studio
Code extension.](/themes/tools/theme-check)

[![](/images/icons/48/cli.png)![](/images/icons/48/cli-dark.png)Shopify CLI
for ThemesA powerful command-line tool for building Shopify themes, and
exploring Liquid code in a REPL interface.Shopify CLI for ThemesA powerful
command-line tool for building Shopify themes, and exploring Liquid code in a
REPL interface.](/themes/tools/cli)

[Shopify CLI for Themes  
  
A powerful command-line tool for building Shopify themes, and exploring Liquid
code in a REPL interface.](/themes/tools/cli)

[![](/images/icons/48/github.png)![](/images/icons/48/github-dark.png)Open
source liquidLiquid is an open source project on GitHub.Open source
liquidLiquid is an open source project on
GitHub.](https://github.com/Shopify/liquid)

[Open source liquid  
  
Liquid is an open source project on
GitHub.](https://github.com/Shopify/liquid)

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

