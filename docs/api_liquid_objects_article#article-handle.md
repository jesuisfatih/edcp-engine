# Source: https://shopify.dev/docs/api/liquid/objects/article#article-handle

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

# article

Copy page MD

An article, or [blog post](https://help.shopify.com/manual/online-
store/blogs/writing-blogs), in a blog.

## Properties

[Anchor to ](/docs/api/liquid/objects/article#article-author)

author

[string](/docs/api/liquid/basics#string)

    

The full name of the author of the article.

[Anchor to ](/docs/api/liquid/objects/article#article-comment_post_url)

comment_post_url

[string](/docs/api/liquid/basics#string)

    

The relative URL where POST requests are sent when creating new comments.

[Anchor to ](/docs/api/liquid/objects/article#article-comments)

comments

array of [comment](/docs/api/liquid/objects/comment)

    

The published comments for the article.

Returns an empty array if comments are disabled.

Tip

Use the [paginate](/docs/api/liquid/tags/paginate) tag to choose how many
comments to show at once, up to a limit of 50.

[Anchor to ](/docs/api/liquid/objects/article#article-comments_count)

comments_count

[number](/docs/api/liquid/basics#number)

    

The number of published comments for the article.

[Anchor to ](/docs/api/liquid/objects/article#article-comments_enabled?)

comments_enabled?

[boolean](/docs/api/liquid/basics#boolean)

    

Returns `true` if comments are enabled. Returns `false` if not.

[Anchor to ](/docs/api/liquid/objects/article#article-content)

content

[string](/docs/api/liquid/basics#string)

    

The content of the article.

[Anchor to ](/docs/api/liquid/objects/article#article-created_at)

created_at

[string](/docs/api/liquid/basics#string)

    

A timestamp for when the article was created.

Tip

Use the [`date` filter](/docs/api/liquid/filters/date) to format the
timestamp.

[Anchor to ](/docs/api/liquid/objects/article#article-excerpt)

excerpt

[string](/docs/api/liquid/basics#string)

    

The excerpt of the article.

[Anchor to ](/docs/api/liquid/objects/article#article-excerpt_or_content)

excerpt_or_content

[string](/docs/api/liquid/basics#string)

    

Returns the article [excerpt](/docs/api/liquid/objects/article#article-
excerpt) if it exists. Returns the article
[content](/docs/api/liquid/objects/article#article-content) if no excerpt
exists.

[Anchor to ](/docs/api/liquid/objects/article#article-handle)

handle

[string](/docs/api/liquid/basics#string)

    

The [handle](/docs/api/liquid/basics#handles) of the article.

[Anchor to ](/docs/api/liquid/objects/article#article-id)

id

[string](/docs/api/liquid/basics#string)

    

The ID of the article.

[Anchor to ](/docs/api/liquid/objects/article#article-image)

image

[image](/docs/api/liquid/objects/image)

    

The featured image for the article.

[Anchor to ](/docs/api/liquid/objects/article#article-metafields)

metafields

    

The [metafields](/docs/api/liquid/objects/metafield) applied to the article.

Tip

To learn about how to create metafields, refer to [Create and manage
metafields](/apps/metafields/manage) or visit the [Shopify Help
Center](https://help.shopify.com/manual/metafields).

[Anchor to ](/docs/api/liquid/objects/article#article-moderated?)

moderated?

[boolean](/docs/api/liquid/basics#boolean)

    

Returns `true` if the blog that the article belongs to is set to [moderate
comments](https://help.shopify.com/manual/online-store/blogs/managing-
comments). Returns `false` if not.

[Anchor to ](/docs/api/liquid/objects/article#article-published_at)

published_at

[string](/docs/api/liquid/basics#string)

    

A timestamp for when the article was published.

Tip

Use the [`date` filter](/docs/api/liquid/filters/date) to format the
timestamp.

[Anchor to ](/docs/api/liquid/objects/article#article-tags)

tags

array of [string](/docs/api/liquid/basics#string)

    

The tags applied to the article.

![](/images/icons/32/lightbulbscroll.png)![](/images/icons/32/lightbulbscroll-
dark.png)

Example

Show the total tag count

When looping through `article.tags`, you can print how many times a tag is
used with `tag.total_count`. This number shows visitors how many blog posts
have been tagged with a particular tag.

CodeData

Reset Code

9

1

2

3

{% for tag in article.tags -%}

{{ tag }} ({{ tag.total_count }})

{%- endfor %}

##### Code

    
    
    {% for tag in article.tags -%}
      {{ tag }} ({{ tag.total_count }})
    {%- endfor %}

##### Data

    
    
    {
      "article": {
        "tags": [
          "clear potions",
          "potion troubleshooting",
          "tips"
        ]
      }
    }

## Output

9

1

clear potions (1)potion troubleshooting (2)tips (2)

##### Output

    
    
    clear potions (1)potion troubleshooting (2)tips (2)

[Anchor to ](/docs/api/liquid/objects/article#article-template_suffix)

template_suffix

[string](/docs/api/liquid/basics#string)

    

The name of the [custom template](/themes/architecture/templates#alternate-
templates) assigned to the article.

The name doesn't include the `article.` prefix, or the file extension (`.json`
or `.liquid`).

If a custom template isn't assigned to the article, then `nil` is returned.

[Anchor to ](/docs/api/liquid/objects/article#article-title)

title

[string](/docs/api/liquid/basics#string)

    

The title of the article.

[Anchor to ](/docs/api/liquid/objects/article#article-updated_at)

updated_at

[string](/docs/api/liquid/basics#string)

    

A timestamp for when the article was updated.

Tip

Use the [`date` filter](/docs/api/liquid/filters/date) to format the
timestamp.

[Anchor to ](/docs/api/liquid/objects/article#article-url)

url

[string](/docs/api/liquid/basics#string)

    

The relative URL of the article.

[Anchor to ](/docs/api/liquid/objects/article#article-user)

user

[user](/docs/api/liquid/objects/user)

    

The user associated with the author of the article.

ExampleAccess

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

{

"author": "Polina Waters",

"comment_post_url": "/blogs/potion-notions/how-to-tell-if-you-have-run-out-of-
invisibility-potion/comments",

"comments": [],

"comments_count": 1,

"comments_enabled?": true,

"content": "<p>We've all had this problem before: we peek into the potions
vault to determine which potions we are running low on, and the invisibility
potion bottle looks completely empty.</p>\n<p>...</p>\n<p> </p>",

"created_at": "2022-04-14 16:56:02 -0400",

"excerpt": "And where to buy <strong>more</strong>!",

"excerpt_or_content": "And where to buy <strong>more</strong>!",

"handle": "potion-notions/how-to-tell-if-you-have-run-out-of-invisibility-
potion",

"id": 556510085185,

"image": {},

"metafields": {},

"moderated?": true,

"published_at": "2022-04-14 16:56:02 -0400",

"tags": [],

"template_suffix": "",

"title": "How to tell if you're out of invisibility potion",

"updated_at": "2022-06-04 19:27:33 -0400",

"url": {},

"user": {}

}

##### Example

    
    
    {
      "author": "Polina Waters",
      "comment_post_url": "/blogs/potion-notions/how-to-tell-if-you-have-run-out-of-invisibility-potion/comments",
      "comments": [],
      "comments_count": 1,
      "comments_enabled?": true,
      "content": "<p>We've all had this problem before: we peek into the potions vault to determine which potions we are running low on, and the invisibility potion bottle looks completely empty.</p>\n<p>...</p>\n<p> </p>",
      "created_at": "2022-04-14 16:56:02 -0400",
      "excerpt": "And where to buy <strong>more</strong>!",
      "excerpt_or_content": "And where to buy <strong>more</strong>!",
      "handle": "potion-notions/how-to-tell-if-you-have-run-out-of-invisibility-potion",
      "id": 556510085185,
      "image": {},
      "metafields": {},
      "moderated?": true,
      "published_at": "2022-04-14 16:56:02 -0400",
      "tags": [],
      "template_suffix": "",
      "title": "How to tell if you're out of invisibility potion",
      "updated_at": "2022-06-04 19:27:33 -0400",
      "url": {},
      "user": {}
    }

[Anchor to ](/docs/api/liquid/objects/article#template-using)

## Templates using article

[![](/images/icons/32/themes.png)![](/images/icons/32/themes-dark.png)Theme
architecturearticle templateTheme architecturearticle
template](/themes/architecture/templates/article)

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

