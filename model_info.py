# model_info.py

def get_model_info(model_type):
    if model_type == "Text-to-Image":
        return (
            "Model Name: stabilityai/stable-diffusion-2\n"
            "Category: Text-to-Image\n"
            "Description: Generates images from text prompts using diffusion techniques."
        )
    elif model_type == "Image Classification":
        return (
            "Model Name: microsoft/resnet-50\n"
            "Category: Image Classification\n"
            "Description: Classifies images into categories using a ResNet-50 architecture."
        )
    else:
        return "No model information available."
