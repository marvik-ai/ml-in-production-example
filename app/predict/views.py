from fastapi.params import Body
from fastapi.exceptions import HTTPException
from fastapi import APIRouter, Request
from starlette.status import HTTP_200_OK
from typing import List

from core.base_objects import Text
from core.pipeline import PredictionPipeline
from core.settings import custom_logger


logger = custom_logger("Predict endpoint")


predict = APIRouter()
pipeline = PredictionPipeline()


@predict.post("", status_code=HTTP_200_OK)
def predict_sentiment(request: Request, payload: List[Text] = Body(...)):
    """Endpoint for predicting the sentiment of a list of texts"""

    if len(payload) > 0:
        return pipeline.run(payload)
    else:
        raise HTTPException(
            status_code=401,
            detail="No texts found within the body",
        )
