from enum import Enum
from pydantic import BaseModel, root_validator
from typing import Any, Dict, Optional


class Language(Enum):
    """
    Available languages for making predictions. Currently available:
    - "en" -> English
    - "es" -> Spanish
    - "pt" -> Portguese
    """

    ENGLISH = "en"
    SPANISH = "es"
    PORTUGUESE = "pt"


class Label(Enum):
    """Available labels for the predictions"""

    NEGATIVE = "negative"
    NEUTRAL = "neutral"
    POSITIVE = "positive"


class Text(BaseModel):
    """Class for defining the main elements for each prediction"""

    text_id: str
    text: str
    language: Language
    pred_label: Optional[Label]
    pred_score: Optional[float]
    metadata: Optional[Dict[str, Any]]


class ModelOutput(BaseModel):
    """Class for wrapping the outputs of the Sentiment Classification model"""

    negative_score: float
    neutral_score: float
    positive_score: float
    global_score: Optional[float]
    global_label: Optional[Label]

    @root_validator
    def get_global_score(cls, values) -> Dict:
        if values["global_score"] is None:
            values["global_score"] = (
                0.5 + (values["positive_score"] - values["negative_score"]) / 2
            )
        return values

    @root_validator
    def get_global_label(cls, values) -> Dict:
        if values["global_label"] is None:
            if values["global_score"] >= 0.7:
                values["global_label"] = Label.POSITIVE
            elif values["global_score"] <= 0.35:
                values["global_label"] = Label.NEGATIVE
            else:
                values["global_label"] = Label.NEUTRAL
        return values
