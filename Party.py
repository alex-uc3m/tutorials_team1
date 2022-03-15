class Party:
    def __init__(self, age, DNI, drink):
        self.age = age
        self.DNI = DNI
        self.drink = drink

    def validate(self):
        if self.age >= 18 and self.DNI and self.drink:
            print("WELCOME TO THE PARTY")
            return True
        else:
            print("Go home please...")
            return False

if __name__ == "__main__":
    guests = [Party(19, False, True), Party(10, False, False), Party(100, True, True)]

    for guest in guests:
        guest.validate()
