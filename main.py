import os
import openai
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
openai.api_key = os.getenv("OPENAI_API_KEY")

class PromptRequest(BaseModel):
    prompt: str

@app.post("/generate")
async def generate_text(req: PromptRequest):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": req.prompt}
        ]
    )
    return {"output": response["choices"][0]["message"]["content"]}
