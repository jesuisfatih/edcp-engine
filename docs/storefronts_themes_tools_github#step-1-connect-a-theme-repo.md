# Source: https://shopify.dev/docs/storefronts/themes/tools/github#step-1-connect-a-theme-repo

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

  * [Features](/docs/storefronts/themes/tools/github#features)
  * [How it works](/docs/storefronts/themes/tools/github#how-it-works)
  * [Limitations](/docs/storefronts/themes/tools/github#limitations)
  * [Repository structure](/docs/storefronts/themes/tools/github#repository-structure)
  * [Branch management strategies](/docs/storefronts/themes/tools/github#branch-management-strategies)
  * [Step 1: Connect a theme repo](/docs/storefronts/themes/tools/github#step-1-connect-a-theme-repo)
  * [Step 2: Test the connection](/docs/storefronts/themes/tools/github#step-2-test-the-connection)
  * [Step 3: Publish the theme](/docs/storefronts/themes/tools/github#step-3-publish-the-theme)

# Shopify GitHub integration for themes

Copy page MD

The [Shopify GitHub app](/docs/api/github-app) lets you connect your GitHub
and Shopify accounts. This lets you sync theme code to and from GitHub
repositories and collaborate with other developers on your themes.

* * *

##

[Anchor to Features](/docs/storefronts/themes/tools/github#features)Features

  * Automatically pull and push theme code from any organization or repository associated with your GitHub account
  * Connect one or more branches from a repository to easily develop and test new theme features or campaigns
  * Keep a theme up to date with commits to a branch, and track edits made in the Shopify admin, including the [code editor](/docs/storefronts/themes/tools/code-editor) and [theme editor](/docs/storefronts/themes/tools/online-editor)
  * Connect branches to unpublished or published themes

* * *

##

[Anchor to How it works](/docs/storefronts/themes/tools/github#how-it-
works)How it works

The GitHub theme integration updates your theme in the Shopify admin whenever
the connected branch is updated. It also commits changes made through the
Shopify admin to the branch to ensure that the branch and theme in the Shopify
admin always match.

Note

Files are updated in GitHub whenever changes are made to a connected theme.
This can't be disabled. If you want to separate the code that Shopify has
access to from the rest of your code, then consider using multiple
repositories or subtrees. For more information, refer to [Version control best
practices for Shopify themes](/docs/storefronts/themes/best-practices/version-
control).

###

[Anchor to Commits by Shopify](/docs/storefronts/themes/tools/github#commits-
by-shopify)Commits by Shopify

When your theme is edited through the Shopify admin, any changes are
automatically committed to your repository by Shopify. A commit is created
when any owner, staff member, or collaborator makes changes. Changes are added
as a commit to the connected branch when they are saved.

You can edit your theme in the following areas of the Shopify admin:

  * The [theme editor](/docs/storefronts/themes/tools/online-editor). When you customize a theme using the theme editor, these customizations are stored in [setting files](/docs/storefronts/themes/architecture/settings), which are part of the theme code.
  * The [code editor](/docs/storefronts/themes/tools/code-editor).
  * [Theme apps](/docs/apps/build/online-store) installed in the Online Store.

####

[Anchor to Organization
access](/docs/storefronts/themes/tools/github#organization-access)Organization
access

If you grant the Shopify GitHub app access to repositories in a GitHub
organization, then any user that has a GitHub account that is part of the
organization, and has the **Manage themes** permission or **Themes**
permission, can view any repository that the app has access to in the list of
available repositories. However, these users can only connect branches for
which they have write permissions, and the branch needs to match the required
repository structure.

If you want to prevent users from viewing certain repositories, then you
should grant Shopify’s GitHub app access to only the repositories that you
want to connect to the Shopify store. If you grant access to only specific
repositories and you create a new repository that you want to use with
Shopify, then you need to [grant the app access to the repository through
GitHub](https://docs.github.com/en/organizations/keeping-your-organization-
secure/reviewing-your-organizations-installed-integrations).

###

[Anchor to Conflicts and error
handling](/docs/storefronts/themes/tools/github#conflicts-and-error-
handling)Conflicts and error handling

If a user is editing an open file in the theme editor while the same file is
being edited in GitHub or the code editor, then the user is warned that
they're overriding the new changes when they save.

There are currently no conflict alerts in the code editor. The version of the
file in the code editor overwrites the GitHub version of the file.

In case of a conflict in commits or pushes made outside Shopify, the developer
has a chance to resolve it in GitHub or force push the change to overwrite the
file in Shopify.

In limited cases, conflicts might occur if a file is saved in the theme editor
or code editor and a change is pushed to the GitHub branch simultaneously. In
this case, the commit coming from Shopify might be viewed as outdated and
rejected by GitHub.

If you suspect that an error has occurred when pushing or pulling changes,
then you can view the logs for the last few version control events by clicking
**View logs** beside the **Last saved** timestamp on the theme card.

If you believe that the theme has fallen out of date with the branch, then you
can pull the latest version of the branch manually by going to the theme card
and selecting **Actions** > **Reset to last commit**.

* * *

##

[Anchor to
Limitations](/docs/storefronts/themes/tools/github#limitations)Limitations

  * Only repositories to which you have write access can be used to create a new theme.
  * Outside collaborators can't connect branches. Only members of the organization with write access can.
  * Personal repositories where you're a collaborator, but not the owner, aren't visible in the list of available repositories.

* * *

##

[Anchor to Repository
structure](/docs/storefronts/themes/tools/github#repository-
structure)Repository structure

You can connect only branches that match the default Shopify theme [folder
structure](/docs/storefronts/themes/architecture#directory-structure-and-
component-types). This structure represents a buildless theme, or a theme that
has already gone through any necessary [file
transformations](/docs/storefronts/themes/best-practices/file-transformation).

Folders in the repository that don't match the default theme structure are
ignored.

* * *

##

[Anchor to Branch management
strategies](/docs/storefronts/themes/tools/github#branch-management-
strategies)Branch management strategies

Consider the following when managing themes connected to GitHub repositories
in Shopify:

  * You can't reconnect a branch to a theme after it has been disconnected. If you reconnect a branch, then it's added as a new theme.

  * If an unpublished theme is connected to a branch and then published, then it maintains its connection to the branch.

To understand the relationship between branches and themes, and how to
optimize your workflow to use branches effectively, refer to our [version
control best practices](/docs/storefronts/themes/best-practices/version-
control).

* * *

##

[Anchor to Step 1: Connect a theme
repo](/docs/storefronts/themes/tools/github#step-1-connect-a-theme-repo)Step
1: Connect a theme repo

Make sure you've installed the [Shopify GitHub app](/docs/api/github-app)
first.

  1. From your Shopify admin, go to **Online Store** > **Themes**.
  2. In the **Theme library** section, click **Add theme** > **Connect from GitHub**.
  3. In the **Connect theme** pane, select your organization or account.
  4. Under **Repository** , select your repo.
  5. Under **Branch** , search for the branch you want to connect.

The theme appears in your theme library. Themes that are connected to GitHub
list the repository, branch name, and last commit time on the theme card.

* * *

##

[Anchor to Step 2: Test the
connection](/docs/storefronts/themes/tools/github#step-2-test-the-
connection)Step 2: Test the connection

Try making a small change to the theme and then verify that a commit was made
in the branch.

  1. From your Shopify admin, go to **Online Store** > **Themes**.
  2. On the theme that's connected to GitHub, click **Customize**.
  3. Change any setting in your theme. For example, in Dawn, you might change the text on the announcement bar.
  4. Click **Save** , and then exit the theme editor.
  5. In the theme library, on the card for the theme, click the name of the branch to navigate to GitHub.
  6. Note the most recent commit. It should list the `shopify` bot as the author of the commit.

![A commit from Shopify in the GitHub
repo](https://cdn.shopify.com/shopifycloud/shopify-
dev/production/assets/assets/images/themes/github/github-update-CZXTUcSD.png)

If desired, you can also push a change to the branch from your local machine.
After you push a commit to your branch, the **Last saved** date on the theme
updates and the change is visible in the theme.

![The card for a theme that's connected to
GitHub](https://cdn.shopify.com/shopifycloud/shopify-
dev/production/assets/assets/images/themes/github/github-card-C62fPPvl.png)

* * *

##

[Anchor to Step 3: Publish the
theme](/docs/storefronts/themes/tools/github#step-3-publish-the-theme)Step 3:
Publish the theme

To track changes to your published theme, you need to publish a theme from
your theme library that's connected to a GitHub branch. You might add your
main branch as a theme so you can keep your [published theme up to
date](/docs/storefronts/themes/best-practices/version-control) using Git.

* * *

Was this page helpful?

YesNo

  * [Features](/docs/storefronts/themes/tools/github#features)
  * [How it works](/docs/storefronts/themes/tools/github#how-it-works)
  * [Limitations](/docs/storefronts/themes/tools/github#limitations)
  * [Repository structure](/docs/storefronts/themes/tools/github#repository-structure)
  * [Branch management strategies](/docs/storefronts/themes/tools/github#branch-management-strategies)
  * [Step 1: Connect a theme repo](/docs/storefronts/themes/tools/github#step-1-connect-a-theme-repo)
  * [Step 2: Test the connection](/docs/storefronts/themes/tools/github#step-2-test-the-connection)
  * [Step 3: Publish the theme](/docs/storefronts/themes/tools/github#step-3-publish-the-theme)

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

