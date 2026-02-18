from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import List
import joblib
import numpy as np
import os


# Load model once at startup
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "model.pkl")

model = joblib.load(MODEL_PATH)


app = FastAPI()

class PredictRequest(BaseModel):
    features: List[float] = Field(..., min_length=4, max_length=4)

class PredictResponse(BaseModel):
    prediction: int
    model_version: str

@app.get("/")
def home():
    return {"message": "Iris Prediction API", "status": "running"}

@app.post("/predict", response_model=PredictResponse)
def predict(request: PredictRequest):
    input_data = np.array(request.features).reshape(1, -1)
    prediction = int(model.predict(input_data)[0])
    
    return PredictResponse(
        prediction=prediction,
        model_version="v1.0.0"
    )
