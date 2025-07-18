## Use Case: E-Commerce Boutque Store 

In this Hands-On-Labs, we deploy an *e-commerce application*, which is based on the [Online Boutique](https://github.com/GoogleCloudPlatform/microservices-demo), provided by [Google Cloud Platform](https://github.com/GoogleCloudPlatform). 

The deployment manifests are modified so that they could be deployed on an OpenShift Cluster. The User Interface of **"Online Boutique"** looks like this:

![Online Boutique Interface](imgages/boutique_interface.png)

### Architecture

On the main page of the Online Boutique, a frontend service forwards the requests to the 10 corresponding backend services, as shown in this architectur image: 

![Architecture of microservices](imgages/architecture-diagram.png)

All these 11 microservices are communicating over gRPC protocol. 

### Microservices

These 11 microservices are written in different programming languages and are responsible for a specific task in this e-commerce website:


| Service                                              | Language      | Description                                                                                                                       |
| ---------------------------------------------------- | ------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| frontend                        | Go            | Exposes an HTTP server to serve the website. Does not require signup/login and generates session IDs for all users automatically. |
| cartservice                     | C#            | Stores the items in the user's shopping cart in Redis and retrieves it.                                                           |
| productcatalogservice           | Go            | Provides the list of products from a JSON file and ability to search products and get individual products.                        |
| currencyservice                 | Node.js       | Converts one money amount to another currency. Uses real values fetched from European Central Bank. It's the highest QPS service. |
| paymentservice                  | Node.js       | Charges the given credit card info (mock) with the given amount and returns a transaction ID.                                     |
| shippingservice                 | Go            | Gives shipping cost estimates based on the shopping cart. Ships items to the given address (mock)                                 |
| emailservice                    | Python        | Sends users an order confirmation email (mock).                                                                                   |
| checkoutservice                 | Go            | Retrieves user cart, prepares order and orchestrates the payment, shipping and the email notification.                            |
| recommendationservice           | Python        | Recommends other products based on what's given in the cart.                                                                      |
| adservice                       | Java          | Provides text ads based on given context words.                                                                                   |
| loadgenerator                   | Python/Locust | Continuously sends requests imitating realistic user shopping flows to the frontend.         


### Prerequisites

Ensure that you have access to a **OpenShift Cluster** to deploy the manifests for the e-commerce application. 

!!! note

    If you do not already have access to a Demo Cluster, ask your training instructor! Or create a Demo Cluster by yourself via the following link: [Red Hat Demo Cluster](https://catalog.partner.demo.redhat.com/catalog)