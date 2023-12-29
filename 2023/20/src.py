from collections import defaultdict

BROADCASTER = "broadcaster"
PULSE_LOW, PULSE_HIGH = "pulse_low", "pulse_high"
STATE_OFF, STATE_ON = "off", "on"


class Module:
    def __init__(self, name, destination_names):
        self.name = name
        self.destination_names = destination_names

    def process_pulse(self, pulse_type):
        raise Exception("poop")


class BroadcasterModule(Module):
    def process_pulse(self, pulse):
        return [Pulse(pulse.type, self.name, destination_name) for destination_name in self.destination_names]


class FlipFlopModule(Module):
    def __init__(self, name, destination_names):
        Module.__init__(self, name, destination_names)
        self.state = STATE_OFF

    def process_pulse(self, pulse):
        output_pulses = []
        if pulse.type == PULSE_LOW:
            if self.state == STATE_OFF:
                self.state = STATE_ON
                output_pulse_type = PULSE_HIGH
            else:
                self.state = STATE_OFF
                output_pulse_type = PULSE_LOW
            output_pulses = [Pulse(output_pulse_type, self.name, destination_name) for destination_name in self.destination_names]
        return output_pulses


class ConjunctionModule(Module):
    def __init__(self, name, destination_names, connected_input_names):
        Module.__init__(self, name, destination_names)
        self.connected_input_pulse_types = {}
        for name in connected_input_names:
            self.connected_input_pulse_types[name] = PULSE_LOW

    def process_pulse(self, pulse):
        self.connected_input_pulse_types[pulse.origin] = pulse.type
        if set(self.connected_input_pulse_types.values()) == {PULSE_HIGH}:
            return [Pulse(PULSE_LOW, self.name, destination_name) for destination_name in self.destination_names]
        else:
            return [Pulse(PULSE_HIGH, self.name, destination_name) for destination_name in self.destination_names]


class NoOpModule(Module):
    def process_pulse(self, pulse):
        return []


class Pulse:
    counts = {PULSE_LOW: 0, PULSE_HIGH: 0}

    def __init__(self, pulse_type, origin, destination):
        self.type = pulse_type
        self.origin = origin
        self.destination = destination
        self.counts[pulse_type] += 1


in_to_out = defaultdict(list)
out_to_in = defaultdict(list)
types = {}
broadcaster = None
with open("input.txt") as file:
    for line in file.readlines():
        input_name, output_names = line.strip().split(" -> ")
        output_names = output_names.split(", ")
        if input_name == BROADCASTER:
            input_type = None
            broadcaster = BroadcasterModule(BROADCASTER, output_names)
        else:
            input_type = input_name[0]
            input_name = input_name[1:]
        types[input_name] = input_type
        in_to_out[input_name].extend(output_names)
        for output_name in output_names:
            out_to_in[output_name].append(input_name)

modules = {BROADCASTER: broadcaster}
for name, output_names in in_to_out.items():
    if types[name] is None:
        module = broadcaster
    elif types[name] == "%":
        module = FlipFlopModule(name, output_names)
    else:
        module = ConjunctionModule(name, output_names, out_to_in[name])
    modules[name] = module

for name in out_to_in:
    if name not in modules:
        modules[name] = NoOpModule(name, [])

for push_index in range(1000):
    cur_pulses = [Pulse(PULSE_LOW, None, BROADCASTER)]
    next_pulses = []
    while cur_pulses:
        for pulse in cur_pulses:
            next_pulses += modules[pulse.destination].process_pulse(pulse)
        cur_pulses = next_pulses
        next_pulses = []

print(Pulse.counts[PULSE_LOW] * Pulse.counts[PULSE_HIGH])
