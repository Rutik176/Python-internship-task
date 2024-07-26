from tkinter import *

class Calculator(Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.geometry("400x600")
        
        self.expression = ""
        
        # Entry widget to display the expression/result
        self.entry = Entry(self, font=('Arial', 24), bd=10, insertwidth=4, width=14, borderwidth=4)
        self.entry.grid(row=0, column=0, columnspan=4)
        
        # Adding buttons
        buttons = [
            '1', '2', '3', '/', 
            '4', '5', '6', '*', 
            '7', '8', '9', '-', 
            '0', '.', '=', '+'
        ]
        
        row = 1
        col = 0
        for button in buttons:
            if button == '=':
                btn = Button(self, text=button, padx=20, pady=20, font=('Arial', 18), command=self.evaluate)
            else:
                btn = Button(self, text=button, padx=20, pady=20, font=('Arial', 18), command=lambda b=button: self.button_click(b))
            btn.grid(row=row, column=col, sticky="nsew")
            col += 1
            if col > 3:
                col = 0
                row += 1
        
        # Adding Clear button
        clear_btn = Button(self, text='C', padx=20, pady=20, font=('Arial', 18), command=self.clear)
        clear_btn.grid(row=row, column=0, columnspan=4, sticky="nsew")
        
        # Configure row and column weights
        for i in range(5):
            self.grid_rowconfigure(i, weight=1)
            self.grid_columnconfigure(i, weight=1)
    
    def button_click(self, value):
        self.expression += str(value)
        self.entry.delete(0, END)
        self.entry.insert(0, self.expression)
    
    def evaluate(self):
        try:
            result = str(eval(self.expression))
            self.entry.delete(0, END)
            self.entry.insert(0, result)
            self.expression = result
        except Exception as e:
            self.entry.delete(0, END)
            self.entry.insert(0, "Error")
            self.expression = ""
    
    def clear(self):
        self.expression = ""
        self.entry.delete(0, END)

if __name__ == "__main__":
    calculator = Calculator()
    calculator.mainloop()
