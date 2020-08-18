import glob
import os
import re

import numpy as np
import matplotlib.pyplot as plt
import ML_reviews.evaluation as evaluation
import ML_reviews.models as models

# Pre-conditions:
# data must be a ndarray matrix of dtype float
# label must be a 1D ndarray of dtype float
# Note: on the line is also negative
def perceptron(data, labels, T, averaged=False, graph=False):
    if not averaged:
        title = "Linear Binary Classification with Perceptron "
        keywords = "Linear_Binary_Classification_with_Perceptron*"
    elif averaged:
        title = "Linear Binary Classification with Averaged Perceptron "
        keywords = "Linear_Binary_Classification_with_Averaged_Perceptron*"

    for filename in glob.glob(keywords):
        os.remove(filename)

    n = np.ma.size(obj=data, axis=1)
    x = data
    y = labels.flatten()
    dimension = np.ma.size(obj=x, axis=0)

    theta = np.zeros(shape=(dimension, 1))
    theta_0 = 0
    thetas = np.zeros(shape=(dimension, 1))
    theta_0s = 0

    # Number of times to run perceptron
    for t in np.arange(start=0, stop=T, step=1):
        old_theta = theta
        old_theta_0 = theta_0

        # Loop through entire data set
        for i in np.arange(start=0, stop=n, step=1):
            # If we discover a mistake:
            if y[i] * (np.matmul(np.transpose(theta), x[:, i:i+1])[0, 0] + theta_0) <= 0:
                theta = theta + y[i] * x[:, i:i+1]
                theta_0 = theta_0 + y[i]

                # For graphing
                if graph and dimension == 2:
                    graph(x, y, theta, theta_0, title + t)

                # Mistakes still present when T is reached.
                # if t == T - 1:
                #     print("T limit reached when there's still mistakes, please increase T!")

            if averaged:
                # Sum of theta and theta_0  out of every step
                thetas = thetas + theta
                theta_0s = theta_0s + theta_0

            # print(theta, theta_0)

        # Break if perfectly classified.
        # We cannot break in averaged perceptron because we need to sum regardless of change.
        if not averaged and np.array_equal(theta, old_theta) and np.array_equal(theta_0, old_theta_0):
            break

    if averaged:
        return (thetas / (n * T), theta_0s / (n * T))
    else:
        return (theta, theta_0)

# def perceptron(table_name, T, averaged=False, graph=False):
#
#
#
#
#     if not averaged:
#         title = "Linear Binary Classification with Perceptron "
#         keywords = "Linear_Binary_Classification_with_Perceptron*"
#     elif averaged:
#         title = "Linear Binary Classification with Averaged Perceptron "
#         keywords = "Linear_Binary_Classification_with_Averaged_Perceptron*"
#
#     for filename in glob.glob(keywords):
#         os.remove(filename)
#
#     n = np.ma.size(obj=data, axis=1)
#     x = data
#     y = labels.flatten()
#     dimension = np.ma.size(obj=x, axis=0)
#
#     theta = np.zeros(shape=(dimension, 1))
#     theta_0 = 0
#     thetas = np.zeros(shape=(dimension, 1))
#     theta_0s = 0
#
#     # Number of times to run perceptron
#     for t in np.arange(start=0, stop=T, step=1):
#         old_theta = theta
#         old_theta_0 = theta_0
#
#         # Loop through entire data set
#         for i in np.arange(start=0, stop=n, step=1):
#             # If we discover a mistake:
#             if y[i] * (np.matmul(np.transpose(theta), x[:, i:i+1])[0, 0] + theta_0) <= 0:
#                 theta = theta + y[i] * x[:, i:i+1]
#                 theta_0 = theta_0 + y[i]
#
#                 # For graphing
#                 if graph and dimension == 2:
#                     graph(x, y, theta, theta_0, title + t)
#
#                 # Mistakes still present when T is reached.
#                 # if t == T - 1:
#                 #     print("T limit reached when there's still mistakes, please increase T!")
#
#             if averaged:
#                 # Sum of theta and theta_0  out of every step
#                 thetas = thetas + theta
#                 theta_0s = theta_0s + theta_0
#
#             # print(theta, theta_0)
#
#         # Break if perfectly classified.
#         # We cannot break in averaged perceptron because we need to sum regardless of change.
#         if not averaged and np.array_equal(theta, old_theta) and np.array_equal(theta_0, old_theta_0):
#             break
#
#     if averaged:
#         return (thetas / (n * T), theta_0s / (n * T))
#     else:
#         return (theta, theta_0)

def graph(x, y, theta, theta_0, title):
    x_plus = np.empty(shape=(2, 0))
    x_minus = np.empty(shape=(2, 0))

    # Append columns of x to correct matrix categories.
    for i in np.arange(start=0, stop=y.size, step=1):
        if y[i] == 1:
            x_plus = np.append(arr=x_plus, values=x[:, i:i+1], axis=1)
        elif y[i] == -1:
            x_minus = np.append(arr=x_minus, values=x[:, i:i+1], axis=1)

    figure1, axes1 = plt.subplots(nrows=1, ncols=1)
    axes1.set_aspect(aspect="equal", adjustable='datalim')
    axes1.set_title(label=title)

    # Plot x_plus
    x_1 = x_plus[0, :]
    x_2 = x_plus[1, :]

    axes1.plot(x_1, x_2, marker="+", linewidth=0, color="g")

    # Plot x_minus
    x_1 = x_minus[0, :]
    x_2 = x_minus[1, :]

    axes1.plot(x_1, x_2, marker="_", linewidth=0, color="r")

    # Plot theta
    axes1.arrow(x=0, y=0, dx=theta[0, 0], dy=theta[1, 0], head_width=0.05, length_includes_head=True)

    # Plot linear hyperplane
    xs = np.array(object=[-3, -2, -1, 0, 1, 2, 3])

    if theta[1, 0] != 0:
        # (theta_1)x + (theta_2)y + theta_0 = 0
        # y = -(theta_1 / theta_2)x - theta_0 / theta_2
        ys = - (theta[0, 0] / theta[1, 0]) * xs - theta_0 / theta[1, 0]
        axes1.plot(xs, ys, marker="None", linestyle="-")
    elif theta[0, 0] != 0:
        # We have a vertical linear hyperplane.
        # (theta_1)x + (theta_2)y + theta_0 = 0
        # (theta_1)x + (0)y + theta_0 = 0
        # x = -theta_0 / theta_1
        axes1.axvline(x=-theta_0 / theta[0, 0])
    else:
        pass



    figure1.savefig(fname=re.sub(pattern="\s+", repl="_", string=axes1.get_title()))
    plt.close(figure1)

if __name__ == "__main__":
    data = np.array(object=
                    [[2, 3, 4, 5]])

    labels = np.array(object=[1, 1, -1, -1])
    
    print(perceptron(data, labels, T=100))


