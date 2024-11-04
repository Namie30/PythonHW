class Person:
    def __init__(self, name, deposit=1000, loan=0):
        self.name = name
        self.deposit = deposit
        self.loan = loan

    def __str__(self):
        return f"Name: {self.name}, Deposit: {self.deposit}, Loan: {self.loan}"

class House:
    def __init__(self, ID, price, owner):
        self.ID = ID
        self.price = price
        self.owner = owner
        self.status = "for sale"

    def sell(self, buyer, loan_amount=0):
        self.owner.deposit += self.price

        self.owner = buyer

        if loan_amount > 0:
            buyer.loan += loan_amount
            self.status = "sold on loan"
            print(f"Apartment sold on loan. Loan amount: {loan_amount}")
        else:
            self.status = "sold"
            print("Apartment sold without loan.")

        print(f"New Owner: {buyer.name}, Sale Status: {self.status}")


seller = Person("Alice")
buyer = Person("Bob")


house = House("123-456", 50000, seller)

print("Initial Owner Information:")
print(seller)
print("\nHouse Information:")
print(f"House ID: {house.ID}, Price: {house.price}, Status: {house.status}, Owner: {house.owner.name}")


house.sell(buyer)

print("\nUpdated Owner Information:")
print(buyer)
print(seller)

house = House("123-456", 50000, seller)
house.sell(buyer, loan_amount=20000)


print("\nFinal Buyer Information:")
print(buyer)
