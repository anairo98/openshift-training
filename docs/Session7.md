# 5. Hands-On Lab

## Tasks

### Task 1: Deploying Jenkins

1. In the Developer Console go to the menu entry "+Add" and choose "All services" from the Developer Catalog.

2. Search for "Jenkins", click on the one first with persistent storage and then on "Instantiate Template".

3. In the resulting form set the "Volume Capacity" to "3Gi". Leave the rest with its default values und click "Create". Wait for the Jenkins Pod to get ready.

    !!! note
    The used Jenkins template still uses the deprecated DeploymentConfig resource, which basically has the same functionality as the Deployment resource.

4. Open the Jenkins WebUI from the URL of the jenkins Route, login with your Openshift credentials and Allow the selected permissions, so that Openshift can handle the authentication for Jenkins.

### Task 2: Configure the Jenkins Pipeline and trigger a build

1. In the Jenkins WebUI create a Job with the name "wealthapp" as a Pipeline.

2. In the resulting form paste the Jenkins pipeline "wealthapp_pipeline" from the session7 directory in the training repository into the Pipeline script field and save the pipeline.

3. Start the newly created pipeline and watch how it executes.

4. Check the console output of the finished pipeline. What happens there?

5. Inspect the pipeline definition, that you copied from the training repository. What is each stage doing?
