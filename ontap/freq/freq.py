def freq(arr:list[int]):
    result = 0
    count = 0
    sortarr = arr.sort(reverse=True)

    for i in range(len(sortarr)):
        if sortarr[i] == sortarr[i-1]:
            count += 1
            result = sortarr[i]
    return result,count

inp = 'D:\idk-python\ontap\freq\freq.inp'
out = 'D:\idk-python\ontap\freq\freq.out'

with open("inp",'r') as f:
    n = f.readline()
    