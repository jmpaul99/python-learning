def main():
    out=open("test.txt","a")
    for i in range(5):
        inputToFile=input("enter string to write:")
        out.write("\n{}".format(inputToFile))
    out.close()

if __name__ == '__main__':main()
