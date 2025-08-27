# 4. Hands-On Lab

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

### Task 1: ImageStreams and Deployment

1. Create a Imagestream which should refer an nginx image from [Quay.io](https://quay.io/repository/nginx/nginx-unprivileged) 

    !!! tip
        There is a template in the GitHub in the folder: session4/nginx
2. Create a deployment based on that newly created Imagestream. 
    - The Deployment should have the following characteristics:
        - name: nginx-unprivileged 
        - port: 8080
        - label: app: nginx-unprivileged
        - image: REFERENCE-TO-IMAGESTREAM:TAG

    !!! hint
        You can create the Deployment by using the survey or by using the YAML input field. If you would like to use the YAML input, it can be helpful to reference the Kubernetes documentation: [Deployments in Kubernetes](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/)

3. Create a Service names *nginx-unprivileged* of the Deployment

    !!! hint
        Keep in mind, that you are connecting the correct Deployment to yout service and to set the *targetPort* correct!

4. Create a Route of the Service to access the *nginx* Deployment from outside the cluster 

5. Verify that the Deployment, Service and Route works correctly by entering the Route. It should look like this: 

    ![Welcome to NGINX](images/session4/welcome_nginx.png)


### Task 2: Deploy from Containerfile 

1. Create a ImageStream 
2. Create a BuildConfig by using the *session4/python_app/buildconfig.yml* file

    !!! hint
        You need to adjust some of the fields in the BuildConfig. 

3. Start a Build 
4. Verify that the Image is tagged to your created ImageStream 

    ![Tagged image](images/session4/tagged_image.png)

5. Create a Deployment of the *python-app*, which uses the newly tagged image of the ImageStream 

6. Create a Service of the *python-app* Deployment

    !!! hint
        Keep in mind, that you need to set the correct *label* and *targetPort*

7. Create a Route to access the *python-app* also from outside the cluster

    !!! success
        If everything works correctly, you should see the following message. 

    ![python-app](images/session4/python_app_output.png)


### Task 3: Setting up Prometheus and Scraping logs from the python-app

We would now like to scrape metrics from the *python-app* in a Prometheus server.

The application has already defined an endpoint **/metrics** in the container file and in the app.py file, which runs on **port 8000**.

1. Make this Endpoint of the *python-app* accessible from inside and outside the cluster (Create service and route). Depending on the names you gave, it should like similar to this:

    ![python-prometheus-accessible](images/session4/python_prometheus-accessible.png)

2. Create a ConfigMap, which should be consumed from the Prometheus server (manifest file can be found under the **session4/prometheus/** folder in the GitHub)

    !!! info
        Contains the configurations for the endpoint from which the metrics are to be obtained (*python-app*) and, for example, the intervals at which the metrics are to be scraped

3. Create an imagestream, which refers to an **Prometheus** image from [Quay.io](https://quay.io/repository/prometheus/prometheus)

    ![Prometheus ImageStream](images/session4/prometheus-imagestream.png)

4. Create a Deployment which uses the *image* from the newly created **ImageStream** 
    
    !!! note
        use the **deployment.yml** template, which can be found in the session4/prometheus folder on GitHub

5. Create a Service and a Route for the *Prometheus server* to acces it:

    ![Prometheus](images/session4/prometheus.png)

6. Verify that the *Prometheus* is scraping data from the *python-app*. In the *Prometheus* UI click on *Status* and then on *Target health*: 

    ![Scraping data from python-app](images/session4/Scraping_python.png)
