def count_substring(string, sub_string):
    count = 0
    len_sub = len(sub_string)
    for i in range(len(string) - len_sub  +1):
        if string[i:i+len_sub] == sub_string:
            count += 1
    return count

if __name__ == '__main__':
    ring = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)