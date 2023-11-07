from typing import Dict, List

from hezar import Model

from app.pipelines import Pipeline


class TextClassificationPipeline(Pipeline):
    def __init__(
        self,
        model_id: str,
    ):
        self.pipeline = Model.load(model_id)

    def __call__(self, inputs: str) -> List[Dict[str, float]]:
        """
        Args:
            inputs (:obj:`str`):
                a string containing some text
        Return:
            A :obj:`dict`:. The object returned should be a list of one list like [[{"label": 0.9939950108528137}]] containing:
                - "label": A string representing what the label/class is. There can be multiple labels.
                - "score": A score between 0 and 1 describing how confident the model is for this label/class.
        """
        outputs = self.pipeline.predict(inputs, return_all_scores=True)
        return outputs
