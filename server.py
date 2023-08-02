import torch
import io

from typing import Annotated
from fastapi import FastAPI, File
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image
from transformers import CLIPProcessor, CLIPModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# load model
model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

@app.post("/find_similarity")
async def find_similarity(image: Annotated[bytes, File()], text: str):
    img: Image.Image = Image.open(io.BytesIO(image))
    inputs = processor(text.split(","), images=img, return_tensors="pt", padding=True)
    with torch.no_grad():
        outputs = model(**inputs)
    logits_per_image = outputs.logits_per_image # this is the image-text similarity score
    probs = logits_per_image.softmax(dim=1) # we can take the softmax to get the label probabilities

    probs = probs.detach().numpy().tolist()[0]
    prob1 = [round(i,2) for i in probs]
    result = dict(zip(text.split(","),prob1))
    return result

@app.get("/health")
async def health():
    return {"message": "ok"}