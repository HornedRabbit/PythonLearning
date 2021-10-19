import pfigur

from enum import IntEnum

Menu_Figury = IntEnum("Menu_Figury", "Prostokąt Kwadrat Trójkąt Trapez Koło Zakończ")

wybor = 0

while (wybor != Menu_Figury.Zakończ):

    print("""Jest to program do liczenia pola powierzchni figur
1: Pole prostokata
2: Pole kwadratu
3: Pole trójkąta
4: Pole trapezu
5: Pole koła
6: Zakończ działanie programu""")

    wybor = int(input("Co chcesz zrobić? "))
    
    if (wybor == Menu_Figury.Prostokąt):
        a = float(input("Podaj pierwszy wymiar prostokąta: "))
        b = float(input("Podaj drugi wymiar prostokąta: "))
        if (pfigur.pole_prostokata(a,b) <= 0):
            print("Podałeś niepoprawne wymiary prostokąta")
        else:
            print("Pole prostokąta jest równe:", pfigur.pole_prostokata(a,b))
      
    elif (wybor == Menu_Figury.Kwadrat):
        a = float(input("Podaj wymiar boku kwadratu: "))
        if (pfigur.pole_kwadratu(a) <= 0):
            print("Podałeś niepoprawne wymiary kwadratu")
        else:
            print("Pole kwadratu jest równe:", pfigur.pole_kwadratu(a))
            
    elif (wybor == Menu_Figury.Trójkąt):
        a = float(input("Podaj wymiar podstawy trójkąta: "))
        h = float(input("Podaj wysokość trójkąta: "))
        if (pfigur.pole_trojkata(a,h) <= 0):
            print("Podałeś niepoprawne wymiary trójkąta")
        else:
            print("Pole trójkąta jest równe:", pfigur.pole_trojkata(a,h))
            
    elif (wybor == Menu_Figury.Trapez):
        a = float(input("Podaj wymiar pierwszej podstawy trapezu: "))
        b = float(input("Podaj wymiar drugiej podstawy trapezu: "))
        h = float(input("Podaj wysokość trapezu: "))
        if (pfigur.pole_trapezu(a,b,h) <= 0):
            print("Podałeś niepoprawne wymiary trapezu")
        else:
            print("Pole trapezu jest równe:", pfigur.pole_trapezu(a,b,h))
            
    elif (wybor == Menu_Figury.Koło):
        r = float(input("Podaj promień koła: "))
        if (pfigur.pole_kola(r) <= 0):
            print("Podałeś niepoprawne wymiary koła")
        else:
            print("Pole koła jest równe:", pfigur.pole_kola(r))
            
    elif (wybor == Menu_Figury.Zakończ):
        print("Wybrałeś zakończenie działania programu, do zobaczenia!")
        
    else:
        print("Nie wybrałeś poprawnej akcji")
