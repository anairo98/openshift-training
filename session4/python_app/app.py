# from flask import Flask
# app = Flask(__name__)

# @app.route("/")
# def hello():
#     return "Hello from OpenShift!"

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=8080)


from flask import Flask
from prometheus_client import start_http_server, Summary
import time
import random

app = Flask(__name__)

# Define Prometheus-metrics
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')

@app.route("/")
@REQUEST_TIME.time()
def hello():
    return "Hello from OpenShift!"

if __name__ == "__main__":
    # Starts Prometheus-metricsserver on port 8000
    start_http_server(8000)
    # Starts Flask-App on port 8080
    app.run(host="0.0.0.0", port=8080)

