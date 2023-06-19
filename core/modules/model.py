import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from typing import List

from core.base_objects import ModelOutput
from core.settings import custom_logger


class SentimentClassificationModel:
    """
    Class for loading and wrapping the main methods for
    interacting with the Sentiment Classification model
    """

    def __init__(self, model_id: str) -> None:
        self.logger = custom_logger(self.__class__.__name__)

        device = "cuda" if torch.cuda.is_available() else "cpu"
        self.logger.info(f"Running model in {device.upper()}!")
        self.device = torch.device(device)

        self.logger.info(f"Loading model: {model_id}")
        self.tokenizer = AutoTokenizer.from_pretrained(model_id)
        self.model = AutoModelForSequenceClassification.from_pretrained(model_id).to(
            self.device
        )
        self.softmax = torch.nn.Softmax(dim=1)

    def predict(self, texts: List[str]):
        """Method for making batch prediction of texts"""

        input_tensors = self.tokenizer(
            texts, return_tensors="pt", padding=True, truncation=True
        )
        with torch.no_grad():
            logits = self.model(**input_tensors).logits
            preds = self.softmax(logits)

        outputs = [
            ModelOutput(
                negative_score=float(pred[0]),
                neutral_score=float(pred[1]),
                positive_score=float(pred[2]),
            )
            for pred in preds
        ]
        return outputs
