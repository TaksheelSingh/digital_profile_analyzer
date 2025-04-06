from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from analyzer import analyze_profile

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/analyze")
async def analyze(request: Request):
    data = await request.json()
    result = analyze_profile(data)
    return result