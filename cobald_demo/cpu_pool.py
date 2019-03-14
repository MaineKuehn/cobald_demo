import threading
import psutil
import time

from cobald.interfaces import Pool
from cobald.daemon import service


@service(flavour=threading)
class CpuPool(Pool):
    """
    Dummy pool showing how demand is adjusted based on allocation/utilisation
    """
    #: we cannot really adjust the number of cores...
    demand = 0.0

    @property
    def supply(self):
        """The current supply this pool could provide"""
        #: TODO: make this drag behind instead of just copying demand
        return self.demand

    @property
    def allocation(self):
        """Fraction of the supply actively allocated for use"""
        # how much resources are used from our (faked) resource pool
        try:
            return self._cpu_percent / self.demand
        except ZeroDivisionError:
            return 2.0

    #: Fraction of the supply actively used
    utilisation = allocation

    def __init__(self, interval=0.1):
        self.interval = interval
        self.demand = 0.0
        self._cpu_percent = psutil.cpu_percent(0.1)

    # entry point for the ``service`` background process
    def run(self):
        while True:
            self._cpu_percent = psutil.cpu_percent(self.interval)
            time.sleep(0.0)
