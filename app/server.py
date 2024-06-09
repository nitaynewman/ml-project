# app/server.py
from fastapi import FastAPI, UploadFile, File
import joblib
from app.model import SugarModel

app = FastAPI()

model_path = "model/sugar_model.joblib"
model = joblib.load(model_path)

@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    # Dummy logic to read image
    image = await file.read()
    prediction = model.predict(image)
    return prediction
