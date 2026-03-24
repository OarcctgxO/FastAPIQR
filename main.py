from fastapi import FastAPI, Path, Response
import uvicorn

import asyncio
from concurrent.futures import ProcessPoolExecutor
from typing import Annotated
from threading import Thread

from qr_code_maker import make_qr_code
from udp_broadcast_discover.check_existing import is_there_running_server
from udp_broadcast_discover.udp_discover_server import UdpDiscoverer
from settings import host, port, workers


app = FastAPI()
cpu_exec = ProcessPoolExecutor(workers)


@app.get("/{str_to_code}")
async def get_qr(str_to_code: Annotated[str, Path(min_length=1, max_length=1000)]):
    loop = asyncio.get_running_loop()
    fut = loop.run_in_executor(cpu_exec, make_qr_code, str_to_code)
    img_bytes = await fut
    return Response(content=img_bytes, media_type="image/png")


if __name__ == '__main__':
    if not is_there_running_server():
        udp_server = Thread(target=UdpDiscoverer().sync_work, daemon=True) # type: ignore
        fastapi_server = Thread(target=uvicorn.run, args=("main:app", ), kwargs={'host': host, 'port': port}, daemon=True)
        
        udp_server.start()
        fastapi_server.start()
        try:
            udp_server.join()
        except KeyboardInterrupt:
            pass