import random
import os
import string

filename = "output.txt"


def deleteFile(file):
    if os.path.exists(file):
        os.remove(file)
        print(f"{file} has been deleted.")
    else:
        print(f"file name '{file}' does not exist.")


def passwordGenerator():
    passphrases = []
    passphrase = ""
    uppercaseAlphabet = list(string.ascii_uppercase)
    lowercaseAlphabet = list(string.ascii_lowercase)
    symbols = list(string.punctuation)
    numbers = list(string.digits)
    options = [uppercaseAlphabet, lowercaseAlphabet, symbols, numbers]

    for i in range(4):
        for i in range(4):
            passphrase += random.choice(random.choice(options))
        passphrases.append(passphrase)
        passphrase = ""

    password = (
        passphrases[0]
        + "-"
        + passphrases[1]
        + "-"
        + passphrases[2]
        + "-"
        + passphrases[3]
    )

    if os.path.exists(filename):
        # print("File found.")
        with open(filename, "a", encoding="utf-8") as file:
            file.write("\n" + password)
    else:
        # print("File not found.")
        with open(filename, "w", encoding="utf-8") as file:
            file.write(password)

    return password


if os.path.exists(filename):
    with open(filename, "r", encoding="utf-8") as file:
        list = file.read().splitlines()
    for i in list:
        print(i)
else:
    for i in range(25):
        passwordGenerator()
