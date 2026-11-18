import random
import os
import string

filename = "output.txt"
passwordSaved = ""
lastPasswordSaved = ""
label = ""


def setLabel(newLabel):
    global label
    label = newLabel


def deleteFile(file):
    global lastPasswordSaved
    if os.path.exists(file):
        os.remove(file)
        lastPasswordSaved = ""
        updateStatus(f"{file} has been deleted.")
        updateStatus(passwordSaved, 1000)
    else:
        updateStatus(f"file name '{file}' does not exist.")
        updateStatus(passwordSaved, 1000)


def updateStatus(message, delay=0):
    if delay:
        label.after(delay, lambda: label.config(text=message))
    else:
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

    updateStatus(password)

    return password


def savePassword():
    global lastPasswordSaved

    if passwordSaved == "":
        updateStatus("Generate a password first.")
        updateStatus(passwordSaved, 1000)
    elif passwordSaved == lastPasswordSaved:
        updateStatus("you already saved this password.")
        updateStatus(passwordSaved, 1000)
    else:
        with open(filename, "a", encoding="utf-8") as file:
            file.write(passwordSaved + "\n")
        updateStatus("Password saved!")
        updateStatus(passwordSaved, 1000)
    lastPasswordSaved = passwordSaved
