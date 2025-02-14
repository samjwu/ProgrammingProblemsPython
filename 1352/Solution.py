class ProductOfNumbers:

    def __init__(self):
        self.prefix_product = [1]
        self.n = 0

    def add(self, num: int) -> None:
        if num == 0:
            self.__init__()
        else:
            product = self.prefix_product[self.n] * num
            self.prefix_product.append(product)
            self.n += 1

    def getProduct(self, k: int) -> int:
        if k > self.n:
            return 0
        
        return self.prefix_product[self.n] // self.prefix_product[self.n - k]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
