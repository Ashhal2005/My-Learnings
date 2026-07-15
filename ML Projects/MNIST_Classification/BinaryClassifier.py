#import pandas as pd 
#import numpy as np 
#import matplotlib.pyplot as plt
#from sklearn.model_selection import train_test_split, cross_val_score, cross_val_predict
#from sklearn.datasets import fetch_openml
#from sklearn.linear_model import SGDClassifier
#from sklearn.metrics import confusion_matrix, precision_score, recall_score
#from sklearn.dummy import DummyClassifier

"""df = fetch_openml("mnist_784", as_frame=False)
X , y = df.data , df.target
print (df.dtype)
#y = y.astype(int)
X = X/255  #Normalization """

#print ("X:",X.shape,"y:",y.shape)

"""def plot_digit(img):
    image = img.reshape(28,28)
    print (image)
    plt.imshow(image,cmap = "binary")
    plt.axis("off")
    plt.show()"""

#instance = X_test[0]
#plot_digit(instance)

"""X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.20, random_state=42)
y_train_3 = (y_train == 8)
y_test_3 = (y_test ==8)
"""


"""#SGDClassifier - update the weight for every single instance
model_SGD = SGDClassifier(random_state=42, max_iter=1000)
model_SGD.fit(X_train, y_train_3)
print(model_SGD.predict(instance.reshape(1,-1)))"""


"""#model evalutaion using cross validation - k=folds
cvs = cross_val_score(model_SGD, X_train,y_train_3, scoring="accuracy")
print (cvs)"""


"""model_dummy = DummyClassifier()
#model_dummy.fit(X_train, y_train_3)
cvs_dummy = cross_val_score(model_dummy,X_train,y_train_3,cv=5,scoring="accuracy" )
print (cvs_dummy.sum()/5)"""


"""model = SGDClassifier(random_state=42)
get_predictions = cross_val_predict(model,X_train,y_train_3,cv=5)
cm = confusion_matrix(y_train_3,get_predictions)
print("confusion matrix: ",cm)
precision = precision_score(y_train_3, get_predictions)
print ("Precision is", precision)
recall = recall_score(y_train_3,get_predictions)
print ("Recall is",recall )
"""



