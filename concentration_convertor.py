# Concentration Converter
def guardian(prompt, max_option=3):
    """
    Validates user input to ensure it is within the specified range.
    """
    try:
        value = int(prompt)
        if 1 > value or value > max_option:
            raise ValueError("Input out of range.")
        return value
    except ValueError:
        raise ValueError("Please enter a valid number for the option.")

def find_mass(valence, molar_mass, value):
    """
    Calculate the mass of a solute from its equivalent weight.
    """
    valence = int(valence)
    molar_mass = float(molar_mass)
    moles = value * (1 / valence)
    mass = moles * molar_mass
    return mass

def chose_eq(valence, molar_mass, solution_mass=None, density=None, total_volume=None):
    """
    Convert Eq to other units.
    """
    mass = find_mass(valence, molar_mass, 1)  # Value of 1 equivalent
    results = {}

    if solution_mass is not None:
        ppm = (mass * 1000) / solution_mass
        mass_percent = (mass * 100) / solution_mass
        results["ppm"] = ppm
        results["mass_percent"] = mass_percent / 1000

    if density is not None and total_volume is not None:
        total_volume_ml = total_volume * 1000
        volume_percent = (mass * (1 / density) * 100) / total_volume_ml
        results["volume_percent"] = volume_percent

    return results

def chose_ppm(value, molar_mass=None, valence=None):
    """
    Convert PPM to other units.
    """
    results = {"ppm": value}
    if molar_mass is not None and valence is not None:
        concentration_pl = value / 1000
        moles_per_liter = concentration_pl / molar_mass
        eq_l = moles_per_liter * valence
        results["eq_l"] = eq_l

    results["mass_percent"] = value / 10000  # Assuming ppm is mass/mass
    results["volume_percent"] = value / 10000  # Assuming ppm is volume/volume
    return results

def chose_mass_percent(value, density=None, molar_mass=None, valence=None, solute_density=None, solution_density=None):
    """
    Convert mass percent to other units.
    """
    results = {}

    if density is not None and molar_mass is not None and valence is not None:
        concentration_gl = value * density
        molar_concentration = concentration_gl / molar_mass
        eq_l = molar_concentration * valence
        results["eq_l"] = eq_l

    results["ppm"] = value * 10000

    if solute_density is not None and solution_density is not None:
        mass_solute = value / 100  # Assumes percentage input
        mass_solution = mass_solute / (value / 100)
        volume_percent = (mass_solute / solute_density) * 100 / (mass_solution / solution_density)
        results["volume_percent"] = volume_percent

    return results

def concen_converter(value, unit, **kwargs):
    """
    Main function to handle concentration conversion based on the unit.
    """
    value = float(value)

    # Check if valence and molar_mass are in kwargs to pass them correctly
    valence = kwargs.get('valence', 1)
    molar_mass = kwargs.get('molar_mass', None)

    if unit == 1:  # Eq
        # Only pass valence and molar_mass explicitly
        return chose_eq(valence, molar_mass, **{key: kwargs[key] for key in kwargs if key not in ['valence', 'molar_mass']})
    elif unit == 2:  # PPM
        return chose_ppm(value, molar_mass=molar_mass, valence=valence)
    elif unit == 3:  # Mass Percent
        return chose_mass_percent(value, molar_mass=molar_mass, valence=valence, **kwargs)
    else:
        raise ValueError("Invalid unit selected.")
