# Source: https://shopify.dev/docs/api/liquid/objects/metafield#metafield-deprecated-metafields

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

# metafield

Copy page MD

A [metafield](/apps/metafields) attached to a parent object.

To learn about how to access a metafield on a specific object, refer to
[Access metafields](/docs/api/liquid/objects/metafield#metafield-access-
metafields).

Metafields support [multiple data types](/apps/metafields/types), which
determine the kind of information that's stored in the metafield. You can also
output the metafield content in a type-specific format using [metafield
filters](/docs/api/liquid/filters/metafield-filters).

* * *

Note

You can't create metafields in Liquid. Metafields can be created in only the
following ways:

  * [In the Shopify admin](https://help.shopify.com/manual/metafields)
  * [Through an app](https://shopify.dev/apps/metafields)

* * *

* * *

Note

Metafields of type `integer`, `json_string`, and `string` are older
implementations that don't have the properties noted on this page, and aren't
compatible with metafield filters. To learn more, refer to [Deprecated
metafields](/docs/api/liquid/objects/metafield#metafield-deprecated-
metafields).

* * *

## Properties

[Anchor to ](/docs/api/liquid/objects/metafield#metafield-list?)

list?

[boolean](/docs/api/liquid/basics#boolean)

    

Returns `true` if the metafield is a list type. Returns `false` if not.

Tip

To learn about metafield types, refer to [Metafield
types](/apps/metafields/types).

[Anchor to ](/docs/api/liquid/objects/metafield#metafield-type)

type

[string](/docs/api/liquid/basics#string) from a set of values

    

The [type](/apps/metafields/types) of the metafield.

Possible values  
---  
single_line_text_field  
multi_line_text_field  
rich_text_field  
product_reference  
collection_reference  
variant_reference  
page_reference  
file_reference  
number_integer  
number_decimal  
date  
date_time  
url_reference  
json  
boolean  
color  
weight  
volume  
dimension  
rating  
money  
  
[Anchor to ](/docs/api/liquid/objects/metafield#metafield-value)

value

    

The value of the metafield.

The following table outlines the value format for each metafield type:

Type| Returned format  
---|---  
`single_line_text_field`  
  
`multi_line_text_field` | [A string](/docs/api/liquid/basics#string)  
`rich_text_field` | A field that supports headings, lists, links, bold, and italics  
`product_reference` | [A product object](/docs/api/liquid/objects/product)  
`collection_reference` | [A collection object](/docs/api/liquid/objects/collection)  
`variant_reference` | [A variant object](/docs/api/liquid/objects/variant)  
`page_reference` | [A page object](/docs/api/liquid/objects/page)  
`file_reference` |  [A generic_file object](/docs/api/liquid/objects/generic-file)  
  
[A media object (images and videos only)](/docs/api/liquid/objects/media)  
`number_integer`  
  
`number_decimal` | [A number](/docs/api/liquid/basics#number)  
`date`  
  
`date_time` | A date string. To format the string, use the [date](/docs/api/liquid/filters/date) filter.  
`url_reference` | [A url string](/docs/api/liquid/basics#string)  
`json` | [A JSON object](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/JSON)  
`boolean` | [A boolean](/docs/api/liquid/basics#boolean)  
`color` | [A color object](/docs/api/liquid/objects/color)  
`weight`  
  
`volume`  
  
`dimension` | [A measurement object](/docs/api/liquid/objects/measurement)  
`rating` | [A rating object](/docs/api/liquid/objects/rating)  
`money` | [A money object, displayed in the customer's local (presentment) currency.](/docs/api/liquid/objects/money)  
  
ExampleAccess

9

1

2

3

4

5

{

"list?": false,

"type": "single_line_text_field",

"value": "Take with a meal."

}

##### Example

    
    
    {
      "list?": false,
      "type": "single_line_text_field",
      "value": "Take with a meal."
    }

[Anchor to Access metafields](/docs/api/liquid/objects/metafield#metafield-
access-metafields)

###

Access metafields

The access path for metafields consists of two layers:

  * namespace - A grouping of metafields to prevent conflicts.
  * key - The metafield name.

Given this, you can access the metafield object with the following syntax:

Copy

9

1

{{ resource.metafields.namespace.key }}

CodeData

Reset Code

9

1

2

Type: {{ product.metafields.information.directions.type }}

Value: {{ product.metafields.information.directions.value }}

##### Code

    
    
    Type: {{ product.metafields.information.directions.type }}
    Value: {{ product.metafields.information.directions.value }}

##### Data

    
    
    {
      "product": {
        "metafields": {}
      }
    }

## Output

9

1

2

Type: single_line_text_field

Value: Take with a meal.

##### Output

    
    
    Type: single_line_text_field
    Value: Take with a meal.

[Anchor to Accessing metafields of type
`json`](/docs/api/liquid/objects/metafield#metafield-accessing-metafields-of-
type-json)

###

Accessing metafields of type `json`

The `value` property of metafields of type `json` returns a [JSON
object](https://developer.mozilla.org/en-
US/docs/Learn/JavaScript/Objects/JSON). You can access the properties of this
object directly in Liquid, either by name or 0-based index. You can also
iterate through the properties.

CodeData

Reset Code

9

1

2

3

4

5

6

Temperature: {{
product.metafields.information.burn_temperature.value.temperature }}

Unit: {{ product.metafields.information.burn_temperature.value['unit'] }}

  

{% for property in product.metafields.information.burn_temperature.value -%}

{{ property.first | capitalize }}: {{ property.last }}

{%- endfor %}

##### Code

    
    
    Temperature: {{ product.metafields.information.burn_temperature.value.temperature }}
    Unit: {{ product.metafields.information.burn_temperature.value['unit'] }}
    
    {% for property in product.metafields.information.burn_temperature.value -%}
      {{ property.first | capitalize }}: {{ property.last }}
    {%- endfor %}

##### Data

    
    
    {
      "product": {
        "metafields": {}
      }
    }

## Output

9

1

2

3

4

5

6

Temperature: 700

Unit: degrees

  

Temperature: 700

Unit: degrees

Scale: Fahrenheit

##### Output

    
    
    Temperature: 700
    Unit: degrees
    
    Temperature: 700
    Unit: degrees
    Scale: Fahrenheit

[Anchor to Accessing metafields of type
`list`](/docs/api/liquid/objects/metafield#metafield-accessing-metafields-of-
type-list)

###

Accessing metafields of type `list`

The `value` property of metafields of type `list` returns an array. You can
iterate through the array to access the values.

CodeData

Reset Code

9

1

2

3

{% for item in product.metafields.information.combine_with.value -%}

{{ item.product.title }}

{%- endfor %}

##### Code

    
    
    {% for item in product.metafields.information.combine_with.value -%}
      {{ item.product.title }}
    {%- endfor %}

##### Data

    
    
    {
      "product": {
        "metafields": {}
      }
    }

## Output

9

1

2

Blue Mountain Flower

Charcoal

##### Output

    
    
    Blue Mountain Flower
    Charcoal

  
  
If the list is of type `single_line_text_field`, then you can access the items
in the array directly in Liquid using a 0-based index.

CodeData

Reset Code

9

1

2

First item in list: {{
product.metafields.information.pickup_locations.value[0] }}

Last item in list: {{
product.metafields.information.pickup_locations.value.last }}

##### Code

    
    
    First item in list: {{ product.metafields.information.pickup_locations.value[0] }}
    Last item in list: {{ product.metafields.information.pickup_locations.value.last }}

##### Data

    
    
    {
      "product": {
        "metafields": {}
      }
    }

## Output

9

1

2

First item in list: Ottawa

Last item in list: Vancouver

##### Output

    
    
    First item in list: Ottawa
    Last item in list: Vancouver

[Anchor to Determining the length of a list
metafield](/docs/api/liquid/objects/metafield#metafield-determining-the-
length-of-a-list-metafield)

###

Determining the length of a list metafield

The way that you determine the length of a list metafield depends on its type:

  * **[Reference types](/docs/apps/custom-data/metafields/types#reference-types)** : Use the `count` property to determine the list length.
  * **Non-reference types** : These lists are rendered as arrays. Use the [`size`](/docs/api/liquid/filters/size) filter to determine the number of items in the array.

CodeData

Reset Code

9

1

2

3

4

5

# list.product_reference

Number of similar products: {{
product.metafields.information.similar_products.value.count }}

  

# list.single_line_text_field

Number of pickup locations: {{
product.metafields.information.pickup_locations.value.size }}

##### Code

    
    
    # list.product_reference
    Number of similar products: {{ product.metafields.information.similar_products.value.count }}
    
    # list.single_line_text_field
    Number of pickup locations: {{ product.metafields.information.pickup_locations.value.size }}

##### Data

    
    
    {
      "product": {
        "metafields": {}
      }
    }

## Output

9

1

2

3

4

5

# list.product_reference

Number of similar products: 2

  

# list.single_line_text_field

Number of pickup locations: 4

##### Output

    
    
    # list.product_reference
    Number of similar products: 2
    
    # list.single_line_text_field
    Number of pickup locations: 4

[Anchor to Deprecated
metafields](/docs/api/liquid/objects/metafield#metafield-deprecated-
metafields)

###

Deprecated metafields

Deprecated metafields are older metafield types with limited functionality.
The following metafield types are deprecated:

  * `integer`
  * `json_string`
  * `string`

These metafield types don't have the same metafield object properties
mentioned in the previous sections. Instead, they return the metafield value
directly.

The following table outlines the value type for each deprecated metafield
type:

Metafield type| Value type  
---|---  
`integer`| [An integer](/docs/api/liquid/basics#number)  
`json_string`| [A JSON object](https://developer.mozilla.org/en-
US/docs/Learn/JavaScript/Objects/JSON)  
`string`| [A string](/docs/api/liquid/basics#string)  
  
Was this section helpful?

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

