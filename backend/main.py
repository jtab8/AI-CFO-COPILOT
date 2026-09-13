"""
AI CFO Copilot — API entry point.

SCAFFOLD. Replace the bodies below with your hackathon code.
The structure exists so the repo is readable before the code lands.
"""

import os

from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel

load_dotenv()

app = FastAPI(title="AI CFO Copilot")


class Question(BaseModel):
    """A finance question from the user, optionally scoped to a company."""

    text: str
    company: str | None = None


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.post("/ask")
def ask(question: Question) -> dict:
    """
    Answer a finance question.

    Intended flow:
      1. Retrieve supporting data for `question.company` via brightdata_client
      2. Pass the question plus retrieved data to claude_client
      3. Return the answer alongside the sources it was grounded in
    """
    # TODO: wire in retrieval + reasoning
    return {"answer": None, "sources": []}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=int(os.getenv("PORT", "8000")))
