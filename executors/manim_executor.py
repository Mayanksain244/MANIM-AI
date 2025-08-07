import os
import subprocess
import uuid
from pathlib import Path
from typing import Optional
from .sandbox import run_in_sandbox

OUTPUT_DIR = Path("outputs/videos")
TEMP_DIR = Path("outputs/temp")

def execute_manim_code(code: str) -> Optional[str]:
    """Execute Manim code in a sandbox and return path to video"""
    # Create output directories if they don't exist
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    TEMP_DIR.mkdir(parents=True, exist_ok=True)
    
    # Generate a unique filename
    file_id = uuid.uuid4().hex
    temp_file = TEMP_DIR / f"temp_{file_id}.py"
    output_file = OUTPUT_DIR / f"animation_{file_id}.mp4"
    
    # Write the code to a temporary file
    with open(temp_file, "w") as f:
        f.write(code)
    
    try:
        # Run in sandbox with timeout
        result = run_in_sandbox(
            f"manim -ql -o {output_file.stem} {temp_file}",
            timeout=60
        )
        
        if result.returncode != 0:
            raise RuntimeError(f"Manim execution failed: {result.stderr}")
        
        # Verify video was created
        if not output_file.exists():
            raise FileNotFoundError("Animation file was not generated")
        
        return str(output_file)
    
    except Exception as e:
        # Clean up temporary files
        if temp_file.exists():
            temp_file.unlink()
        raise e