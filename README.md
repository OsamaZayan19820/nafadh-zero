
# 🔷 Nafadh-Zero – واجهة نَفَاذ التجريبية

## 📌 الوصف (Arabic):
نَفَاذ-زيرو هو مشروع API مجاني تجريبي مبني باستخدام FastAPI، يهدف إلى تقديم منصة ذكية لتوليد المحتوى باستخدام الأوامر التوليدية (Prompts).  
هذه النسخة صُممت لتكون بسيطة، آمنة، وقابلة للتوسع لاحقًا باستخدام أدوات مفتوحة المصدر.

## 🔧 الوظائف الرئيسية:
- إرسال أمر توليدي (prompt)
- حماية باستخدام رمز token
- استلام استجابة ذكية فورية
- جاهز للنشر على Render أو أي منصة Python

---

## 🌐 Description (English):
**Nafadh-Zero** is a free experimental API built with FastAPI, designed to serve as an intelligent interface for generative content using structured prompts.  
This lightweight version is perfect for testing, personal use, and future extensions.

### ✅ Features:
- Accepts a `prompt` and `token` via POST request
- Returns a dynamically generated response
- Easily deployable on Render or any Python host

---

## 🚀 Quickstart

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the server:
```bash
uvicorn main:app --reload --port 10000
```

3. Send a POST request to:
```
http://localhost:10000/generate
```

---

## 🛡️ ملاحظات أمنية | Security Notes:
- تأكد من إبقاء token سريًا
- ينصح باستخدام HTTPS عند نشر الخدمة علنًا

---

## 🧠 تم الإنشاء بواسطة | Created by:
**Osama Z. (أسامة زيان)**  
In partnership with ChatGPT + Nafadh Engine
