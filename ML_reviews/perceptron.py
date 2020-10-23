import glob
import os

import numpy as np
import ML_reviews.evaluation as evaluation
import ML_reviews.models as models

# Pre-conditions:
# data must be a ndarray matrix of dtype float
# label must be a 1D ndarray of dtype float
# Note: on the line is also negative
def perceptron(data, labels, T, averaged=False, graph=False):
    keywords= None

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
    title = None

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

if __name__ == "__main__":
    data = np.array(object=
                    [[2, 3, 4, 5]])

    labels = np.array(object=[1, 1, -1, -1])
    
    print(perceptron(data, labels, T=100))


