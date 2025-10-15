import string
import tkinter
import python_library 

def ceasar(text:str,shift:int,mode:int):
    result = ''

    if mode == 2:
        shift = -shift

    for i,ch in enumerate(text):
        if ch.isalpha():
            is_upper = ch.isupper()

            base = ord(ch) - ord("A") if is_upper else ord("a")
            after = (ord(ch) - base + shift) % 26
            result += after
        else:
            result += ch
    return result

def vigenere(text:str,key:str,mode:int):
    result = ''

    for i,ch in enumerate(text):
        if ch.isalpha():
            is_upper = ch.isupper()

            base = ord(ch) - ord("A") if is_upper else ord("a")
            key_char = key[i % len(key)].lower()
            shift = ord(key_char) - ord("a")
            
            if mode == 2:
                shift = -shift

            result += chr((ord(ch) - base + shift) % 26 + base)

        else:
            result += ch
    return result

def aibash(text:str,mode:int):
    result = ''

    for i,ch in enumerate(text):
        if ch.isalpha():
            pass
