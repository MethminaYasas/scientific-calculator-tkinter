import tkinter as tk
from tkinter import messagebox
import math

class ScientificCalculator:
    def __init__(self, master):
        self.master = master
        master.title("Scientific Calculator")
        master.geometry("400x600")
        master.config(bg="black")
        self.expression = ""
        self.input_text = tk.StringVar()
        self.last_answer = "0"
        self.normal_mode = False  # Start in scientific mode

        # Display
        self.input_field = tk.Entry(
            master, font=('arial', 24, 'bold'),
            textvariable=self.input_text,
            bg="black", fg="white", bd=0,
            justify=tk.RIGHT
        )
        self.input_field.pack(fill="both", ipadx=8, ipady=25, pady=(10, 0))

        # Button Frame
        self.buttons_frame = tk.Frame(master, bg="black")
        self.buttons_frame.pack(expand=True)

        # Start with scientific buttons
        self.create_scientific_buttons()

    # ---------------- BUTTON CREATION ---------------- #
    def create_scientific_buttons(self):
        self.normal_mode = False
        for widget in self.buttons_frame.winfo_children():
            widget.destroy()

        buttons = [
            ["2nd", "deg", "sin", "cos", "tan"],
            ["x²", "lg", "ln", "(", ")"],
            ["√x", "AC", "⌫", "%", "÷"],
            ["x!", "7", "8", "9", "×"],
            ["1/x", "4", "5", "6", "-"],
            ["π", "1", "2", "3", "+"],
            ["⟲", "e", "0", ".", "="]   # Ans → ⟲
        ]

        for i, row in enumerate(buttons):
            for j, btn_text in enumerate(row):
                self.create_button(btn_text, i, j)

    def create_normal_buttons(self):
        self.normal_mode = True
        for widget in self.buttons_frame.winfo_children():
            widget.destroy()

        buttons = [
            ["AC", "⌫", "(", ")", "÷"],
            ["7", "8", "9", "×"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["0", ".", "=", "🔬"]  # Added Sci toggle
        ]

        for i, row in enumerate(buttons):
            for j, btn_text in enumerate(row):
                self.create_button(btn_text, i, j)

    def create_button(self, text, row, col):
        # Colors
        if text in ["=", "+", "-", "×", "÷"]:
            bg, fg = "#ff9500", "white"  # Orange buttons
        elif text in ["AC", "⌫"]:
            bg, fg = "#333333", "#ff3b30"  # Dark + red
        else:
            bg, fg = "#333333", "white"  # Normal dark

        button = tk.Button(
            self.buttons_frame, text=text,
            font=('arial', 16, 'bold'),
            fg=fg, bg=bg, bd=0,
            activebackground="#666666",
            activeforeground="white",
            width=5, height=2,
            command=lambda: self.on_button_click(text)
        )
        button.grid(row=row, column=col, padx=4, pady=4, sticky="nsew")

        # Make grid expand evenly
        self.buttons_frame.grid_rowconfigure(row, weight=1)
        self.buttons_frame.grid_columnconfigure(col, weight=1)

    # ---------------- LOGIC ---------------- #
    def on_button_click(self, char):
        if char == "=":
            try:
                result = eval(self.expression.replace("×", "*").replace("÷", "/"))
                self.input_text.set(result)
                self.expression = str(result)
                self.last_answer = str(result)
            except:
                messagebox.showerror("Error", "Invalid Input")
                self.expression = ""
                self.input_text.set("")

        elif char == "AC":
            self.expression = ""
            self.input_text.set("")

        elif char == "⌫":
            self.expression = self.expression[:-1]
            self.input_text.set(self.expression)

        elif char == "π" and not self.normal_mode:
            self.expression += str(math.pi)
            self.input_text.set(self.expression)

        elif char == "e" and not self.normal_mode:
            self.expression += str(math.e)
            self.input_text.set(self.expression)

        elif char == "x²" and not self.normal_mode:
            self.expression += "**2"
            self.input_text.set(self.expression)

        elif char == "√x" and not self.normal_mode:
            self.expression += "**0.5"
            self.input_text.set(self.expression)

        elif char == "1/x" and not self.normal_mode:
            self.expression = f"1/({self.expression})"
            self.input_text.set(self.expression)

        elif char == "x!" and not self.normal_mode:
            try:
                self.expression = str(math.factorial(int(self.expression)))
                self.input_text.set(self.expression)
            except:
                messagebox.showerror("Error", "Invalid Factorial")
                self.expression = ""
                self.input_text.set("")

        elif char == "⟲":   # Switch to normal mode
            self.expression += self.last_answer
            self.input_text.set(self.expression)
            self.create_normal_buttons()

        elif char == "🔬":  # Back to scientific mode
            self.create_scientific_buttons()

        else:
            self.expression += str(char)
            self.input_text.set(self.expression)


if __name__ == "__main__":
    root = tk.Tk()
    calc = ScientificCalculator(root)
    root.mainloop()
