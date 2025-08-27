# 4. Hands-On Lab

## Tasks

### Task 0: Recap 

### Task 1: ImageStreams and Deployment

1. Create a Imagestream which should refer an nginx image from [Quay.io](https://quay.io/repository/nginx/nginx-unprivileged) 
2. Create a deployment based on that newly created Imagestream. 
    - The Deployment should have the following characteristics:
        - name: nginx-unprivileged 
        - port: 8080
        - label: app: nginx-unprivileged
        - image: REFRENCE-TO-IMAGESTREAM:TAG

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


### Task 3: You can do it all by yourself! 
