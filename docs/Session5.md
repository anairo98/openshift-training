# 5. Hands-On Lab

## Tasks

### Task 0: Recap Quiz 

To recap your knowledge until now. You should be able to answer the following questions. You can access the Quiz under the following link: 

[Recap Quiz](https://forms.office.com/Pages/ResponsePage.aspx?id=ZGZljjZfW0qVTMVAX9KSBjhzaJv-m0hJoQL2QDQKeitUQTdUVzhLQ1RPT1RGNEtZSjhXSlQxWEU4Wi4u)

1. How does a Kubernetes Service in OpenShift know which Pods to route traffic to?
    1. It uses the Pod's IP address directly
    2. It matches the Pod's labels with its selector
    3. It queries the Deployment for Pod information
    4. It uses the container image name as a reference

2. What happens if a Deployment in OpenShift references an image that does not exist in the ImageStream?
    1. The Deployment will automatically build the image
    2. The Pod will start but fail during runtime
    3. The Pod will fail to start due to ImagePull errors
    4. OpenShift will fallback to a default image

3. Which of the following best describes the role of an ImageStream in OpenShift 
    1. It stores container images in the internal registry
    2. It defines the build strategy for applications
    3. It acts as a reference point for image versions and triggers
    4. It manages network access between Pods 

4. Which of the following statements about Deployments in OpenShift is true?
    1. A Deployment directly manages Pods without ReplicaSets 
    2. A Deployment must always be paired with a BuildConfig
    3. A Deplyoment can be triggered by changes in an ImageStream
    4. A Deployment cannot be scaled manually 

5. In OpenShift, what is the correct relationship between a Route and a Service?
    1. A Route exposes a Service, which then routes traffic to matching Pods
    2. A Route exposes a Deployment directly to external traffic
    3. A Route forwards to a Pod based on its IP address
    4. A Route must reference an ImageStream to function correctly 

### Task 1: Secrets and ConfigMaps

1. Create a Secret with name "wealthapp", that contains the following keys and values:

| Key         | Value      |
|-------------|------------|
| DB_USERNAME | wealthapp  |
| DB_PASSWORD | eatTheRich |
| DB_DATABASE | revenue    |

    !!! tip
        You can do this directly in the WebUI, which shows a form for creating secrets.

2. Create a ConfigMap with name "wealthapp", that contains the following keys and values:

| Key         | Value      |
|-------------|------------|
| API\_HOST    | backend    |
| API\_PORT    | "8080"     |
| DB\_HOST     | database   |
| cgi-default-app.conf  | <Directory "/var/www/html"\><br>  Options +ExecCGI<br>  DirectoryIndex /cgi-bin/app.py<br></Directory\> |
| cgi-default-data.conf | <Directory "/var/www/html"\><br>  Options +ExecCGI<br>  DirectoryIndex /cgi-bin/data.py<br></Directory\> |

    !!! danger
        The last two keys contain multiline data. Preserve the newlines in the ConfigMap, so that the corresponding files can be used as provided here.

3. Look at your Secret and ConfigMap in the WebUI. Inspect their YAML representation and check, if the values are set how you expect it.

    !!! tip
        As some values are base64-encoded, you might need to decode the values from the Secret/ConfigMap with the command `base64 -d`.


### Task 2: Adding environment variables form Secrets/ConfigMaps to Deployments

1. Deploy the resource manifests, that are provided in the repository under `session5_task1_2`, with the 3 components "frontend", "backend" and "database".

    !!! hint
        Keep in mind, that you are using your own images with the provided BuildConfigs. Thus you need to place the correct references to your ImageStreams in the Deployment manifests. The database deployment has 2 mentions of the image, that you need to replace.
2. Check your Deployments, if they are healthy. Then check the application by opening the Route URL. Do you see any errors? Diagnose them.

    !!! hint
        You might have to wait a moment for the Builds to finish. You can check the build status and logs to verify this.

3. Provide the needed environment variables to your Deployments. You can look into the YAML resource definition or at the `Environment` tab of the Deployments. The Deployments need the follwing environment variables:

| Deployment | Environment variable                               |
|------------|----------------------------------------------------|
| frontend   | API\_HOST, API\_PORT                               |
| backend    | DB\_HOST, DB\_USERNAME, DB\_PASSWORD, DB\_DATABASE |
| database   | DB\_HOST, DB\_USERNAME, DB\_PASSWORD, DB\_DATABASE |

4. Verify, that the application now works correctly. It should look like this:

    ![wealth-app](images/session5/wealth-app.png)


### Task 3: Mounting files from ConfigMaps and Secrets in Deployments

Our webapp got an update with new requirements.

1. Change the BuildConfigs for the `frontend` and `backend` components, so that the `contextDir` now points to `session5_task3/build_directories/frontend` and `session5_task3/build_directories/backend` respectively and start the builds. After the builds finished, put the new image digest (the SHA Identifier) from the ImageStream into the corresponding deployments to update the used image.

2. Trigger a new Build for the `frontend` and `backend` BuildConfigs and check, if the Deployments are still healthy. Do you see any errors?

    !!! hint
        You might have to wait a moment for the Builds to finish. You can check the build status and logs to verify this.

    !!! hint
        You can look at the events and the logs of each Pod.

3. Mount the needed file from the ConfigMap in the corresponding Deployment by editing the YAML resource definitions.

| Deployment | Key in ConfigMap      | Path to mount the file to               |
|------------|-----------------------|-----------------------------------------|
| frontend   | cgi-default-app.conf  | /etc/httpd/conf.d/cgi-default-app.conf  |
| backend    | cgi-default-data.conf | /etc/httpd/conf.d/cgi-default-data.conf |

4. Verify, that the updated application now runs as intended. Check each Deployment to be healthy and access the application via its Route.
