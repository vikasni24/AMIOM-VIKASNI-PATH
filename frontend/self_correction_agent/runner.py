import subprocess
from typing import Tuple

class CodeRunner:
    @staticmethod
    def run_script(filepath: str) -> Tuple[bool, str, str]:
        """
        Runs the python script locally using subprocess.
        Returns a tuple: (success, stdout, stderr_or_error_message).
        """
        try:
            result = subprocess.run(
                ["python", filepath],
                capture_output=True,
                text=True,
                check=False
            )
            
            success = result.returncode == 0
            stdout = result.stdout
            stderr = result.stderr
            
            return success, stdout, stderr
            
        except Exception as e:
            return False, "", str(e)
