from fastapi.testclient import TestClient

from src.main import app

client=TestClient(app)

def test_home():
    response=client.get("/")
    assert response.status_code==200

def test_predict():

    student1={
        "math1":12,
        "math2":13,
        "math3":14,
        "math4":15

    }
    response=client.post("/predict",json=student1)  
    assert "predict_score" in response.json()  

    assert response.status_code==200


def test_invalid_score():
    student2={
        "math1":11,
        "math2":10,
        "math3":12,
        "math4":122

    }  

    response=client.post("/predict",json=student2)

    assert response.status_code==422
    assert "predict_score"  in response.json() 