import numpy as np
import joblib
from fastapi import FastAPI, UploadFile, File
from PIL import Image

model = joblib.load("DigitClassifierRFC.pkl")
app = FastAPI()

@app.get('/')
def root():
    return {"Message!":"Digit classifier is running"}

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    img = Image.open(file.file).convert("L")
    img = img.resize((28,28))
    img = np.array(img).astype(np.float32)
    img = img/255.0
    img = img.reshape(1,-1)
    prediction = model.predict(img)
    return {"Your number is ":int(prediction[0])}

