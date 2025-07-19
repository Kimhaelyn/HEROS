import pandas as pd
import joblib
import numpy as np
np.float_ = np.float64


def load_get_on_model():
    MODEL_PATH = "app\models\model.pkl"
    return joblib.load(MODEL_PATH)

def load_get_off_model():
    MODEL_PATH = "app\models\model (1).pkl"
    return joblib.load(MODEL_PATH)


def make_prediction(model, data):
    input_data = pd.DataFrame([data.dict()])
    input_data["ds"] = pd.to_datetime(input_data["ds"])

    forecast = model.predict(input_data)
    result = forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].copy()

    for col in ['yhat', 'yhat_lower', 'yhat_upper']:
        result[col] = result[col].apply(float)

    return result.to_dict(orient='records')
