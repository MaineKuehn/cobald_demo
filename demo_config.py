from cobald.controller.linear import LinearController

from cobald_demo.cpu_pool import CpuPool
from cobald_demo.draw_line import DrawLineHook

pipeline = LinearController.s(low_utilisation=0.9, high_allocation=1.1) >> DrawLineHook.s() >> CpuPool(interval=1)
