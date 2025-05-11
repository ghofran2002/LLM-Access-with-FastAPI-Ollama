from fastapi import FastAPI, Depends, HTTPException, Header
import ollama, os
from dotenv import load_dotenv

app = FastAPI()
load_dotenv()

API_KEYS = {os.getenv("API_KEY")}

def verify_api_key(x_api_key: str = Header(None)):
    if x_api_key not in API_KEYS:
        raise HTTPException(status_code=401, detail="Invalid API Key")
    return x_api_key

@app.post("/generate")
def generate(prompt: str, api_key: str = Depends(verify_api_key)):
    response = ollama.chat(model="mistral", messages=[{"role": "user", "content": prompt}])
    return {"response": response["message"]["content"]}
