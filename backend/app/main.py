from fastapi import FastAPI
from app.schemas import SleepInput
from app.model import predict_sleep_score

app = FastAPI(title="Sleep Quality API")

@app.post("/predict")
def predict_sleep(data: SleepInput):
    score = round(float(predict_sleep_score(data)), 2)

    return {
        "sleep_score": score,
        "quality": (
            "Excellent" if score >= 85 else
            "Good" if score >= 70 else
            "Poor"
        )
    }
