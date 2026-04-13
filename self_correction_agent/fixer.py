import re
import os
from groq import Groq

MODEL_NAME = "llama-3.3-70b-versatile"

class AIFixer:
    def __init__(self):
        api_key = os.getenv("GROQ_API_KEY")
        if not api_key:
            raise ValueError("GROQ_API_KEY environment variable is not set.")
        self.client = Groq(api_key=api_key)

    def get_fix(self, code: str, error_message: str) -> str:

        prompt = (
            "Fix the following Python code. Return ONLY the corrected executable Python code without explanation.\n\n"
            "### Original Code ###\n"
            f"{code}\n\n"
            "### Error Message ###\n"
            f"{error_message}\n"
        )

        try:
            response = self.client.chat.completions.create(
                model=MODEL_NAME,
                messages=[
                    {
                        "role": "system",
                        "content": "You are an expert Python debugging AI. Output only corrected Python code."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.2
            )

            fixed_code = response.choices[0].message.content.strip()

            if fixed_code.startswith("```python"):
                fixed_code = fixed_code[9:]
            elif fixed_code.startswith("```"):
                fixed_code = fixed_code[3:]

            if fixed_code.endswith("```"):
                fixed_code = fixed_code[:-3]

            return fixed_code.strip()

        except Exception as e:
            raise RuntimeError(f"Failed to communicate with AI: {e}")