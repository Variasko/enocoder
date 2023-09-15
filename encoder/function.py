from pyperclip import *
import hashlib

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

def pasteCopyed():
    return paste()

def hashEnocode(text, type):

    if type == "md5":
        hash = hashlib.md5(text.encode('utf-8'))
        val = hash.hexdigest()
    elif type == "sha3_224":
        hash = hashlib.sha224(text.encode('utf-8'))
        val = hash.hexdigest()
    elif type == "sha3_256":
        hash = hashlib.sha256(text.encode('utf-8'))
        val = hash.hexdigest()
    elif type == "sha384":
        hash = hashlib.sha384(text.encode('utf-8'))
        val = hash.hexdigest()
    return val



