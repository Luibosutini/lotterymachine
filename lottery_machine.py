import tkinter as tk
import random

selected_numbers = set ()

def select_random_numbers():
    global selected_numbers
    if len(selected_numbers)< 75:
        new_number = random.randint(1,75)
        while new_number in selected_numbers:
            new_number = random.randint(1,75)
        selected_numbers.add(new_number)
        label.config(text=str(new_number))
        history_label.config(text=sorted(selected_numbers))

root = tk.Tk()
root.title("抽選機")

label = tk.Label(root , text="",font=("Helvetica",48))
label.pack(pady=20)

history_label = tk.Label(root , text="",font=("Helvetica",14))
history_label.pack()

button = tk.Button(root , text="次の数字を選ぶ",command=select_random_numbers)
button.pack(pady=10)

select_random_numbers()
root.mainloop()