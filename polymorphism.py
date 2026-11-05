#  1.Write a Python program to implement an Online Shopping Discount System using inheritance and method overriding.
#   Create electronics, clothing, and grocery classes with 10%, 20%, and 5% discounts respectively

class product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def calculate_discount(self):
        pass

class electronics(product):
    def __init__(self, name, price):
        super().__init__(name, price)

    def calculate_discount(self):
        discount = self.price * 0.10
        total_price = self.price - discount
        return discount, total_price

class clothing(product):
    def __init__(self, name, price):
        super().__init__(name, price)

    def calculate_discount(self):
        discount = self.price * 0.20
        total_price = self.price - discount
        return discount, total_price

class grocery(product):
    def __init__(self, name, price):
        super().__init__(name, price)

    def calculate_discount(self):
        discount = self.price * 0.05
        total_price = self.price - discount
        return discount, total_price
e1 = electronics('laptop', 5000)
c1 = clothing('shirt', 3000)
g1 = grocery('wallet', 1000)
objects = [e1, c1, g1]
def display():
    for obj in objects:
        discount, total_price = obj.calculate_discount()

        print(f'Product name is: {obj.name}')
        print(f'Price is: {obj.price}')
        print(f'Discount is: {discount}')
        print(f'Total price is: {total_price}')
        print()
display()



# 2.  Create three classes: Circle → area() Rectangle → area() Square → area()

class circle():
    def __init__(self,r):
        self.r=r
            
    def area(self):
        print(3.14*self.r*self.r)
            
class rectangle():
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        print(self.length*self.breadth)
            
class square():
    def __init__(self,side):
        self.side=side
    def area(self):
        print(self.side*self.side)

c1=circle(12)
r1=rectangle(12,12)
s1=square(4)
objects=[c1,r1,s1]
def display():
    for obj in objects:
        obj.area()
display()


#  3.  create 3 classes Use __init__() to initialize a user name in each class.Use the same send() method.
#Create three objects.Store them in a list.Call send() using a loop.


class email:
    def __init__(self,name):
        self.name=name
    def send(self):
        print(f'{self.name} notification send through email')
        
class sms:
    def __init__(self, name):
        self.name = name

    def send(self):
        print(f'{self.name} notification sent through SMS')


class whatsapp:
    def __init__(self, name):
        self.name = name

    def send(self):
        print(f'{self.name} notification sent through WhatsApp')
        
e1=email('chandu')
s1=sms('bhanu')
w1=whatsapp('kishore')
objects=[e1,s1,w1]

def display():
    for obj in objects:
        obj.send()
display()


#  4.Create all three classes.Create their objects.Store the objects in a list. Use a loop to call pay().

class googlepay():
    def payment(self):
        print('payment done through googlepay')
        
class creditcard():
    def payment(self):
        print('payment done through card')
        
class cash():
    def payment(self):
        print('payment completed by paying cash')
g1=googlepay()
c1=creditcard()
c2=cash()
objects=[g1,c1,c2]
def display():
    for obj in objects:
        obj.payment()
display()