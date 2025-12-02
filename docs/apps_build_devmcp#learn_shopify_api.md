# Source: https://shopify.dev/docs/apps/build/devmcp#learn_shopify_api

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

Apps

  * [Build](/docs/apps/build)
  * [Design](/docs/apps/design)
  * [Launch](/docs/apps/launch)

Collapse sidebar

  * ### Getting started

    * [Shopify app platform](/docs/apps/build)
    * [App surfaces](/docs/apps/build/app-surfaces)
    * [Scaffold an app](/docs/apps/build/scaffold-app)
    * [Build an app](/docs/apps/build/build)
  * ### Dev tools

    * [Dev MCP server](/docs/apps/build/devmcp)
    * Shopify CLI for apps

    * Dev Dashboard

  * ### Extending Shopify

    * Admin

    * Checkout

    * Customer accounts

    * Flow

    * Online store

    * Point of Sale

  * ### Building blocks

    * GraphQL

    * Extensions

    * Shopify Functions

    * Storefront MCP

    * Webhooks

    * Custom data

    * Authentication

  * ### Use cases

    * Marketing and analytics

    * Discounts

    * Product merchandising

    * Purchase options

    * Global markets

    * Orders and fulfillment

    * Payments

    * Sales channels

    * B2B

    * Shopify Collective

    * Blockchain

  * ### Best practices

    * Performance

    * [Accessibility](/docs/apps/build/accessibility)
    * [Localize your app](/docs/apps/build/localize-your-app)
    * [Integrating with Shopify](/docs/apps/build/integrating-with-shopify)
    * [Mobile support](/docs/apps/build/mobile-support)
    * [Non-deceptive code](/docs/apps/build/non-deceptive-code)
    * Compliance

    * Security

Full index

