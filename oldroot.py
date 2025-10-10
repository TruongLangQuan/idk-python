import string
import tkinter

stringlower = string.ascii_lowercase
stringupper = string.ascii_uppercase

def ceasar(text:str,shift:int):
    result = ''
    shift %= 26
    for i in range(len(text)):
        if text[i] in stringupper:
            result += chr(((ord(text[i] - ord('A') + shift)) % 26) + ord("A"))
        elif text[i] in stringlower:
            result += chr(((ord(text[i]) - ord('a') + shift) % 26) + ord('a'))
        else:
            result += text[i]  
    return result

def ceasard(text:str,shift:int):
    result += ceasar(text, -shift)
    return result

def vigenere(text:str,key:int):
    pass

