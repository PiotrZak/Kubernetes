# Importing TensorFlow
import tensorflow as tf
import datetime
import os
# Loading the data
mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()
# Data preprocessing (here, normalization)
x_train, x_test = x_train / 255.0, x_test / 255.0
# Building the model
model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(28, 28)),
  tf.keras.layers.Dense(128, activation='relu'),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(10)
])
# Loss function declaration
loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
# Model compilation
model.compile(optimizer='adam',
              loss=loss_fn,
              metrics=['accuracy'])
# Training
model.fit(x_train, y_train, epochs=5)
model(x_test[:2])

# Save Model
current_date = datetime.date.today().strftime("%Y-%m-%d")
path_to_save_model = f"../{current_date}/1/"
os.makedirs(path_to_save_model, exist_ok=True)

model.save(path_to_save_model)