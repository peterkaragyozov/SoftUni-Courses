import datetime


class DVD:
    def __init__(self, name: str, id: int, creation_year: int, creation_month: str, age_restriction: int):
        self.name = name
        self.id = id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    def check_status(self):
        return self.is_rented

    def __repr__(self):
        if self.check_status():
            return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) has age restriction {self.age_restriction}. Status: rented"
        return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) has age restriction {self.age_restriction}. Status: not rented"

    @classmethod
    def from_date(cls, id: int, name: str, date: str, age_restriction: int):
        (day, month_number, year) = date.split(".")
        datetime_object = datetime.datetime.strptime(month_number, "%m")
        full_month_name = datetime_object.strftime("%B")
        return cls(name, id, int(year), full_month_name, age_restriction)