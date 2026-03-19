from fastapi import FastAPI, Path, Response

from asyncio import get_running_loop
from typing import Annotated

from qr_code_maker import make_qr_code
from executor import get_executor


app = FastAPI()
cpu_exec = get_executor()


@app.get("/{str_to_code}")
async def get_qr(str_to_code: Annotated[str, Path(min_length=1, max_length=1000)]):
    loop = get_running_loop()
    fut = loop.run_in_executor(cpu_exec, make_qr_code, str_to_code)
    img_bytes = await fut
    return Response(content=img_bytes, media_type="image/png")