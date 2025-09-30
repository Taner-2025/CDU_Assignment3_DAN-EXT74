# model_handlers.py

from transformers import pipeline
from diffusers import StableDiffusionPipeline
import torch
from PIL import Image

class BaseModelHandler:
    def run(self, input_data, model_key, input_type):
        raise NotImplementedError("Subclasses must override this method.")

class TextToImageHandler(BaseModelHandler):
    def __init__(self):
        self.pipe = StableDiffusionPipeline.from_pretrained("stabilityai/stable-diffusion-2", torch_dtype=torch.float32)
        self.pipe.to("cpu")

    def run(self, input_data, model_key, input_type):
        image = self.pipe(input_data).images[0]
        image_path = "generated_image.png"
        image.save(image_path)
        return f"Image generated and saved to {image_path}"

class ImageClassificationHandler(BaseModelHandler):
    def __init__(self):
        self.classifier = pipeline("image-classification", model="microsoft/resnet-50")

    def run(self, input_data, model_key, input_type):
        if input_type == "image":
            image = Image.open(input_data)
            result = self.classifier(image)
            return str(result)
        return "Invalid input type for image classification."

class ModelFactory:
    @staticmethod
    def get_model_handler(model_type):
        if model_type == "Text-to-Image":
            return TextToImageHandler()
        elif model_type == "Image Classification":
            return ImageClassificationHandler()
        else:
            return None
