from sklearn.model_selection import train_test_split
from sklearn import datasets


# Load the Iris dataset
iris = datasets.load_iris()

# Assign the features (X) and target labels (y)
X = iris.data
y = iris.target


# Split the dataset into 80% training and 20% testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Check the shapes of the resulting subsets
print("X_train shape:", X_train.shape)
print("X_test shape:", X_test.shape)
print("y_train shape:", y_train.shape)
print("y_test shape:", y_test.shape)
