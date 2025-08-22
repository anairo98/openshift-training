# Welcome to the world of OpenShift 

This guide is designed to help you get started with Red Hat OpenShift. Whether you're new to OpenShift or looking to solidify your foundational knowledge, this training will provide you with the basic concepts and hands-on experience needed to start to utilize Kubernetes effectively.

## Workshop Structure
This workshop will start at the very beginning with very simple hands-on sessions and then build up step by step. At the end, participants should be able to get to grips with OpenShift.

To get started, we will start with the basic objects in OCP. Thereby, the sessions 1 to 3 are based on a simple UseCase to make it easier to understand. After that we will continue to have a deeper look into different objects of OCP. Most of the sessions have tasks included, in which the participants have to troubleshoot some mistakes. By that, the participants of this workshop should be enabled to solve *real-life* problems and get a deeper understanding of the dependencies between the different objects.

Here is short overview of the covered topics in each of the sessions (**Disclaimer**: *Work in progress*) 

| Session        | Description                                                | Content                                                                 |
|----------------|----------------------------------------------------------- | ------------------------------------------------------------------------|
| 1 to 3         | Build up on a simple Use Case of a *Boutique Online Shop*  | Basic OCP objects, like Deployment, Services, Routes etc.               |
|----------------|--------------------------------------------------------------------------------------------------------------------------------------|
| 4              | Deploy a simple webserver by using an nginx image          | Containerfile, BuildConfigs, Builds, Images, Imagestreams etc.    |          


## Prerequisites
Participants must have access to an Openshift cluster to carry out the hands-on tasks. Ideally, each participant uses their own namespace and can try out and test all exercises and tasks in it.

## References on GitHub

The whole GitHub Repository is linked below:

[OpenShift Trainings Repository](https://github.com/anairo98/openshift-training)

## Hands-On Labs
For the Hands-On Tasks thery will be a usecase provided. In the usecase, a simple web app is set up step by step as part of an online boutique store. The entire online store is made up of individual microservices.

The microservices have to be connected to each other and made accessible with routes and services (everything else is covered in the specific tasks). The idea of the online boutique store is based on the GoogleCloudPlatform repository
[Original Source of Manifest Files](https://github.com/GoogleCloudPlatform/microservices-demo/tree/49be1bca8067b4957ff2b27a2c5790c99f2e86b2)

## Disclaimer

These Github pages are based on DevOps principles and are thereby, constantly developed and changed. This means that incomplete information or explanations and exercises that have not yet been fully described cannot be ruled out.

> Happy Learning!