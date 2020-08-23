from project.technology.technology import Technology


class Laptop(Technology):

    def install_software(self, software, software_memory):
        try:
            memory_left = self.get_capacity(self.memory, self.memory_taken + software_memory)
            self.memory_taken += software_memory
            return memory_left
        except Exception as ex:
            return f"You don't have enough space for {software}!"
