def pw(text):
    result = 0

    for i in range(len(text)):
        if text[i].isdigit():
            if int(text[i]) % 2 == 0:
                result += int(text[i])
    return result

with open("pword.inp", "r") as f:
    n = f.read()
text = str(n)
with open("pword.out", "w") as f:
    f.write(str(pw(text)))