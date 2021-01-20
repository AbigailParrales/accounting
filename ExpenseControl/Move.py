import datetime
class Move():
    def __init__(self, amount, account, description, dateStr=None):
        "Date format   YYYY-MM-DD"
        self.amount = amount
        self.account = account
        self.description = description
        if dateStr:
            dateHolder = dateStr.split("-")
            nYear = int(dateHolder[0])
            nMonth = int(dateHolder[1])
            nDay = int(dateHolder[2])
            self.date = datetime.date(nYear, nMonth, nDay)
        else:
            self.date = datetime.date.today()

    def record(self):
        pass