# need examples of inheritance and multiple inheritance

class Employee:
    def __init__(self, ID, salary):
        self.ID = ID
        self.__salary = salary  # salary is a private property

    # private method
    def __displayID(self):
        print(f"ID: {self.ID}")

me = Employee(3789, 2500)
print("ID:", me.ID)
