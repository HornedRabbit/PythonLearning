wybor = 0

slownik = {}

while (wybor != "4"):
    
    print("1: Dodawanie definicji")
    print("2: Wyszukiwanie definicji")
    print("3: Usuwanie definicji")
    print("4: Zakończenie działania słownika")
    
    wybor = input("Wybierz akcję: ")
  
    if (wybor == "1"):
        klucz = input("Podaj klucz (słowo) do zdefiniowania (pamietaj o użyciu dużej litery): ")
        definicja = input("Podaj definicję: ")
        slownik.update({klucz: definicja})
        print("Dodano definicję")
        
    elif (wybor == "2"):
        szklucz = input("Podaj szukane słowo (pamiętaj o użyciu dużej litery): ")
        if szklucz in slownik:
            print(szklucz, "-",slownik[szklucz])
        else:
            print("Nie znaleziono definicji o nazwie", szklucz)
        
    elif (wybor == "3"):
        usklucz = input("Podaj klucz definicji do usunięcia: ")
        if usklucz in slownik:
            print("Usunąłęś ze słownika:", usklucz, "-", slownik.pop(usklucz))
        else:
            print("Nie znaleziono definicji o nazwie", usklucz)
                
    elif (wybor == "4"):
        print("Postanowiłeś zakończyć korzystanie ze słownika: ")
        
    else:
        print("Wybrałeś niepoprawną akcję.")
