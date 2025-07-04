try:
    mydict = {'Name':30,'Age':15}
    value = mydict['waifu']
except KeyError:
    value = "Bruh"

print(f"{value}")