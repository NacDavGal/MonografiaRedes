from operator import concat
import tensorflow as tf

from tensorflow.keras.layers import Input, Conv2D, ReLU, BatchNormalization,\
                                    Add, MaxPooling2D, Flatten, Dense
from tensorflow.keras.models import Model



def residual_block(x: tf.Tensor, downsample: bool, filters: int, kernel_size: int = 3) -> tf.Tensor:
    #Se pasa el tensor de entrada x por dos capas de convolucion y se guarda en y
    y = Conv2D(kernel_size=kernel_size,
               strides= (1 if not downsample else 2),
               filters=filters,
               padding="same")(x)
    y = relu_bn(y)
    y = Conv2D(kernel_size=kernel_size,
               strides=1,
               filters=filters,
               padding="same")(y)
    # Si es necesario downsamplear se pasa a x por una capa de convolucion con padding = same
    if downsample:
        x = Conv2D(kernel_size=1,
                   strides=2,
                   filters=filters,
                   padding="same")(x)
    #Se suman ambas y se hace relu + bn
    out = Add()([x, y])
    out = relu_bn(out)
    return out

def relu_bn(inputs : tf.Tensor) -> tf.Tensor:
	relu = ReLU()(inputs)
	bn = BatchNormalization()(relu)
	return bn	

def sub_net():
    inputs = Input(shape=(256, 256, 3))
    num_filters = 64
    #Se normaliza las entradas
    t = BatchNormalization()(inputs)
    #Se las pasa por una capa inicial de convolución
    t = Conv2D(kernel_size=3,
               strides=1,
               filters=num_filters,
               padding="same")(t)
    #Se hace relu y batch normalization (No faltaria hacer un max pooling?)
    t = relu_bn(t)
    
    num_blocks_list = [2, 5, 5, 2]
    for i in range(len(num_blocks_list)):
        num_blocks = num_blocks_list[i]
        for j in range(num_blocks):
            t = residual_block(t, downsample=(j==0 and i!=0), filters=num_filters)
        num_filters *= 2
    
    t = MaxPooling2D(4)(t)
    return t


def create_res_net():
    
    n = sub_net()
    s = sub_net()
    w = sub_net()
    e = sub_net()

    t = tf.concat(n,s,e,w)
    #Esta capa deberia realizarse despues de concatenar las 4 imagenes
    t = Flatten()(t)
    outputs = Dense(10, activation='softmax')(t)
    
    model = Model(inputs, outputs)

    model.compile(
        optimizer='adam',
        loss='sparse_categorical_crossentropy',
        metrics=['accuracy']
    )

    return model