from ExpenseManager import ExpenseManager
class Menu:
    
    def __init__(self):
        self.manager= ExpenseManager()
        self.flag=True
    def run(self):
        while(self.flag):
            print('''Enter the choice please :
        1. Add Expense
        2. View Expense
        3. Get highest Expense
        4. Get the category wise expense
        5. Exit
        ''')
          
            choice=int(input())
            if(choice.is_integer):
                if choice==1:
                    self.manager.add_expense()
                if choice==2:
                    self.manager.viewExpense(self.manager.expenses)
                if choice==3:
                    self.manager.get_highest_expense(self.manager.expenses)
                if choice==4:
                    categories=[]
                    print("Enter the category you are like to check expense: ")
                    print(
                        "The available categories are"
                    )
                    for i in self.manager.expenses:
                        categories.append(i.category)
                    print(", ".join(categories))
                    category_need = input()
                    self.manager.get_expense_by_category(category_need,self.manager.expenses)
                if choice==5 :
                    self.flag=False
                    print("the program exit!!!")
            else:
             print("Please enter the valid choice!")
          

          
