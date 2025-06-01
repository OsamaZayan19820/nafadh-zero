from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# ✅ إضافة دعم CORS للسماح للواجهة بالتواصل مع الخادم
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # يمكنك استبدال * بـ "https://osamazayan19820.github.io" للخصوصية
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 🔐 رمز التحقق
API_KEY = "Nafadh@2025"

# 📦 نموذج البيانات المستقبلة
class PromptRequest(BaseModel):
    prompt: str
    token: Optional[str] = None

# 🚀 نقطة النهاية الأساسية
@app.post("/generate")
async def generate_text(req: PromptRequest):
    if req.token != API_KEY:
        return {"error": "رمز الحماية غير صحيح"}
    
    # 🧠 هنا المنطق التوليدي (مؤقتًا مجرد محاكاة)
    output = f"🔮 توليد نَفَاذ: {req.prompt[::-1]}"
    
    return {"output": output}
    ✅ إضافة دعم CORS لتفعيل واجهة نَفَاذ من GitHub Pages
