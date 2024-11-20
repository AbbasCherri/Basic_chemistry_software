def seprate_name_from_subscrit(formula):
    length_of_formula = len(formula)
    L_formula_ints = []
    L_formula_strings = []

    for i in range(length_of_formula):
        try:
            L_formula_ints.append(int(formula[i]))
        except ValueError:
            L_formula_strings.append(formula[i])
    return L_formula_strings, L_formula_ints

def extract_elem_subscript(L_formula_ints):
    length_of_formula = len(L_formula_ints)

    if length_of_formula > 2:
        L_formula_ints = L_formula_ints[0]
    elif L_formula_ints == []:
        subscript_of_elem = 1
        return subscript_of_elem
    else:
        subscrit_of_elem = 0
        power = length_of_formula - 1 
        for i in range(length_of_formula):
            subscrit_of_elem += L_formula_ints[i]*(10**power)
            power -= 1
    return subscrit_of_elem

def extract_elem_name(L_formula_strings):
    length_of_formula = len(L_formula_strings)

    if length_of_formula > 2:
        elem_name = L_formula_strings[0]
    else:
        elem_name = ""
        for i in range(length_of_formula):
            elem_name += L_formula_strings[i]
    return elem_name

formula_right = input()

strL, intL = seprate_name_from_subscrit(formula_right)

elem_name = extract_elem_name(strL)
subscript_of_elem = extract_elem_subscript(intL)


print(elem_name)
print(subscript_of_elem)