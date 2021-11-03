class Car:
    def __init__(self, make, model, year, price, miles, owner):
        self.make = make
        self.model = model
        self.year = year
        self.price = price
        self.miles = miles
        self.owner = owner
    def GetPrice(self):
        return self.price - (self.miles*2)

def main():
    myCar = Car("BMW", "i3", 2015, 10000, 2000, "Jeff")
    print("{}'s car new Price {}".format(myCar.owner,myCar.GetPrice()))

if __name__ == '__main__':main()