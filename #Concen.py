#Concentration Convertor
def Gaurdian(x,y=3):
    g = True
    while g:
        try:
            value = int(input(x))
            if 1>value or value>y:
                print("\nenter the number of the above options please, input invalid\n")
            else:
                return value
        except:
            print("\nPlease enter a valid input (the number of the option) \n")
message_1 = "what is the unit of the value you would like to convert?\n1.Eq?\n2.Parts Per Million\n3.Mass Percent\n"

def find_mass():
    valence=int(input("what is the valence?: "))
    Molar_mass = float(input("What is the Molar mass in g/mol?: "))
    moles = value*(1/valence)
    mass = moles*Molar_mass
    return mass

List = ["Eq", "ppm", "Mass percent", "Volume percent"]

unit= Gaurdian(message_1) #make sure that the input is valid

value =float(input(f"what is the value for this unit ({List[unit-1]}): "))

if unit == 1:
    message_1 = "what is the unit of the value you would like to convert to?\n1.Parts Per Million\n2.Mass Percent\n3.Volume percent\n"
    operation= Gaurdian(message_1)
    mass = find_mass()
    if operation==1 or operation==2:
        Solution_Mass = float(input("What is the mass of the solution in kg?: "))
    if operation ==1:
        ppm = ((mass)*1000)/Solution_Mass
        print(f"{ppm} ppm")
    if operation ==2:
        Mass_percent = mass*100/Solution_Mass
        print(f"{Mass_percent/1000} %")
    if operation ==3:
        density= float(input("please give the density in g/mL: "))
        Total_Volume = float(input(("please enter the volume of the solution in L: ")))*1000
        Volume_percent = (mass*(1/density)*100)/Total_Volume
        print(f"{Volume_percent }%")

if unit == 2:
    message_1 = "what is the unit of the value you would like to convert to?\n1.Eq/L\n2.Mass Percent\n3.Volume percent\n"
    operation= Gaurdian(message_1)
    if operation==1:
        Concentration_PL = value/1000
        valence=int(input("what is the valence?: "))
        Molar_mass= float(input("Please enter the Molar mass in g/mol: "))
        Moles_per_liter= Concentration_PL/Molar_mass
        Eq_L= Moles_per_liter*valence
        print(f"{Eq_L} Eq/L")
    if operation ==2:
        print("assuming ppm is m/m")
        Mass_percent = value/10000
        print(f"{Mass_percent} %")
    if operation ==3:
        print("assuming ppm is v/v")
        Volume_percent = value/10000
        print(f"{Volume_percent} %")

if unit ==3:
    message = "what is the unit of the value you would like to convert to?\n1.Eq/L\n2.Parts Per Million\n3.Volume percent\n"
    operation= Gaurdian(message_1)
    if operation ==1:
        density= float(input("please give the density in g/mL: "))*10
        Molar_mass= float(input("Please enter the Molar mass in g/mol: "))
        valence = int(input("What is the valence?: "))
        Concentration_gL = value*density
        Molar_concentration = Concentration_gL/Molar_mass
        Eq_L = Molar_concentration*valence
        print(f"{Eq_L} Eq/L")
    if operation ==2:
        ppm = value*10000
        print(f"{ppm} ppm")
    if operation == 3:
        mass_solute = float(input("please enter the mass of the solute"))
        mass_solution = mass_solute/(value/100)
        solute_density = float(input("what is the density of the solute in g/ml"))
        solution_density = float(input("what is the density of the solution in g/ml"))
        Volume_percent = (mass_solute/solute_density)*100/(mass_solution/solution_density)
        print(f"{Volume_percent} %")