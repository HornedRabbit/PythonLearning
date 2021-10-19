szukanaLiczba = 40
zgadywana = 0


while (zgadywana != szukanaLiczba):
    zgadywana = int(input("Zgadnij liczbę: "))
    
    if (zgadywana > szukanaLiczba):
        print("Wpisałeś za dużą liczbę, spróbuj ponownie")
    elif (zgadywana < szukanaLiczba):
        print("Wpisałeś za małą liczbę, spróbuj ponownie")
    else:
        print("Brawo")


        
    
