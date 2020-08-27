from project.hardware.hardware import Hardware


class HeavyHardware(Hardware):
    def __init__(self, name, capacity, memory):
        Hardware.__init__(self, name, "Heavy", 2 * capacity, int(0.75 * memory))
