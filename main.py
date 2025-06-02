from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
import openai
import os

# تهيئة تطبيق FastAPI
app = FastAPI()

# إعدادات CORS للسماح من أي مصدر (يمكن تضييقها لاحقًا)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# تحميل مفتاح OpenAI من متغير بيئي
openai.api_key = os.getenv("OPENAI_API_KEY")

# نموذج البيانات المستقبلة من الفرونت
class PromptRequest(BaseModel):
    prompt: str

# نقطة النهاية للتوليد
@app.post("/generate")
async def generate_text(req: PromptRequest):
    try:
        # إرسال الطلب إلى GPT-4
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "user", "content": req.prompt}
            ],
        )
        output = response.choices[0].message.content.strip()
        return {"output": output}
    except Exception as e:
        return {"error": f"❌ حدث خطأ أثناء التوليد: {str(e)}"}
