from typing import Any, Dict, List

from hezar import Model

from app.pipelines import Pipeline


class TokenClassificationPipeline(Pipeline):
    def __init__(
        self,
        model_id: str,
    ):
        self.model = Model.load(model_id)

    def __call__(self, inputs: str) -> List[Dict[str, Any]]:
        """
        Args:
            inputs (:obj:`str`):
                a string containing some text
        Return:
            A :obj:`list`:. The object returned should be like [{"entity_group": "XXX", "word": "some word", "start": 3, "end": 6, "score": 0.82}] containing :
                - "entity_group": A string representing what the entity is.
                - "word": A substring of the original string that was detected as an entity.
                - "start": the offset within `input` leading to `answer`. context[start:stop] == word
                - "end": the ending offset within `input` leading to `answer`. context[start:stop] === word
                - "score": A score between 0 and 1 describing how confident the model is for this entity.
        """
        model_outputs = self.model.predict(inputs, return_scores=True, return_offsets=True)[0]

        outputs = []
        for entity in model_outputs:
            output = {
                "entity_group": entity["label"],
                "word": entity["token"],
                "start": entity["start"],
                "end": entity["end"],
                "score": entity["score"],
            }
            outputs.append(output)
        return outputs
