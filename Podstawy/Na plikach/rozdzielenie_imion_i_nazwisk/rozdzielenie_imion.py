
namesandsurnames = []

#opening file and taking data
with open("imionanazwiska.txt", "r", encoding="UTF-8") as file:
   for line in file:
      namesandsurnames.append(tuple(line.replace("\n", "").split(" ")))
#end

    
#Writing names into new file
with open("imiona.txt", "w", encoding="UTF-8") as file:
    for item in namesandsurnames:
        file.write(item[0] + "n")


#Writing surnames into new file        
with open("nazwiska.txt", "w", encoding="UTF-8") as file:
    for item in namesandsurnames:
        try:
            file.write(item[1] + "\n")
        except IndexError:  #In case of tuple index error
            file.write("\n")
