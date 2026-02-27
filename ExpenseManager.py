from Expense import Expense
class ExpenseManager:
    def __init__(self):
        self.expenses=[]
    def add_expense(self):
        print("Enter the Expense amount")
        Expense_amount=float(input())
        print("Enter the Expense category: e.g. books,food,clothes")
        Expense_category=input()
        print("Enter the Expense Description :")
        Expense_description=input()
        expense = Expense(Expense_amount,Expense_category,Expense_description)
        self.expenses.append(expense)
        print("The expense entered successfully!!!")
        print("=========================================================================")
        
    def viewExpense(self,Expense):
         for index,exp  in enumerate(Expense,start=0):
            serial_no=index+1
            print("Expense ",serial_no,":")
            print("The expense amount is:",exp.amount )
            print("The expense amount is:",exp.category )
            print("The expense amount is:",exp.description )
            print("--------------------------------------------------------------------------")
         print("=========================================================================")
          
    def get_highest_expense(self,Expense):
        max_amt=0
        max_exp=None
        for exp  in Expense:
            if max_amt<exp.amount:
                max_amt=exp.amount
                max_exp=exp
        print("The highest Expense is below:")
        print("The expense amount is:",max_exp.amount )
        print("The expense category is:",max_exp.category )
        print("The expense description is:",max_exp.description )
        print("==========================================================")

    def get_expense_by_category(self,category,Expense):
        results=[]
        tota_exp=0
        for index,exp  in enumerate(Expense,start=0):
            if exp.category==category:
                results.append(exp)
                tota_exp+=exp.amount
        print('''The total Expense by category",category,"is: 
          The Expenses on this category are :
    ''')
        for exp1 in results:
            print("The expense amount is:",exp1.amount )
            print("The expense category is:",exp1.category )
            print("The expense description is:",exp1.description )
            print("--------------------------------------------")
        print("=======================================================================")
