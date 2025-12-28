from expense import Expense
import calendar
import datetime

def main():
    print(f"Running Expense Tracker!")
    expense_file_path = "expenses.csv"
    now = datetime.datetime.now()

    months = {
        1: "janvier",
        2: "février",
        3: "mars",
        4: "avril",
        5: "mai",
        6: "juin",
        7: "juillet",
        8: "août",
        9: "septembre",
        10: "octobre",
        11: "novembre",
        12: "décembre"
    }

    month = now.month
    mois = months[month]
    budget = int(input(f"Quel est votre budget pour le mois de {mois}?"))

    # Get user input for expense
    expense = get_user_expense()

    # Reset the file
    reset_file(expense_file_path)

    # Write their expense to a file
    save_expense(expense, expense_file_path)

    # Read the file and summarise expenses
    summarise_expenses(expense_file_path, budget)

def get_user_expense():
    print(f"Getting User Expense...")
    expense_name = input("Enter expense name:")
    expense_amount = float(input("Enter amount of expense:"))
    print(f"Name: {expense_name}, Amout spent: {expense_amount}")
    
    expense_categories = [
        "🍔 Food",
        "🏚️ Home",
        "💻 Work",
        "🥂 Fun",
        "⭐ Miscellaneous",
    ]

    while True:
        print("Select a category:")
        for i, category_name in enumerate(expense_categories):
            print(f"  {i + 1}. {category_name}")

        value_range = f"[1 - {len(expense_categories)}]"
        selected_index = int(input(f"Enter a category number {value_range}:")) - 1
        
        if selected_index in range(len(expense_categories)):
            selected_category = expense_categories[selected_index]
            new_expense = Expense(name=expense_name, category=selected_category, amount=expense_amount)
            return new_expense
        
        else:
            print("Category not within range. Please try again.")

def reset_file(expense_file_path):
    response =input("Would you like to clear the file before entering your data ? Yes/No: ")
    if response == "No" or response == "no":
        global opening_mode
        opening_mode = "a"
    elif response == "Yes" or response == "yes":
        opening_mode = "w"
    else:
        print("Sorry, you must only answer with 'Yes' or 'No'. Please try again.")
        reset_file(expense_file_path)

def save_expense(expense:Expense, expense_file_path):
    print(f"Saving User Expense: {expense} to {expense_file_path}")
    global opening_mode
    with open(expense_file_path, opening_mode) as f:
        f.write(f"{expense.name},{expense.category},{expense.amount}\n")

def summarise_expenses(expense_file_path, budget):
    print(f"Summarising User Expense...")
    expenses:list[Expense] = []

    with open(expense_file_path, "r") as f:
        lines = f.readlines() # Gives us a list that can be enumerated
        for line in lines:
            stripped_line = line.strip()
            expense_name, expense_category, expense_amount = stripped_line.split(",")
            line_expense = Expense(
                name=expense_name,
                amount=float(expense_amount),
                category=expense_category,
            )
            expenses.append(line_expense)
    
    amount_by_category = {}
    for expense in expenses:
        key = expense.category
        if key in amount_by_category:
            amount_by_category[key] += expense.amount
        else:
            amount_by_category[key] = expense.amount
    
    print("Expenses by category:")
    for key, amount in amount_by_category.items():
        print(f"{key}: {amount:.2f}€")
        
    total_spent = sum([exp.amount for exp in expenses])
    print(f"You've spent {total_spent:.2f}€")

    remaining_budget = budget - total_spent
    print(f"Budget remaining: {remaining_budget:.2f}€")

    # Getting the current date
    now = datetime.datetime.now()

    # Getting the nb of days in the current month
    days_in_month = calendar.monthrange(now.year, now.month)[1]

    # Calculating the remaining number of days in the current month
    remaining_days = days_in_month - now.day

    # Calculating the daily budget
    daily_budget = remaining_budget/remaining_days
    print(f"Budget per day: {daily_budget:.2f}€")
        


if __name__ == "__main__":
    main()