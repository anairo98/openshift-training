# 5. Hands-On Lab

## Tasks

### Task 0: Recap Task

1. Create a Secret with name "wealthapp", that contains the following keys and values:

    !!! tip
        You can do this directly in the WebUI, which shows a form for creating secrets. If you need further information about secrets, refer to the [Secret documentation](https://docs.redhat.com/en/documentation/openshift_container_platform/4.17/html/nodes/working-with-pods#nodes-pods-secrets).

| Key         | Value      |
|-------------|------------|
| DB_USERNAME | wealthapp  |
| DB_PASSWORD | eatTheRich |
| DB_DATABASE | revenue    |


2. Create a ConfigMap with name "wealthapp", that contains the following keys and values:

| Key         | Value      |
|-------------|------------|
| API\_HOST    | backend    |
| API\_PORT    | "8080"     |
| DB\_HOST     | database   |


3. Deploy the manifests from the repository under session6/backend, frontend and database. Be sure to first create the ImageStream and BuildConfig, then the rest of the manifests.

    !!! tip
        Keep in mind, that you need to replace the image references in the deployment manifests with the image repository of your specific ImageStream

4. Check all deployments for their health and if you can reach the web application through the URL provided by the Route.

    !!! warning
        Keep in mind, that we are creating an unsecured route, meaning http, not https. Your browser might automatically redirect to https, when clicking on the link of the route. In that case you need to manually change the URL in the browser back to http.


### Task 1: Ephemeral Storage


1. Use the form at the top of the webapp to add a new data line to the database. You can choose whatever values you see fit.

2. Load the URL again and see, if the added dataline is still there.

3. Go into the Openshift WebUI under Workloads -> Deployments, choose the "database" deployment from the list and then click on the "Pods" tab for this deployment. Delete the existing database Pod and watch it being recreated by Openshift.

4. When the new database Pod is ready again, load the webapp again. Is the new dataline still there?

### Task 2: Persistent Storage

1. We want to persist the database of our webapp, so that it can survive restarts of the database Pod. In the database Deployment click on the "Actions" button and add storage to the deployment. For this choose to create a new PVC (Persistent Volume Claim) and mount it into the container with the following properties (leave non-mentioned properties with their default value):

| Property    | Value     |
|-------------|-----------|
| PVC name    | wealthapp |
| Access mode | Single user (RWO) |
| Size        | 1GiB      |
| Mount path  | /var/lib/mysql/data |

2. Save and wait until the database Deployment is ready again.


3. Reload the webapp and use the form at the top of the webapp to again add a new dataline with whatever values you see fit. Check if the new dataline appears in the list after you clicked on submit.

4. Go into the Openshift WebUI under Workloads -> Deployments, choose the "database" deployment from the list and then click on the "Pods" tab for this deployment. Delete the existing database Pod and watch it being recreated by Openshift.

5. When the database Deployment is ready, reload the webapp again. Is the new dataline still there?

