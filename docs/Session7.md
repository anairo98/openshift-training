# 5. Hands-On Lab

## Tasks

### Task 1: Deploying Jenkins

To increase the speed of development and decrease the time to market, the dev team wants to deploy the wealthapp via a Jenkins Pipeline on Openshift. You are tasked to deploy Jenkins in a namespace.

1. In the Developer Console go to the menu entry "+Add" and choose "All services" from the Developer Catalog.

2. Search for "Jenkins", click on the one first with persistent storage and then on "Instantiate Template".

3. In the resulting form set the "Volume Capacity" to "3Gi". Leave the rest with its default values und click "Create". Wait for the Jenkins Pod to get ready.

    !!! note
        The used Jenkins template still uses the deprecated DeploymentConfig resource, which basically has the same functionality as the Deployment resource.

4. Open the Jenkins WebUI from the URL of the jenkins Route, login with your Openshift credentials and Allow the selected permissions, so that Openshift can handle the authentication for Jenkins.

### Task 2: Configure the Jenkins Pipeline and trigger a build

The dev team has build a working prototype of a Pipeline for deploying the wealthapp. You are tasked with adding it to your Jenkins instance and testing it.

1. In the Jenkins WebUI create a Job with the name "wealthapp" as a Pipeline.

2. In the resulting form paste the Jenkins pipeline "wealthapp_pipeline" from the session7 directory in the training repository into the Pipeline script field and save the pipeline.

3. Start the newly created pipeline and watch how it executes.

4. Check the console output of the finished pipeline. What happens there?

5. Inspect the pipeline definition, that you copied from the training repository. What is each stage doing?

### Task 3: Changing the pipeline and troubleshooting

To facilitate future staging of the wealthapp, the ops team wants to also tag every image, that is build via the pipeline, with the tag "staging". This ensures, that the build image version can be used for a future pipeline, promoting it though to the testing and production stage.

1. Add a new stage named "tagging" at the end of the pipeline definition. Use the other stages for reference on how to build up a stage for execution with openshift. For each of the three images, that is build for the wealthapp, add the line (and replace "<imagename>" with the name of the corresponding Imagestream):

```
openshift.tag("<imagename>:latest", "<imagename>:staging")
```

2. Save and let the pipeline run. Look at the console output. Is everything working correctly? If not, why?

3. Fix the pipeline by adding the following code snippet directly before the tagging lines:

<details>
  <summary>Code fix:</summary>
  
  ```
  echo "Waiting for builds to finish..."
  def build = openshift.selector('build', [app: 'wealthapp'])
  timeout(time: 10, unit: 'MINUTES') {
      build.untilEach {
          def phase = it.object().status.phase
          echo "Build ${it.name()} is in phase: ${phase}"
          return (phase == "Complete" || phase == "Failed" || phase == "Cancelled")
      }
  }
  echo "tagging"
  ```

  This code snippet will wait for the builds to finish, before trying to tag the resulting images.
  
</details>

4. Test the pipeline again. Does it work now? Check in the Openshift WebUI, if you can find the "staging" tags in the Imagestreams.
