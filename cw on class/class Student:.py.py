class Student:
    # self is not counted as parameter
    def __init__(self, first_name,last_name ,address,year_of_birth): # first function to run when creating a student
        self.first_name = first_name # attributes
        self.last_name = last_name
        self.address = address
        self.full_name = f"{self.first_name} {self.last_name}"
        self.year_of_birth = year_of_birth
        self.age = 2025-self.year_of_birth
        

student_1 = Student("Abraham","Smith","Floreal",2000) # 2
print(f"{student_1.full_name} aged {2025-student_1.year_of_birth} lives at {student_1.address}")

student_2 = Student("Anjelina","Jolie","Curepipe",2002)
print(f"{student_2.full_name} aged {2025-student_2.year_of_birth} lives at {student_2.address}")

student_3 = Student("Junaid","Jahaly","Curepipe",2005)
print(f"{student_3.full_name} aged {2025-student_3.year_of_birth} lives at {student_3.address}")


class Car:
    def __init__(self,make,model,color): # constructor: runs everytime we create a car
        self.make=make
        self.model=model
        self.color=color
        self.fuel_level=50
        self.engine_status="off"
        self.speed=0
    def show_status(self):
         print(f"{self.make} {self.model} is driving at {self.speed} km/h")
    def drive(self,engine_status):
        if self.engine_status == "off":
         print("turn on engine")
        else:
         self.speed=10
         print("car is starting to drive")

    def turn_on(self):
       print



nayar_car = Car("VW","Polo","grey")
abraham_car = Car("BMW","316","red")

nayar_car.show_status()
abraham_car.drive("off")


class BankAccount: # by convention, class names are Capital
    # constructor method
    def __init__(self, customer,acc_number):
        self.balance = 0
        self.customer = customer
        self.acc_number = acc_number # normally autogerated. 

    def deposit(self,amount):
        self.balance = self.balance + amount

    def withdraw(self,amount):
        if(self.balance >=  amount):
            self.balance = self.balance - amount
        else:
            print("Insufficient Balance")

    def show_balance(self):
        print(f"You currently have Rs {self.balance}")

nayar_acc = BankAccount("Nayar Joolfoo","00001")
nayar_acc.show_balance()
# nayar deposits Rs 2000
nayar_acc.deposit(2000)
nayar_acc.deposit(1000)
nayar_acc.show_balance()
nayar_acc.withdraw(500)
nayar_acc.show_balance()
nayar_acc.withdraw(6000)
nayar_acc.show_balance()