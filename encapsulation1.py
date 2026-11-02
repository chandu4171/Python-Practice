# encapsulation:  accessing the data for only Authorizing persons 

# class Student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     def details(self):
#         print(f' name is : {self.name}')
#         print(f'marks is : {self.marks}')

# s1=Student('chandu',99)
# s1.details()
# print(s1.name)



# write a program to print id,salary,name of a employee and add hike and print total salary
# class employee:
#     def __init__(self,id,salary,name):
#         self.id=id
#         self._salary=salary
#         self.name=name

#     def details(self):
#         print(f'employee id is: {self.id}')
#         print(f'employee salary is: {self._salary}')
#         print(f'employee name is: {self.name}')

#     def salary_hike(self,amount):
#         self._salary+=self._salary+amount
#         print(f'total salary after adding salary_hike is : {self._salary}')

# e1=employee(563,50000,'chandu')
# e1.details()

# print(e1.name)
# print(e1._salary)
# e1.salary_hike(5000)


# write a program to print name,account number,balance of a customer using protected
# class bank:
#     def __init__(self,name,accountnum,balance):
#         self.name=name
#         self._accountnum=accountnum
#         self.__balance=balance

#     def details(self):
#         print(f' name is : {self.name}')
#         print(f'account number is : {self._accountnum}')

#     def balance_check(self):
#         print(f'account balance is : {self.__balance}')

# b1=bank('chandu',9392503201,500000)
# b1.details()
# b1.balance_check()
# print(b1.balance)



#write a private method and access the data to print the salary of an emloyee based on the company profits
class movate:
    def __init__(self,price,quantity):
        self.price=price
        self._quantity=quantity

    def __profit(self):
        investors=50000000000
        sales=self.price*self._quantity
        tax=sales*0.20
        shares=1000000
        netpro=investors+sales+tax+shares
        return netpro
    def income(self):
        salary=self.__profit()*0.10
        return salary


m1=movate(34567,5)
print(m1.income())



 








































