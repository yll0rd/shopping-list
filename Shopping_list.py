
while True: #for an infinite loop
    with open("Options.txt","r") as f:
        content = f.read() 
        print(f"\n{content}")
    n = int(input()) 
    while n not in range(1,6):
        print("This option is not in the list of options. Please choose another ")
        n = int(input())
    if n == 5:
        break
    # Defining the different options
    match n:
        case 1:
            added = input("Enter the name of the element to add: ")
            with open("Items_list.txt", "r") as f:
                cont = f.read()
            with open("Items_list.txt", "a") as f:
                if cont == "":
                    f.write(added) #If the text file is originally empty, the added element won't go the next line
                else:
                    f.write(f"\n{added}") #If the elements in the file, the element will be added in the next line
        
        case 2:
            rmv = input("Enter the name of the element to remove: ")
            with open("Items_list.txt", "r") as f:
                liste = f.read().splitlines() #reading the text while converting it into a list
                if rmv in liste:
                    liste.remove(rmv)
                else:
                    print(f"The item '{rmv}' is not in the shopping list")
                liste = "\n".join(liste) #Joining the diff elements of the list while seperating with a \n
            with open("Items_list.txt", "w") as f:
                f.write(liste)
                

        case 3:
            with open("Items_list.txt", "r") as f:
                content = f.read()
                if content == "":
                    print("The list is already empty")
                else:
                    print(content)
        case 4:
            with open("Items_list.txt", "r") as f:
                conte = f.read()
                liste = f.read().splitlines()
                liste.clear() 
                liste = "".join(liste)
            with open("Items_list.txt", "w") as f:
                f.write(liste)
            if conte == "":
                print("The list is already empty")
            else:
                print("The list has been emptied")
    
