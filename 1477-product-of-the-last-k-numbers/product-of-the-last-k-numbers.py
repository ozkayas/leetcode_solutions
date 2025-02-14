class ProductOfNumbers:

    def __init__(self):
        # Size will be +1 of the stream
        self.prefix = 1
        self.prefixProduct = []
        

    def add(self, num: int) -> None:
        if num == 0:
            self.prefix = 1
            self.prefixProduct = []
        else:
            self.prefix *= num
            self.prefixProduct.append(self.prefix)
        # print(self.prefix, "\n", self.prefixProduct)
        
    def getProduct(self, k: int) -> int:
        prefSize =  len(self.prefixProduct)
        if k > prefSize:
            return 0
        if k == prefSize:
            return self.prefixProduct[-1]
        return self.prefixProduct[-1]//self.prefixProduct[prefSize-k-1]
        
'''

 3 1 2 10 40
[3,0,2,5,4] - 1:4, 2:20, 3:40

 

'''

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
