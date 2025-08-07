from groq import Groq
from .prompts import SYSTEM_PROMPT, FEW_SHOT_EXAMPLES

def generate_manim_code(prompt: str, api_key: str) -> str:
    """Generate Manim code from natural language prompt using Groq API"""
    client = Groq(api_key=api_key)
    
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        *FEW_SHOT_EXAMPLES,
        {"role": "user", "content": prompt}
    ]
    
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",  # or "llama3-70b-8192"
        messages=messages,
        temperature=0.3,
        max_tokens=2000,
        top_p=1,
        stop=None,
    )
    
    return response.choices[0].message.content