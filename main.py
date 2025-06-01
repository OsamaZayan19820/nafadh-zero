from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
import openai
import os

# تهيئة التطبيق
app = FastAPI()

# السماح بالوصول من أي جهة
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# الحصول على المفتاح من المتغير البيئي
openai.api_key = os.getenv("OPENAI_API_KEY")

# نموذج الطلب
class PromptRequest(BaseModel):
    prompt: str
    token: Optional[str] = None

@app.post("/generate")
async def generate_text(req: PromptRequest):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": req.prompt}],
        )
        output = response.choices[0].message.content
        return {"output": output}
    except Exception as e:
        return {"error": str(e)}
