import tensorflow as tf

def Discriminator():
    initializer = tf.random_normal_initializer(0., 0.02)
    input_image = tf.keras.layers.Input(shape=[256, 256, 3], name='input_image')
    target_image = tf.keras.layers.Input(shape=[256, 256, 3], name='target_image')
    # Concatenate images to channel axis
    x = tf.keras.layers.Concatenate()([input_image, target_image])
    # PatchGAN: series of conv layers...
    ...
    output = tf.keras.layers.Conv2D(1, 4, strides=1, padding='same',
                                    kernel_initializer=initializer)(x)
    return tf.keras.Model(inputs=[input_image, target_image], outputs=output)
