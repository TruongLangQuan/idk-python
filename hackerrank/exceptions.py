test = int(input())

for i in range(test):
    try:
        a , b = input().split()
        a = int(a)
        b = int(b)
        print(a//b)
    except ZeroDivisionError as e:
        print(f"Error Code: {e}")
    except ValueError:
        print(f"Error Code:{e}")    