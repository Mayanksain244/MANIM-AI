import os
import sys
import uuid
import platform
import subprocess
from pathlib import Path
from typing import Optional, Tuple

OUTPUT_DIR = Path("outputs/videos")
TEMP_DIR = Path("outputs/temp")

def execute_manim_code(code: str) -> Optional[str]:
    """Execute Manim code using the virtual environment's Python and return path to video"""
    # Create output directories if they don't exist
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    TEMP_DIR.mkdir(parents=True, exist_ok=True)
    
    # Generate a unique filename
    file_id = uuid.uuid4().hex
    temp_file = TEMP_DIR / f"temp_{file_id}.py"
    output_file = OUTPUT_DIR / f"animation_{file_id}"
    
    # Write the code to a temporary file
    with open(temp_file, "w", encoding="utf-8") as f:
        f.write(code)
    
    try:
        # Extract the scene class name from the code
        scene_class = extract_scene_class(code)
        if not scene_class:
            raise ValueError("No valid Scene class found in the generated code")
        
        # Get Python executable from the virtual environment
        python_exec = sys.executable
        
        # Build the command to run Manim through Python with PYTHONHASHSEED=0
        command = [
            python_exec,
            "-m", "manim",
            str(temp_file),
            scene_class,
            "-ql",  # low quality for faster rendering
            "--output_file", output_file.name,
            "--media_dir", str(OUTPUT_DIR)
        ]
        
        # Set up environment variables
        env = os.environ.copy()
        env["PYTHONHASHSEED"] = "0"  # Disable hash randomization
        
        # Run the command
        result = subprocess.run(
            command,
            env=env,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=120
        )
        
        if result.returncode != 0:
            error_msg = f"Manim execution failed (code {result.returncode}):\n"
            error_msg += f"STDOUT:\n{result.stdout}\n"
            error_msg += f"STDERR:\n{result.stderr}"
            raise RuntimeError(error_msg)
        
        # Find the actual output file
        actual_output = find_output_file(output_file)
        if not actual_output:
            raise FileNotFoundError(f"Animation file was not generated. Searched for {output_file.stem}*.mp4")
        
        return str(actual_output)
    
    except subprocess.TimeoutExpired:
        raise RuntimeError("Manim rendering timed out after 120 seconds")
    except Exception as e:
        # Clean up temporary files
        if temp_file.exists():
            temp_file.unlink()
        raise e
    finally:
        # Clean up any temporary files
        pass

def extract_scene_class(code: str) -> Optional[str]:
    """Extract the first Scene class name from the code"""
    try:
        lines = code.split('\n')
        for line in lines:
            line = line.strip()
            if line.startswith("class ") and ("(Scene)" in line or "(Scene):" in line):
                return line.split("class ")[1].split("(")[0].strip()
        return None
    except Exception:
        return None

def find_output_file(base_path: Path) -> Optional[Path]:
    """Find the actual output file since Manim might add suffixes"""
    directory = base_path.parent
    
    # Look for files with the same stem but possibly different extensions
    for pattern in [f"{base_path.stem}*.mp4", f"{base_path.name}*.mp4"]:
        for file in directory.glob(pattern):
            return file
    
    return None