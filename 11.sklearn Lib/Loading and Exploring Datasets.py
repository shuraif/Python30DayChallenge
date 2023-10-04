from sklearn import datasets

# Load a built-in dataset (e.g., Iris dataset)
iris = datasets.load_iris()

# Access the features and target labels
X = iris.data  # Features
y = iris.target  # Target labels

# Explore dataset properties
print("Number of samples:", len(X))
print("Number of features:", X.shape[1])
print("Target labels:", set(y))
