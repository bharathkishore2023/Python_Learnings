from datetime import datetime
class Expense:
    def __init__(self,amount,category,description,date=None):
        self.amount=amount
        self.category=category
        self.description=description
        self.date= date if date else datetime.today()
    def __str__(self):
        return f"amount:{self.amount},category:{self.category,},description:{self.description}" 
