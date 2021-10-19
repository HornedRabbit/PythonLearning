import math

def pole_prostokata(a, b):
    return a * b

def pole_kwadratu(a):
    return a ** 2

def pole_trojkata(a, h):
    return (a*h/2)

def pole_trapezu(a, b, h):
    return h*(a+b)/2

def pole_kola(r):
    return math.pi *(r**2)
    

wybor = 0

while (wybor != "6"):

    print("Jest to program do liczenia pola powierzchni figur")
    print("1: Pole prostokata")
    print("2: Pole kwadratu")
    print("3: Pole trójkąta")
    print("4: Pole trapezu")
    print("5: Pole koła")
    print("6: Zakończ działanie programu")

    wybor = input("Co chcesz zrobić? ")

    if wybor == "1" :
        a = int(input("Podaj pierwszy wymiar prostokąta: "))
        b = int(input("Podaj drugi wymiar prostokąta: "))
        if (pole_prostokata(a,b) <= 0):
            print("Podałeś niepoprawne wymiary prostokąta")
        else:
            print("Pole prostokąta jest równe:", pole_prostokata(a,b))
      
    elif wybor == "2" :
        a = int(input("Podaj wymiar boku kwadratu: "))
        if (pole_kwadratu(a) <= 0):
            print("Podałeś niepoprawne wymiary kwadratu")
        else:
            print("Pole kwadratu jest równe:", pole_kwadratu(a))
            
    elif wybor == "3" :
        a = int(input("Podaj wymiar podstawy trójkąta: "))
        h = int(input("Podaj wysokość trójkąta: "))
        if (pole_trojkata(a,h) <= 0):
            print("Podałeś niepoprawne wymiary trójkąta")
        else:
            print("Pole trójkąta jest równe:", pole_trojkata(a,h))
            
    elif wybor == "4" :
        a = int(input("Podaj wymiar pierwszej podstawy trapezu: "))
        b = int(input("Podaj wymiar drugiej podstawy trapezu: "))
        h = int(input("Podaj wysokość trapezu: "))
        if (pole_trapezu(a,b,h) <= 0):
            print("Podałeś niepoprawne wymiary trapezu")
        else:
            print("Pole trapezu jest równe:", pole_trapezu(a,b,h))
            
    elif wybor == "5" :
        r = int(input("Podaj promień koła: "))
        if (pole_kola(r) <= 0):
            print("Podałeś niepoprawne wymiary koła")
        else:
            print("Pole koła jest równe:", pole_kola(r))
            
    elif wybor == "6" :
        print("Wybrałeś zakończenie działania programu, do zobaczenia!")
        
    else:
        print("Nie wybrałeś poprawnej akcji")
        
                            
