def trunglap(text):
    for ch in text:
        if text.count(ch) > 1:
            return True
    return False

text = "hello"
print(trunglap(text))