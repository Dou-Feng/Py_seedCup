#coding=utf-8

import numpy as np
import tensorflow as tf
import  PreOperate
import F1
from sklearn.cross_validation import  train_test_split

#获得训练的原始数据
matrix = PreOperate.Data_matrix()
data_x = matrix.inputMatrix
data_y = matrix.outputMatrix

train_x, test_x, train_y, test_y = train_test_split(data_x, data_y, test_size=0.1)


def compute_accuracy(v_xs, v_ys):
    global prediction
    y_pre = sess.run(prediction, feed_dict={xs: v_xs})
    correct_prediction = tf.equal(tf.argmax(y_pre, 1), tf.argmax(v_ys, 1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
    result = sess.run(accuracy, feed_dict={xs: v_xs, ys: v_ys})
    return result


def add_layer(inputs, in_size, out_size, activation_function=None):
    Weights = tf.Variable(tf.random_normal([in_size, out_size]))
    biases = tf.Variable(tf.zeros([1, out_size]) + 0.1)
    Wx_plus_b = tf.matmul(inputs, Weights) + biases
    if activation_function is None:
        outputs = Wx_plus_b
    else:
        outputs = activation_function(Wx_plus_b)
    return outputs


xs = tf.placeholder(tf.float32, [None, 9])
ys = tf.placeholder(tf.float32, [None, 2])

l1 = add_layer(xs, 9, 20, activation_function=tf.nn.softmax)
prediction = add_layer(l1, 20, 2, activation_function=tf.nn.softmax)


cross_entropy = tf.reduce_mean(-tf.reduce_sum(ys * tf.log(prediction),
reduction_indices=[1])) # loss

train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)
sess = tf.Session()

sess.run(tf.global_variables_initializer())

for i in range(500):
    sess.run(train_step, feed_dict={xs: train_x, ys: train_y})

    if i % 50 == 0:
        print(compute_accuracy(test_x, test_y))







