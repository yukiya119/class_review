class Customer:
    def __init__(self, first_name, family_name, age):
        self.firstname = first_name
        self.familyname = family_name
        self.age = age

    def full_name(self):
        print(f"{self.firstname} {self.familyname}")

    def entry_fee(self):
        if self.age < 20:
            return 1000
        elif self.age < 65:
            return 1500
        else:
            return 1200

    def info_csv(self):
        print(str(self.firstname) + " " + str(self.familyname) + "," + str(self.age) + "," + str(self.entry_fee()))


print("■ANSER■")  # 回答が見やすいように便宜上記載
ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
ken.full_name()  # "Ken Tanaka" という値を返す
print(ken.age)
print(ken.entry_fee())  # 1000 という値を返す
print(ken.info_csv())  # "Ken Tanaka,15,1000" という値を返す
print("\n", end="")

tom = Customer(first_name="Tom", family_name="Ford", age=57)
tom.full_name()  # "Tom Ford" という値を返す
print(tom.age)
print(tom.entry_fee())  # 1500 という値を返す
print(ken.info_csv())  # "Ken Tanaka,15,1000" という値を返す
print("\n", end="")

ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)
ieyasu.full_name()
print(ieyasu.age)  # 73 という値を返す
print(ieyasu.entry_fee())  # 1200 という値を返す
print(ken.info_csv())  # "Ken Tanaka,15,1000" という値を返す
