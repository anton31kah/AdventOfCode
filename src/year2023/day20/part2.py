from collections import deque
from src.common.common import get_lines
from dataclasses import dataclass, field

@dataclass
class Module:
    name: str
    input_modules: set['Module']
    output_modules: set['Module']

    def processSignal(self, pulse: bool, signal: 'Signal') -> bool:
        if self.name == 'rx' and not pulse:
            raise ValueError("GOT THE ANSWER")
        return None

    def dirty(self):
        return False

    def __repr__(self) -> str:
        return self.name
    
    def __hash__(self) -> int:
        return hash(self.name)

@dataclass
class FlipFlopModule(Module):
    state: bool # off -> False, on -> True

    def processSignal(self, pulse: bool, signal: 'Signal') -> bool:
        if pulse:
            return None
        
        # low pulse

        self.state = not self.state
        return self.state

    def dirty(self):
        return self.state

    def __repr__(self) -> str:
        return f"{self.name} [{'on' if self.state else 'off'}]"

    def __hash__(self) -> int:
        return hash(self.name)

@dataclass
class ConjunctionModule(Module):
    memory: dict[str, bool] # low -> False, high -> True

    def processSignal(self, pulse: bool, signal: 'Signal') -> bool:
        self.memory[signal.source.name] = pulse
        if all(self.memory.get(mod.name, False) for mod in self.input_modules):
            return False
        return True

    def is_done(self):
        return all(self.memory.get(mod.name, False) for mod in self.input_modules)

    def dirty(self):
        return any(self.memory.get(mod.name, False) for mod in self.input_modules)

    def __repr__(self) -> str:
        memory_str = ','.join(f"{mod.name}:{'high' if self.memory[mod.name] else 'low'}" for mod in self.input_modules)
        return f"{self.name} [{memory_str}]"

    def __hash__(self) -> int:
        return hash(self.name)

@dataclass
class BroadcastModule(Module):
    def processSignal(self, pulse: bool, signal: 'Signal') -> bool:
        return pulse

    def dirty(self):
        return False

    def __repr__(self) -> str:
        return self.name
    
    def __hash__(self) -> int:
        return hash(self.name)

@dataclass
class Signal:
    source: Module
    destinations: list[Module]
    pulse: bool

    def __str__(self) -> str:
        return f"{self.source.name} -{'high' if self.pulse else 'low'}-> {self.destinations[0].name}"

MODULES_TYPE = dict[str, Module]
SIGNALS_TYPE = dict[str, Signal]

def parse_input(lines):
    modules: MODULES_TYPE = {}
    signals: SIGNALS_TYPE = {}

    for line in lines:
        source, destination = line.split(" -> ")

        source_module: Module = None
        if source == 'broadcaster':
            source_module = BroadcastModule(name=source, input_modules=set(), output_modules=set())
        elif source.startswith('%'):
            source_module = FlipFlopModule(name=source[1:], state=False, input_modules=set(), output_modules=set())
        elif source.startswith('&'):
            source_module = ConjunctionModule(name=source[1:], memory={}, input_modules=set(), output_modules=set())
        modules[source_module.name] = source_module

        destinations = destination.split(', ')

        signals[source_module.name] = Signal(source_module, destinations, None)

    for signal in signals.values():
        destinations_names = signal.destinations[:]
        signal.destinations = []

        for dest in destinations_names:
            if dest not in modules:
                modules[dest] = Module(name=dest, input_modules=set(), output_modules=set())
            modules[dest].input_modules.add(signal.source)
            signal.destinations.append(modules[dest])

        src = signal.source
        for dest in signal.destinations:
            src.output_modules.add(dest)
            dest.input_modules.add(src)
    
    modules['button'] = Module(name='button', input_modules=set(), output_modules={modules['broadcaster']})
    signals['button'] = Signal(modules['button'], [modules['broadcaster']], False)

    return signals, modules

def count_signals(signals: SIGNALS_TYPE, modules: MODULES_TYPE):
    queue: deque[Signal] = deque([])

    queue.append(signals['button'])

    high_pulses = 0
    low_pulses = 0

    while queue:
        signal = queue.popleft()
        
        if signal.pulse:
            high_pulses += 1
        else:
            low_pulses += 1

        # print(signal)

        dest = signal.destinations[0]
        new_pulse = dest.processSignal(signal.pulse, signal)

        if new_pulse is not None:
            for new_dest in signals[dest.name].destinations:
                queue.append(Signal(dest, [new_dest], new_pulse))

    return high_pulses, low_pulses

def main():
    lines = get_lines('')
    signals, modules = parse_input(lines)

    for mod in modules.values():
        print(mod.name, [m.name for m in mod.input_modules], [m.name for m in mod.output_modules])

    buttons_pushed = 0

    while True:
        buttons_pushed += 1
        # print(buttons_pushed)
        count_signals(signals, modules)
        # dirty_modules = [mod for mod in modules.values() if mod.dirty()]
        # if not dirty_modules:
            # break
        if buttons_pushed % 10000 == 0:
            print(buttons_pushed)

    print(buttons_pushed)


if __name__ == "__main__":
    main()
