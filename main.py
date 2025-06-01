from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # استبدل * بدومينك للخصوصية
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

API_KEY = "Nafadh@2025"

class PromptRequest(BaseModel):
    prompt: str
    token: Optional[str] = None

@app.post("/generate")
async def generate_text(req: PromptRequest):
    if req.token != API_KEY:
        return {"error": "رمز الحماية غير صحيح"}
    output = f"🔮 توليد نَفَاذ: {req.prompt[::-1]}"
    return {"output": output}
