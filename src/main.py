from fastapi import FastAPI

import joblib
from pathlib import Path

from pydantic import BaseModel,Field



BASE_DIR=Path(__file__).resolve().parent.parent

path_model=BASE_DIR/"models"/"model1.joblib"



model=joblib.load(path_model)

print("model loaded")


app=FastAPI()

class Student(BaseModel):
    math1:float=Field(ge=0,le=20)
    math2:float=Field(ge=0,le=20)
    math3:float=Field(ge=0,le=20)
    math4:float=Field(ge=0,le=20)

@app.get("/")
def home():
    return {
        "message":"hiiiiiii"
    }

@app.post("/predict")
def predict(student:Student):
    student_scores=[[
     student.math1,
     student.math2,
     student.math3,
     student.math4

    ]]

    prediction=model.predict(student_scores)
    return {
        "information":"scores",
        "math1":student.math1,
        "math2":student.math2,
        "math3":student.math3,
        "math4":student.math4,
        "predict_score":float(prediction[0])
    }  