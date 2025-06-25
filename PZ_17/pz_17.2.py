# Дано двузначное число. Вывести вначале его левую цифру (десятки),
# а затем — его правую цифру (единицы). Для нахождения десятков использовать операцию
# деления нацело, для нахождения единиц — операцию взятия остатка от деления.

import tkinter as tk

def show_digits():
    try:
        number = int(entry.get())
        if 10 <= number < 100:
            tens = number // 10
            units = number % 10
            entry.delete(0, tk.END)
            entry.insert(tk.END, f"Десятки: {tens}, Единицы: {units}")
        else:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Введите двузначное число!")
    except ValueError:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Введите корректное число!")

def clear_entry():
    entry.delete(0, tk.END)

root = tk.Tk()
root.geometry('300x400')

label = tk.Label(root, text='Введите двузначное число', font=('Arial', 10, 'normal'))
label.pack()
entry = tk.Entry(root, width=30)
entry.pack(pady=5)
button = tk.Button(root, text='Показать результат', font=('Arial', 10, 'normal'), width=25, command=show_digits)
button.pack()
clear_but = tk.Button(root, text='Очистить поле', font=('Arial', 10, 'normal'), width=25, command=clear_entry)
clear_but.pack(pady=5)

root.mainloop()