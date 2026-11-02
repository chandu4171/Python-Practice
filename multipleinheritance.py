# multilple inheritence: one child class act as parent class to upcoming child class there is one child class and more than one parent class

# import time
# class watch:
#     def curr_time(self):
#         print(time.ctime())
# class fitness_trak:
#     def count_step(self):
#         print('it shows number of steps walked')
# class smartwatch(watch,fitness_trak):
#     def check_bp(self):
#         print('it check the human blood pressure')
# w1=smartwatch()
# w1.count_step()
# w1.check_bp()
# w1.curr_time()




# write a program in multilevel with features of car class and aeroplane class and inherit them with another class
# class car:
#     def drive_on_roads(self):
#         print('we can drive cars only on roads')

# class aeroplane:
#     def fly(self):
#         print('aeroplanes are fly on sky')

# class flyingcars(car,aeroplane):

#     def tesla(self):
#         print('tesla company cars are can drive on roads and fly on sky')

# c1=flyingcars()
# c1.fly()
# c1.tesla()




# write a program with class music player with some methods and add some songs to that method and access them
# class musicplayer:
#     def __init__(self):
#         self.songs=[]

#     def add_sond(self,songname):
#         self.songs+=[songname]
#         print(f'{songname } is added to playlist')

#     def playmusic(self):
#         if self.songs:
#             print(f'playing{self.songs[0]}')
#         else:
#             print('music list is empty')

# m1=musicplayer()
# m1.add_sond('kanulunavina.mp3')
# m1.playmusic()



#write a program for multilevel inheritence with classes of person,employee,manager and inherit them

class person:
    def __init__(self, name):
        self.name = name
class employee(person):
    def __init__(self, name, empid, role, salary):
        super().__init__(name)
        self.empid = empid
        self.role = role
        self.salary = salary
    def annualincome(self):
        return self.salary * 12
class manager(employee):
    def __init__(self, name, empid, role, salary, bonus):
        super().__init__(name, empid, role, salary)
        self.bonus = bonus
    def pay(self):
        return self.salary + self.bonus
m1 = manager('chandu', '228A1A0563', 'manager', 1200000, 600000)
print("Name:", m1.name)
print("Employee ID:", m1.empid)
print("Role:", m1.role)
print("Annual Income:", m1.annualincome())
print("Manager Salary with Bonus:", m1.pay())
print(m1.pay())


















 

























