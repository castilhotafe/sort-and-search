class BankAccount:
    def __init__(self, balance, accounts=None): # __init__ method allows building instances of a class
        # by receiving its parameters
        self.balance = balance
        self.accounts = accounts if accounts is not None else []

    #def __len__(self):
        #return len(self.accounts) #Here you pass to the function an iterable attribute of the class

    #def __gt__(self, other):
        #self.balance > other.balance #here you pass the function what attributes to compare within the class


account1 = BankAccount(1000)
account2 = BankAccount(1500)
accounts_list = BankAccount(0, [account1, account2])

print(len(accounts_list)) #wrong unless you have a __len__() function
print(account1 > account2) #This is wrong unless yhou you have the __gt__ method implemented