from Move import Move
class Expense(Move):
    def __init__(self, amount, account, description, date, destiny):
        Move.__init__(self, amount, account, description, date)
        self.destiny = destiny

    def __str__(self):
        return f"Expense: \nDescription: {self.description}\nAccount: {self.account}\nAmount: $ {self.amount}\nTo: {self.destiny}"