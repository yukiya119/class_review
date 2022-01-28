class Customer:
    def __init__(self, first_name, family_name, age):
        self.firstname = first_name
        self.familyname = family_name
        self.age = age

    def full_name(self):
        print(f"{self.firstname} {self.familyname}")


ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
ken.full_name()  # "Ken Tanaka" という値を返す
print(ken.age)

tom = Customer(first_name="Tom", family_name="Ford", age=57)
tom.full_name()  # "Tom Ford" という値を返す
print(tom.age)

ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)
ieyasu.full_name()
print(ieyasu.age) # 73 という値を返す
