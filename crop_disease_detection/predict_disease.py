# crop_disease_detection/predict_disease.py

from transformers import AutoModelForImageClassification, AutoImageProcessor
from PIL import Image
import torch

# Load model and processor from Hugging Face (local or remote)
model_path = "linkanjarad/mobilenet_v2_1.0_224-plant-disease-identification"

# If you want to use a local path (offline usage), download the files first
# model_path = "crop_disease_detection/mobilenet_model"

model = AutoModelForImageClassification.from_pretrained(model_path)
processor = AutoImageProcessor.from_pretrained(model_path)

# Ensure labels exist
if not hasattr(model.config, "id2label"):
    model.config.id2label = {i: f"Class {i}" for i in range(model.config.num_labels)}

def predict_disease(image_path):
    image = Image.open(image_path).convert("RGB")
    inputs = processor(images=image, return_tensors="pt")

    with torch.no_grad():
        outputs = model(**inputs)

    predicted_class = outputs.logits.argmax(-1).item()
    label = model.config.id2label[predicted_class]

    return label
