class BankAccount():
    # attributes: customer, balance
    # method: deposit, withdraw, status
    def __init__(self,name):
        self.customer = name
        self.__balance = 0 # protect it

    def status(self):
        print(f"Hello {self.customer}. Your balance is {self.__balance}")
        print(self.__calculate_interest())

    def __deposit(self,amount):
        self.__balance = self.__balance + amount

    def deposit(self,amount):
        if(amount <= 0):
            raise Exception("Deposit should be positive")
        self.__deposit(amount)

    def __calculate_interest(self): # can be called only within the class
        return self.__balance * 0.031

nayar_bank_acc = BankAccount("Nayar")
nayar_bank_acc.deposit(3000) # BankAccount.deposit(3000) -> BankAccount.__deposit(3000)
nayar_bank_acc.status()
nayar_bank_acc.__balance = 5000 # this was unable to change self.__balance
nayar_bank_acc.status()