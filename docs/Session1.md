# Lets get started with the First Hands-On Session

## Tasks

### Task 1
1. Create your own Project Namespace
*Picture*
2. Create the frontend Deployment by importing the yaml template
	1. Go to the Github Repository and navigate over the e-commerce folder to the frontend and then to the deployment.yml 
	2. Copy the content of the deployment.yml 
	3. Paste the deployment.yml in OpenShift into the "Import Yaml" field
		*Picture*
	4. Click on Create and you will create the frontend deployment
		*Picture*
> Go to *Topology* in Openshift and Check on your Pod
3. Find out what is the problem with your Pod!? 
4. When you fixed the Problem, you maybe need to scale down and after that scale up your Pod again (so the changes are getting activated):
*Picture scale_frontend.png*
5. Give it a moment and wait until the Pod is running!
*Picture running_frontend.png*

### Task 2
1. Create a Service, which abstracts the frontend Deployment
2. Go to the *Administrator* view and then you can find services under the *Networking* section
*Picture services.png*
3. Click on *Create Service*
4. Enter all necessary Informations 
> If you are unsure how to enter it, have a look at the following yml file: 

``` e-commerce/frontend/service.yml
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

5. Verify if the Service is linked to the prior created frontend Pod 
	1. Click on the *frontend* Service
	2. Click on the *Pods* section:
	*Picture service_pod.png*
	3. You can also verify by going back to the *Topology* section and click on the *frontend* Pod. There is now under the *Resources* section also the *frontend* Service linked
*Picture service_pod2.png*


### Task 3 
- Route anlegen über Openshift direkt (nicht über manifest file)
	- Die tls section im manifestfile gibt es damit auch http traffic immer auf https weitergeleitet wird, ist einfach sicherer
1. Go to *Administrator* and click on *Routes* under the *Networking* section and click on *Create Route*
*Picture create_route.png*
2. Give the Route a name (*frontend*)
3. Select the correct *frontend* Service, which we created in Task 2
4. Select the correct Port (Service Port) --> TargetPort (Port on the Container)
> Only fill out the fields which are necessary (marked with a red asterisk)
5. Click on *Create*
*Picture create.png*
6. Give it a second 
7. verify the Route: Go back to the *Topology* and click on the Route sign on the Pod 
*Picture verify_route.png*

> You will see that the frontend is loading but you get an *500 Internal Server Error*. 

!!! note 
    You get the *Internal Server Error*, because you only have the frontend and all of the backend is still missing
    *Picture inetrnal_server_error.png*


## Solutions for Troubleshooting

### Solution of Task 1

> Frontend Pod was not created
1. Check the Error message
	*Picture*
2. Go to the Deployments (hint you can find it, if you switch to the administrator and under *Workloads*)
3. Check the ReplicaSet of the frontend Deployment 
	*Picture*
4. Check the *Events* of the *Replicaset* 
	*Picture - replicaset_events*
5. You got it! You are missing the expected Service Account
6. Create the missing *frontend*- ServiceAccount
*Picture - create_serviceaccount*
> As you can see there are already three serviceaccounts. These serviceaccounts are the default Serviceaccounts. For the frontend Deployment we were assigning the specific *frontend* Serviceaccount. So lets create it: 
*Picture create_serviceaccount2.png*