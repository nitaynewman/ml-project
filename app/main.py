# app.py
from fastapi import FastAPI, HTTPException
from .pklpredict import PredictClass
import uvicorn
import os


'''
    the fast api app 
    loads the model from PredictClass in the pklpredict.py
    def endpoint /predict that takes input data and returns predicts useing the model 
'''

app = FastAPI()

# Load model
model_path = os.getenv('MODEL_PATH', 'model/MODEL.pkl')
model = PredictClass(model_path)

@app.post("/predict")
async def predict(input_data: dict):
    try:
        prediction = model.predict(input_data)
        return {"prediction": prediction}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)


