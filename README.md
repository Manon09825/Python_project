# Python_project
## About the project
This is my first Python project outside of university. I'm doing this to practice and get better at Python.

Link to the video that helped me do this project:https://www.youtube.com/watch?v=HTD86h69PtE&list=PLZJBfja3V3Rsbiz84Z63IXnTQZH_Rnfuo&index=13

## Goals of the project
The goal of this project is to create an app that helps the user track their expenses.
Here are the requirements of the app:
- The user will enter their expenses
- The expenses will be saved to a CSV file
- The app will summarise the totals of the expenses
- The app will show the remaining budget

## Summary of the project
The project contains two scripts:
- expense.py
- expense_tracker.ipynb
It also contains a csv file in which the expenses are saved.

### expense.py
This script defines the class Expense, which we will use in our expense_tracker.py script.
It has an init function and a repr function.

### expense_tracker.ipynb
This is the "main" script of the project. I wrote it in a notebook because I feel more comfortable using this format, but I did include a .py file containing the same code in this repository, just in case. This script contains 3 main functions:
- `get_user_expense()`: gets the user's expenses (product, price and category of the product)  using `input`. It sets a list of categories for the user to select from (Food, Home, Work, Fun and Miscellaneous) and it stores the input data into a variable.
- `save_expense`: saves the data (product, price, category) into a csv file.
- `summarise_expenses`: uses the csv file to calculate how much the user spent by category, how much they spent in total and how much they have left in their budget.

## Conclusion
This was quite a rewarding project, since it was fairly easy and it helped me get more familiar with Python. I will likely do more of these, because it was really helpful; although it wasn't exactly challenging (as it was a beginner project), it gave me practice and it allowed me to focus just on Python for a few hours.
I might try a Retrieval Augmented Generation (RAG) project, and some NLP-related projects next!
