import Chem_dictionaries as p

def molar_mass_calc(mass_of_substance:float, number_of_moles:float):
    molar_mass =  mass_of_substance/number_of_moles
    return molar_mass

def mol_calculator(mass:float , element:str):
    number_of_moles = mass * (1/p.atomic_mass[element])
    return number_of_moles

