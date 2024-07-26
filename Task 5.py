import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd

class ExpenseTracker:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Expense Tracker")
        self.window.geometry("400x400")

        self.expenses = []

        self.date_label = tk.Label(self.window, text="Date:")
        self.date_label.pack()
        self.date_entry = tk.Entry(self.window, width=20)
        self.date_entry.pack()

        self.category_label = tk.Label(self.window, text="Category:")
        self.category_label.pack()
        self.category_entry = tk.Entry(self.window, width=20)
        self.category_entry.pack()

        self.amount_label = tk.Label(self.window, text="Amount:")
        self.amount_label.pack()
        self.amount_entry = tk.Entry(self.window, width=20)
        self.amount_entry.pack()

        self.add_button = tk.Button(self.window, text="Add Expense", command=self.add_expense)
        self.add_button.pack()

        self.view_button = tk.Button(self.window, text="View Expenses", command=self.view_expenses)
        self.view_button.pack()

        self.summary_button = tk.Button(self.window, text="Summary", command=self.summary)
        self.summary_button.pack()

        self.figure = plt.Figure(figsize=(5, 4), dpi=100)
        self.ax = self.figure.add_subplot(111)
        self.chart_type = FigureCanvasTkAgg(self.figure, self.window)
        self.chart_type.get_tk_widget().pack()

    def add_expense(self):
        date = self.date_entry.get()
        category = self.category_entry.get()
        amount = float(self.amount_entry.get())
        self.expenses.append({"date": date, "category": category, "amount": amount})
        self.date_entry.delete(0, tk.END)
        self.category_entry.delete(0, tk.END)
        self.amount_entry.delete(0, tk.END)

    def view_expenses(self):
        expense_list = ""
        for expense in self.expenses:
            expense_list += f"Date: {expense['date']}, Category: {expense['category']}, Amount: {expense['amount']}\n"
        messagebox.showinfo("Expenses", expense_list)

    def summary(self):
        df = pd.DataFrame(self.expenses)
        self.ax.clear()
        df.groupby("category")["amount"].sum().plot(kind="bar", ax=self.ax)
        self.chart_type.draw()

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    tracker = ExpenseTracker()
    tracker.run()