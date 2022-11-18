# Defining the paths that'll be used
path1 = r"C:\Users\pers\Desktop\Programs\Python Programming\options.txt"
path2 = r"C:\Users\pers\Desktop\Programs\Python Programming\liste_elements.txt"
while True: #for an infinite loop
    with open(path1, "r") as f:
        content = f.read() 
        print(f"\n{content}")
    n = int(input()) 
    while n not in range(1,6):
        print("Cette option ne figure pas dans le liste des options. Veuillez choisir une autre ")
        n = int(input())
    if n == 5:
        break
    # Defining the different options
    match n:
        case 1:
            added = input("Entrez le nom de l'element a ajouter: ")
            with open(path2, "r") as f:
                cont = f.read()
            with open(path2, "a") as f:
                if cont == "":
                    f.write(added) #If the text file is originally empty, the added element won't go the next line
                else:
                    f.write(f"\n{added}") #If the elements in the file, the element will be added in the next line
        
        case 2:
            rmv = input("Entrez le nom de l'element a enlever: ")
            with open(path2, "r") as f:
                liste = f.read().splitlines() #reading the text while converting it into a list
                if rmv in liste:
                    liste.remove(rmv)
                else:
                    print(f"L'element '{rmv}' n'est point dans la liste de courses")
                liste = "\n".join(liste) #Joining the diff elements of the list while seperating with a \n
            with open(path2, "w") as f:
                f.write(liste)
                
         
        case 3:
            with open(path2, "r") as f:
                contenu = f.read()
                if contenu == "":
                    print("La liste ne contient aucun element")
                else:
                    print(contenu)
        case 4:
            with open(path2, "r") as f:
                conte = f.read()
                liste = f.read().splitlines()
                liste.clear() 
                liste = "".join(liste)
            with open(path2, "w") as f:
                f.write(liste)
            if conte == "":
                print("La liste est deja vide")
            else:
                print("La liste a ete vider")
    
