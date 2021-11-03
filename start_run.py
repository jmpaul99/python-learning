from class_op import MultipOperations

def main():
    muOp = MultipOperations()
    print(muOp.multi(1,3))
    print(muOp.sum(1,3))
    print(muOp.div(1,3))

if __name__ == '__main__':main()