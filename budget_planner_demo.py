# import necessary libraries 
# GeeksforGeeks. (2025). Python GUI – Tkinter. [online]
# Available at: https://www.geeksforgeeks.org/python-gui-tkinter/ [Accessed 8 Apr. 2025].
import tkinter as tk  # for creating guis
from tkinter import messagebox  # for displaying message boxes
# W3Schools. (2025). Python Pandas Tutorial. [online] 
# Available at: https://www.w3schools.com/python/pandas/default.asp [Accessed 8 Apr. 2025].
import pandas as pd  # for handling the data in csv
import matplotlib.pyplot as plt  # for plotting a graph

# display the welcome window function
def welcome_window_function(): 
    # W3Schools. (2025). Python global Keyword. [online] 
    # Available at: https://www.w3schools.com/python/ref_keyword_global.asp [Accessed 8 Apr. 2025].
    global welcome_window # make the window global for later use
    welcome_window = tk.Tk() # create the window
    welcome_window.title("Personal Budget Planner") # window title
    welcome_window.geometry("400x200") # window size
    
    # add welcome message and buttons for login and registration
    welcome_label = tk.Label(welcome_window, text="Welcome To Personal Budget Planner") # write inside the window
    welcome_label.pack() # place it in an available area
    welcome_label = tk.Label(welcome_window, text="Please Select :") # write inside the window
    welcome_label.pack() # place it in an available area
    
    login_button = tk.Button(welcome_window, text="Login", command=login_window_function) # create login button
    login_button.pack() # place it in an available area
    register_button = tk.Button(welcome_window, text="Register", command=register_window) # create register button
    register_button.pack() # place it in an available area
    welcome_window.mainloop() # start the program with the welcome window

# display the registration window function
def register_window():  
    global register_window  # make the window global for later use
    register_window = tk.Tk() # create the window
    register_window.title("Registration") # window title
    register_window.geometry("500x200") # window size
    
    registration_msg = tk.Label(register_window, text="Welcome to Personal Budget Planner \n" 
                                "Please Continue Registration Down Below !") # write inside the window
    registration_msg.pack() # place it in an available area
    
    username_label = tk.Label(register_window, text="Username")  # write inside the window
    username_label.pack() # place it in an available area
    username_entry = tk.Entry(register_window) # get user entry
    username_entry.pack() # place it in an available area
    
    password_label = tk.Label(register_window, text="Password")  # write inside the window
    password_label.pack() # place it in an available area
    password_entry = tk.Entry(register_window) # get user entry
    password_entry.pack() # place it in an available area
    
    register_button = tk.Button(register_window, text="Register", command=lambda :registration(username_entry, password_entry)) # create button
    register_button.pack() # place it in an available area

# function for user registration
def registration(username_entry, password_entry):
    username = username_entry.get().strip() # get username
    password = password_entry.get().strip() # get password
    
    # handle errors
    if not username or not password:
        messagebox.showerror("Error !", "Username and password cannot be empty !") # show error
        return 
    
    user_data = pd.read_csv("budget.csv") # read data from the csv file
    
    if username in user_data["Username"].values: # check if the username already exists
        messagebox.showerror("Error ! ", "Username is already taken !") # show error
        return
    else:
        # add new user data 
        new_user = pd.DataFrame({
            "Username": [username],
            "Password": [password],
            "Income": [0],
            "Savings Goal": [0],
            "Savings Amount": [0],
            "Food": [0],
            "Transport": [0],
            "Entertainment": [0],
            "Utilities": [0],
            "Other": [0]
        })
        user_data = pd.concat([user_data, new_user], ignore_index=True) # add new user's data to the existing user data
        user_data.to_csv("budget.csv", index=False) # save the data to the csv file
        messagebox.showinfo("Registration", "Registration successful !") # show error
        register_window.destroy() # destroy the window
        welcome_window.destroy() # destroy the window
        account_choice(username, password) # show the account choice
        
