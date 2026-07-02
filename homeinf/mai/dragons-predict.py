import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

data = pd.read_csv("dragons_dataset.csv")
X = data.iloc[:, :-1]
y = data.iloc[:, -1]

X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2)

knn_model = KNeighborsClassifier(n_neighbors=3)
knn_model.fit(X_train, y_train)

knn_predictions = knn_model.predict(X_val)

# Calculate metrics
knn_accuracy = accuracy_score(y_val, knn_predictions)

print("KNN Results:")
print(f"Accuracy:  {knn_accuracy:.4f}")
