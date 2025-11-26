import string

def ceasar(text:str,shift:int,mode:int):
    result = ''

    if mode == 2:
        shift = -shift

    if mode == 1:
        for i,ch in enumerate(text):
            if ch.isalpha():
                is_upper = ch.isupper()

                base = ord(ch) - ord("A") if is_upper else ord("a")
                after = (ord(ch) - base + shift) % 26
                result += str(after)
        else:
            result += ch
    return result

def vigenere(text:str,key:str,mode:int):
    result = ''

    if mode == 1:
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

def atbash(text:str):
    result = ''
    
    for i,ch in enumerate(text):
        if ch.isalpha():
            is_upper = ch.isupper()
            if is_upper:
                base = ord(ch) - ord("A")
                result += chr(ord("Z") - base)
            else:
                base = ord(ch) - ord("a")
                result += chr(ord("z") - base)
        else:
            result += ch
    return result

def chedo(mode):
    print("I:Ceasar  II:Vigenere  III:Atbash")
    return mode

def main():
    result = ""
    
    if mode == 1:
        text = str(input("Text:"))
        step = int(input("Step:"))
        mode = int(input("Step:"))
        
        result = ceasar(text,step,mode)

    return result

mode = chedo(int(input("Choose:")))
main()