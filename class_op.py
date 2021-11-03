class Operations:
    def sum(self, n1,n2):
        return n1+n2
    def div(self,n1,n2):
        return n1/n2
class MultipOperations(Operations):
    def multi(self,n1,n2):
        return n1*n2
    def sum(self, n1,n2):
        return (n1+n2)*2
    def sumParent(self, n1, n2):
        return super().sum(n1,n2)

def main():
    muOp = MultipOperations()
    print(muOp.multi(2,3))
    print(muOp.sum(2,3))
    print(muOp.sumParent(2,3))

if __name__ == '__main__':main()