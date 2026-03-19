from subprocess import run
from sys import platform
from pathlib import Path

venv_path = Path(".venv")
try:
    if platform == "win32":
        activate = venv_path / "Scripts" / "activate.bat"
        cmd = f"call {activate} && uvicorn main:app --host 0.0.0.0 --port 8000 --reload"
        run(cmd, shell=True)
    else:
        activate = venv_path / "bin" / "activate"
        cmd = f"source {activate} && uvicorn main:app --host 0.0.0.0 --port 8000 --reload"
        run(["bash", "-c", cmd])
except KeyboardInterrupt:
    pass