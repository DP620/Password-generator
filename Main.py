import Functions as func
import os
import tkinter as tk

filename = "output.txt"

root = tk.Tk()
root.title("Button example")
root.geometry("300x150")

button_del = tk.Button(
    root,
    text="Click me to delete output file",
    command=lambda: func.deleteFile(filename),
)
button_del.pack(pady=10)

button_generate = tk.Button(
    root,
    text="Click me to generate a password",
    command=lambda: func.passwordGenerator(),
)
button_generate.pack(pady=10)

button_close = tk.Button(
    root,
    text="Click me to close the window",
    command=lambda: root.destroy(),
)
button_close.pack(pady=10)

root.mainloop()

if os.path.exists(filename):
    with open(filename, "r", encoding="utf-8") as file:
        list = file.read().splitlines()
    for i in list:
        print(i)
else:
    print(f"{filename} does not exist.")
