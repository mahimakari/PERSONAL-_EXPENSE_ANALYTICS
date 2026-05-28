import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("hostel_life_expense_tracker.csv")

print(df.head())

df.groupby("Expense_Type")["Amount"].sum().plot(kind="bar")

plt.xlabel("Expense Type")
plt.ylabel("Total Amount")
plt.title("Expenses by Category")

plt.show()