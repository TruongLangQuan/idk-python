if __name__ == '__main__':
    n = int(input())
    mylist = []
    for _ in range(n):
        cmd = input().strip().split()
        if cmd[0] == 'insert':
            mylist.insert(int(cmd[1]),int(cmd[2]))
        if cmd[0] == 'print':
            print(mylist)
        if cmd[0] == 'remove':
            mylist.remove(int(cmd[1]))
        if cmd[0] == 'append':
            mylist.append(int(cmd[1]))
        if cmd[0] == 'sort':
            mylist.sort()
        if cmd[0] == 'pop':
            mylist.pop()
        if cmd[0] == 'reverse':
            mylist.reverse()