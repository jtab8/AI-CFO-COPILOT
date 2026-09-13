"""
Anthropic Claude API wrapper.

SCAFFOLD. Replace with your hackathon implementation.
Keep the API key in the environment — never hardcode it.
"""

import os

from anthropic import Anthropic

client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))


def analyze(question: str, context: str) -> str:
    """Send a finance question plus retrieved context to Claude and return the answer."""
    # TODO: replace with your prompt and model configuration
    raise NotImplementedError
