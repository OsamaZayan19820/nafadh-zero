
from fastapi import FastAPI, Request, HTTPException
from pydantic import BaseModel
import uvicorn

app = FastAPI()

API_KEY = "your-secret-token"

class GenerateRequest(BaseModel):
    prompt: str
    token: str

@app.post("/generate")
async def generate_text(request: GenerateRequest):
    if request.token != API_KEY:
        raise HTTPException(status_code=403, detail="Unauthorized")

    response_text = f"🧠 تم توليد استجابة لنَفَاذ بناءً على: '{request.prompt}'"
    return {"output": response_text}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=10000, reload=True)
