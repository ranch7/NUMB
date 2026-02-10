import tkinter as tk
from tkinter import messagebox
import math

def on_click(text):
    current = entry.get()
    
    if text == "=":
        try:
            # Логика процентов: заменяем "число1 - число2 %" на "число1 - (число1 * число2 / 100)"
            # Для упрощения: заменяем символ '%' на '/100' при вычислении
            expr = current.replace('^', '**').replace('√', 'math.sqrt').replace('π', str(math.pi))
            if '%' in expr:
                # Пример: 200 - 10% -> 200 - (200 * 0.10)
                # Упрощенная реализация через eval, если % стоит в конце выражения
                parts = expr.split()
                # Здесь можно добавить сложную логику, но для базы просто заменим % на /100
                expr = expr.replace('%', '/100')
            
            result = eval(expr, {"math": math})
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception:
            messagebox.showerror("Ошибка", "Некорректное выражение")
            
    elif text == "C":
        entry.delete(0, tk.END)
    elif text == "DEL":
        entry.delete(len(current)-1, tk.END)
    elif text == "n!":
        try:
            res = math.factorial(int(float(current)))
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(res))
        except: messagebox.showerror("Ошибка", "Только целые числа")
    else:
        entry.insert(tk.END, text)

root = tk.Tk()
root.title("Pro Calculator 3.13")
root.geometry("360x500")
root.configure(bg="#2c3e50")

entry = tk.Entry(root, font=("Consolas", 28), bg="#ecf0f1", fg="#2c3e50", borderwidth=0, justify="right")
entry.pack(fill="both", padx=15, pady=25)

buttons_frame = tk.Frame(root, bg="#2c3e50")
buttons_frame.pack()

# Сетка кнопок: добавили проценты, степени и константы
buttons = [
    ('C', '#e74c3c'), ('DEL', '#e67e22'), ('^', '#34495e'), ('/', '#34495e'),
    ('7', '#95a5a6'), ('8', '#95a5a6'), ('9', '#95a5a6'), ('*', '#34495e'),
    ('4', '#95a5a6'), ('5', '#95a5a6'), ('6', '#95a5a6'), ('-', '#34495e'),
    ('1', '#95a5a6'), ('2', '#95a5a6'), ('3', '#95a5a6'), ('+', '#34495e'),
    ('√', '#34495e'), ('0', '#95a5a6'), ('.', '#95a5a6'), ('=', '#2ecc71'),
    ('%', '#34495e'), ('π', '#34495e'), ('n!', '#34495e'), ('(', '#34495e')
]

r, c = 0, 0
for btn_text, color in buttons:
    cmd = lambda x=btn_text: on_click(x)
    tk.Button(buttons_frame, text=btn_text, width=6, height=2, font=("Arial", 12, "bold"),
              bg=color, fg="white", relief="flat", command=cmd).grid(row=r, column=c, padx=3, pady=3)
    c += 1
    if c > 3:
        c = 0
        r += 1

root.mainloop()
