from typing import Any, Dict, List

from core.base_objects import Text, Label


class PredictionPipeline:
    """Class for hanlding the main operations within the prediction"""

    def __init__(self) -> None:
        pass

    def run(self, texts: List[Text]):
        """Method for orchestrating the prediction steps within the PredictionPipeline"""

        self._predict_texts_sentiment(texts)
        response = self._format_response(texts)
        return response

    def _predict_texts_sentiment(self, texts: List[Text]) -> None:
        texts_batch = [text.text for text in texts]
        model_responses = [(Label.NEUTRAL, 1.0) for i in range(len(texts_batch))]
        for text, (label, score) in zip(texts, model_responses):
            text.pred_label = label
            text.pred_score = score

    def _format_response(self, texts: List[Text]) -> Dict[str, Any]:
        return {"preds": [text.dict() for text in texts]}
