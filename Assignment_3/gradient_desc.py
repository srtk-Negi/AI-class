import pandas as pd

basePath = "/Users/Sarthak/Desktop/School_Projects/AI/AI-class/Assignment_3"

# Data file name variables
train = basePath + "gd-train.dat"
test = basePath + "gd-test.dat"


# Activation Function - implement Sigmoid
def activation_function(h):
    # given 'h' compute and return 'z' based on the activation function implemented
    pass

# Train the model using the given training dataset and the learning rate
# return the "weights" learnt for the perceptron - include the weight assocaited with bias as the last entry


def train(train_data, learning_rate=0.05):
    # initialize weights to 0
    # go through each training data instance
    # get 'x' as one multi-variate data instance and 'y' as the ground truth class label
    # obtain h(x)
    # call the activation function with 'h' as parameter to obtain 'z'
    # update all weights individually using learning_rate, (y-z), and the corresponding 'x'
    # return the final learnt weights
    pass


# Test the model (weights learnt) using the given test dataset
# return the accuracy value
def test(test_data, weights, threshold):
    # go through each testing data instance
    # get 'x' as one multi-variate data instance and 'y' as the ground truth class label
    # obtain h(x)
    # call the activation function with 'h' as parameter to obtain 'z'
    # use 'threshold' to convert 'z' to either 0 or 1 so as to match to the ground truth binary labels
    # compare the thresholded 'z' with 'y' to calculate the positive and negative instances for calculating accuracy
    # return the accuracy value for the given test dataset
    pass


# Gradient Descent function
def gradient_descent(df_train, df_test, learning_rate=0.05, threshold=0.5):
    # call the train function to train the model and obtain the weights
    # call the test function with the training dataset to obtain the training accuracy
    # call the test function with the testing dataset to obtain the testing accuracy
    # return (trainAccuracy, testAccuracy)
    pass


# Threshold of 0.5 will be used to classify the instance for the test. If the value is >= 0.5, classify as 1 or else 0.
threshold = 0.5


# Main algorithm loop
# Loop through all the different learning rates [0.05, 1]
# For each learning rate selected, call the gradient descent function to obtain the train and test accuracy values
# Print both the accuracy values as "Accuracy for LR of 0.1 on Training set = x %" OR "Accuracy for LR of 0.1 on Testing set = x %"
