x = 10

def show():
    global x
    print(x)


def main():
    global x
    show()
    print("x={}".format(x))


if __name__ == '__main__': main()