# display the login window function
def login_window_function():
    global login_window  # make the window global for later use
    login_window = tk.Tk() # create the window
    login_window.title("Login") # window title
    login_window.geometry("500x200") # window size
    
    login_msg = tk.Label(login_window, text="Welcome Back to Personal Budget Planner \n"
                                "Please Login Down Below !")  # write inside the window
    login_msg.pack() # place it in an available area
    
    username_label = tk.Label(login_window, text="Username")  # write inside the window
    username_label.pack() # place it in an available area
    username = tk.Entry(login_window) # get user entry
    username.pack() # place it in an available area
    
    password_label= tk.Label(login_window, text="Password")  # write inside the window
    password_label.pack() # place it in an available area
    password = tk.Entry(login_window, show="*") # get user entry
    password.pack() # place it in an available area
    
    # button to trigger the login process
    login_button = tk.Button(login_window, text="Login", command=lambda: control_login(username.get(), password.get(), login_window)) # create button
    login_button.pack() # place it in an available area

# function to control logins
def control_login(username, password, login_window):
    user_data = pd.read_csv("budget.csv") # read data from file
    
    # check if the username and password matches
    if (username in user_data["Username"].values) & (password in user_data["Password"].values): # check is the username and password are in the file
        messagebox.showinfo("Login", "Login successful !") # show message
        login_window.destroy() # destroy window
        welcome_window.destroy() # destroy window
        account_choice(username, password) # show the account choice
    else:
        messagebox.showerror("Login", "Login failed please try again !") # show message

# display the income window function
def income_window_function(username):
    global income_window # make the window global for later use
    income_window = tk.Tk() #create window
    income_window.title("Add Income") # window title
    income_window.geometry("300x200") # window size

    income_label = tk.Label(income_window, text="Please enter your income : ")  # write inside the window
    income_label.pack() # place it in an available area
    
    income_amount_entry = tk.Entry(income_window) # get user input
    income_amount_entry.pack() # place it in an available area

    income_button = tk.Button(income_window, text="Add", command=lambda: add_income(income_amount_entry, username)) # create button
    income_button.pack() # place it in an available area

# function to add incomes
def add_income(income_amount_entry, username):
    income_amount = income_amount_entry.get() # get income amount
    
    if not income_amount.isdigit(): # check if the amount is valif
        messagebox.showerror("Error ! ", "Please enter a valid value ! ") # show message
        return
    
    income_amount = float(income_amount) # make the amount into a float
    income_data = pd.read_csv("budget.csv") # read data from file
    
    user_index = income_data[income_data["Username"] == username].index[0] # find the users index
    income_data.at[user_index, "Income"] += income_amount # add the amount the users existing amount
    
    if pd.isna(income_data.at[user_index, "Transaction History"]): # check if the transaction history is empty
        income_data.at[user_index, "Transaction History"] = "" # turn it into an empty string if its empty

    transaction_history = income_data.at[user_index, "Transaction History"] # get users transaction history
    counter = len(transaction_history.split(',')) if transaction_history else 0 # count the number of transactions
    transaction = f"{counter + 1}. Income: {income_amount:.2f}" # writing format of the income
    income_data.at[user_index, "Transaction History"] += f",{transaction}" if transaction_history else transaction # add income to transaction history
    
    income_data.to_csv("budget.csv", index=False) # save the data to the file
    messagebox.showinfo("Add Income", "Income added successfully !") # show message
    income_window.destroy() # destroy window

# display the add expenses window function
def expenses_window_function(username):
    global expenses_window # make the window global for later use
    expenses_window = tk.Tk() # create window
    expenses_window.title("Add Expenses") # window title
    expenses_window.geometry("300x200")  # window size
    
    expense_amount = tk.Label(expenses_window, text="Please enter your expense : ") # write inside the window
    expense_amount.pack() # place it in an available area
    expense_amount_entry = tk.Entry(expenses_window) # get user input
    expense_amount_entry.pack() # place it in an available area
    
    categories = ["Food", "Transport", "Entertainment", "Utilities", "Other"] # assign categories
    selected_category = tk.StringVar(expenses_window)  # store selected category
    selected_category.set(categories[0]) # set the default selected category with the first item
    
    expense_category_menu = tk.OptionMenu(expenses_window, selected_category, *categories) # create an options menu for categories
    expense_category_menu.pack() # place it in an available area
   
    expense_button = tk.Button(expenses_window, text="Add", command=lambda: add_expenses(username,expense_amount_entry, selected_category.get())) # create button
    expense_button.pack() # place it in an available area

