#!/usr/bin/python
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

def show_plt():
    plt.figure(figsize=(10,10))
    for i in range(25):
        plt.subplot(5,5,i+1)
        plt.xticks([])
        plt.yticks([])
        plt.grid(False)
        plt.imshow(train_images[i], cmap=plt.cm.binary)
        plt.xlabel(class_names[train_labels[i]])
    plt.show()

#fetch date_set 
fashion_mnist = tf.keras.datasets.fashion_mnist

(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

class_names = ["T-shirt/top", "Trouser", "Pullover", "Dress", "Coat",
               "Sandal", "Shirt", "Sneaker", "Bag", "Ankle boot"]
#show_plt()

model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128, activation="relu"),
    tf.keras.layers.Dense(10)
])
model.compile(optimizer="adam",
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=["accuracy", "mae"])

model.fit(train_images, train_labels, epochs=10)

test_loss, test_acc, test_mae = 0
test_data = {}
test_data = model.evaluate(test_images,  test_labels, verbose=2)
print(test_data)
print("\nTest acc: ", test_acc, "Test loss: ",test_loss, "Test mae: ", test_mae)
