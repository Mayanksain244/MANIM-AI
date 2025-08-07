from groq import Groq
from typing import List

def fix_code(code: str, errors: List[str], api_key: str) -> str:
    """Attempt to fix the code based on verification errors"""
    client = Groq(api_key=api_key)
    
    error_message = "\n".join(errors)
    prompt = f"""The following Manim code has errors:
{code}

Errors detected:
{error_message}

Please fix the code while maintaining all the original functionality. 
Return ONLY the corrected code with no additional explanation.
NO PREAMBLE
without '''python at start and ''' at the end"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
        max_tokens=2000
    )
    
    return response.choices[0].message.content