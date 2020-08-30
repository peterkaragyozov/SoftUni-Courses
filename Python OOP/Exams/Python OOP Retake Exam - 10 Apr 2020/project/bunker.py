class Bunker:
    def __init__(self):
        self.survivors = []
        self.supplies = []
        self.medicine = []

    @property
    def food(self):
        food_supplies = [o for o in self.supplies if o.__class__.__name__ == "FoodSupply"]
        if len(food_supplies) == 0:
            raise IndexError("There are no food supplies left!")
        return food_supplies

    @property
    def water(self):
        water_supplies = [o for o in self.supplies if o.__class__.__name__ == "WaterSupply"]
        if len(water_supplies) == 0:
            raise IndexError("There are no water supplies left!")
        return water_supplies

    @property
    def painkillers(self):
        painkillers_supplies = [o for o in self.medicine if o.__class__.__name__ == "Painkiller"]
        if len(painkillers_supplies) == 0:
            raise IndexError("There are no painkillers left!")
        return painkillers_supplies

    @property
    def salves(self):
        salves_supplies = [o for o in self.medicine if o.__class__.__name__ == "Salve"]
        if len(salves_supplies) == 0:
            raise IndexError("There are no salves left!")
        return salves_supplies

    def add_survivor(self, survivor):
        if survivor in self.survivors:
            raise ValueError(f"Survivor with name {survivor.name} already exists.")
        self.survivors.append(survivor)

    def add_supply(self, supply):
        self.supplies.append(supply)

    def add_medicine(self, medicine):
        self.medicine.append(medicine)

    def heal(self, survivor, medicine_type):
        if not survivor.needs_healing:
            return

        if medicine_type == "Painkiller":
            pill = self.painkillers[-1]
        else:
            pill = self.salves[-1]
        del self.medicine[-1]
        pill.apply(survivor)
        return f"{survivor.name} healed successfully with {medicine_type}"

    def sustain(self, survivor, sustenance_type):
        if not survivor.needs_sustenance:
            return

        if sustenance_type == "FoodSupply":
            supp = self.food[-1]
        else:
            supp = self.water[-1]
        del self.supplies[-1]
        supp.apply(survivor)
        return f"{survivor.name} sustained successfully with {sustenance_type}"

    def next_day(self):
        for s in self.survivors:
            s.needs -= s.age * 2

        for s in self.survivors:
            self.sustain(s, "FoodSupply")
            self.sustain(s, "WaterSupply")