ExpandOn this page

  * [How it works](/docs/apps/build/devmcp#how-it-works)
  * [Requirements](/docs/apps/build/devmcp#requirements)
  * [What you can ask your AI assistant](/docs/apps/build/devmcp#what-you-can-ask-your-ai-assistant)
  * [Supported APIs](/docs/apps/build/devmcp#supported-apis)
  * [Set up the server](/docs/apps/build/devmcp#set-up-the-server)
  * [Available tools](/docs/apps/build/devmcp#available-tools)
  * [Related resources](/docs/apps/build/devmcp#related-resources)

# Shopify Dev MCP server

Copy page MD

Connect your AI assistant to Shopify's development resources. The Shopify Dev
Model Context Protocol (MCP) server enables your AI assistant to search
Shopify docs, explore API schemas, build Functions, and get up-to-date answers
about Shopify APIs.

* * *

##

[Anchor to How it works](/docs/apps/build/devmcp#how-it-works)How it works

Your AI assistant uses the MCP server to read and interact with Shopify's
development resources:

  1. Ask your AI assistant to build something or help with Shopify development tasks.
  2. The assistant searches Shopify documentation and API schemas based on your prompt.
  3. The MCP server gives your AI assistant access to Shopify's development resources, so it can provide accurate code, solutions, and guidance based on current APIs and best practices.

* * *

##

[Anchor to Requirements](/docs/apps/build/devmcp#requirements)Requirements

Before you set up the Dev MCP server, make sure you have:

  * **Node.js 18 or higher** installed on your system.
  * An **AI development tool** that supports MCP, such as Cursor or Gemini CLI.

* * *

##

[Anchor to What you can ask your AI assistant](/docs/apps/build/devmcp#what-
you-can-ask-your-ai-assistant)What you can ask your AI assistant

After you set up the MCP server, you can ask your AI assistant questions like:

  * "How do I create a product using the Admin API?"
  * "What fields are available on the Order object?"
  * "Show me an example of a webhook subscription"
  * "How do I authenticate my Shopify app?"
  * "What's the difference between Admin API and Storefront API?"
  * "Build a new POS UI extension that shows all the product SKUs of the order in the order details screen"

Your AI assistant will use the MCP server to search Shopify's documentation
when providing responses.

* * *

##

[Anchor to Supported APIs](/docs/apps/build/devmcp#supported-apis)Supported
APIs

The MCP server provides tools to interact with the following Shopify APIs:

  * [Admin GraphQL API](/docs/api/admin-graphql)
  * [Customer Account API](/docs/api/customer)
  * [Functions](/docs/api/functions)
  * [Liquid](/docs/api/liquid)
  * [Partner API](/docs/api/partner)
  * [Payment Apps API](/docs/api/payments-apps)
  * [Polaris Web Components](/docs/api/polaris)
  * [POS UI Extensions](/docs/api/pos-ui-extensions)
  * [Storefront API](/docs/api/storefront)

* * *

##

[Anchor to Set up the server](/docs/apps/build/devmcp#set-up-the-server)Set up
the server

The server runs locally in your development environment and doesn't require
authentication.

###

[Anchor to Step 1: Configure your AI development
tool](/docs/apps/build/devmcp#step-1-configure-your-ai-development-tool)Step
1: Configure your AI development tool

Add configuration code that tells your AI tool how to connect to and use the
Dev MCP server. This configuration enables your AI assistant to automatically
access Shopify documentation, API schemas, and development guidance when you
ask questions.

#### Cursor

  1. Open Cursor and go to **Cursor** > **Settings** > **Cursor Settings** > **Tools and integrations** > **New MCP server**.

  2. Add this configuration to your MCP servers (or [use this link](https://cursor.com/en/install-mcp?name=shopify-dev-mcp&config=eyJjb21tYW5kIjoibnB4IC15IEBzaG9waWZ5L2Rldi1tY3BAbGF0ZXN0In0%3D) to add it automatically):

## Cursor configuration

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

{

"mcpServers": {

"shopify-dev-mcp": {

"command": "npx",

"args": ["-y", "@shopify/dev-mcp@latest"]

}

}

}

If you see connection errors on Windows, try this alternative configuration:

## Alternative configuration for Windows

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

{

"mcpServers": {

"shopify-dev-mcp": {

"command": "cmd",

"args": ["/k", "npx", "-y", "@shopify/dev-mcp@latest"]

}

}

}

Note

For more information, see the [Cursor MCP
documentation](https://docs.cursor.com/context/model-context-protocol).

  3. Save your configuration and restart Cursor.

#### Claude Desktop

  1. Open Claude Desktop and access your configuration file through settings.

  2. Add this configuration to your MCP servers section:

## Claude Desktop configuration

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

{

"mcpServers": {

"shopify-dev-mcp": {

"command": "npx",

"args": ["-y", "@shopify/dev-mcp@latest"]

}

}

}

Note

For more information, read the [Claude Desktop MCP
guide](https://modelcontextprotocol.io/quickstart/user).

  3. Save your configuration and restart Claude Desktop.

#### Codex CLI

  1. Add this configuration to your `~/.codex/config.toml` file:

## Codex configuration

Copy

9

1

2

3

[mcp_servers.shopify-dev-mcp]

command = "npx"

args = ["-y", "@shopify/dev-mcp@latest"]

Note

Codex uses TOML format with `mcp_servers` (snake_case) instead of JSON with
`mcpServers` (camelCase). For more information, see the [Codex MCP
documentation](https://github.com/openai/codex/blob/main/docs/config.md#mcp_servers).

  2. Restart Codex to load the new MCP server configuration.

#### Gemini CLI

  1. Add the [Dev MCP server extension](https://github.com/shopify/dev-mcp-gemini-cli) using the Gemini CLI command:

## Terminal

Copy

$

$

gemini extensions install https://github.com/shopify/dev-mcp-gemini-cli

Or you can manually add this configuration in your `settings.json` file:

## Gemini CLI configuration

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

{

"mcpServers": {

"shopify-dev-mcp": {

"command": "npx",

"args": ["-y", "@shopify/dev-mcp@latest"]

}

}

}

Note

By default, this adds the server to your project configuration. To make it
available across all projects, add the `--scope user` flag. For more
information, see the [Gemini CLI MCP documentation](https://google-
gemini.github.io/gemini-cli/docs/tools/mcp-server.html).

  2. Restart Gemini CLI to load the new MCP server configuration.

CursorClaude DesktopCodex CLIGemini CLI

  1. Open Cursor and go to **Cursor** > **Settings** > **Cursor Settings** > **Tools and integrations** > **New MCP server**.

  2. Add this configuration to your MCP servers (or [use this link](https://cursor.com/en/install-mcp?name=shopify-dev-mcp&config=eyJjb21tYW5kIjoibnB4IC15IEBzaG9waWZ5L2Rldi1tY3BAbGF0ZXN0In0%3D) to add it automatically):

## Cursor configuration

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

{

"mcpServers": {

"shopify-dev-mcp": {

"command": "npx",

"args": ["-y", "@shopify/dev-mcp@latest"]

}

}

}

If you see connection errors on Windows, try this alternative configuration:

## Alternative configuration for Windows

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

{

"mcpServers": {

"shopify-dev-mcp": {

"command": "cmd",

"args": ["/k", "npx", "-y", "@shopify/dev-mcp@latest"]

}

}

}

Note

For more information, see the [Cursor MCP
documentation](https://docs.cursor.com/context/model-context-protocol).

  3. Save your configuration and restart Cursor.

###

[Anchor to Step 2: (Optional) Configure advanced
options](/docs/apps/build/devmcp#step-2-optional-configure-advanced-
options)Step 2: (Optional) Configure advanced options

The Dev MCP server supports several advanced configuration options:

####

[Anchor to Disable instrumentation](/docs/apps/build/devmcp#disable-
instrumentation)Disable instrumentation

This package makes instrumentation calls to better understand how to improve
the MCP server. To disable them, set the `OPT_OUT_INSTRUMENTATION` environment
variable in Cursor or Claude Desktop:

## Disable instrumentation

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

{

"mcpServers": {

"shopify-dev-mcp": {

"command": "npx",

"args": ["-y", "@shopify/dev-mcp@latest"],

"env": {

"OPT_OUT_INSTRUMENTATION": "true"

}

}

}

}

####

[Anchor to Liquid and Theme validation
support](/docs/apps/build/devmcp#liquid-and-theme-validation-support)Liquid
and Theme validation support

You can control the validation mode by setting `LIQUID_VALIDATION_MODE` in the
environment:

  * `full` (default, recommended): Enables the `validate_theme` tool for validating entire theme directories.
  * `partial` (not recommended): Enables the `validate_theme_codeblocks` tool for validating individual codeblocks. Only use this for self-contained Liquid files that don't require theme context.

## Configure the validation mode

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

{

"mcpServers": {

"shopify-dev-mcp": {

"command": "npx",

"args": ["-y", "@shopify/dev-mcp@latest"],

"env": {

"LIQUID_VALIDATION_MODE": "full"

}

}

}

}

* * *

##

[Anchor to Available tools](/docs/apps/build/devmcp#available-tools)Available
tools

The Dev MCP server provides the following tools:

###

[Anchor to [object
Object]](/docs/apps/build/devmcp#learn_shopify_api)`learn_shopify_api`

Teaches the LLM about supported Shopify APIs and how to use this MCP server's
tools to generate valid code blocks for each API. This tool makes a request to
[shopify.dev](https://shopify.dev) to get the most up-to-date instruction for
how to best work with the API the user would need to use for their prompt.

Note

Always call this tool first when working with Shopify APIs. It provides
essential context about supported APIs and generates a conversation ID for
tracking usage across tool calls.

* * *

###

[Anchor to [object
Object]](/docs/apps/build/devmcp#search_docs_chunks)`search_docs_chunks`

Search across all [shopify.dev](https://shopify.dev) documentation to find
relevant chunks matching your query.

Best for broad research across multiple topics or when you're not sure where
to look. Returns quick results from many sections, though individual snippets
might lack full context.

* * *

###

[Anchor to [object
Object]](/docs/apps/build/devmcp#fetch_full_docs)`fetch_full_docs`

Retrieve complete documentation for specific paths from
[shopify.dev](https://shopify.dev). Provides full context without chunking
loss, but requires knowing the exact path. Paths are provided via
`learn_shopify_api`.

* * *

###

[Anchor to [object
Object]](/docs/apps/build/devmcp#introspect_graphql_schema)`introspect_graphql_schema`

Explore and search Shopify GraphQL schemas to find specific types, queries,
and mutations.

Essential for GraphQL development - discover what fields, queries, and
mutations are available before writing your operations, along with the
necessary access scopes.

* * *

###

[Anchor to [object
Object]](/docs/apps/build/devmcp#validate_graphql_codeblocks)`validate_graphql_codeblocks`

Validate GraphQL code blocks against a specific GraphQL schema to ensure they
don't contain hallucinated fields or operations.

Use when generating or modifying GraphQL code to ensure it doesn't contain
fields or operations that don't exist in Shopify's API.

* * *

###

[Anchor to [object
Object]](/docs/apps/build/devmcp#validate_component_codeblocks)`validate_component_codeblocks`

Validates JavaScript and TypeScript code blocks containing Shopify components
against the schema to ensure they don't contain hallucinated components,
props, or prop values.

Use when generating or modifying component code to ensure it uses only valid
components and properties that exist in Shopify's component libraries.

* * *

###

[Anchor to [object
Object]](/docs/apps/build/devmcp#validate_theme_codeblocks)`validate_theme_codeblocks`

Validates individual Liquid codeblocks and supporting theme files (JSON, CSS,
JS, SVG) to ensure correct syntax and references.

Limited use case

This tool only works for self-contained Liquid files generated by the LLM. If
the generated files require any context from an existing theme, this isn't the
right choice. Use `validate_theme` instead for comprehensive theme validation.

Requires `LIQUID_VALIDATION_MODE=partial` in your MCP server configuration.

* * *

###

[Anchor to [object
Object]](/docs/apps/build/devmcp#validate_theme)`validate_theme`

Validates entire theme directories using Shopify's Theme Check to detect
errors in Liquid syntax, missing references, and other theme issues.

Run this on complete themes to catch cross-file issues and ensure consistency.
Applies all [Theme Check rules](/docs/storefronts/themes/tools/theme-check)
for comprehensive validation.

Note

This tool is enabled by default when `LIQUID_VALIDATION_MODE=full`.

* * *

##

[Anchor to Related resources](/docs/apps/build/devmcp#related-
resources)Related resources

[![](/images/icons/48/clicode.png)![](/images/icons/48/clicode-
dark.png)Shopify CLICommand-line tool for building Shopify apps and
themes.Shopify CLICommand-line tool for building Shopify apps and
themes.](/docs/apps/build/cli-for-apps)

[Shopify CLI  
  
Command-line tool for building Shopify apps and themes.](/docs/apps/build/cli-
for-apps)

[![](/images/icons/48/mcp.png)![](/images/icons/48/mcp-dark.png)Storefront
MCPConnect AI assistants to real-time commerce data for customer-facing
shopping experiences.Storefront MCPConnect AI assistants to real-time commerce
data for customer-facing shopping experiences.](/docs/apps/build/storefront-
mcp)

[Storefront MCP  
  
Connect AI assistants to real-time commerce data for customer-facing shopping
experiences.](/docs/apps/build/storefront-mcp)

* * *

Was this page helpful?

YesNo

  * [How it works](/docs/apps/build/devmcp#how-it-works)
  * [Requirements](/docs/apps/build/devmcp#requirements)
  * [What you can ask your AI assistant](/docs/apps/build/devmcp#what-you-can-ask-your-ai-assistant)
  * [Supported APIs](/docs/apps/build/devmcp#supported-apis)
  * [Set up the server](/docs/apps/build/devmcp#set-up-the-server)
  * [Available tools](/docs/apps/build/devmcp#available-tools)
  * [Related resources](/docs/apps/build/devmcp#related-resources)

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

