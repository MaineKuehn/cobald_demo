from cobald.controller.linear import LinearController

from cobald_demo.cpu_pool import CpuPool
from cobald_demo.draw_line import DrawLineHook

pool = CpuPool()
hook = DrawLineHook(pool)
controller = LinearController(hook, low_utilisation=0.9, high_allocation=1.1)
