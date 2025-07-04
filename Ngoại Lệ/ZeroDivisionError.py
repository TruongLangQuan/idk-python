try:
    result = 10/0
except ZeroDivisionError:
    result = "Bruh"

print(f"{result}")