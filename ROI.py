
class roi():

    def __init__(self):
        pass

    def income(self):
        self.total_income = []
        
        rental_income  = input("Enter the amount received from rental income: " )
        self.total_income.append(float(rental_income))
        
        laundry = input("Enter the amount received from laundry: ")
        self.total_income.append(float(laundry))
        
        storage = input("Enter the amount received from storage: ")
        self.total_income.append(float(storage))
        
        misc = input("Enter all other amounts of income received from the rental property: ")
        self.total_income.append(float(misc))

    def expense(self):
        self.total_expense = []
        
        tax = input("\nEnter the monthly amount spent on taxes: ")
        self.total_expense.append(float(tax))
        
        insurance = input("Enter the monthly amount spent on insurance for the property: ")
        self.total_expense.append(float(insurance))
        
        utilities =  input("Enter the monthly amount spent on total utilities: ")
        self.total_expense.append(float(utilities))

        hoa = input("Enter the monthly amount spent on HOA fees if applicable: ")
        self.total_expense.append(float(hoa))

        landscape = input("Enter the monthly amount spent on landscaping:  ")
        self.total_expense.append(float(landscape))

        vacancy = input("Enter the amount you will save away each month in case of vacancy: ")
        self.total_expense.append(float(vacancy))

        repair = input("Enter the amount you will save away each month to deal with future repairs: ")
        self.total_expense.append(float(repair))

        capex = input("Enter the amount you will spend monthly on capital expenses: ")
        self.total_expense.append(float(capex))

        management =  input("Enter the monthly amount spent on property management: ")
        self.total_expense.append(float(management))

        mortgage =  input("Enter the monthly mortgage payment: ")
        self.total_expense.append(float(mortgage))
    
    def initial(self):

        self.total_investment = []

        down = input("\nEnter the down payment amount: ")
        self.total_investment.append(float(down))

        closing = input("Enter the total closing costs: ")
        self.total_investment.append(float(closing))

        repair = input("Enter the amount spent on repairs or changes to the home: ")
        self.total_investment.append(float(repair))

        misc2 = input("Enter any other amount spent on the initial investment: ")
        self.total_investment.append(float(misc2))

    def investment_return(self):
        self.calc_income = 0
        for i in self.total_income:
            self.calc_income += i

        self.calc_expense = 0
        for j in self.total_expense:
            self.calc_expense += j

        self.calc_investment = 0
        for x in self.total_investment:
            self.calc_investment += x

        self.flow = (self.calc_income - self.calc_expense) * 12.0

        self.percent = print(f'The total return on investment for this property is {(self.flow/self.calc_investment)*100}%')

example = roi()
example.income()
example.expense()
example.initial()
example.investment_return()


        







        






