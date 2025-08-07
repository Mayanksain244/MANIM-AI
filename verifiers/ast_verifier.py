import ast
import re
from typing import Dict, List

def verify_code(code: str) -> Dict:
    """Verify the generated Manim code using AST and safety checks"""

    
    result = {
        "is_valid": True,
        "errors": []
    }
    
    # Basic checks before AST parsing
    if not code.strip():
        result["is_valid"] = False
        result["errors"].append("Empty code")
        return result
    
    # Check for required imports
    if "from manim import *" not in code:
        result["is_valid"] = False
        result["errors"].append("Missing 'from manim import *'")
    
    # Check for Scene class
    if "class " not in code or "Scene" not in code:
        result["is_valid"] = False
        result["errors"].append("No Scene class found")
    
    try:
        # Parse the AST
        tree = ast.parse(code)
        
        # Check for dangerous constructs
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    if alias.name in ["os", "sys", "subprocess"]:
                        result["is_valid"] = False
                        result["errors"].append(f"Dangerous import detected: {alias.name}")
            
            if isinstance(node, ast.Call):
                if hasattr(node.func, 'id') and node.func.id in ['eval', 'exec', 'open']:
                    result["is_valid"] = False
                    result["errors"].append(f"Dangerous function call detected: {node.func.id}")
    
    except SyntaxError as e:
        result["is_valid"] = False
        result["errors"].append(f"Syntax error: {str(e)}")
    
    return result