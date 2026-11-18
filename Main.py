import Functions as func
import os
import tkinter as tk

filename = "output.txt"

root = tk.Tk()
root.title("Password Generator")
root.geometry("300x300")
label = tk.Label(root, text="ready!", font=("Arial", 12))
label.pack(pady=20)


button_generate = tk.Button(
    root,
    text="Click me to generate a password",
    command=lambda: func.updateStatus(func.passwordGenerator(), label),
)
button_generate.pack(pady=10)

button_save = tk.Button(
    root,
    text="Click me to save the password",
    command=lambda: func.savePassword(label),
)
button_save.pack(pady=10)

button_del = tk.Button(
    root,
    text="Click me to delete output file",
    command=lambda: (
        func.deleteFile(filename),
        func.updateStatus(f"{filename} has been deleted.", label),
    ),
)
button_del.pack(pady=10)

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
