from Move import Move
class Income(Move):
    def __init__(self, amount, account, description, date, source):
        Move.__init__(self, amount, account, description, date)
        self.source = source

    def __str__(self):
        return f"INCOME: \nDescription: {self.description}\nAccount: {self.account}\nAmount: $ {self.amount}\nFrom: {self.source}"