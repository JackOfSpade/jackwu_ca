import numpy as np


# Returns whether a data point is positive
def positive(x, th, th0):
   return np.sign(np.dot(np.transpose(th), x) + th0)


#  Returns the number of points for which the actual label == expected label.
def score(data, labels, th, th0):
   return np.sum(positive(data, th, th0) == labels)

#  Returns the percentage correct on a new testing set as a float between 0. and 1.
def eval_classifier(learner, data_train, labels_train, data_test, labels_test, T, averaged):
    theta, theta_0 = learner(data=data_train, labels=labels_train, T=T, averaged=averaged)
    return score(data_test, labels_test, theta, theta_0)/data_test.shape[1]

# Requirement: data is shuffled
# Cross evaluation of a learning algorithm's ability to predict new data with a fixed data set.
def xval_learning_alg(learner, data, labels, T, averaged, k):
    score_sum = 0

    # Split the data into k separate sets.
    s_data = np.array_split(data, k, axis=1)
    s_labels = np.array_split(labels, k, axis=1)

    # We run k evaluations.
    for i in np.arange(start=0, stop=k-1, step=1):
        # All data set except one is the training data.
        data_train = np.concatenate(s_data[:i] + s_data[i+1:], axis=1)
        labels_train = np.concatenate(s_labels[:i] + s_labels[i+1:], axis=1)

        # One test data set.
        data_test = np.array(s_data[i])
        labels_test = np.array(s_labels[i])

        # Evaluate with the combined k training data sets and one test set.
        score = eval_classifier(learner=learner, data_train=data_train, labels_train=labels_train, data_test=data_test, labels_test=labels_test, T=T, averaged=averaged)
        score_sum += score
    return score_sum/k

if __name__ == "__main__":
    pass