# Personal Budget Planner

A Python desktop application that helps users manage their personal finances.  
The program allows users to track income, expenses, savings goals, and view their financial balance using a graphical user interface.

## Features

- User registration and login system
- Add and track income
- Record expenses with categories
- View expense distribution with a pie chart
- View account balance
- Set and track savings goals
- Transaction history
- Savings account management

## Technologies Used

- Python
- Tkinter (GUI)
- Pandas (data management)
- Matplotlib (data visualisation)

## How the Program Works

The program uses a **CSV file (`budget.csv`)** to store user data.

Each user has the following information stored:

- Username
- Password
- Income
- Savings Goal
- Savings Amount
- Expense categories:
  - Food
  - Transport
  - Entertainment
  - Utilities
  - Other
- Transaction History

Users can register or log in through the interface and manage their financial data.

## How to Run the Program

1. Install Python.
2. Install required libraries:
   pip install pandas matplotlib

3. Run the program:
   python budget_planner.py

The program will open a GUI window where users can register or log in.

## Example Workflow

1. Start the application.
2. Register a new account.
3. Log in to your account.
4. Add income.
5. Add expenses by category.
6. View expense distribution in a pie chart.
7. Set savings goals and track progress.

## Project Structure
project-folder
│
├── budget_planner.py
├── budget.csv
└── README.md


## References

GeeksforGeeks. (2025). *Python GUI – Tkinter*.  
https://www.geeksforgeeks.org/python-gui-tkinter/

W3Schools. (2025). *Python Pandas Tutorial*.  
https://www.w3schools.com/python/pandas/default.asp

W3Schools. (2025). *Matplotlib Pie Charts*.  
https://www.w3schools.com/python/matplotlib_pie_charts.asp

W3Schools. (2025). *Python Lambda*.  
https://www.w3schools.com/python/python_lambda.asp
