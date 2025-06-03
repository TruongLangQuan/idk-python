if __name__ == '__main__':
    hocs = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        hocs.append([name,score])
        
    unique_scores = sorted({s[1] for s in hocs})
    
    if len(unique_scores) >= 2:
        scdiem = unique_scores[1]
    else:
        scdiem = unique_scores[0]

    final = sorted([s[0] for s in hocs if s[1] == scdiem])

    for name in final:
            print(name)