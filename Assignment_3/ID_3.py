basePath = "/content/drive/My Drive/Colab Notebooks/Artificial Intelligence/Data/"


# Data file name variables
train = basePath + "id3-train.dat"
test = basePath + "id3-test.dat"


# Pseudocode for the ID3 algorithm. Use this to create function(s).
# def ID3(data, root, attributesRemaining):
# If you reach a leaf node in the decision tree and have no examples left or the examples are equally split among multiple classes
# Choose and the class that is most frequent in the entire training set and return the updated tree
# If all the instances have only one class label
# Make this as the leaf node and use the label as the class value of the node and return the updated tree
# If you reached a leaf node but still have examples that belong to different classes (there are no remaining attributes to be split)
# Assign the most frequent class among the instances at the leaf node and return the updated tree
# Find the best attribute to split by calculating the maximum information gain from the attributes remaining by calculating the entropy
# Split the tree using the best attribute and recursively call the ID3 function using DFS to fill the sub-tree
# return the root as the tree


# Following is the base code structure. Feel free to change the code structure as you see fit, maybe even create more functions.

# Read the first line in the training data file, to get the number of attributes
# Read all the training instances and the ground truth class labels.
# Create the decision tree by implementing the ID3 algorithm. Pseudocode provided above.
# Print the tree in the example format mentioned.
# Use the above created tree to predict the training data and print the accuracy as "Accuracy on the Training data = x %"
# For each training instance, predict the output label
# Compare it with the ground truth class label and calculate the accuracy accordingly
# Use the above created tree to predict the testing data and print the accuracy as "Accuracy on the Test data = x %"
# For each testing instance, predict the output label
# Compare it with the ground truth class label and calculate the accuracy accordingly
