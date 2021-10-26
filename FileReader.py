def main():
    try:
        file = open("tesft.txt", "r")
        print(file.read())
        file.close()
    except BaseException:
        print("An error occured")

if __name__ == '__main__': main()
