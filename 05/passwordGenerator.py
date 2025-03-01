import string
from random import choices, shuffle

#cria lista com dos caracteres usando o modulo string
lettersList = list(string.ascii_letters)
symbolsList = list(string.punctuation)
numbersList = list(string.digits)

#coleta as entradas de personalizacao da senha do usuario
print("Welcome to the PyPassword Generator!")
letters = int(input("How many letters would you like in your password?\n"))
symbols = int(input("How many symbols would you like?\n"))
numbers = int(input("How many numbers would you like?\n"))

#coloca todas as escolhas personalizadas de caracteres em uma lista
passwordCharList = choices(lettersList, k=letters) + choices(symbolsList, k=symbols) + choices(numbersList, k=numbers)

#bagunça a ordem da lista
shuffle(passwordCharList)

#cria 1 acumulador
finalPassword = ""

#junta os caracteres da lista em uma unica string
for char in passwordCharList:
    finalPassword += char

#printa a senha gerada no console
print(f"Here is your high security password: {finalPassword}")