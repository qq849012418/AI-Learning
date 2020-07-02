import tensorflow.compat.v1 as tf
import tensorflow as tf2
import torch
tf.disable_v2_behavior()
hello = tf.constant('Hello tensorfolw')
sess = tf.Session()
print(sess.run(hello))
print(tf.__version__)
print(torch.__version__)
