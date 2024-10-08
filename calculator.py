import tkinter as tk
from tkinter import ttk
import sys

class Calculator(tk.Tk):
  def __init__(self, icon_path=None):
      super().__init__()

      self.title("Calculator")
      self.resizable(False, False)

      if sys.platform.startswith('win') and icon_path:
          self.iconbitmap(icon_path)

      self.expression = ""
      self.create_widgets()

  def create_widgets(self):
      style = ttk.Style()
      style.theme_use('clam')  
      style.configure("TButton", font=("Helvetica", 14), padding=10)
      style.configure("TEntry", font=("Helvetica", 18))

      self.entry = ttk.Entry(self, justify="right", font=("Helvetica", 18))
      self.entry.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)

      buttons = [
          ('C', 1, 0, self.clear),
          ('%', 1, 1, lambda: self.append('%')),
          ('÷', 1, 2, lambda: self.append('/')),
          ('⌫', 1, 3, self.backspace),
          ('7', 2, 0, lambda: self.append('7')),
          ('8', 2, 1, lambda: self.append('8')),
          ('9', 2, 2, lambda: self.append('9')),
          ('×', 2, 3, lambda: self.append('*')),
          ('4', 3, 0, lambda: self.append('4')),
          ('5', 3, 1, lambda: self.append('5')),
          ('6', 3, 2, lambda: self.append('6')),
          ('-', 3, 3, lambda: self.append('-')),
          ('1', 4, 0, lambda: self.append('1')),
          ('2', 4, 1, lambda: self.append('2')),
          ('3', 4, 2, lambda: self.append('3')),
          ('+', 4, 3, lambda: self.append('+')),
          ('±', 5, 0, self.toggle_negative),
          ('0', 5, 1, lambda: self.append('0')),
          ('.', 5, 2, lambda: self.append('.')),
          ('=', 5, 3, self.calculate),
      ]

      for (text, row, col, command) in buttons:
          button = ttk.Button(self, text=text, command=command)
          button.grid(row=row, column=col, sticky="nsew", padx=2, pady=2)

      for i in range(6):
          self.rowconfigure(i, weight=1)
      for j in range(4):
          self.columnconfigure(j, weight=1)

  def append(self, char):
      self.expression += str(char)
      self.update_entry()

  def clear(self):
      self.expression = ""
      self.update_entry()

  def backspace(self):
      self.expression = self.expression[:-1]
      self.update_entry()

  def toggle_negative(self):
      if self.expression.startswith('-'):
          self.expression = self.expression[1:]
      else:
          self.expression = '-' + self.expression
      self.update_entry()

  def calculate(self):
      try:
          expression = self.expression.replace('÷', '/').replace('×', '*').replace('%', '/100')
          result = eval(expression)
          self.expression = str(result)
      except ZeroDivisionError:
          self.expression = "You cant divide by zero"
      self.update_entry()

  def update_entry(self):
      self.entry.delete(0, tk.END)
      self.entry.insert(tk.END, self.expression)

if __name__ == "__main__":
  ICON_PATH = "icon.ico" 

  app = Calculator(icon_path=ICON_PATH)
  app.mainloop()
