#t ko bt hash là cái j
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    mytuple = tuple(integer_list)
    print(mytuple)
    print(hash(mytuple))