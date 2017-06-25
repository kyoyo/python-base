import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

### create data

x_data = np.random.rand(100).astype(np.float32)
noise = np.random.normal(0,0.005,x_data.shape)


y_data = x_data * 0.1 + 0.3 + noise


### create tensorflow structure start ###

Weights = tf.Variable(tf.random_uniform([1],-1,1))
biases = tf.Variable(tf.zeros([1]))

y = Weights * x_data + biases

#loss = tf.reduce_mean(np.square(y - y_data))
loss = tf.losses.mean_squared_error(y_data,y)
optimizer = tf.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(loss)

#init = tf.initialize_all_variables()

### create tensorflow structure end ###


if int((tf.__version__).split('.')[1]) < 12 and int((tf.__version__).split('.')[0]) < 1:
    init = tf.initialize_all_variables()
else:
    init = tf.global_variables_initializer()

sess = tf.Session()
sess.run(init)

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.scatter(x_data,y_data)
plt.ion()
plt.show()



for step in range(201):
    sess.run(train)

    if step % 5 == 0:
        try:
            ax.lines.remove(lines[0])
        except Exception:
            pass
        print(step,sess.run(Weights),sess.run(biases))
        y = sess.run(Weights) * x_data + sess.run(biases)

        lines = ax.plot(x_data,y,'r-')
        plt.pause(0.5)








