from pydantic import BaseModel

class SleepInput(BaseModel):
    sleep_duration: float
    rem_percentage: float
    deep_percentage: float
    light_percentage: float
    awakenings: int