# Source: https://shopify.dev/docs/apps/launch/deployment/deploy-to-google-cloud-run#next-steps

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

  * ### Quality assurance

    * [Going live](/docs/apps/launch)
    * [Checklist of requirements](/docs/apps/launch/app-requirements-checklist)
    * Built for Shopify

    * [Privacy requirements](/docs/apps/launch/privacy-requirements)
    * [Work with protected customer data](/docs/apps/launch/protected-customer-data)
  * ### Pricing strategy

    * [About billing for your app](/docs/apps/launch/billing)
    * [Managed pricing](/docs/apps/launch/billing/managed-pricing)
    * [Redirect to plan selection](/docs/apps/launch/billing/redirect-plan-selection-page)
    * [Offer free trials](/docs/apps/launch/billing/offer-free-trials)
    * Subscription billing

    * [Support one-time purchases](/docs/apps/launch/billing/support-one-time-purchases)
    * [Award app credits](/docs/apps/launch/billing/award-app-credits)
    * [Refund app charges](/docs/apps/launch/billing/refund-app-charges)
    * [View charges and earnings](/docs/apps/launch/billing/view-charges-earnings)
  * ### Deployment

    * [About deployment](/docs/apps/launch/deployment)
    * [Deploy to Google Cloud Run](/docs/apps/launch/deployment/deploy-to-google-cloud-run)
    * [Deploy to a hosting service](/docs/apps/launch/deployment/deploy-to-hosting-service)
    * [About app versions](/docs/apps/launch/deployment/app-versions)
    * [Deploy and release app versions](/docs/apps/launch/deployment/deploy-app-versions)
    * [Deploy app components in a CD pipeline](/docs/apps/launch/deployment/deploy-in-ci-cd-pipeline)
  * ### Reaching customers

    * [About app distribution](/docs/apps/launch/distribution)
    * [Select a distribution method](/docs/apps/launch/distribution/select-distribution-method)
    * [Support your customers](/docs/apps/launch/distribution/support-your-customers)
    * [Sunsetting your app](/docs/apps/launch/distribution/sunsetting-your-app)
    * [Go-to-market success](/docs/apps/launch/distribution/go-to-market-success)
    * [Track app usage](/docs/apps/launch/distribution/track-app-usage)
    * [App listing visibility](/docs/apps/launch/distribution/visibility)
    * [App revenue share](/docs/apps/launch/distribution/revenue-share)
  * ### Shopify app store review

    * [About the Shopify App Store](/docs/apps/launch/app-store-review)
    * [About the app review process](/docs/apps/launch/app-store-review/review-process)
    * [Submit your app for review](/docs/apps/launch/app-store-review/submit-app-for-review)
    * [Pass app review](/docs/apps/launch/app-store-review/pass-app-review)
    * [App listing categories](/docs/apps/launch/app-store-review/app-listing-categories)
    * [Policy violations](/docs/apps/launch/app-store-review/policy-violations)
    * [About app audits](/docs/apps/launch/app-store-review/app-audits)
  * ### Shopify App Store ads

    * [About Shopify App Store ads](/docs/apps/launch/marketing/advertising)
    * [Create ads](/docs/apps/launch/marketing/advertising/create-ads)
    * [Manage ads](/docs/apps/launch/marketing/advertising/manage-ads)
    * [Check ad performance](/docs/apps/launch/marketing/advertising/check-ad-performance)
    * [Ad billing](/docs/apps/launch/marketing/advertising/ad-billing)
    * [Ad permissions](/docs/apps/launch/marketing/advertising/permissions)
    * [Ads FAQ](/docs/apps/launch/marketing/advertising/faq)
  * ### Marketing your app

    * [About marketing your app](/docs/apps/launch/marketing)
    * [Write a press release](/docs/apps/launch/marketing/write-press-release)
    * [Shopify brand assets](/docs/apps/launch/marketing/shopify-brand-assets)
    * [Track your listing traffic](/docs/apps/launch/marketing/track-listing-traffic)
    * [Manage app reviews](/docs/apps/launch/marketing/manage-app-reviews)

Full index

