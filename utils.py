import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get API key
api_key = os.getenv("OPENAI_API_KEY")

# Initialize client only if key exists
client = OpenAI(api_key=api_key) if api_key else None


def summarize_text(text: str) -> str:
    """
    Summarizes text using LLM.
    Falls back to mock response if API fails or quota is exceeded.
    """
    
    # 🟢 Try real API (if available)
    if client:
        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {
                        "role": "system",
                        "content": "You are a helpful summarizer."
                    },
                    {
                        "role": "user",
                        "content": f"Summarize this text in bullet points:\n{text}"
                    }
                ],
                temperature=0.4
            )

            return response.choices[0].message.content

        except Exception as e:
            print("API Error:", e)

    # 🟡 Fallback (Mock response)
    return (
        "• Key ideas are summarized clearly\n"
        "• Important points extracted from text\n"
        "• Simplified for quick understanding\n"
        "• Demonstrates AI-based summarization"
    )
