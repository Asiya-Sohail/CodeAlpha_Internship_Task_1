import tkinter as tk
from tkinter import messagebox
from string import ascii_lowercase
import random

word = ["admire", "chocolate", "soccer", "guitar", "croissant", "penguin", "koala", "kangaroo", "elephant", 
"giraffe", "iguana", "hamburger", "sandwich",  "ninja", "lollywood", "biryani", "qawwali", "paratha", "cricket", 
"tajmahal", "mehndi", "samosa", "sherwani", 
"rickshaw", "pakistan", "lahore", "karachi", "islamabad", "punjab", "sindh", "balochistan", "khyber", 
"peshawar", "multan", "gilgit", "quetta", "mohenjo", "pakora", "sharbat",  "kashmir", "lahori", "punjabi", 
"sindhi", "balochi", "chitral", "hunza", "karimabad", "rawalpindi", "faisalabad", "hyderabad", "murree", 
"karakoram", "quran", "hijab", "halal", "haram", "sunnah", "hadith", 
"namaz", "zakat", "umrah", "muslim", "ameen", "Saudiarabia", "makkah", "madinah", "fasting", "prayer", "mosque", 
"iqbal", "allama", "poetry", "urdupoetry", "literature", "cricket", "hockey", 
"football", "squash", "badminton", "boxing", "wrestling", "judo"]

class HangmanGUI():

    def __init__(self, master):

        self.master = master
        self.master.title("Hangman")

        self.canvas = tk.Canvas(master, width=300, height=300, bg="#FFD1DC")
        self.canvas.create_line(50, 250, 250, 250, width=4, tags="hangman")
        self.canvas.create_line(200, 250, 200, 100, width=4, tags="hangman")
        self.canvas.create_line(100, 100, 200, 100, width=4, tags="hangman")
        self.canvas.create_line(150, 100, 150, 120, width=4, tags="hangman")
        self.canvas.pack(padx=3, pady=3)

        self.word_label = tk.Label(master, text="", font=('Arial', 16), bg="#FFD1DC") #light pink
        self.word_label.pack(padx=10, pady=10)

        self.letter_entry = tk.Entry(master, width=5, font=('Arial', 14), bg="white")
        self.letter_entry.pack(padx=2, pady=2)

        self.attempts_label = tk.Label(master, text="",font=("Times New Roman", 16), bg="#FFD1DC")
        self.attempts_label.pack(padx=3, pady=3)

        self.guess_button = tk.Button(master, text="Guess", font=("Times New Roman", 14), command=self.guess_letter, bg= "#FFCBA5") #slightly dark peach
        self.guess_button.pack(padx=2, pady=2)

        self.reset_game()

    def reset_game(self):
        self.random_word = random.choice(word)
        self.attempts_remaining = 6
        self.display_hints = [random.randint(0, len(self.random_word)-1) for _ in range(3)]
        self.idxs = [i in self.display_hints for i in range(len(self.random_word))]
        self.remaining_letters = set(ascii_lowercase)
        self.wrong_letters = []
        self.draw_hangman(0)
        self.update_display()

    def get_display_word(self):
        return ''.join([n if self.idxs[i] else "_ " for i, n in enumerate(self.random_word)])

    def update_display(self):
        self.word_label.config(text=self.get_display_word())
        self.attempts_label.config(text= f"Attempts Remaining : {self.attempts_remaining}")

    def draw_hangman(self, step):
        if step == 0:
            self.canvas.delete("hangman")
            self.canvas.create_line(50, 250, 250, 250, width=4, tags="hangman")
            self.canvas.create_line(200, 250, 200, 100, width=4, tags="hangman")
            self.canvas.create_line(100, 100, 200, 100, width=4, tags="hangman")
            self.canvas.create_line(150, 100, 150, 120, width=4, tags="hangman")
        elif step == 1:
            self.canvas.create_oval(125, 125, 175, 175, width=4, tags="hangman")
        elif step == 2:
            self.canvas.create_line(150, 175, 150, 225, width=4, tags="hangman")
        elif step == 3:
            self.canvas.create_line(150, 200, 125, 175, width=4, tags="hangman")
        elif step == 4:
            self.canvas.create_line(150, 200, 175, 175, width=4, tags="hangman")
        elif step == 5:
            self.canvas.create_line(150, 225, 125, 250, width=4, tags="hangman")
        elif step == 6:
            self.canvas.create_line(150, 225, 175, 250, width=4, tags="hangman")

    def guess_letter(self):
        next_letter = self.letter_entry.get().lower()
        self.letter_entry.delete(0, tk.END)

        if len(next_letter) != 1 or next_letter not in ascii_lowercase:
            messagebox.showinfo(title="Error", message= "Please enter a valid letter")
            return

        if next_letter in self.remaining_letters:
            self.remaining_letters.remove(next_letter)
            if next_letter in self.random_word:
                for i, n in enumerate(self.random_word):
                    if n == next_letter:
                        self.idxs[i] = True
            else:
                self.wrong_letters.append(next_letter)
                self.attempts_remaining -= 1
                self.draw_hangman(6 - self.attempts_remaining)

            self.update_display()

            if "_ " not in self.get_display_word():
                messagebox.showinfo(title="Hangman", message="Congratulations! You won")
                if messagebox.askyesno(title="Reset Game", message="Do you want to try again?"):
                    self.reset_game()
                else:
                    self.master.destroy()

            elif self.attempts_remaining == 0:
                messagebox.showinfo(title="Hangman", message="Sorry! You Lost")
                if messagebox.askyesno(title="Reset Game", message="Do you want to try again?"):
                    self.reset_game()
                else:
                    self.master.destroy()

        else:
            messagebox.showinfo(title="Hangman", message=f"You've already guessed {next_letter}.")


def main():
    root = tk.Tk()
    root.configure(bg="#FFD1DC")
    HangmanGUI(root)
    root.mainloop()

if __name__ == '__main__':
    main()