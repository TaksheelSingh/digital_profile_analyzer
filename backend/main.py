from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from fastapi.responses import JSONResponse

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ProfileRequest(BaseModel):
    profile: str

@app.get("/")
def read_root():
    return {"message": "Welcome to the Digital Profile Analyzer API!"}

@app.post("/analyze")
def analyze_profile(request: ProfileRequest):
    # Dummy logic to simulate analysis
    profile_text = request.profile
    if "python" in profile_text.lower():
        return {"result": "You're a Python Developer! You might love Django or FastAPI."}
    elif "java" in profile_text.lower():
        return {"result": "You're a Java Developer! Spring Boot is your friend."}
    elif "github.com" in profile_text:
        return {"result": "GitHub profile detected! Pulling in your repositories... (just kidding)"}
    else:
        return {"result": "Could not determine the profile type. Please provide more details."}
