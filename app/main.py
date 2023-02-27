from typing import Union

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import GPT2TokenizerFast

app = FastAPI()
tokenizer = GPT2TokenizerFast.from_pretrained("gpt2")

class CalData(BaseModel):
    s: str

@app.get("/")
def root():
    return "OK"

@app.get("/token")
def token_cal_get(s: str):
    if s == "":
        raise HTTPException(status_code=401, detail="request parameter is empty")
    return {"s": s, "token": len(tokenizer(s)["input_ids"])}

@app.post("/token")
def token_cal_post(cd: CalData):
    if cd.s == "":
        raise HTTPException(status_code=401, detail="request parameter is empty")
    return {"s": cd.s, "token": len(tokenizer(cd.s)["input_ids"])}
