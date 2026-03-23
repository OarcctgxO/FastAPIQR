import concurrent.futures
from sys import version_info
from sysconfig import get_config_var

from settings import workers


def get_executor():
    """
    Возвращает Executor, наиболее подходящий для CPU-bound задач.
    Если GIL отключен (3.13+), возвращает ThreadPoolExecutor.
    Если версия >= 3.14, возвращает InterpreterPoolExecutor.
    Иначе или при любой ошибке возвращает ProcessPoolExecutor как наиболее универсальный выбор.
    """
    try:
        python_version = (version_info.major, version_info.minor)
        gil = True
        interpreter = False

        if python_version >= (3, 13):
            gil = not bool(get_config_var("Py_GIL_DISABLED"))
        if python_version >= (3, 14):
            interpreter = True

        if gil and interpreter:
            cpu_exec = concurrent.futures.InterpreterPoolExecutor(workers)
        elif not gil:
            cpu_exec = concurrent.futures.ThreadPoolExecutor(workers)
        else:
            cpu_exec = concurrent.futures.ProcessPoolExecutor(workers)
    except:
        cpu_exec = concurrent.futures.ProcessPoolExecutor(workers)
    
    return cpu_exec