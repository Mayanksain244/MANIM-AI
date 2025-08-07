import subprocess
from typing import NamedTuple

class ExecutionResult(NamedTuple):
    returncode: int
    stdout: str
    stderr: str

def run_in_sandbox(command: str, timeout: int = 30) -> ExecutionResult:
    """Run a command in a restricted environment"""
    try:
        result = subprocess.run(
            command,
            shell=True,
            timeout=timeout,
            capture_output=True,
            text=True,
            # Additional security measures
            env={"PATH": "/usr/bin", "PYTHONPATH": ""},
        )
        return ExecutionResult(
            returncode=result.returncode,
            stdout=result.stdout,
            stderr=result.stderr
        )
    except subprocess.TimeoutExpired:
        return ExecutionResult(
            returncode=-1,
            stdout="",
            stderr=f"Command timed out after {timeout} seconds"
        )
    except Exception as e:
        return ExecutionResult(
            returncode=-1,
            stdout="",
            stderr=str(e)
        )