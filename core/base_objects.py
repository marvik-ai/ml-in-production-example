from enum import Enum
from pydantic import BaseModel
from typing import Optional


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


class ModelOutput(BaseModel):
    """Class for wrapping the outputs of the Sentiment Classification model"""

    negative_score: float
    neutral_score: float
    positive_score: float
