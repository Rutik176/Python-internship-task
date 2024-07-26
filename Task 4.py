import tkinter as tk
from tkinter import messagebox

class Quiz:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Quiz Application")
        self.window.geometry("400x300")

        self.questions = []
        self.current_question = 0
        self.score = 0

        self.question_label = tk.Label(self.window, text="", wraplength=400)
        self.question_label.pack()

        self.option_buttons = []
        for i in range(4):
            button = tk.Button(self.window, text="", command=lambda i=i: self.check_answer(i))
            button.pack()
            self.option_buttons.append(button)

        self.score_label = tk.Label(self.window, text="Score: 0")
        self.score_label.pack()

        self.add_question_button = tk.Button(self.window, text="Add Question", command=self.add_question)
        self.add_question_button.pack()

        self.next_question_button = tk.Button(self.window, text="Next Question", command=self.next_question)
        self.next_question_button.pack()

        self.load_questions()

    def load_questions(self):
        # Load questions from a file or database
        # For this example, we'll hardcode some questions
        self.questions = [
            {"question": "What is the capital of France?", "options": ["Paris", "London", "Berlin", "Rome"], "answer": 0},
            {"question": "What is the largest planet in our solar system?", "options": ["Earth", "Saturn", "Jupiter", "Uranus"], "answer": 2},
            {"question": "What is the smallest country in the world?", "options": ["Vatican City", "Monaco", "Nauru", "Tuvalu"], "answer": 0},
        ]

    def add_question(self):
        # Create a new window to add a question
        add_window = tk.Toplevel(self.window)
        add_window.title("Add Question")

        question_label = tk.Label(add_window, text="Question:")
        question_label.pack()
        question_entry = tk.Entry(add_window, width=40)
        question_entry.pack()

        options_label = tk.Label(add_window, text="Options (comma separated):")
        options_label.pack()
        options_entry = tk.Entry(add_window, width=40)
        options_entry.pack()

        answer_label = tk.Label(add_window, text="Answer (index of correct option):")
        answer_label.pack()
        answer_entry = tk.Entry(add_window, width=40)
        answer_entry.pack()

        def save_question():
            question = question_entry.get()
            options = [option.strip() for option in options_entry.get().split(",")]
            answer = int(answer_entry.get())
            self.questions.append({"question": question, "options": options, "answer": answer})
            add_window.destroy()

        save_button = tk.Button(add_window, text="Save Question", command=save_question)
        save_button.pack()

    def next_question(self):
        if self.current_question < len(self.questions):
            self.display_question()
        else:
            self.display_results()

    def display_question(self):
        question = self.questions[self.current_question]
        self.question_label.config(text=question["question"])
        for i, option in enumerate(question["options"]):
            self.option_buttons[i].config(text=option)

    def check_answer(self, option_index):
        question = self.questions[self.current_question]
        if option_index == question["answer"]:
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")
        self.current_question += 1
        self.next_question()

    def display_results(self):
        messagebox.showinfo("Results", f"Your final score is {self.score} out of {len(self.questions)}")

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    quiz = Quiz()
    quiz.run()