from project.software.light_software import LightSoftware
from project.software.express_software import ExpressSoftware
from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware


class System:
    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        ph = PowerHardware(name, capacity, memory)
        System._hardware.append(ph)

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        hh = HeavyHardware(name, capacity, memory)
        System._hardware.append(hh)

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        hardware = [x for x in System._hardware if x.name == hardware_name]
        if not hardware:
            return "Hardware does not exist"
        es = ExpressSoftware(name, capacity_consumption, memory_consumption)
        try:
            hardware[0].install(es)
            System._software.append(es)
        except Exception:
            return "Software cannot be installed"

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        hardware = [x for x in System._hardware if x.name == hardware_name]
        if not hardware:
            return "Hardware does not exist"
        ls = LightSoftware(name, capacity_consumption, memory_consumption)
        try:
            hardware[0].install(ls)
            System._software.append(ls)
        except Exception:
            return "Software cannot be installed"

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        hardware_list = [x for x in System._hardware if x.name == hardware_name]
        software_list = [x for x in System._software if x.name == software_name]
        if hardware_list and software_list:
            hardware = hardware_list[0]
            software = software_list[0]
            hardware.uninstall(software)
            System._software.remove(software)
        else:
            return "Some of the components do not exist"

    @staticmethod
    def analyze():
        total_used_memory = sum([software.memory_consumption for hardware in System._hardware for software in hardware.software_components])
        total_used_capacity = sum([software.capacity_consumption for hardware in System._hardware for software in hardware.software_components])

        result = "System Analysis\n"
        result += f"Hardware Components: {len(System._hardware)}\n"
        result += f"Software Components: {len(System._software)}\n"
        result += f"Total Operational Memory: {total_used_memory} / {sum([x.memory for x in System._hardware])}\n"
        result += f"Total Capacity Taken: {total_used_capacity} / {sum([x.capacity for x in System._hardware])}"
        return result

    @staticmethod
    def system_split():
        result = ""
        for hardware in System._hardware:
            result += f"Hardware Component - {hardware.name}\n"
            number = len([software for software in hardware.software_components if software.__class__.__name__ == "ExpressSoftware"])
            result += f"Express Software Components: {number}\n"
            number = len([software for software in hardware.software_components if software.__class__.__name__ == "LightSoftware"])
            result += f"Light Software Components: {number}\n"
            used = sum([s.memory_consumption for s in hardware.software_components])
            result += f"Memory Usage: {used} / {hardware.memory}\n"
            used = sum([s.capacity_consumption for s in hardware.software_components])
            result += f"Capacity Usage: {used} / {hardware.capacity}\n"
            result += f"Type: {hardware.type}\n"
            components = None if not hardware.software_components else ', '.join(software.name for software in hardware.software_components)
            result += f"Software Components: {components}"
        return result