#function to add expenses    
def add_expenses(username, expense_amount_entry, expense_category):
    
    expense_amount = expense_amount_entry.get() # get expense amount
    
    if not expense_amount.isdigit(): # check if the amount is valid
        messagebox.showerror("Error !", "Please enter a valid number !") # show message
        return
    
    expense_amount = float(expense_amount) # make the input a float
    expense_data = pd.read_csv("budget.csv") # get dat from the file
    
    user_index = expense_data[expense_data["Username"] == username].index[0] # find user index
    expense_data.at[user_index, expense_category] += expense_amount # add expense to the category
    
    if pd.isna(expense_data.at[user_index, "Transaction History"]): # check if the transaction history is empty
        expense_data.at[user_index, "Transaction History"] = "" # make it an empty string if its empty
    
    transaction_history = expense_data.at[user_index, "Transaction History"] # get users transaction histroy
    counter = len(transaction_history.split(',')) if transaction_history else 0 # count the transactions
    transaction = f"{counter + 1}. Expense ({expense_category}): {expense_amount:.2f}" # writting format for adding expenses as transactions
    expense_data.at[user_index, "Transaction History"] += f",{transaction}" if transaction_history else transaction # add the new transaction
    
    expense_data.to_csv("budget.csv", index=False) # save data to the file
    expenses_window.destroy() # destroy window
    messagebox.showinfo("Expenses", "Expense added successfully") # shoe message

# function to view expenses
def view_expenses(username):

    expenses_data = pd.read_csv("budget.csv") # get data from the file
    
    user_index = expenses_data[expenses_data["Username"] == username].index[0] # get user index
        
    expenses_categories = ["Food", "Transport", "Entertainment", "Utilities", "Other"]  # define categories
    expenses = expenses_data.loc[user_index, expenses_categories]  # get the user's expenses 
        
    expenses = expenses[expenses > 0] # filter the expenses with no amount in it
        
    if expenses.empty: # check if there are no expenses
        messagebox.showinfo("No Expenses ! ", "No expenses recorded yet ! ") # show meesage
        return
    
    # W3Schools. (2025). Matplotlib Pie Charts. [online] 
    # Available at: https://www.w3schools.com/python/matplotlib_pie_charts.asp [Accessed 8 Apr. 2025].   
    plt.figure(figsize=(6, 6)) # create a pie chart
    plt.pie(
        expenses, # data of the pie chart
        labels=expenses.index, # labels for the pie chart
        autopct='%1.1f%%', # format of the percentage
        startangle=0, # starting angle 
        colors=plt.cm.Paired.colors # use a predefined colour palette
        )
    plt.title("Expense Distribution") # the title
    plt.show() # display the chart

# display the balance function         
def balance_window_function(username):
    balance_window = tk.Tk() # create window
    balance_window.title("View Balance") # window title
    balance_window.geometry("300x200") # window size
    
    balance_data = pd.read_csv("budget.csv") # get data from the file

    user_index = balance_data[balance_data["Username"] == username].index[0] # find users index
        
    expense_categories = ["Food", "Transport", "Entertainment", "Utilities", "Other"] # define the expenses
    total_expenses = balance_data.loc[user_index, expense_categories].fillna(0).sum() # calcluate total expense
        
    total_income = balance_data.at[user_index, "Income"] if "Income" in balance_data.columns else 0 # get users total income
        
    balance = total_income - total_expenses # calcluate users balance
        
    if balance < 0: # if balance is lees than zero
        balance_label = tk.Label(balance_window, text=f"Your current balance is: {balance:.2f}. You are in debt !") # print message
    elif balance == 0: # if balance is zero
        balance_label = tk.Label(balance_window, text=f"Your current balance is: {balance:.2f}.")  # print message
    else:
        balance_label = tk.Label(balance_window, text=f"Your current balance is: {balance:.2f}") # print message
    balance_label.pack() # place it in an available area
        
    balance_button = tk.Button(balance_window, text="OK", command=balance_window.destroy) # create button
    balance_button.pack() # place it in an available area
    
    balance_window.mainloop() # start the program with the welcome window
 
