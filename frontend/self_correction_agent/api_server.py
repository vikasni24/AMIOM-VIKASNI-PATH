import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from .runner import CodeRunner
from .fixer import AIFixer

app = FastAPI(title="Self-Correction AI Agent API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class CodeRequest(BaseModel):
    code: str
    model: str

class DebugResponse(BaseModel):
    error: str
    fixed_code: str

@app.post("/api/debug", response_model=DebugResponse)
def debug_code(request: CodeRequest):
    # Setup temporary file execution
    temp_filename = "temp_execution.py"
    try:
        with open(temp_filename, "w", encoding="utf-8") as f:
            f.write(request.code)
            
        success, stdout, stderr = CodeRunner.run_script(temp_filename)
        
        if success:
            return DebugResponse(error="", fixed_code=request.code)
            
        # If there's an error, initialize fixer and request fix
        # Ensure the AI uses the model requested by the user
        from . import fixer
        fixer.MODEL_NAME = request.model
        ai_fixer = AIFixer()
        
        fixed_code = ai_fixer.get_fix(request.code, stderr)
        return DebugResponse(error=stderr, fixed_code=fixed_code)
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        if os.path.exists(temp_filename):
            os.remove(temp_filename)
