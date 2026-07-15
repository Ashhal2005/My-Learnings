from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier 
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.datasets import fetch_openml
#import matplotlib.pyplot as plt
df = fetch_openml("mnist_784", as_frame=False)
X , y = df.data , df.target.astype(int)
X = X/255

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.20, random_state=42)

model_svm = SVC(random_state=42)
cv_svc = cross_val_score(model_svm,X_train,y_train,cv=5,scoring="accuracy")
print ("Accuracy of SVC is",cv_svc)

"""image = X_test[:1].reshape(28,28)
plt.imshow(image,cmap = "binary")
plt.axis("off")
plt.show()"""


model_rfc = RandomForestClassifier()
cv_rfc = cross_val_score(model_rfc, X_train,y_train, cv=5, scoring='accuracy')
print ("Accuracy of RFC is",cv_rfc)



