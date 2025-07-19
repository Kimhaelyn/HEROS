from fastapi import APIRouter
from app.schemas.predict import PredictRequest
from app.models.prophet_model import load_get_on_model, make_prediction, load_get_off_model


router = APIRouter()

@router.post("/get_on_predict")
def predict(data: PredictRequest):
    model = load_get_on_model()
    return make_prediction(model, data)


@router.post("/get_off_predict")
def predict(data: PredictRequest):
    model = load_get_off_model()
    return make_prediction(model, data)


