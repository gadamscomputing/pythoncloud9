#This is my attempt at the new GCSE topic for the GTIN #.

gtinNum = input("Please enter a 7 digit GTIN number!!")

gtinList = []
calc = 0

gtinList = list(gtinNum)

print(gtinList)

for x in gtinList:
        if (x % 2) == 0   :
            calc = calc + int(x) * 3
        else:
            calc = calc + int(x) * 1
            
print(calc)

            
