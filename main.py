from typing import Union

from fastapi import FastAPI
from transformers import GPT2TokenizerFast

app = FastAPI()


@app.get("/")
def read_root():
    return "OK"


@app.get("/token")
def read_item(s: str):
    tokenizer = GPT2TokenizerFast.from_pretrained("gpt2")
    return {"s": s, "token": len(tokenizer(s)["input_ids"])}
