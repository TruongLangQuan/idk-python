def swap(text):
    result = ""
    for chars in text:
        if chars.islower():
            result += chars.upper()
        elif chars.isupper():
            result += chars.lower()
        else:
            result += chars
    return result

text = str(input("Input str:"))
print(swap(text))