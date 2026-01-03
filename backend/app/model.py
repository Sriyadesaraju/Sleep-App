import joblib
import numpy as np
from app.schemas import SleepInput

model = joblib.load("app/sleep_model.pkl")

def predict_sleep_score(data: SleepInput):
    X = np.array([[
        data.sleep_duration,
        data.rem_percentage,
        data.deep_percentage,
        data.light_percentage,
        data.awakenings
    ]])
    return model.predict(X)[0]
