def datafromfile(fileTitle):
    
    try:
        with open(fileTitle, "r", encoding="UTF-8") as file:
            data = file.read().splitlines()
            return data
    except FileNotFoundError:
        print("There is no file with this name.")

fileTitle = input("Podaj nazwę pliku z rozszerzeniem: ")
print(datafromfile(fileTitle))
