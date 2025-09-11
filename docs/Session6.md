# 5. Hands-On Lab

## Tasks

### Task 0: Recap Task 



### Task 1: Ephemeral Storage

1. Deploy the manifests from the repository under session6/backend, frontend and database. Be sure to first create the ImageStream and BuildConfig, then the rest of the manifests.

    !!! tip
        Keep in mind, that you need to replace the image references in the deployment manifests with the image repository of your specific ImageStream

2. Open the URL from the Route. Check, if the webapp works as expected


3. Use the form at the top of the webapp to add a new data line to the database. You can choose whatever value you see fit.

4. Load the URL again and see, if the added dataline is still there.

5. Go into the Openshift WebUI under Workloads -> Deployments, choose the "database" deployment from the list and then click on the "Pods" tab for this deployment. Delete the existing database Pod and watch it being recreated by Openshift.

6. When the new database Pod is ready again, load the webapp again. Is the new dataline still there?

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

