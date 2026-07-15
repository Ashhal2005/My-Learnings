import joblib
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score


data = fetch_openml("mnist_784", as_frame=False)
X, y = data.data, data.target.astype(int)
X = X / 255.00

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model_svm = SVC(kernel='rbf', gamma='scale')  # rbf kernel
model_svm.fit(X_train, y_train)

prediction = model_svm.predict(X_test)
print("Accuracy:", accuracy_score(y_test, prediction))

joblib.dump(model_svm, "DigitClassifierSVM.pkl")