# get savings goal function       
def savings_goal_window_function(username):
    global savings_window # make window global for later use
    savings_window = tk.Tk() # create window
    savings_window.title("Savings") # window title
    savings_window.geometry("300x200") # window size
     
    savings_goal_label = tk.Label(savings_window, text="Please enter your savings goal :") # write inside the window
    savings_goal_label.pack() # place it in an available area
        
    savings_goal_entry = tk.Entry(savings_window) # get user entry
    savings_goal_entry.pack() # place it in an available area
        
    savings_goal_button = tk.Button(savings_window, text="Set", command=lambda: add_savings(savings_goal_entry, username)) # create button
    savings_goal_button.pack() # place it in an available area

# function to add savings goal   
def add_savings(savings_goal_entry, username):
    savings_goal = savings_goal_entry.get() # get information

    if not savings_goal.isdigit(): # check if the input is valid
        messagebox.showerror("Error !", "Please enter a valid value !") # show message
        return
    
    savings_goal = float(savings_goal) # make the input a float
    savings_data = pd.read_csv("budget.csv") # get data from the file
    
    user_index = savings_data[savings_data["Username"] == username].index[0] # find user index
    savings_data.at[user_index, "Savings Goal"] = savings_goal # add the savings goal to the users data
    
    savings_data.to_csv("budget.csv", index=False) # save data to the file
    savings_window.destroy() # destroy window
    messagebox.showinfo("Savings", "Savings goal added successfully !") # show message

# display the savings account window function   
def savings_account_window_function(username):
    global savings_account_window # make window global for later use
    savings_account_window = tk.Tk() # create window
    savings_account_window.title("Add Savings ") # window title
    savings_account_window.geometry("300x200") # window size
    
    savings_account_data = pd.read_csv("budget.csv") # get data from the file
    savings_account_label = tk.Label(savings_account_window, text="Please enter your savings amount :") # write inside the window
    savings_account_label.pack() # place it in an available area
        
    savings_account_entry = tk.Entry(savings_account_window) # get user entry
    savings_account_entry.pack() # place it in an available area
        
    savings_account_button = tk.Button(savings_account_window, text="OK", command=lambda: add_savings_amount(savings_account_entry, username)) # create button
    savings_account_button.pack() # place it in an available area

# function to add savings amount    
def add_savings_amount(savings_amount_entry, username):
    savings_amount = savings_amount_entry.get() # get user input
    
    if not savings_amount.isdigit(): # check if the input is valid
        messagebox.showerror("Error !", "Please enter a valid value !") # show message
        return
    
    savings_amount = float(savings_amount) # make the input a float
    savings_account_data = pd.read_csv("budget.csv") # get data from the file
    
    user_index = savings_account_data[savings_account_data["Username"] == username].index[0] # find user index
        
    savings_goal = savings_account_data.at[user_index, "Savings Goal"] # get the users savings goal
    if savings_goal == 0: # check if the savings goal is zero
        messagebox.showerror("Error !", "You must set a savings goal before adding money to your savings account !") # show message
        savings_account_window.destroy() # destroy window
        return

        
    current_savings = savings_account_data.at[user_index, "Savings Amount"] # get the users current savings amount
    savings_account_data.at[user_index, "Savings Amount"] = current_savings + savings_amount # add the savings to the current savings 
        
    if savings_account_data.at[user_index, "Savings Amount"] == savings_goal: # check if the savings amount is equal to the savings goal
        message = "Congratulations! You have reached your savings goal." # show message
    elif savings_account_data.at[user_index, "Savings Amount"] < savings_goal: # check if the savings amount is less than the savings goal
        message = f"You are {savings_goal - savings_account_data.at[user_index, 'Savings Amount']:.2f} away from reaching your savings goal." # show message
    else:
        message = (
            f"You have exceeded your savings goal!\n"
            f"Your Savings Goal: {savings_goal:.2f}\n"
            f"Your Savings Amount: {savings_account_data.at[user_index, 'Savings Amount']:.2f}\n"
            f"Excess: {savings_account_data.at[user_index, 'Savings Amount'] - savings_goal:.2f}"
            ) # show message
        
    messagebox.showinfo("Savings", message) # show message
    
    savings_account_data.to_csv("budget.csv", index=False) # save data to the file
    savings_account_window.destroy() # destroy window

