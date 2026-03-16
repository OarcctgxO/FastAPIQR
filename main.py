from fastapi import FastAPI
from fastapi.responses import Response
from concurrent.futures import InterpreterPoolExecutor
from os import cpu_count
from asyncio import get_running_loop

from qr_server_cpu import make_qr_code


app = FastAPI()
cpu_exec = InterpreterPoolExecutor(cpu_count())

@app.get("/{str_to_code}")
async def get_qr(str_to_code: str):
    loop = get_running_loop()
    fut = loop.run_in_executor(cpu_exec, make_qr_code, str_to_code)
    img_bytes = await fut
    return Response(content=img_bytes, media_type="image/png")