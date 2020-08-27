from project.software.software import Software


class Hardware:
    def __init__(self, name, type, capacity, memory):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.memory = memory
        self.software_components = []

    def install(self, software: Software):
        occupied_capacity = sum([x.capacity for x in self.software_components])
        occupied_memory = sum([x.memory for x in self.software_components])
        if occupied_capacity + software.capacity_consumption > self.capacity or\
                occupied_memory + software.memory_consumption > self.memory:
            raise Exception("Software cannot be installed")
        self.software_components.append(software)

    def uninstall(self, software: Software):
        if software in self.software_components:
            self.software_components.remove(software)
