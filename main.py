from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import openai
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# المفتاح يُقرأ من متغير بيئة لحماية أقوى
openai.api_key = os.getenv("OPENAI_API_KEY")

class PromptRequest(BaseModel):
    prompt: str
    token: str

@app.post("/generate")
async def generate_text(req: PromptRequest):
    if req.token != "Nafadh@2025":
        return {"error": "رمز الحماية غير صحيح ❌"}
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "user", "content": req.prompt}
            ]
        )
        result = response["choices"][0]["message"]["content"]
        return {"output": result}
    except Exception as e:
        return {"error": str(e)}
