# Source: https://shopify.dev/docs/api/liquid/tags/assign

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

# assign

Copy page MD

Creates a new variable.

You can create variables of any [basic type](/docs/api/liquid/basics#types),
[object](/docs/api/liquid/objects), or object property.

* * *

Caution

Predefined Liquid objects can be overridden by variables with the same name.
To make sure that you can access all Liquid objects, make sure that your
variable name doesn't match a predefined object's name.

* * *

## Syntax

9

1

{% assign variable_name = value %}

variable_name

The name of the variable being created.

value

The value you want to assign to the variable.

CodeData

Reset Code

9

1

2

3

{%- assign product_title = product.title | upcase -%}

  

{{ product_title }}

##### Code

    
    
    {%- assign product_title = product.title | upcase -%}
    
    {{ product_title }}

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

