from fastapi import FastAPI

app = FastAPI(
    title="AI Lab 7",
    description="A lightweight, non-commercial educational API for learning AI application basics.",
    version="0.1.0",
)


@app.get("/")
def home():
    return {
        "project": "AI Lab 7",
        "purpose": "Open-source AI API education",
        "status": "online",
    }


@app.get("/health")
def health():
    return {"ok": True}
