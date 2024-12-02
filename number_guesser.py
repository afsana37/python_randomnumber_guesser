import tkinter as tk
from tkinter import messagebox, font
import random
import time

class NumberGuesser(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Number Guesser Game")
        self.geometry("500x350")  # Increased window size
        self.configure(bg='#a7bed3')  # Pastel blue background for the window

        self.target = random.randint(1, 100)
        self.attempts_left = 10
        self.time_limit = 30  # seconds
        self.start_time = time.time()

        self.create_widgets()
        self.update_timer()

    def create_widgets(self):
        # Check if the desired font is available
        available_font = "Comic Sans MS" if "Comic Sans MS" in font.families() else "Helvetica"

        self.lbl_timer = tk.Label(self, text="", font=(available_font, 16), bg='#b5a7d5', fg='black')
        self.lbl_timer.pack(pady=10)

        self.lbl_attempts = tk.Label(self, text=f"Attempts Left: {self.attempts_left}", font=(available_font, 16), bg='#b5a7d5', fg='black')
        self.lbl_attempts.pack(pady=10)

        self.lbl_result = tk.Label(self, text="Guess a number between 1 and 100", font=(available_font, 20), bg='#ffd1dc', fg='black')
        self.lbl_result.pack(pady=15)

        self.entry_guess = tk.Entry(self, font=(available_font, 18), width=10)
        self.entry_guess.pack(pady=10)

        self.btn_check = tk.Button(self, text="Check", command=self.check_guess, bg='#b4f8c8', fg='black', font=(available_font, 14))
        self.btn_check.pack(pady=10)

        self.btn_reset = tk.Button(self, text="New Game", command=self.new_game, bg='#faf0af', fg='black', font=(available_font, 14))
        self.btn_reset.pack(pady=10)

    def check_guess(self):
        if not self.entry_guess.get().isdigit():
            messagebox.showerror("Error", "Please enter a valid number!")
            return

        guess = int(self.entry_guess.get())
        self.attempts_left -= 1
        self.lbl_attempts.config(text=f"Attempts Left: {self.attempts_left}")

        if guess < self.target:
            self.lbl_result.config(text="Too low, try again!")
        elif guess > self.target:
            self.lbl_result.config(text="Too high, try again!")
        else:
            elapsed_time = time.time() - self.start_time
            self.lbl_result.config(text=f"Congratulations! You guessed the number {self.target} correctly in {10 - self.attempts_left} attempts and {elapsed_time:.2f} seconds.", font=("Helvetica", 24))
            self.btn_check.config(state="disabled")
        
        self.entry_guess.delete(0, tk.END)

        if self.attempts_left == 0:
            self.lbl_result.config(text=f"Game Over! The correct number was {self.target}.", font=("Helvetica", 24))
            self.btn_check.config(state="disabled")
            messagebox.showinfo("Game Over", f"You've run out of attempts! The correct number was {self.target}.")

    def update_timer(self):
        elapsed_time = int(time.time() - self.start_time)
        remaining_time = self.time_limit - elapsed_time
        self.lbl_timer.config(text=f"Time Left: {remaining_time}s")
        if remaining_time > 0:
            self.after(1000, self.update_timer)
        else:
            self.lbl_result.config(text=f"Time's up! The correct number was {self.target}.", font=("Helvetica", 24))
            self.btn_check.config(state="disabled")
            messagebox.showinfo("Game Over", f"Time is up! The correct number was {self.target}.")

    def new_game(self):
        self.target = random.randint(1, 100)
        self.attempts_left = 10
        self.start_time = time.time()
        self.lbl_attempts.config(text=f"Attempts Left: {self.attempts_left}")
        self.lbl_result.config(text="Guess a number between 1 and 100", font=("Helvetica", 20))
        self.btn_check.config(state="normal")
        self.update_timer()

if __name__ == "__main__":
    app = NumberGuesser()
    app.mainloop()
