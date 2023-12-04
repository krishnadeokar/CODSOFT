import tkinter as tk
from tkinter import ttk, messagebox
import random

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game")

        self.questions = [
            {
                'question': 'What is the capital of Japan?',
                'choices': ['Beijing', 'Seoul', 'Tokyo', 'Bangkok'],
                'correct_answer': 'Tokyo'
            },
            {
                'question': 'Which programming language is known as the "language of the web"?',
                'choices': ['Java', 'Python', 'JavaScript', 'C++'],
                'correct_answer': 'JavaScript'
            },
            {
                'question': 'Which planet is known as the "Blue Planet"?',
                'choices': ['Earth', 'Mars', 'Venus', 'Jupiter'],
                'correct_answer': 'Earth'
            },
            {
                'question': 'Who is known as the father of modern physics?',
                'choices': ['Isaac Newton', 'Galileo Galilei', 'Albert Einstein', 'Niels Bohr'],
                'correct_answer': 'Albert Einstein'
            },
            {
                'question': 'Which country is famous for the Great Barrier Reef?',
                'choices': ['Australia', 'Brazil', 'Canada', 'India'],
                'correct_answer': 'Australia'
            },
            {
                'question': 'What is the largest mammal in the world?',
                'choices': ['Elephant', 'Blue Whale', 'Giraffe', 'Hippopotamus'],
                'correct_answer': 'Blue Whale'
            },
            {
                'question': 'Which element has the chemical symbol "O"?',
                'choices': ['Osmium', 'Oxygen', 'Oganesson', 'Oxygenium'],
                'correct_answer': 'Oxygen'
            },
            {
                'question': 'Who wrote "Romeo and Juliet"?',
                'choices': ['William Shakespeare', 'Jane Austen', 'Charles Dickens', 'Homer'],
                'correct_answer': 'William Shakespeare'
            },
            {
                'question': 'In which year did the Titanic sink?',
                'choices': ['1905', '1912', '1920', '1931'],
                'correct_answer': '1912'
            },
            {
                'question': 'What is the currency of Brazil?',
                'choices': ['Peso', 'Yen', 'Real', 'Dollar'],
                'correct_answer': 'Real'
            }
        ]

        self.current_question_index = 0
        self.score = 0

        # Apply themed style
        style = ttk.Style()
        style.theme_use("clam")  # You can experiment with different themes
        style.configure("TLabel", font=("Arial", 14), foreground="blue")
        style.configure("TButton", font=("Arial", 12), foreground="white", background="purple")
        style.configure("TFrame", background="lightblue")

        # Create main frame
        main_frame = ttk.Frame(root, style="TFrame")
        main_frame.pack(padx=20, pady=20)

        # Create widgets
        self.question_label = ttk.Label(main_frame, text="", style="TLabel")
        self.question_label.grid(row=0, column=0, columnspan=2, pady=10)

        self.choice_buttons = []
        for i in range(4):
            button = ttk.Button(main_frame, text="", command=lambda i=i: self.check_answer(i), style="TButton", width=20)
            self.choice_buttons.append(button)
            button.grid(row=i+1, column=0, pady=5)

        self.next_button = ttk.Button(main_frame, text="Next Question", command=self.next_question, style="TButton")
        self.next_button.grid(row=5, column=0, columnspan=2, pady=10)

        # Load the first question
        self.load_question()

    def load_question(self):
        question_data = self.questions[self.current_question_index]
        self.question_label.config(text=question_data['question'])
        random.shuffle(question_data['choices'])
        for i in range(4):
            self.choice_buttons[i].config(text=question_data['choices'][i])

    def check_answer(self, choice_index):
        question_data = self.questions[self.current_question_index]
        user_answer = question_data['choices'][choice_index]
        correct_answer = question_data['correct_answer']

        if user_answer == correct_answer:
            self.score += 1
            messagebox.showinfo("Correct!", "Your answer is correct.")
        else:
            messagebox.showerror("Incorrect", f"Sorry, the correct answer is {correct_answer}.")

        self.next_question()

    def next_question(self):
        self.current_question_index += 1

        if self.current_question_index < len(self.questions):
            self.load_question()
        else:
            self.show_final_results()

    def show_final_results(self):
        final_result_window = tk.Toplevel(self.root)
        final_result_window.title("Final Results")

        final_label = ttk.Label(final_result_window, text=f"Your final score is {self.score} out of {len(self.questions)}.", font=("Arial", 16))
        final_label.pack(padx=20, pady=20)

        play_again_button = ttk.Button(final_result_window, text="Play Again", command=self.play_again, style="TButton")
        play_again_button.pack(pady=10)

        exit_button = ttk.Button(final_result_window, text="Exit", command=self.exit_game, style="TButton")
        exit_button.pack(pady=10)

    def play_again(self):
        self.current_question_index = 0
        self.score = 0
        self.load_question()

    def exit_game(self):
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
