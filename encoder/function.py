from customtkinter import *
from pyperclip import *

def cezar_encode(message, language, key):
    ruUpperLetters = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

    engUpperLetters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    resault = ""

    text = message.upper()

    if language == 'Русский RU':
        for i in text:
            mesto = ruUpperLetters.find(i)  # Алгоритм для шифрования сообщения на русском
            new_mesto = (mesto + key) % 33
            if i in ruUpperLetters:
                resault += ruUpperLetters[new_mesto]
            else:
                resault += i
    else:
        for i in text:
            mesto = engUpperLetters.find(i)  # Алгоритм для шифрования сообщения на английском
            new_mesto = (mesto + key) % 26
            if i in engUpperLetters:
                resault += engUpperLetters[new_mesto]
            else:
                resault += i


    return resault.lower()

def cezar_decode(message, language, key):
    ruUpperLetters = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

    engUpperLetters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    resault = ""

    text = message.upper()

    if language == 'Русский RU':
        for i in text:
            mesto = ruUpperLetters.find(i)  # Алгоритм для шифрования сообщения на русском
            new_mesto = (mesto - key) % 33
            if i in ruUpperLetters:
                resault += ruUpperLetters[new_mesto]
            else:
                resault += i
    else:
        for i in text:
            mesto = engUpperLetters.find(i)  # Алгоритм для шифрования сообщения на английском
            new_mesto = (mesto - key) % 26
            if i in engUpperLetters:
                resault += engUpperLetters[new_mesto]
            else:
                resault += i

    return resault.lower()

def copyResault(a):
    copy(a)