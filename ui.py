from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.lab_score = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.lab_score.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, highlightthickness=0, bg="white")
        self.question_text = self.canvas.create_text(150,
                                                     125,
                                                     width=280,
                                                     text="some question",
                                                     fill=THEME_COLOR,
                                                     font=("Arial", 20, "italic"))

        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        file_path_right = PhotoImage(file="images/true.png")
        self.right_bot = Button(image=file_path_right,  highlightthickness=0, command=self.true_pressed)
        self.right_bot.grid(row=2, column=0)

        file_path_false = PhotoImage(file="images/false.png")
        self.false_bot = Button(image=file_path_false,  highlightthickness=0, command=self.false_pressed)
        self.false_bot.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.lab_score.config(text=f" Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)

        else:
            self.canvas.itemconfig(self.question_text, text="you 've reached the end of the quiz.")
            self.right_bot.config(state="disabled")
            self.false_bot.config(state="disabled")
    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)
    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")

        else:
            self.canvas.config(bg="red")

        self.canvas.after(1000, func=self.get_next_question)
