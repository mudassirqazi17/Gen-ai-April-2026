import os
import google.generativeai as genai


def ask_gemini(question, docs):
    key = os.getenv("GEMINI_API_KEY")
    genai.configure(api_key=key)

    context = "\n".join(docs)

    prompt = f"""
Answer using the provided context.

Context:
{context}

Question:
{question}
"""

    models = [
        "gemini-2.5-flash-lite"
    ]

    for name in models:
        try:
            model = genai.GenerativeModel(name)
            response = model.generate_content(prompt)
            return response.text
        except Exception:
            continue

    return "No available model found for this API key/project."
