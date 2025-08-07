import os
from dotenv import load_dotenv
from generators.code_generator import generate_manim_code
from verifiers.ast_verifier import verify_code
from fixers.code_fixer import fix_code
from executors.manim_executor import execute_manim_code

load_dotenv()

class Prompt2Anim:
    def __init__(self):
        self.groq_api_key = os.getenv("GROQ_API_KEY")
        if not self.groq_api_key:
            raise ValueError("GROQ_API_KEY not found in .env file")

    def process_prompt(self, prompt: str) -> str:
        """Main pipeline: prompt -> code -> verification -> fixing -> execution"""
        # Step 1: Generate initial code
        generated_code = generate_manim_code(prompt, self.groq_api_key)
        print(f"Generated code:\n{generated_code}")


        
        # Step 2: Verify code
        verification_result = verify_code(generated_code)
        if not verification_result["is_valid"]:
            print(f"Code verification failed: {verification_result['errors']}")
            
            # Step 3: Attempt to fix code
            fixed_code = fix_code(generated_code, verification_result["errors"], self.groq_api_key)
            print(f"Attempting to fix code:\n{fixed_code}")
            
            # Verify fixed code
            fixed_verification = verify_code(fixed_code)
            if not fixed_verification["is_valid"]:
                raise ValueError(f"Unable to fix code. Errors: {fixed_verification['errors']}")
            
            generated_code = fixed_code


            
        
        # Step 4: Execute the code
        video_path = execute_manim_code(generated_code)
        return video_path

if __name__ == "__main__":
    animator = Prompt2Anim()
    prompt = input("Enter your animation prompt: ")
    try:
        video_path = animator.process_prompt(prompt)
        print(f"Animation successfully created at: {video_path}")
    except Exception as e:
        print(f"Error creating animation: {str(e)}")