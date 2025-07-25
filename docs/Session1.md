# Lets get started with the First Hands-On Session

## Tasks

### Task 1: Deployment
1. Create your own Namespace (like your own project)

    ![Create Project](images/create_project.png)

2. Create the frontend Deployment by importing the yaml template
	1. Go to the [Github Repository](https://github.com/anairo98/openshift-training/tree/main) and navigate over the **e-commerce** folder to the **frontend** folder and then to the **deployment.yml** 
	2. Copy the content of the **deployment.yml** 
	3. Switch to the Openshift Console and paste the content into the *Import Yaml* field
		
        ![Import YAML](images/import_yml.png)

	4. Click on **Create** and you will create the *frontend* deployment
    5. Go to **Topology** in Openshift Console and check on your newly created Pod

        ![Issue with Frontend](images/frontend_not_running.png)

3. There is some problem with your Pod, it is not running! Find out what the problem is about!?

    !!! note "Do you need help?"
        If you cannot solve the problem, switch to the **Solutions for Troubleshooting** chapter on this website (scroll down :winking_face:) 

4. When you fixed the Problem, you maybe need to scale down and after that scale up your Pod again (so the changes are getting activated):

    ![Scale Frontend](images/scale_frontend.png)

5. Give it a moment and wait until the Pod is running!

    ![Running Frontend](images/running_frontend.png)

---

### Task 2: Services
1. Create a Service, which abstracts the *frontend* Deployment
2. Go to the **Administrator** view and search for **services** under the **Networking** section

    ![Services](images/services.png)

3. Click on **Create Service** button
4. Enter all necessary information

    !!! tip
        If you are unsure how to enter it, have a look at the following Yaml file: 

    ```yaml
    apiVersion: v1
    kind: Service
    metadata:
      name: frontend
      labels:
        app: frontend
    spec:
      type: ClusterIP
      selector:
        app: frontend
      ports:
      - name: http
        port: 80
        targetPort: 8080
    ```

5. Verify if the Service is linked to the prior created *frontend* Pod 
	1. Click on the *frontend* Service
	2. Click on the *Pods* section:

        ![Service Pod](images/service_pod.png)

	3. You can also verify by going back to the **Topology** section and click on the *frontend* Pod. There is now under the **Resources** section also the *frontend* Service linked

        ![Service Pod 2](images/service_pod2.png)

---

### Task 3: Routing
Create a Route by using the OpenShift UI  (not by using the manifest files given in the Github)

1. Go to **Administrator** view and click on **Routes** under the **Networking** section and click on the **Create Route** button

    ![Create Route](images/create_route.png)

2. Give the Route a name: *frontend*
3. Select the correct *frontend* Service, which we created in **Task 2**
4. Select the correct *Port* (Service Port) :right_arrow: *TargetPort* (Port on the Container)

    !!! note
        Only fill out the fields which are necessary (marked with a red asterisk)

5. Click on **Create** to create the service 

    ![Create](images/create.png)

6. Give it a second :stopwatch:
7. verify the Route: Go back to the **Topology** and click on the Route sign on the right hand side of the Pod 

    ![Verify Route](images/verify_route.png)


!!! info
    You will see that the frontend is loading but you get an *500 Internal Server Error* if you open the website. The *Internal Server Error* occurs, because you only have the frontend deployed and all of the backend is still missing. 
    So don't worry, we will do this together step by step!

![Internal Server Error](images/internal_server_error.png)

---

### Task 4: Scaling
Scaling the Pod

1. Scale down the Pod to zero 
    
    ![Scale Down](images/scale_down.png)

2. Check the Route (Link) to the website - The website should not be reachable

    ![App not available](images/app_not_available.png)

3. Scale the Pod up again and verify the link to the website 

!!! info
    The frontend should be reachable again

--- 

### Task 5: Microservices-Architecture
Create a Microservice Architecture by creating multiple other deployments and connect those by connecting the services

1. Go into the [Github Repository](https://github.com/anairo98/openshift-training/tree/main/e-commerce)
2. Lets start with the *Ad-Service*. You can find the Yaml files under the folder **adservice**
3. Start with the *serviceaccount.yml*
4. Go to the OpenShift Console and navigate to **Administrator** - **User Management** - **ServiceAccounts** 
5. Create a Service Account with the name: *adservice* in your created namespace (of Task 1)
6. Now it is time to create the Deployment, copy the *deployment.yml* of the *adservice* from the GitHub Repository
7. Go back to the OpenShift Console and navigate to: **Administrator** - **Workloads** - **Deployments**
8. Click on **Create Deployment** 
9. Click on **YAML view**, delete the default content and paste inside your copied *deployment.yml*

    ![Deployment via Yaml](images/deployment_via_yaml.png)

10. Lastly, create the regarding Service of the *adservice* Deployment
11. Copy the *service.yml* from the **adservice** folder of the GitHub Repository and switch back to the OpenShift Console
12. Create the service in OpenShift by using the *service.yml* like we did with the *deployment.yml* of the **adservice** 

    !!! info
        You can verify, if you go to the **Topology** and check if your Pod named *adservice* with the expecting Service is present

13. Now create the *cartservice*, the *checkoutservice* and the *currencyservice* by your own

!!! hint
    For the three other microservices you can use the whole *manifest.yml* file and create the whole microservices (including ServiceAccount, Deployment and Service) all at once. For that navigate to **Developer** - **+Add** - **Import YAML** and paste in the whole manifest file. This saves time :rocket: 

![Import Manifest File](images/import_manifest.png)










## Solutions for Troubleshooting

### Solution of Task 1

Frontend Pod was not created, but why?!

1. Check the Error message

    ![Frontend Not Running](images/frontend_not_running.png)

2. Go to the **Deployments** (*Hint*: you can find it, if you switch to the **Administrator** and under **Workloads**)
3. Check the **ReplicaSet** of the *frontend* Deployment 

    ![RepliaSet](images/replicaset_frontend.png)

4. Check the **Events** of the *Replicaset*

    ![Events ReplicaSet](images/replicaset_events.png)

5. You got it! You are missing the expected *Service Account*
6. Create the missing *frontend* Service Account

    ![Service Account](images/create_serviceaccount.png)

!!! info
    As you can see there are already three Service Accounts. These serviceaccounts are the default Service Accounts. But for our created *frontend* deployment we do not want to use one of the default once. 

![Create SA](images/create_serviceaccount2.png)

!!! hint
    It is important that you name the Service Account exactly as mentioned in you Deployment.yml file