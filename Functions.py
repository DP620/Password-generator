import random
import os
import string

filename = "output.txt"
passwordSaved = ""
lastPasswordSaved = ""


def deleteFile(file):
    if os.path.exists(file):
        os.remove(file)
        print(f"{file} has been deleted.")
    else:
        print(f"file name '{file}' does not exist.")


def updateStatus(message, label):
    label.config(text=message)


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

    global passwordSaved
    passwordSaved = password

    return password


def savePassword(label):
    global lastPasswordSaved

    if passwordSaved == lastPasswordSaved and passwordSaved != "":
        updateStatus("you already saved this password.", label)
    elif passwordSaved == "":
        updateStatus("Generate a password first.", label)
    else:
        if os.path.exists(filename):
            with open(filename, "a", encoding="utf-8") as file:
                file.write("\n" + passwordSaved)
        else:
            print("File not found.")
            with open(filename, "w", encoding="utf-8") as file:
                file.write(passwordSaved)
    lastPasswordSaved = passwordSaved
