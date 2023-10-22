from pyperclip import *
import hashlib

from datetime import *

def cezar_encode(message, language, key):
    ruUpperLetters = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

    engUpperLetters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    resault = ""

    text = message.upper()

    if language == 'RU':
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

    if language == 'RU':
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

def hex_encoder(text):
    encoded_text = text.encode('utf-8').hex()
    return encoded_text

def hex_decoder(encoded_text):
    decoded_text = bytes.fromhex(encoded_text).decode('utf-8')
    return decoded_text


def ASCII_encode(text):

    resault = ''
    resault_a = ''

    for i in text:
        resault_a += str(ord(i)) + " "

        resault = resault_a[:len(resault_a) - 3]

    return resault

def ASCII_decode(text):
    resault = ''

    text = text.split()

    for i in text:
        resault += str(chr(int(i)))

    return resault


def binary_encode_russian(text):
    result = ""
    for char in text:
        binary_code = bin(ord(char))[2:].zfill(16)
        result += binary_code
    return result

def binary_decode_russian(binary_text):
    result = ""
    for i in range(0, len(binary_text), 16):
        binary_code = binary_text[i:i+16]
        char = chr(int(binary_code, 2))
        result += char
    return result

def binary_encode_english(text):
    result = ""
    for char in text:
        binary_code = bin(ord(char))[2:].zfill(8)
        result += binary_code
    return result

def binary_decode_english(binary_text):
    result = ""
    for i in range(0, len(binary_text), 8):
        binary_code = binary_text[i:i+8]
        char = chr(int(binary_code, 2))
        result += char
    return result
