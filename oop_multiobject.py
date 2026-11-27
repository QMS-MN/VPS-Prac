class car:
    def __init__(self,brand,price):
        self.brand = brand
        self.price = price

    def print_car_det(self):
        print(self.brand ,'-', self.price)    


car1 = car('BMW',500000)
car2 = car('Aoudi',100000)
car3 = car('Maruti',200000)

car1.print_car_det()
car2.print_car_det()
car3.print_car_det()