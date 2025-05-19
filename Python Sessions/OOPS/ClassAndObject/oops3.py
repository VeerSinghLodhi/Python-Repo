class Product:
    def setProduct(self,pro_id,name,price):
        self.pro_id=pro_id
        self.name=name
        self.price=price
    def getProduct(self):
        print('Product id : ',self.pro_id)
        print('Name : ',self.name)
        print('Price : ',self.price)
    def getDiscount(self):
        if self.price>=10000:
            dis=self.price*5/100
            print('Discount : ',dis)

p1=Product()
p2=Product()
p1.setProduct(101,"A",6000)
p2.setProduct(102,"B",11000)

p1.getProduct()
p1.getDiscount()
print('----------------------------------')
p2.getProduct()
p2.getDiscount()