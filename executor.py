import concurrent.futures
from os import cpu_count
from sys import version_info
from sysconfig import get_config_var


def get_executor():
    try:
        python_version = (version_info.major, version_info.minor)
        gil = True
        new = False
        interpreter = False

        if python_version >= (3, 13):
            gil = not bool(get_config_var("Py_GIL_DISABLED"))
            new = True
        if python_version >= (3, 14):
            interpreter = True

        if gil and interpreter:
            cpu_exec = concurrent.futures.InterpreterPoolExecutor(cpu_count())
        elif new and not gil:
            cpu_exec = concurrent.futures.ThreadPoolExecutor(cpu_count())
        else:
            cpu_exec = concurrent.futures.ProcessPoolExecutor(cpu_count())
    except:
        cpu_exec = concurrent.futures.ProcessPoolExecutor(cpu_count())
    
    return cpu_exec