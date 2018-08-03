import threading
import psutil
import time

from cobald.interfaces import Pool
from cobald.daemon.service import service


@service(flavour=threading)
class CpuPool(Pool):
    """
    Dummy pool showing how demand is adjusted based on allocation/utilisation
    """
    #: we cannot really adjust the number of cores...
    demand = 0.0

    @property
    def supply(self):
        return self.demand

    @property
    def allocation(self):
        # how much resources are used from our (faked) resource pool
        try:
            return self._cpu_percent / self.demand
        except ZeroDivisionError:
            return 2.0

    utilisation = allocation

    def __init__(self, interval=0.1):
        self.interval = interval
        self.demand = 0.0
        self._cpu_percent = psutil.cpu_percent(0.1)

    def run(self):
        while True:
            self._cpu_percent = psutil.cpu_percent(self.interval)
            time.sleep(0.0)
