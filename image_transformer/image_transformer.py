import kfserving
from typing import List, Dict
from PIL import Image
import numpy as np
import io
import base64
import cv2


def image_transform(instance):
    byte_array = base64.b64decode(instance['image_bytes']['b64'])
    image = Image.open(io.BytesIO(byte_array))
    #img = cv2.imread(image, cv2.IMREAD_GRAYSCALE)
    g = cv2.resize(255 - np.asarray(image), (28, 28))
    g = g.flatten() / 255.0
    return g.tolist()


class ImageTransformer(kfserving.KFModel):
    def __init__(self, name: str, predictor_host: str):
        super().__init__(name)
        self.predictor_host = predictor_host
        self._key = None

    def preprocess(self, inputs: Dict) -> Dict:
        return {'instances': [image_transform(instance) for instance in inputs['instances']]}
