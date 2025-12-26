# کلاس والد
class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def display_info(self):
        print(f"برند: {self.brand}")
        print(f"سال ساخت: {self.year}")

# کلاس فرزند Car
class Car(Vehicle):
    def __init__(self, brand, year, num_doors):
        super().__init__(brand, year)
        self.num_doors = num_doors

    def display_info(self):
        super().display_info()
        print(f"تعداد درها: {self.num_doors}")

# کلاس فرزند Motorcycle
class Motorcycle(Vehicle):
    def __init__(self, brand, year, has_sidecar):
        super().__init__(brand, year)
        self.has_sidecar = has_sidecar

    def display_info(self):
        super().display_info()
        print(f"دارای سایدکار: {'بله' if self.has_sidecar else 'خیر'}")

# ساخت شی از هر کلاس
v1 = Vehicle("بنز", 2015)
c1 = Car("تویوتا", 2020, 4)
m1 = Motorcycle("هوندا", 2018, False)

# نمایش اطلاعات
print("اطلاعات وسیله نقلیه:")
v1.display_info()

print("\nاطلاعات ماشین:")
c1.display_info()

print("\nاطلاعات موتور:")
m1.display_info()