# Import the necessary modules
import requests
import numpy as np
import json
import tensorflow as tf
# Loading data
mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()
# Data preprocessing (here, normalization)
x_train, x_test = x_train / 255.0, x_test / 255.0
# Format the image data so as to be sent as JSON
payload = json.dumps( { 'instances': x_test[:2].tolist() } )
# URL of the TensorFlow Serving container's API (Kubernetes)
url = 'http://10.111.103.234:30111/v1/models/mymodel:predict'
# Send the request
response = requests.post(url, data=payload)
# Parse the response
prediction =  response.json()["predictions"]
# Print the result
print(prediction)