# display the account choice window function
def account_choice(username, password):
    account_window = tk.Tk() # create window
    account_window.title("Account") # window title
    account_window.geometry("300x200") # window size
    
    normal_account = tk.Button(account_window, text="Debit Account", command=lambda: main_menu(username , password)) # create button
    normal_account.pack() # place it in an available area
    
    savings_account = tk.Button(account_window, text = "Savings Account", command =lambda : savings_acc_menu(username)) # create button
    savings_account.pack() # place it in an available area
    
    exit_button = tk.Button(account_window, text="Exit", command=account_window.destroy) # create button
    exit_button.pack() # place it in an available area

# display the savings account menu function
def savings_acc_menu(username):
    global savings_acc_window # make window global for later use
    savings_acc_window = tk.Tk() # create window
    savings_acc_window.title("Savings Account") # window title
    savings_acc_window.geometry("300x200") # window size
    savings_goal_button = tk.Button(savings_acc_window, text="Set Savings Goal", command=lambda: savings_goal_window_function(username)) # create button
    savings_goal_button.pack() # place it in an available area
    
    savings_account_button = tk.Button(savings_acc_window, text="Add Savings Amount", command=lambda: savings_account_window_function(username)) # create button
    savings_account_button.pack() # place it in an available area
    
    exit_button = tk.Button(savings_acc_window, text="Exit", command=savings_acc_window.destroy) # create button
    exit_button.pack() # place it in an available area

# display the main menu function
def main_menu(username, password):
    menu_window = tk.Tk() # create window
    menu_window.title("Debit Account") # window title
    menu_window.geometry("300x200") # window size
    
    # W3Schools. (2025). Python Lambda. [online] 
    # Available at: https://www.w3schools.com/python/python_lambda.asp [Accessed 8 Apr. 2025].
    income_button = tk.Button(menu_window, text="Add Income", command=lambda: income_window_function(username)) # create button
    income_button.pack() # place it in an available area
    
    expenses_button = tk.Button(menu_window, text="Add Expense", command=lambda: expenses_window_function(username)) # create button
    expenses_button.pack() # place it in an available area
    
    view_expenses_button = tk.Button(menu_window, text="View Expenses", command=lambda:view_expenses(username)) # create button
    view_expenses_button.pack() # place it in an available area
    
    balance_button = tk.Button(menu_window, text="View Balance", command=lambda: balance_window_function(username)) # create button
    balance_button.pack() # place it in an available area
    
    transaction_button = tk.Button(menu_window, text="Transaction History", command=lambda: view_transaction_history(username)) # create button
    transaction_button.pack() # place it in an available area
    
    exit_button = tk.Button(menu_window, text="Exit", command=menu_window.destroy) # create button
    exit_button.pack() # place it in an available area
    
    menu_window.mainloop() # start the program with the welcome window

# display the transaction history function    
def view_transaction_history(username):
    transaction_window = tk.Tk()  # Create window
    transaction_window.title("Transaction History")  # Window title
    transaction_window.geometry("400x300")  # Window size

    transaction_data = pd.read_csv("budget.csv")  # Get data from the file
    user_index = transaction_data[transaction_data["Username"] == username].index[0]  # Find user index

    transaction_history = transaction_data.at[user_index, "Transaction History"]  # Get the transaction history

    if pd.isna(transaction_history) or not transaction_history.strip():  # Check if the transaction history is empty
        transaction_label = tk.Label(transaction_window, text="No transactions recorded yet.")  # Show message
        transaction_label.pack()  # place it in an available area
    else:
        sorted_history = transaction_history.replace(',', '\n')  # Format the transaction history
        transaction_label = tk.Label(transaction_window, text=sorted_history, justify="left", anchor="w")  # Show formatted history
        transaction_label.pack()  # place it in an available area

    close_button = tk.Button(transaction_window, text="Exit", command=transaction_window.destroy)  # Create close button
    close_button.pack()  # place it in an available area
    
welcome_window_function() # start the program with the welcome window
