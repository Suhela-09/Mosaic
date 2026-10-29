import torch
from transformers import AutoTokenizer, AutoModel

tok = AutoTokenizer.from_pretrained("facebook/contriever")
model = AutoModel.from_pretrained("facebook/contriever")

def embed(texts):
    inputs = tok(texts, padding=True, truncation=True, return_tensors="pt")
    with torch.no_grad():
        out = model(**inputs)
    mask = inputs["attention_mask"].unsqueeze(-1)
    return (out.last_hidden_state * mask).sum(1) / mask.sum(1)

q = embed(["stray dogs get hit by cars at night"])
d = embed(["retroreflective tape makes signs visible in headlights",
           "a thermostat that controls an air conditioner"])
print(q @ d.T)