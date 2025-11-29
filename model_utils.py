# model_utils.py
from typing import Any
from PIL import Image
import io

# For now, these are simple placeholder functions.
# Later we will plug in LangChain, LlamaIndex, and a real multimodal model.

def handle_text_query(question: str) -> str:
    """Handle plain text questions."""
    if not question.strip():
        return "Please ask a question."
    # TODO: replace with real LLM call
    return f"You asked: '{question}'. This is a placeholder response for now."


def handle_image_query(image_file: Any, question: str) -> str:
    """Handle image + text questions."""
    try:
        # Read bytes from uploaded image to ensure it's valid
        image_bytes = image_file.read()
        image = Image.open(io.BytesIO(image_bytes))
        _ = image.size  # just to ensure it's loadable
    except Exception:
        return "Could not read the uploaded image. Please try another image."

    if not question.strip():
        question = "Describe this image."

    # TODO: replace with multimodal model
    return (
        f"(Placeholder) I received an image of size {image.size} "
        f"and your question: '{question}'. "
        "Later I'll use a real multimodal model to answer."
    )
