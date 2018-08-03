import weakref
import trio

from cobald.interfaces import PoolDecorator
from cobald.daemon.service import service


class DrawLineHook(PoolDecorator):
    instances = {}

    @property
    def allocated(self):
        return self.supply * self.allocation

    def __init__(self, target, symbols='^v', maximum=100, minimum=0, style='[-]', identifier='default'):
        super().__init__(target=target)
        self.symbols = symbols
        self.identifier = identifier
        self._register(maximum, minimum, style)

    def _register(self, maximum=100, minimum=0, style='[-]'):
        try:
            self.instances[self.identifier].add(self)
        except KeyError:
            instances = self.instances[self.identifier] = weakref.WeakSet()
            instances.add(self)
        if self.identifier not in DrawLine.instances:
            DrawLine(self.identifier, maximum, minimum, style)


@service(flavour=trio)
class DrawLine:
    instances = {}

    def __init__(self, identifier: str, maximum: int, minimum: int, style: str):
        self.identifier = identifier
        self.maximum = maximum
        self.minimum = minimum
        self.style = style
        self.instances[identifier] = self

    @property
    def hooks(self):
        return list(DrawLineHook.instances[self.identifier])

    def __str__(self):
        line = [
            self.style[0],
            *[self.style[1]]*(self.maximum - self.minimum),
            self.style[2],
        ]
        for hook in self.hooks:
            demand, allocated, symbols = int(hook.demand), int(hook.allocated), hook.symbols
            for value, symbol in ((demand, symbols[:1]), (allocated, symbols[1:])):
                try:
                    line[self._coordinate(value)] = symbol
                except ValueError:
                    pass
        return ''.join(line)

    def _coordinate(self, value):
        if value <= self.maximum:
            relative_value = value - self.minimum
            if relative_value > 0:
                return relative_value
        raise ValueError

    async def run(self):
        while True:
            print(self)
            await trio.sleep(0.5)
