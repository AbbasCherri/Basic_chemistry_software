def dilution():
    choice = input('What do you want to calculate? C1, V1, C2, V2: ') # choose which variable to calculate
    if choice == 'C1': # in case of inital concentration
        V1 = float(input('Enter the initial volume: '))
        C2 = float(input('Enter the final concentration: '))
        V2 = float(input('Enter the final volume: '))
        unit = input('Which unit would you like to use for the concentration? M/ml,M/cl,M/dl,M/L,M/dal,M/hl,M/kl: ') # choose the unit of measurment
        rounding = int(input('How many digits after the decimal point?: ')) # choose how many digits to round after the decimal point
        if unit == 'M/ml':  # convert units if needed (standard unit is Mol/Liter)
            V2 = V2 * 0.001
            V1 = V1 * 0.001
        elif unit == 'M/cl':
            V2 = V2 * 0.01
            V1 = V1 * 0.01
        elif unit == 'M/dl':
            V2 = V2 * 0.1
            V1 = V1 * 0.1
        elif unit == 'M/dal':
            V2 = V2 * 10
            V1 = V1 * 10
        elif unit == 'M/hl':
            V2 = V2 * 100
            V1 = V1 * 100
        elif unit == 'M/kl':
            V2 = V2 * 1000
            V1 = V1 * 1000
        C1 = (C2 * V2)/V1
        print(f'The initial concentration is: {round(C1,rounding)} {unit}')
    elif choice == 'V1': # in case of initial volume
        C1 = float(input('Enter the initial concentration: '))
        C2 = float(input('Enter the final concentration: '))
        V2 = float(input('Enter the final volume: '))
        unit = input('Which unit would you like to use for the volume? ml,cl,dl,L,dal,hl,kl: ') # choose the unit of measurments
        rounding = int(input('How many digits after the decimal point?: ')) # choose how many digits to round after the decimal point
        if unit == 'ml':  # convert units if needed (standard unit is Liters)
            V2 = V2 * 0.001
        elif unit == 'cl':
            V2 = V2 * 0.01
        elif unit == 'dl':
            V2 = V2 * 0.1
        elif unit == 'dal':
            V2 = V2 * 10
        elif unit == 'hl':
            V2 = V2 * 100
        elif unit == 'kl':
            V2 = V2 * 1000
        V1 = (C2 * V2)/C1
        print(f'The initial volume is: {round(V1,rounding)} {unit}')
    elif choice == 'C2': # in case of final concentration
        C1 = float(input('Enter the initial concentration: '))
        V1 = float(input('Enter the initial volume: '))
        V2 = float(input('Enter the final volume: '))
        unit = input('Which unit would you like to use for the concentration? M/ml,M/cl,M/dl,M/L,M/dal,M/hl,M/kl: ') # choose the unit of measurment
        rounding = int(input('How many digits after the decimal point?: ')) # choose how many digits to round after the decimal point
        if unit == 'M/ml': # convert units if needed (standard unit is Mol/Liter)
            V2 = V2 * 0.001
            V1 = V1 * 0.001
        elif unit == 'M/cl':
            V2 = V2 * 0.01
            V1 = V1 * 0.01
        elif unit == 'M/dl':
            V2 = V2 * 0.1
            V1 = V1 * 0.1
        elif unit == 'M/dal':
            V2 = V2 * 10
            V1 = V1 * 10
        elif unit == 'M/hl':
            V2 = V2 * 100
            V1 = V1 * 100
        elif unit == 'M/kl':
            V2 = V2 * 1000
            V1 = V1 * 1000
        C2 = (C1 * V1)/V2
        print(f'The final concentration is: {round(C2,rounding)} {unit}')
    elif choice == 'V2':
        C1 = float(input('Enter the initial concentration: '))
        V1 = float(input('Enter the initial volume: '))
        C2 = float(input('Enter the final concentration: '))
        unit = input('Which unit would you like to use for the volume? ml,cl,dl,L,dal,hl,kl: ') # choose the unit of measurment
        rounding = int(input('How many digits after the decimal point?: ')) # choose how many digits to round after the decimal point
        if unit == 'ml': # convert units if needed (standard unit is Liters)
            V1 = V1 * 0.001
        elif unit == 'cl':
            V1 = V1 * 0.01
        elif unit == 'dl':
            V1 = V1 * 0.1
        elif unit == 'dal':
            V1 = V1 * 10
        elif unit == 'hl':
            V1 = V1 * 100
        elif unit == 'kl':
            V1 = V1 * 1000
        V2 = (C1 * V1)/C2
        print(f'The final volume is: {round(V2,rounding)} {unit}')
dilution()