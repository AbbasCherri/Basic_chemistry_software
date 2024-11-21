def Good_to_Go(y,x=""):
    while True:
        try:
            x = float(input(f"how many {y} do we have?: "))
            if x==int(x):
                return int(x)
        except ValueError:
            print("\nplease enter a valid number in integer form")

def Get_List(x,z):
    y =[]
    for index in range(x):
        x = input(f"what is the {index+1} {z}?: ")
        y.append(x)
    return(y)

def Get_coefficient(x):
    list_of_coefficients = []
    for i in range(len(x)): #we check every compound in list x
         while True:
            try:
                y = float(input(f"what is the coefficient of {x[i]}?: ")) #we ask for the coefficient of each element in list x
                if y==int(y):
                    list_of_coefficients.append(int(y))
                    break
                else: #if the float does not equal the integer then it cannot be written in integer form, obliging us to ask the user for a valid input
                    print("\nplease enter a valid number in integer form")
            except ValueError:
                print("\nplease enter a valid number in integer form")
    return(list_of_coefficients)

def cofcompound(x,y): #attaching coefficient to compound
    z = []
    y = [str(index) for index in y]
    for i in range(len(x)):
        z.append(y[i]+ "_" + x[i])
    return(z)


nbr_reactants = Good_to_Go("reactants")
nbr_products = Good_to_Go("products")

List_of_reactants = Get_List(nbr_reactants,"reactant")
List_of_products = Get_List(nbr_products,"product")

Coeifficent_reactants = Get_coefficient(List_of_reactants)
Coeifficient_products = Get_coefficient(List_of_products)

last = cofcompound(List_of_reactants,Coeifficent_reactants)
last2 = cofcompound(List_of_products,Coeifficient_products)


print(" + ".join(last), "-->"," + ".join(last2))
def stoichiometry():
    Theoretical = False
    while True:
        print("\nplease enter the number of the operations presented\n")
        operation = (input("What are we trying to find?:\n1. Limiting and Excess reagent?\n2. +Theoretical Product Yield?\n"))
        if operation =="2":
            Theoretical = True
        ask = input("is the number of moles for the reactants given?: ")
        if ask == "no" or ask == "No" or ask == "negative":
            ask_again = input("is the Volume and concentration given?: ")
            if ask_again=="no" or ask_again == "No" or ask_again == "negative":
                print("this falls outside the capabilities of the program :(")
                last_ask = input("would you like to stop this program?: ")
                if last_ask == "yes" or last_ask=="Yes" or last_ask=="Yeah" or last_ask=="yeah":
                    break
            else:
                L = []
                for i in range(len(List_of_reactants)):
                    Volume = float(input(f"what is the volume of {List_of_reactants[i]} in Liters?: "))
                    Concentration = float(input(f"what is the concentration of {List_of_reactants[i]} in moles/L?: "))
                    moles = Volume*Concentration
                    L.append(moles)
                    for i in range(len(L)):
                        y = L[i]/Coeifficent_reactants[i]
                        L[i] = y   
                    
        else:
            L = []
            for i in range(len(List_of_reactants)):
                y = float(input(f"what is the number of moles of {List_of_reactants[i]}?: ")) 
                L.append(y)
                #getting the number of moles of each reactant
        for i in range(len(L)):
            y = L[i]/Coeifficent_reactants[i]
            L[i] = y
        #getting the stoiciometric ratios of each reactant in accordance with their coefficients
        if min(L)==max(L):
            #if the minimum stoiciometric ratio is equal to the maximum then there is no liming and excess
            print("the reaction is at stoichiometric equivalence")
            print(L)
        else:
            print(List_of_reactants[L.index(min(L))],f"is the Limiting reagent\nmoles={min(L)} ")
            print(List_of_reactants[L.index(max(L))],f"is the excess reagent\nmoles={max(L)}")
        if Theoretical:
            print(List_of_products)
            answer = input("choose a product from the above")
            while answer not in List_of_products:
                print(f"{answer} is not in the list. Please try again\n")
                print(List_of_products)
                answer = input("choose a product from the above: ")
            place = List_of_products.index(answer)
            print(f"Theoretical yield of {answer} is {min(L)*Coeifficient_products[place]} moles")
        break


stoichiometry()