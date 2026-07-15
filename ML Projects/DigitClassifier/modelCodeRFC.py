import joblib
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestClassifier 
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report

df = fetch_openml("mnist_784", as_frame=False)
X , y = df.data , df.target.astype(int)
X = X/255

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.20, random_state=42)

model_rfc = RandomForestClassifier(n_estimators=100, n_jobs=-1,random_state=42)
model_rfc.fit(X_train,y_train)  #Training

cv_rfc = cross_val_score(model_rfc, X_train,y_train, cv=5, scoring='accuracy')
print ("CV Accuracy",cv_rfc.mean())  
# CV Score [0.96767857 0.96714286 0.97080357 0.96758929 0.96678571]
# Mean 

y_prediction = model_rfc.predict(X_test) #Testing 

print ("Accuracy Score", accuracy_score(y_test, y_prediction))
print("Report of model",classification_report(y_test, y_prediction))
joblib.dump(model_rfc,"DigitClassifierRFC.pkl")