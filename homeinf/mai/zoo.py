import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

df = pd.read_csv("zoo.csv")
X = df[["длина", "громкость"]].values
y = df["животное"].values
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X, y)

data = {"длина": [550, 185, 50, 95], "громкость": [120, 185, 65, 60]}

new_animals = pd.DataFrame(data).values
predictions = model.predict(new_animals)
print(predictions)
