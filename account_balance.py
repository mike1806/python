class Account():

    def __index__(self, owner, balance=0):

        self.owner = owner
        self.balance = balance

    def deposit(self, dep_amount):

        self.balance = slef.balance + dep_amount
        print (f"added {dep_amount} to the balance")

    def withdraw(self, wd_amount):

        if self.balance >= wd_amount:
            self.balance = self.balance - wd_amount
            print("Withdrawal accept")
        else:
            print("Sorry no funds")

    def __str__(self):
        return f"Owner: {self.owner} \n Balance: {self.balance}"

    a = Account("Mike", 600)

    print(a)