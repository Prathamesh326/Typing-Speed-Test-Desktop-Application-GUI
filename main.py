import tkinter as tk
from tkinter import messagebox
import time
import random

# Sample Text
sample_texts = [
    "The quick brown fox jumps over the lazy dog.",
    "Typing is a skill that can improve with practice.",
    "Learning to code requires patience and dedication.",
    "Python is an easy-to-learn programming language.",
]


# main app
class TypingSpeedTest:
    def __init__(self, window):
        self.window = window
        self.window.title("Typing Speed Test")
        self.window.geometry("700x500")
        self.window.config(bg="#f0f0f0")

        self.sample_text = random.choice(sample_texts)
        self.start_time = None

        # Title Label
        self.title_label = tk.Label(window, text="Typing Speed Test", font=("Helvetica", 18, "bold"), bg="#f0f0f0",
                                    fg="#4b4b4b")
        self.title_label.pack(pady=20)

        # Instruction Label
        self.text_label = tk.Label(window, text="Type the following text:", font=("Helvetica", 14), bg="#f0f0f0")
        self.text_label.pack(pady=5)

        # Sample Text Display
        self.sample_text_label = tk.Label(window, text=self.sample_text, font=("Helvetica", 12), wraplength=600,
                                          justify="left", bg="#ffffff", relief="solid", bd=1, padx=10, pady=10)
        self.sample_text_label.pack(pady=10)

        # Text Entry box
        self.text_entry = tk.Text(window, height=5, font=("Helvetica", 12), wrap='word', relief="solid", bd=1, padx=10,
                                  pady=10)
        self.text_entry.pack(pady=10)
        self.text_entry.bind("<KeyPress>", self.start_timer)

        # Finish Button
        self.finish_button = tk.Button(window, text="Finish", command=self.calculate_wpm, font=("Helvetica", 12),
                                       bg="#4CAF50", fg="white", relief="flat", padx=10, pady=5)
        self.finish_button.pack(pady=10)

        # Results Label
        self.result_label = tk.Label(window, text="", font=("Helvetica", 14), bg="#f0f0f0", fg="#4b4b4b")
        self.result_label.pack(pady=10)

        # Reset Button
        self.reset_button = tk.Button(window, text="Reset", command=self.reset, font=("Helvetica", 12), bg="#f44336",
                                      fg="white", relief="flat", padx=10, pady=5)
        self.reset_button.pack(pady=10)

    def start_timer(self, event):
        if self.start_time is None:
            self.start_time = time.time()

    def reset(self):
        self.sample_text = random.choice(sample_texts)
        self.sample_text_label.config(text=self.sample_text)
        self.text_entry.delete(1.0, tk.END)
        self.result_label.config(text="")
        self.start_time = None

    def calculate_wpm(self):
        end_time = time.time()
        total_time = end_time - self.start_time

        typed_text = self.text_entry.get(1.0, tk.END).strip()
        typed_word_count = len(typed_text.split())

        # Calculates words per minute (WPM)
        wpm = typed_word_count / (total_time / 60)

        # Validate typed text
        if typed_text == self.sample_text:
            feedback_message = f"Your typing speed is {wpm:.2f} WPM. Well done!"
        else:
            typed_words = typed_text.split()
            sample_words = self.sample_text.split()
            incorrect_count = sum(1 for typed, sample in zip(typed_words, sample_words) if typed != sample)
            feedback_message = f"Your typing speed is {wpm:.2f} WPM. You had {incorrect_count} incorrect word(s)."

        # Display WPM results
        self.result_label.config(text=feedback_message)

        # Show feedback
        if wpm < 40:
            messagebox.showinfo("Result", feedback_message + " Keep practicing!")
        elif 40 <= wpm < 100:
            messagebox.showinfo("Result", feedback_message + " Great job!")
        else:
            messagebox.showinfo("Result", feedback_message + " Amazing!")


if __name__ == "__main__":
    window = tk.Tk()
    app = TypingSpeedTest(window)
    window.mainloop()
