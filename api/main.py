from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import pandas as pd

app = FastAPI()

# Charger le modèle à partir du fichier .sav
with open('../files/model.sav', 'rb') as model_file:
    model = pickle.load(model_file)

class InputData(BaseModel):
    age: int
    traveltime: int
    freetime: int
    health: int
    absences: int
    Walc: int
    Dalc: int
    goout: int

@app.post('/predict')
def predict(data: InputData):
    form_data = data.dict()
    X_new = pd.DataFrame([form_data])
    y_pred = model.predict(X_new)
    return {'prediction': y_pred[0]}
