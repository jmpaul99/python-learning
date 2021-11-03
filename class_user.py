class User:
    def __init__(self, userName):
        self.userName = userName

def main():
    u1 = User("Jeff")
    print(u1.userName)
    u2 = User("Hussein")
    print(u2.userName)

if __name__ =='__main__':main()