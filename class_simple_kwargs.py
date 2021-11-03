class Car:
    def __init__(self, **kwargs):
        self.data = kwargs
    def GetPrice(self):
        return self.data["price"] - (self.data["miles"]*2)

def main():
    myCar = Car(make="BMW", model="i3", year=2015, price=10000, miles=2000, owner="Jeff")
    print("{}'s car new Price {}".format(myCar.data["owner"],myCar.GetPrice()))

if __name__ == '__main__':main()