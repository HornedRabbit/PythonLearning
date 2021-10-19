"""
Od 100 do 470 włącznie
podzielne przez 7 i niepodzielne przez 5

"""


"""
Przez Generator
numbersGenerated = (
    element
    for element in range (100, 471)
    if (element % 7 == 0)
    if (element % 5 != 0)
    )

for element in numbersGenerated :
    print(element)


dobre do wypisania
"""

"""
Przez Listę
numbersList = [
    element
    for element in range (100, 471)
    if (element % 7 == 0)
    if (element % 5 != 0)
    ]

print(numbersList)


przydatne gdy chcemy zachować i potrzebujemy poprawnej kolejności
"""


"""
Przez Zbiór
numbersPool = {
    element
    for element in range (100, 471)
    if (element % 7 == 0)
    if (element % 5 != 0)
    }

print(numbersPool)

przydatne gdy będziemy korzystali z operacji na zbiorach
"""


    
