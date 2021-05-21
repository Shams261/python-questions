## create a laptop class with different attribute.
# in this exmaple we also findout the discount rate. 
class Laptop:
    def __init__(self , model_name,model_number,price,generation):
        self.laptop_model_name = model_name
        self.laptop_model_number = model_number
        self.laptop_price = price
        self.laptop_generation = generation
    def discount(self,num):
        # self.price
        offer_price = (num/100)*self.laptop_price
        return self.laptop_price - offer_price

p1 = Laptop('hp',2051,2601562,1)
print(p1.discount(20))
#print()