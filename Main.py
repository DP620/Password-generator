import Functions as func
import os

filename = "output.txt"

if not os.path.exists(filename):
    for i in range(25):
        func.passwordGenerator()

with open(filename, "r", encoding="utf-8") as file:
    list = file.read().splitlines()
for i in list:
    print(i)