ExpandOn this page

  * [What you'll learn](/docs/apps/launch/deployment/deploy-to-google-cloud-run#what-youll-learn)
  * [How it works](/docs/apps/launch/deployment/deploy-to-google-cloud-run#how-it-works)
  * [Requirements](/docs/apps/launch/deployment/deploy-to-google-cloud-run#requirements)
  * [Step 1: Gather app configuration](/docs/apps/launch/deployment/deploy-to-google-cloud-run#step-1-gather-app-configuration)
  * [Step 2: Create and connect a project](/docs/apps/launch/deployment/deploy-to-google-cloud-run#step-2-create-and-connect-a-project)
  * [Step 3: Configure your project](/docs/apps/launch/deployment/deploy-to-google-cloud-run#step-3-configure-your-project)
  * [Step 4: Manage secrets](/docs/apps/launch/deployment/deploy-to-google-cloud-run#step-4-manage-secrets)
  * [Step 5: Deploy your app to Cloud Run](/docs/apps/launch/deployment/deploy-to-google-cloud-run#step-5-deploy-your-app-to-cloud-run)
  * [Step 6: Set up a production database](/docs/apps/launch/deployment/deploy-to-google-cloud-run#step-6-set-up-a-production-database)
  * [Step 7: Connect your app to Shopify](/docs/apps/launch/deployment/deploy-to-google-cloud-run#step-7-connect-your-app-to-shopify)
  * [Optional: Deploy to multiple regions](/docs/apps/launch/deployment/deploy-to-google-cloud-run#optional-deploy-to-multiple-regions)
  * [Next steps](/docs/apps/launch/deployment/deploy-to-google-cloud-run#next-steps)

# Deploy apps to Google Cloud Run

Copy page MD

This guide shows you how to deploy a Shopify app to [Google Cloud
Run](https://cloud.google.com/run), making your app available to merchants in
production. Deploying to Google Cloud Run provides a scalable, managed hosting
solution that handles the infrastructure so you can focus on your app's
functionality.

Note

This guide focuses on [deploying a Shopify app](/docs/apps/launch/deployment)
to [Google Cloud Run](https://cloud.google.com/run) as it generalizes well to
many common frameworks used to develop apps. Consult the deployment
documentation if you'd rather [deploy to another supported
provider](/docs/apps/launch/deployment#hosting-and-deployment-options), or
[follow general guidelines to manually deploy
elsewhere](/docs/apps/launch/deployment/deploy-to-hosting-service).

A note on permissions and settings

This tutorial demonstrates deploying a CLI-scaffolded React Router app to
Google Cloud Run using simplified permissions and default service accounts.
These settings work for learning and development but are likely over-
permissive for production environments.

Review and adjust IAM permissions and service accounts to match your
organization's security requirements before deploying production apps.

* * *

##

[Anchor to What you'll learn](/docs/apps/launch/deployment/deploy-to-google-
cloud-run#what-youll-learn)What you'll learn

In this guide you'll learn how to do the following tasks:

  * Retrieve sensitive configuration details about your Shopify app needed to deploy.
  * Configure a Cloud Run project to host a Shopify app, including providing access to secrets specific to your Shopify app.
  * Deploy your app's code to either a single or multiple regions on Google Cloud Run, depending on your needs.
  * Test your deployment by reconfiguring your development store to use your new deployment.

Note

References in this guide assume you're deploying a Shopify app built with
[Shopify React Router](/docs/apps/build/build), which automatically handles
key deployment requirements such as authentication, session management,
webhook handling, and environment configuration.

* * *

##

[Anchor to How it works](/docs/apps/launch/deployment/deploy-to-google-cloud-
run#how-it-works)How it works

When you deploy a Shopify app, you're making your code available to merchants.
This involves:

  * Moving your code from your local development environment to a hosting service
  * Connecting your hosted app to Shopify through the Partner Dashboard
  * Managing app extensions and configurations separately through app versions

Your hosting service manages the app's runtime environment and handles
incoming requests through authenticated connections set up in the Partner
Dashboard.

This guide focuses on the first step - moving code from your local development
environment to a hosting service. You will set up a very basic project on
Google Cloud Run, and deploy your app there.

* * *

##

[Anchor to Requirements](/docs/apps/launch/deployment/deploy-to-google-cloud-
run#requirements)Requirements

  * [Scaffold](/docs/apps/build/scaffold-app) and then [Build](/docs/apps/build/build) a Shopify app.
  * [Test your app functionality](/docs/apps/build/cli-for-apps/manage-app-config-files#test-your-app-functionality) in a development environment
  * [Install](https://cloud.google.com/sdk/docs/install) the `gcloud` CLI and authenticate with your account.

* * *

##

[Anchor to Step 1: Gather app
configuration](/docs/apps/launch/deployment/deploy-to-google-cloud-
run#step-1-gather-app-configuration)Step 1: Gather app configuration

Gather the configuration details and credentials from your local development
environment that you'll need to deploy your app to a hosting service.

  1. Use the Shopify CLI to export the API token, API secret, and scopes from your Shopify app into the terminal session by running the following command:

Mac/Linux (bash)Windows (PowerShell)

Copy

9

1

eval $(shopify app info \--web-env)

9

1

shopify app info --web-env | Invoke-Expression

##### Mac/Linux (bash)

         
         eval $(shopify app info --web-env)

##### Windows (PowerShell)

         
         shopify app info --web-env | Invoke-Expression

  2. Generate a `shopify.app.toml` configuration file for the version of your app you're going to deploy by running the `app config link` command below (if you haven't done so already):

## Terminal

Copy

9

1

shopify app config link

* * *

##

[Anchor to Step 2: Create and connect a
project](/docs/apps/launch/deployment/deploy-to-google-cloud-
run#step-2-create-and-connect-a-project)Step 2: Create and connect a project

In this step you will create project to act as a production workspace for this
tutorial, as well as a
[service](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)
that will contain your actual running app code.

  1. Create identifying environment variables for both the service and the project you will reuse throughout this tutorial:

Mac/Linux (bash)Windows (PowerShell)

Copy

9

1

export PROJECT_ID="my-app-name-project" && export SERVICE_NAME="my-app-name-
service"

9

1

$env:PROJECT_ID="my-app-name-project"; $env:SERVICE_NAME="my-app-name-service"

##### Mac/Linux (bash)

         
         export PROJECT_ID="my-app-name-project" && export SERVICE_NAME="my-app-name-service"

##### Windows (PowerShell)

         
         $env:PROJECT_ID="my-app-name-project"; $env:SERVICE_NAME="my-app-name-service"

  2. Create a project on Google Cloud Run:

## Terminal

Copy

9

1

gcloud projects create $PROJECT_ID

  3. Connect your repository to the new project so that all the commands that follow in this tutorial will apply to the project:

## Terminal

Copy

9

1

gcloud config set project $PROJECT_ID

* * *

##

[Anchor to Step 3: Configure your
project](/docs/apps/launch/deployment/deploy-to-google-cloud-
run#step-3-configure-your-project)Step 3: Configure your project

With the project created, you'll now need to configure the project with the
necessary APIs and permissions to deploy and run your Shopify app.

  1. Enable the required APIs for deployment ([Cloud Run Admin API](https://cloud.google.com/run/docs/reference/rest), [Cloud Build API](https://cloud.google.com/build/docs/api), [Secret Manager API](https://cloud.google.com/secret-manager/docs/reference/rest), and the [Artifact Registry API](https://cloud.google.com/artifact-registry/docs/reference/rest)), using the `services enable` command:

## Terminal

Copy

9

1

2

gcloud services enable run.googleapis.com cloudbuild.googleapis.com \

secretmanager.googleapis.com artifactregistry.googleapis.com

  2. Export your Google Cloud account email address to the environment variable `$USER_EMAIL`:

Mac/Linux (bash)Windows (PowerShell)

Copy

9

1

export USER_EMAIL="salma.ayad@example.com"

9

1

$env:USER_EMAIL="salma.ayad@example.com"

##### Mac/Linux (bash)

         
         export USER_EMAIL="salma.ayad@example.com"

##### Windows (PowerShell)

         
         $env:USER_EMAIL="salma.ayad@example.com"

  3. Grant yourself the necessary roles by running the following command:

Mac/Linux (bash)Windows (PowerShell)

Copy

9

1

2

3

for role in "roles/run.developer" "roles/secretmanager.admin"
"roles/iam.serviceAccountUser" "roles/cloudbuild.builds.editor"; do

gcloud projects add-iam-policy-binding $PROJECT_ID
\--member="user:$USER_EMAIL" \--role="$role"

done

9

1

2

3

foreach ($role in @("roles/run.developer", "roles/secretmanager.admin",
"roles/iam.serviceAccountUser", "roles/cloudbuild.builds.editor")) {

gcloud projects add-iam-policy-binding $env:PROJECT_ID
--member="user:$env:USER_EMAIL" --role="$role"

}

##### Mac/Linux (bash)

         
         for role in "roles/run.developer" "roles/secretmanager.admin" "roles/iam.serviceAccountUser" "roles/cloudbuild.builds.editor"; do
           gcloud projects add-iam-policy-binding $PROJECT_ID --member="user:$USER_EMAIL" --role="$role"
         done

##### Windows (PowerShell)

         
         foreach ($role in @("roles/run.developer", "roles/secretmanager.admin", "roles/iam.serviceAccountUser", "roles/cloudbuild.builds.editor")) {
           gcloud projects add-iam-policy-binding $env:PROJECT_ID --member="user:$env:USER_EMAIL" --role="$role"
         }

* * *

##

[Anchor to Step 4: Manage secrets](/docs/apps/launch/deployment/deploy-to-
google-cloud-run#step-4-manage-secrets)Step 4: Manage secrets

In order for your Shopify app to run successfully on Cloud Run, it needs
access to the environment variables you defined at the beginning of this
tutorial. This involves defining secrets for each variable, and configuring
them so that can be accessed at runtime.

In Cloud Run, this means first granting access to a service account (in this
case, the [Compute Engine default service
account](https://docs.cloud.google.com/compute/docs/access/service-
accounts#default_service_account)) that will handle your deployments. Later in
**Step 5** you'll run another command that will actually make the variables
accessible at runtime.

  1. Create secrets in Secret Manager, using the API key and API secret environment variables you created earlier to create secrets for each of them:

API keyAPI secret

Copy

9

1

echo $SHOPIFY_API_KEY | gcloud secrets create shopify-api-key \--data-file=-

9

1

echo $SHOPIFY_API_SECRET | gcloud secrets create shopify-api-secret \--data-file=-

##### API key

         
         echo $SHOPIFY_API_KEY | gcloud secrets create shopify-api-key --data-file=-

##### API secret

         
         echo $SHOPIFY_API_SECRET | gcloud secrets create shopify-api-secret --data-file=-

You can verify that the secrets were created successfully by running the
command below:

## Terminal

Copy

9

1

gcloud secrets list

  2. Run the command below to find and export the unique `PROJECT_NUMBER` associated with your project:

Mac/Linux (bash)Windows (PowerShell)

Copy

9

1

PROJECT_NUMBER=$(gcloud projects describe $PROJECT_ID
\--format="value(projectNumber)")

9

1

$env:PROJECT_NUMBER = gcloud projects describe $env:PROJECT_ID
--format="value(projectNumber)"

##### Mac/Linux (bash)

         
         PROJECT_NUMBER=$(gcloud projects describe $PROJECT_ID --format="value(projectNumber)")

##### Windows (PowerShell)

         
         $env:PROJECT_NUMBER = gcloud projects describe $env:PROJECT_ID --format="value(projectNumber)"

  3. Use `PROJECT_NUMBER` to build the default service account email address associated with your project, and then give it access to the secrets you defined previously through the [Secret Manager Secret Accessor role](https://cloud.google.com/secret-manager/docs/access-control):

## Terminal

Copy

9

1

2

3

gcloud projects add-iam-policy-binding $PROJECT_ID \

\--member="serviceAccount:$PROJECT_NUMBER-
compute@developer.gserviceaccount.com" \

\--role="roles/secretmanager.secretAccessor"

* * *

##

[Anchor to Step 5: Deploy your app to Cloud
Run](/docs/apps/launch/deployment/deploy-to-google-cloud-run#step-5-deploy-
your-app-to-cloud-run)Step 5: Deploy your app to Cloud Run

Deploy your app code to Cloud Run and configure it with the necessary
environment variables to make it accessible online. Note that in the steps
below, it's expected that the first deployment will fail.

Note

This section outlines commands and requirements for deploying your Shopify app
to a single region on Google Cloud Run. Alternatively, your actual
requirements (for example, high availability or serving a global user base)
may require you instead to deploy to [multiple
regions](https://docs.cloud.google.com/run/docs/multiple-regions).

In that case, skip ahead to Deploy to multiple regions if you need multi-
region support.

  1. Define the [region location](https://cloud.google.com/run/docs/locations) your app will be deployed to. Run the command below, substituting the region example with one of your choosing:

Mac/Linux (bash)Windows (PowerShell)

Copy

9

1

export SERVICE_REGION="us-central1"

9

1

$env:SERVICE_REGION="us-central1"

##### Mac/Linux (bash)

         
         export SERVICE_REGION="us-central1"

##### Windows (PowerShell)

         
         $env:SERVICE_REGION="us-central1"

  2. Deploy your code to the Cloud Run service you've defined by running the command below from your Shopify app's project directory:

## Terminal

Copy

9

1

2

3

4

5

6

7

gcloud run deploy $SERVICE_NAME \

\--source . \

\--region $SERVICE_REGION \

\--set-secrets="SHOPIFY_API_KEY=shopify-api-
key:latest,SHOPIFY_API_SECRET=shopify-api-secret:latest" \

\--set-env-vars="SCOPES=$SCOPES" \

\--port 3000 \

\--allow-unauthenticated

This first deployment _will_ fail with the error `The user-provided container
failed to start`, and this is expected. The Shopify app fails at runtime when
it's unable to locate the expected `SHOPIFY_APP_URL` environment variable,
which you haven't yet defined.

This variable corresponds to the unique URL of the service you've just
deployed, but you couldn't access _until_ it was deployed.

Note

By default, [Shopify React Router](/docs/apps/build/build) built apps run on
port 3000 defined in their `Dockerfile`, while the Cloud Run service uses port
8088. This behavior is overwritten in the passed `--port` flag in the command
above.

Update the command if you have overwritten this default port, or if your app
has a different one.

The `--source .` flag uses [Google Cloud's buildpacks and Cloud
Build](https://docs.cloud.google.com/run/docs/deploying-source-code) to
automatically build container images from your source code. An Artifact
Registry Docker repository will be built automatically for you in your
`SERVICE_REGION`. For production deployments, consider building and submitting
custom container images and passing the `--image` flag instead.

  3. Run the following command to retrieve the service URL now that the service has deployed:

## Command

Copy

9

1

SHOPIFY_APP_URL=$(gcloud run services list
\--filter="metadata.name:$SERVICE_NAME" \--format="get(URL)")

  4. Rerun the deploy command again, now including the expected `SHOPIFY_APP_URL` environment variable in that command:

## Command

Copy

9

1

2

3

4

5

6

7

gcloud run deploy $SERVICE_NAME \

\--source . \

\--region $SERVICE_REGION \

\--set-secrets="SHOPIFY_API_KEY=shopify-api-
key:latest,SHOPIFY_API_SECRET=shopify-api-secret:latest" \

\--set-env-vars="SCOPES=$SCOPES,SHOPIFY_APP_URL=$SHOPIFY_APP_URL" \

\--port 3000 \

\--allow-unauthenticated

  5. Visit `SHOPIFY_APP_URL` or run the command below to verify the service is functioning correctly:

## Command

Copy

9

1

gcloud run services describe $SERVICE_NAME \--region $SERVICE_REGION

* * *

##

[Anchor to Step 6: Set up a production
database](/docs/apps/launch/deployment/deploy-to-google-cloud-run#step-6-set-
up-a-production-database)Step 6: Set up a production database

The default SQLite database used in local development won't work for your
deployed app on Cloud Run long term. Sessions and data would be lost on every
deployment.

To fix this, you'll set up a persistent PostgreSQL database using Cloud SQL
and configure your app to use it in production while keeping SQLite for local
development.

  1. Create a `prisma/schema.prod.prisma` file for your production schema with the following content:

## prisma/schema.prod.prisma

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

33

34

35

36

37

38

generator client {

provider = "prisma-client-js"

}

  

datasource db {

provider = "postgresql"

url = env("DATABASE_URL")

}

  

model Session {

id String @id

shop String

state String

isOnline Boolean @default(false)

scope String?

expires DateTime?

accessToken String

userId BigInt?

firstName String?

lastName String?

email String?

accountOwner Boolean @default(false)

locale String?

collaborator Boolean @default(false)

emailVerified Boolean @default(false)

}

  

model QRCode {

id Int @id @default(autoincrement())

title String

shop String

productId String

productHandle String

productVariantId String

destination String

scans Int @default(0)

createdAt DateTime @default(now())

}

The new file should be identical to your existing `prisma/schema.prisma` file,
with only the `datasource db` configuration changing to now suit the
PostgreSQL `provider`.

  2. Update your `Dockerfile` to match the following contents:

## Dockerfile

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

FROM node:20-alpine

RUN apk add --no-cache openssl curl

  

# Download Cloud SQL Auth Proxy

RUN curl -o /cloud-sql-proxy https://storage.googleapis.com/cloud-sql-
connectors/cloud-sql-proxy/v2.14.1/cloud-sql-proxy.linux.amd64

RUN chmod +x /cloud-sql-proxy

  

EXPOSE 3000

  

WORKDIR /app

  

ENV NODE_ENV=production

  

COPY package.json package-lock.json* ./

  

RUN npm ci --omit=dev && npm cache clean --force

  

COPY . .

  

# Use production schema for PostgreSQL

RUN cp prisma/schema.prod.prisma prisma/schema.prisma

  

# Delete SQLite migrations (incompatible with PostgreSQL)

RUN rm -rf prisma/migrations

  

RUN npm run build

  

# Copy and set permissions for startup script

RUN chmod +x start.sh

  

CMD ["sh", "start.sh"]

Notice what's changed here:

     1. **[4-6] Download Cloud SQL Auth Proxy:** The [Cloud SQL Proxy](https://docs.cloud.google.com/sql/docs/mysql/sql-proxy) creates a standard TCP endpoint at `localhost:5432` inside the container, allowing Prisma to connect using familiar TCP connections.
     2. **[20-21] Use production schema for PostgreSQL:** Prisma requires the database `provider` to be hardcoded at build time. Instead of changing the local behavior of this app, these lines overwrite the schema using PostgreSQL only in the production context.
     3. **[23-24] Delete SQLite migrations (incompatible with PostgreSQL):** SQLite migrations would fail when applied to a PostgreSQL database, so they are deleted. You will use `prisma db push` to create tables directly from the schema instead in a later step in this tutorial.
     4. **[28-31] Copy and set permissions for startup script:** Because app requires that the database connection is available when Prisma interacts with it, running the multiple commands required to make this work is simpler when included in a dedicated script.
  3. Create a `start.sh` script in your project root containing the following:

## start.sh

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

#!/bin/sh

  

# Start Cloud SQL Proxy in background

/cloud-sql-proxy \--port 5432 ${INSTANCE_CONNECTION_NAME} &

  

# Wait for proxy to be ready

sleep 3

  

# Run production setup and start the app

npm run setup:prod && npm run start

This script launches the Cloud SQL Proxy before the app starts, ensuring the
database connection is available when Prisma tries to generate the client and
sync the schema.

  4. Add a `setup:prod` script to your `package.json` file to specifically handle migrations in the production context:

## package.json

Copy

9

1

"setup:prod": "prisma generate && prisma db push"

  5. Enable the [Cloud SQL Admin API](https://docs.cloud.google.com/sql/docs/mysql/admin-api) on the project:

## Terminal

Copy

9

1

gcloud services enable sqladmin.googleapis.com

  6. Create a password for your database:

## Terminal

Copy

9

1

export DB_PASSWORD="your-secure-password"

  7. Create a PostgreSQL database instance that will persist across deployments:

## Terminal

Copy

9

1

2

3

4

5

gcloud sql instances create ${SERVICE_NAME}-db \

\--database-version=POSTGRES_15 \

\--tier=db-f1-micro \

\--region=$SERVICE_REGION \

\--root-password=$DB_PASSWORD

Note

This command can take as long as 10 minutes to complete.

You can verify the instance is running correctly at this point by running the
following command:

## Terminal

Copy

9

1

gcloud sql instances describe ${SERVICE_NAME}-db \--format="get(state)"

Note

This command should return `RUNNABLE`.

  8. Create an application database called `shopify_app` in the instance:

## Terminal

Copy

9

1

gcloud sql databases create shopify_app \--instance=${SERVICE_NAME}-db

  9. Retrieve the Service Account you've configured in this tutorial:

## Terminal

Copy

9

1

SERVICE_ACCOUNT=$(gcloud run services describe $SERVICE_NAME
\--region=$SERVICE_REGION
\--format="value(spec.template.spec.serviceAccountName)")

  10. Grant the [Cloud SQL Client](https://docs.cloud.google.com/sql/docs/mysql/roles-and-permissions) role for the Service Account:

## Terminal

Copy

9

1

2

3

gcloud projects add-iam-policy-binding $PROJECT_ID \

\--member="serviceAccount:${SERVICE_ACCOUNT}" \

\--role="roles/cloudsql.client"

  11. Get the Cloud SQL connection name:

## Terminal

Copy

9

1

CONNECTION_NAME=$(gcloud sql instances describe ${SERVICE_NAME}-db
\--format="get(connectionName)")

  12. Build the DATABASE_URL connection string:

## Terminal

Copy

9

1

DATABASE_URL="postgresql://postgres:${DB_PASSWORD}@localhost:5432/shopify_app"

  13. Update the Cloud Run service with all configurations:

## Terminal

Copy

9

1

2

3

4

gcloud run services update $SERVICE_NAME \

\--region=$SERVICE_REGION \

\--add-cloudsql-instances=$CONNECTION_NAME \

\--update-env-
vars="DATABASE_URL=$DATABASE_URL,INSTANCE_CONNECTION_NAME=$CONNECTION_NAME,SHOPIFY_APP_URL=$SHOPIFY_APP_URL"

  14. Deploy the updated application:

## Terminal

Copy

9

1

2

3

4

gcloud run deploy $SERVICE_NAME \

\--source . \

\--region=$SERVICE_REGION \

\--allow-unauthenticated

* * *

##

[Anchor to Step 7: Connect your app to
Shopify](/docs/apps/launch/deployment/deploy-to-google-cloud-
run#step-7-connect-your-app-to-shopify)Step 7: Connect your app to Shopify

Connect your deployed app to Shopify by updating your app configuration with
the new service URL and testing the integration.

  1. Update your `shopify.app.toml` file with the Cloud Run service URL:

## shopify.app.toml

Copy

9

1

application_url = "https://gcp-test-app-xyz123-uc.us-central1.run.app"

  2. Push your configuration to your Shopify development store to verify the service is now accessible:

## Terminal

Copy

9

1

shopify app deploy

  3. Test that the core functionality of your app is still working, now that your store is communicating with the Cloud Run service rather than your local installation.

* * *

##

[Anchor to Optional: Deploy to multiple
regions](/docs/apps/launch/deployment/deploy-to-google-cloud-run#optional-
deploy-to-multiple-regions)Optional: Deploy to multiple regions

Your app may serve a global user base, require high availability, or otherwise
have regionally-specific performance considerations. In these cases, you can
deploy to multiple regions, then use a global load balancer to route traffic
to the nearest region.

Note

Multi-region deployment adds complexity and cost (load balancer fees). For
most apps, single-region deployment is sufficient. Consult Step 5 if you don't
need multi-region support.

Make sure to complete steps 1-6 in the tutorial above before proceeding.

###

[Anchor to Step 1: Deploy to regions](/docs/apps/launch/deployment/deploy-to-
google-cloud-run#step-1-deploy-to-regions)Step 1: Deploy to regions

  1. Choose your target regions from the [available Cloud Run locations](https://cloud.google.com/run/docs/locations). In this guide, we'll use `us-central1` (United States), `europe-west1` (Belgium), and `asia-northeast1` (Tokyo). Replace in the subsequent commands with your real world requirements.

  2. Deploy your app to each region using the command below:

Mac/Linux (bash)Windows (PowerShell)

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

for region in us-central1 europe-west1 asia-northeast1; do

gcloud run deploy $SERVICE_NAME-$region \

\--source . \

\--region $region \

\--set-secrets="SHOPIFY_API_KEY=shopify-api-
key:latest,SHOPIFY_API_SECRET=shopify-api-secret:latest" \

\--set-env-
vars="SCOPES=$SCOPES,DATABASE_URL=$DATABASE_URL,INSTANCE_CONNECTION_NAME=$CONNECTION_NAME"
\

\--add-cloudsql-instances=$CONNECTION_NAME \

\--port 3000 \

\--no-allow-unauthenticated

done

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

foreach ($region in @("us-central1", "europe-west1", "asia-northeast1")) {

gcloud run deploy "$env:SERVICE_NAME-$region" `

\--source . `

\--region $region `

\--set-secrets="SHOPIFY_API_KEY=shopify-api-
key:latest,SHOPIFY_API_SECRET=shopify-api-secret:latest" `

\--set-env-
vars="SCOPES=$env:SCOPES,DATABASE_URL=$env:DATABASE_URL,INSTANCE_CONNECTION_NAME=$env:CONNECTION_NAME"
`

\--add-cloudsql-instances=$env:CONNECTION_NAME `

\--port 3000 `

\--no-allow-unauthenticated

}

##### Mac/Linux (bash)

         
         for region in us-central1 europe-west1 asia-northeast1; do
           gcloud run deploy $SERVICE_NAME-$region \
             --source . \
             --region $region \
             --set-secrets="SHOPIFY_API_KEY=shopify-api-key:latest,SHOPIFY_API_SECRET=shopify-api-secret:latest" \
             --set-env-vars="SCOPES=$SCOPES,DATABASE_URL=$DATABASE_URL,INSTANCE_CONNECTION_NAME=$CONNECTION_NAME" \
             --add-cloudsql-instances=$CONNECTION_NAME \
             --port 3000 \
             --no-allow-unauthenticated
         done

##### Windows (PowerShell)

         
         foreach ($region in @("us-central1", "europe-west1", "asia-northeast1")) {
           gcloud run deploy "$env:SERVICE_NAME-$region" `
             --source . `
             --region $region `
             --set-secrets="SHOPIFY_API_KEY=shopify-api-key:latest,SHOPIFY_API_SECRET=shopify-api-secret:latest" `
             --set-env-vars="SCOPES=$env:SCOPES,DATABASE_URL=$env:DATABASE_URL,INSTANCE_CONNECTION_NAME=$env:CONNECTION_NAME" `
             --add-cloudsql-instances=$env:CONNECTION_NAME `
             --port 3000 `
             --no-allow-unauthenticated
         }

In this tutorial, all regions connect to the same Cloud SQL instance. The
database remains in the original `$SERVICE_REGION`, which may add latency for
distant regions. Like the single region deployment in previous steps, this
command will fail for each region until we provide the load balancer URL in a
later step.

Note

We use `--no-allow-unauthenticated` because the load balancer will handle
public access.

  3. Create a [Network Endpoint Group (NEG)](https://docs.cloud.google.com/load-balancing/docs/negs) for each regional Cloud Run service:

Mac/Linux (bash)Windows (PowerShell)

Copy

9

1

2

3

4

5

6

for region in us-central1 europe-west1 asia-northeast1; do

gcloud compute network-endpoint-groups create $SERVICE_NAME-neg-$region \

\--region=$region \

\--network-endpoint-type=serverless \

\--cloud-run-service=$SERVICE_NAME-$region

done

9

1

2

3

4

5

6

foreach ($region in @("us-central1", "europe-west1", "asia-northeast1")) {

gcloud compute network-endpoint-groups create "$env:SERVICE_NAME-neg-$region"
`

\--region=$region `

\--network-endpoint-type=serverless `

\--cloud-run-service="$env:SERVICE_NAME-$region"

}

##### Mac/Linux (bash)

         
         for region in us-central1 europe-west1 asia-northeast1; do
           gcloud compute network-endpoint-groups create $SERVICE_NAME-neg-$region \
             --region=$region \
             --network-endpoint-type=serverless \
             --cloud-run-service=$SERVICE_NAME-$region
         done

##### Windows (PowerShell)

         
         foreach ($region in @("us-central1", "europe-west1", "asia-northeast1")) {
           gcloud compute network-endpoint-groups create "$env:SERVICE_NAME-neg-$region" `
             --region=$region `
             --network-endpoint-type=serverless `
             --cloud-run-service="$env:SERVICE_NAME-$region"
         }

###

[Anchor to Step 2: Configure load
balancer](/docs/apps/launch/deployment/deploy-to-google-cloud-
run#step-2-configure-load-balancer)Step 2: Configure load balancer

  1. Create a backend service that will route traffic to your regional services:

## Terminal

Copy

9

1

2

3

gcloud compute backend-services create $SERVICE_NAME-backend \

\--global \

\--load-balancing-scheme=EXTERNAL_MANAGED

  2. Add each NEG as a backend:

Mac/Linux (bash)Windows (PowerShell)

Copy

9

1

2

3

4

5

6

for region in us-central1 europe-west1 asia-northeast1; do

gcloud compute backend-services add-backend $SERVICE_NAME-backend \

\--global \

\--network-endpoint-group=$SERVICE_NAME-neg-$region \

\--network-endpoint-group-region=$region

done

9

1

2

3

4

5

6

foreach ($region in @("us-central1", "europe-west1", "asia-northeast1")) {

gcloud compute backend-services add-backend $env:SERVICE_NAME-backend `

\--global `

\--network-endpoint-group="$env:SERVICE_NAME-neg-$region" `

\--network-endpoint-group-region=$region

}

##### Mac/Linux (bash)

         
         for region in us-central1 europe-west1 asia-northeast1; do
           gcloud compute backend-services add-backend $SERVICE_NAME-backend \
             --global \
             --network-endpoint-group=$SERVICE_NAME-neg-$region \
             --network-endpoint-group-region=$region
         done

##### Windows (PowerShell)

         
         foreach ($region in @("us-central1", "europe-west1", "asia-northeast1")) {
           gcloud compute backend-services add-backend $env:SERVICE_NAME-backend `
             --global `
             --network-endpoint-group="$env:SERVICE_NAME-neg-$region" `
             --network-endpoint-group-region=$region
         }

  3. Create a URL map to route all traffic to your backend service:

## Terminal

Copy

9

1

2

gcloud compute url-maps create $SERVICE_NAME-url-map \

\--default-service=$SERVICE_NAME-backend

  4. Reserve a static external IP address for your load balancer:

## Terminal

Copy

9

1

2

gcloud compute addresses create $SERVICE_NAME-ip \

\--global

  5. Retrieve the IP address:

## Terminal

Copy

9

1

2

3

LOAD_BALANCER_IP=$(gcloud compute addresses describe $SERVICE_NAME-ip \

\--global \

\--format="get(address)")

  6. In your domain registrar, create an A record pointing to the load balancer IP address:

Copy

9

1

2

3

Type: A

Name: app (or your subdomain)

Value: [LOAD_BALANCER_IP]

Going forward, your load balancer URL will be `https://app.yourdomain.com` (or
your chosen subdomain).

  7. Wait for DNS propagation (typically 5-15 minutes) and verify the command below returns your load balancer IP address:

## Terminal

Copy

9

1

nslookup app.yourdomain.com

  8. Create a managed SSL certificate for your domain:

## Terminal

Copy

9

1

2

3

gcloud compute ssl-certificates create $SERVICE_NAME-ssl-cert \

\--domains=app.yourdomain.com \

\--global

  9. Create an HTTPS target proxy:

## Terminal

Copy

9

1

2

3

gcloud compute target-https-proxies create $SERVICE_NAME-https-proxy \

\--url-map=$SERVICE_NAME-url-map \

\--ssl-certificates=$SERVICE_NAME-ssl-cert

  10. Create a global forwarding rule using the reserved IP:

## Terminal

Copy

9

1

2

3

4

5

gcloud compute forwarding-rules create $SERVICE_NAME-forwarding-rule \

\--global \

\--address=$SERVICE_NAME-ip \

\--target-https-proxy=$SERVICE_NAME-https-proxy \

\--ports=443

  11. Check SSL certificate provisioning status:

## Terminal

Copy

9

1

2

3

gcloud compute ssl-certificates describe $SERVICE_NAME-ssl-cert \

\--global \

\--format="get(managed.status)"

Wait for status to change from `PROVISIONING` to `ACTIVE` before testing. This
can take up to 60 minutes.

###

[Anchor to Step 3: Redeploy and verify](/docs/apps/launch/deployment/deploy-
to-google-cloud-run#step-3-redeploy-and-verify)Step 3: Redeploy and verify

  1. Grant public access to each regional service so the load balancer can route traffic to them:

## Terminal

Copy

9

1

2

3

4

5

6

for region in us-central1 europe-west1 asia-northeast1; do

gcloud run services add-iam-policy-binding $SERVICE_NAME-$region \

\--region=$region \

\--member="allUsers" \

\--role="roles/run.invoker"

done

  2. Export the newly defined load balancer URL:

## Terminal

Copy

9

1

export LOAD_BALANCER_URL="https://app.yourdomain.com"

  3. Redeploy each regional service with the load balancer URL:

Mac/Linux (bash)Windows (PowerShell)

Copy

9

1

2

3

4

5

6

for region in us-central1 europe-west1 asia-northeast1; do

gcloud run deploy $SERVICE_NAME-$region \

\--source . \

\--region $region \

\--update-env-vars="SHOPIFY_APP_URL=$LOAD_BALANCER_URL"

done

9

1

2

3

4

5

6

7

8

$env:LOAD_BALANCER_URL="https://app.yourdomain.com"

  

foreach ($region in @("us-central1", "europe-west1", "asia-northeast1")) {

gcloud run deploy "$env:SERVICE_NAME-$region" `

\--source . `

\--region $region `

\--update-env-vars="SHOPIFY_APP_URL=$env:LOAD_BALANCER_URL"

}

##### Mac/Linux (bash)

         
         for region in us-central1 europe-west1 asia-northeast1; do
           gcloud run deploy $SERVICE_NAME-$region \
             --source . \
             --region $region \
             --update-env-vars="SHOPIFY_APP_URL=$LOAD_BALANCER_URL"
         done

##### Windows (PowerShell)

         
         $env:LOAD_BALANCER_URL="https://app.yourdomain.com"
         
         foreach ($region in @("us-central1", "europe-west1", "asia-northeast1")) {
           gcloud run deploy "$env:SERVICE_NAME-$region" `
             --source . `
             --region $region `
             --update-env-vars="SHOPIFY_APP_URL=$env:LOAD_BALANCER_URL"
         }

  4. Verify that your load balancer is routing traffic correctly:

## Terminal

Copy

9

1

curl -I https://app.yourdomain.com

You can test from different geographic locations using services like [Global
Ping](https://www.globalping.io/) to verify regional routing.

  5. Update your `shopify.app.toml` file with your load balancer URL:

## shopify.app.toml

Copy

9

1

application_url = "https://app.yourdomain.com"

  6. Push your configuration to your Shopify development store to verify the service is now accessible:

## Terminal

Copy

9

1

shopify app deploy

  7. Test that the core functionality of your app is still working, now that your store is communicating with the Cloud Run services rather than your local installation.

* * *

##

[Anchor to Next steps](/docs/apps/launch/deployment/deploy-to-google-cloud-
run#next-steps)Next steps

Now that your app is deployed and connected to Shopify, you can explore these
related topics:

  * [Launch your app](/docs/apps/launch) to learn about app distribution and the review process.

* * *

Was this page helpful?

YesNo

  * [What you'll learn](/docs/apps/launch/deployment/deploy-to-google-cloud-run#what-youll-learn)
  * [How it works](/docs/apps/launch/deployment/deploy-to-google-cloud-run#how-it-works)
  * [Requirements](/docs/apps/launch/deployment/deploy-to-google-cloud-run#requirements)
  * [Step 1: Gather app configuration](/docs/apps/launch/deployment/deploy-to-google-cloud-run#step-1-gather-app-configuration)
  * [Step 2: Create and connect a project](/docs/apps/launch/deployment/deploy-to-google-cloud-run#step-2-create-and-connect-a-project)
  * [Step 3: Configure your project](/docs/apps/launch/deployment/deploy-to-google-cloud-run#step-3-configure-your-project)
  * [Step 4: Manage secrets](/docs/apps/launch/deployment/deploy-to-google-cloud-run#step-4-manage-secrets)
  * [Step 5: Deploy your app to Cloud Run](/docs/apps/launch/deployment/deploy-to-google-cloud-run#step-5-deploy-your-app-to-cloud-run)
  * [Step 6: Set up a production database](/docs/apps/launch/deployment/deploy-to-google-cloud-run#step-6-set-up-a-production-database)
  * [Step 7: Connect your app to Shopify](/docs/apps/launch/deployment/deploy-to-google-cloud-run#step-7-connect-your-app-to-shopify)
  * [Optional: Deploy to multiple regions](/docs/apps/launch/deployment/deploy-to-google-cloud-run#optional-deploy-to-multiple-regions)
  * [Next steps](/docs/apps/launch/deployment/deploy-to-google-cloud-run#next-steps)

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

