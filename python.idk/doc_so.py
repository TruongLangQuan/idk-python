def inputso():
    try:
        so = int(input("0 to 9:"))
        return so
    except ValueError:
        return "Ko hop le"
    
def docso(so):
    numlist = ['Khong','Mot','Hai','Ba','Bon','Nam','Sau','Bay','Tam','Chin']

    return numlist[so]
    
def main():
    so = inputso()
    print(docso(so))

main()