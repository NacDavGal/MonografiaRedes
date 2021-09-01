import tensorflow as tf

from tensorflow.keras import datasets, layers, models
#from tensorflow.keras.layers import Input, Dense

import matplotlib.pyplot as plt
from tensorflow.python.ops.gen_math_ops import Add
#from tensorflow.python.keras.engine.input_layer import Input
#from tensorflow.python.keras.layers.core import Dense


inputs = layers.Input(shape=(784,))
output_1 = layers.Dense(64, activation='relu')(inputs)
output_2 = layers.Dense(64, activation='relu')(output_1)
predictions = layers.Dense(10, activation='softmax')(output_2)
model = models.Model(inputs=inputs, outputs=predictions)
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])
model.fit(data, labels)
print("Aprendiendo Tensorflow")

