import tensorflow as tf
from tensorflow import keras
from model_congiguration import *

print("\nScript start...")

(x_train, y_train), (x_test, y_test) = keras.datasets.cifar100.load_data()
assert x_train.shape == (50000, 32, 32, 3)
assert x_test.shape == (10000, 32, 32, 3)
assert y_train.shape == (50000, 1)
assert y_test.shape == (10000, 1)

# Parse numbers as floats
x_train, x_test = x_train.astype('float32'), x_test.astype('float32')
x_train, x_test = x_train / 255.0, x_test / 255.0

print('\n---------------\nTrain neural network...')
model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Conv2D(32, (3, 3), activation=activation_r, input_shape=input_shape))
model.add(tf.keras.layers.MaxPooling2D((2, 2)))
model.add(tf.keras.layers.Conv2D(32, (3, 3), activation=activation_r))
model.add(tf.keras.layers.MaxPooling2D((2, 2)))
model.add(tf.keras.layers.Conv2D(32, (3, 3), activation=activation_r))
model.add(tf.keras.layers.Flatten())
model.add(tf.keras.layers.Dense(64, activation=activation_r))
model.add(tf.keras.layers.Dense(classes, activation=activation_s))
print('\nNeural network learning accomplished')

print('\n------------------------\nLoad data...')
model.compile(optimizer=optimizer, loss=loss_function, metrics=[metrics])
model.fit(x_train, y_train, epochs=epochs, validation_data=(x_test, y_test))
model.save('../models/cifar_classifier.model2')

score = model.evaluate(x_test, y_test, verbose=0)
print(f'\nTest loss: {score[0]} / Test accuracy: {score[1]}')

print('\n--------------------------------\nScript end.')
