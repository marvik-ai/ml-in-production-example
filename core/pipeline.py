from typing import Any, Dict, List

from core.base_objects import Text, Label, ModelOutput
from core.modules.model import SentimentClassificationModel
from core.settings import custom_logger, get_config


class PredictionPipeline:
    """Class for handling the main operations within the prediction"""

    def __init__(self) -> None:
        self.logger = custom_logger(self.__class__.__name__)
        self.model = SentimentClassificationModel(**get_config("ModelConfig"))

    def run(self, texts: List[Text]):
        """Method for orchestrating the prediction steps within the PredictionPipeline"""

        self._predict_texts_sentiment(texts)
        response = self._format_response(texts)
        return response

    def _predict_texts_sentiment(self, texts: List[Text]) -> None:
        outputs = self.model.predict([text.text for text in texts])
        for text, output in zip(texts, outputs):
            text.pred_label = output.global_label
            text.pred_score = output.global_score
            text.metadata = {
                "negative_score": output.negative_score,
                "neutral_score": output.neutral_score,
                "positive_score": output.positive_score,
            }

    def _format_response(self, texts: List[Text]) -> Dict[str, Any]:
        return {"preds": [text.dict() for text in texts]}
