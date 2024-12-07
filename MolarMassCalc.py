import Chem_dictionaries as p

def molar_mass_calc(mass_of_substance:float, element: float):
    molar_mass =  mass_of_substance/mol_calculator(mass_of_substance, element)
    return molar_mass

def mol_calculator(mass:float , element:str):
    number_of_moles = mass * (1/p.atomic_mass[element])
    return number_of_moles

