import time

import torch
from fire import Fire
from torch.nn import functional as F
from transformers import (AutoModelForSequenceClassification, AutoTokenizer,
                          BertForSequenceClassification, BertTokenizer)


def text2toxicity(tokenizer, model, text, aggregate=True):
    """Calculate toxicity of a text (if aggregate=True) or a vector of toxicity aspects (if aggregate=False)"""
    with torch.no_grad():
        inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True).to(
            model.device
        )
        proba = torch.sigmoid(model(**inputs).logits).cpu().numpy()
    if isinstance(text, str):
        proba = proba[0]
    if aggregate:
        return 1 - proba.T[0] * (1 - proba.T[-1])
    return proba


def bert_toxic(
    comment: str, toxic_threshold: int = 0.8, big_model=False, aggregate=True
):
    if big_model:
        tokenizer = BertTokenizer.from_pretrained(
            "SkolkovoInstitute/russian_toxicity_classifier"
        )
        model = BertForSequenceClassification.from_pretrained(
            "SkolkovoInstitute/russian_toxicity_classifier"
        )
        batch = tokenizer.encode(comment, return_tensors="pt")
        logits = model(batch).logits
        probs = F.softmax(logits, dim=1).detach().numpy()[0]
        print(probs[1])
        return probs[1] > toxic_threshold
    else:
        model_checkpoint = "cointegrated/rubert-tiny-toxicity"
        tokenizer = AutoTokenizer.from_pretrained(model_checkpoint)
        model = AutoModelForSequenceClassification.from_pretrained(model_checkpoint)
        if torch.cuda.is_available():
            model.cuda()
        probs = text2toxicity(tokenizer, model, comment, aggregate)
        return probs > toxic_threshold


if __name__ == "__main__":
    Fire(bert_toxic)
