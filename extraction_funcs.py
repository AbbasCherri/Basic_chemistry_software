import re

def extract_reactants(reaction: str):
    def remove_charge(formula: str) -> str:
            return re.sub(r'\^\d+[+-]', '', formula)
    def expand_parentheses(formula: str) -> str:
        while '(' in formula:
            match = re.search(r'\(([()]+)\)(\d*)', formula)
            if not match:
                break

            group, multiplier = match.groups()
            multiplier = int(multiplier) if multiplier else 1
            
            expanded_group = ""
            for part in re.finditer(r'([A-Z][a-z]*)(\d*)', group):
                element, count = part.groups()
                count = int(count) if count else 1
                expanded_group += f"{element}{count * multiplier}"
            
            formula = formula[:match.start()] + expanded_group + formula[match.end():]
        
        return formula

    reaction = remove_charge(reaction)
    reaction = expand_parentheses(reaction)

    elem_dict = dict()
    elem_list = []
    list_of_ints = []

    for i in range(len(reaction)):
        try:
            int(reaction[i])
            list_of_ints.append(reaction[i])
        except ValueError:
            if reaction[i].isupper():
                try:
                    if reaction[i + 1].islower():
                        elem_list.append(reaction[i] + reaction[i + 1])
                    else:
                        elem_list.append(reaction[i])
                except IndexError:
                    elem_list.append(reaction[i])

                list_of_ints.append("")
    # print(elem_list)
    # print(list_of_ints)
    if list_of_ints[0] == "" and (len(reaction) == 1 or list_of_ints[0] == "" or list_of_ints[1] == ""): # S
        list_of_ints[0] = 1
    else:
        list_of_ints.pop(0)

    for i in range(len(list_of_ints)):
        try:
            if list_of_ints[i] == "" and list_of_ints[i + 1] == "":
                list_of_ints.insert(i + 1, 1)
        except IndexError:
            continue

    uniq = []

    int_length = len(list_of_ints)
    elem_length = len(elem_list)

    if int_length != elem_length:
        i = 0
        while i < int_length:
            if list_of_ints[i] != "":
                k = list_of_ints[i]
            if i + 1 < int_length and list_of_ints[i + 1] != "":
                for j in range(i + 1, int_length):
                    if list_of_ints[j] == "":
                        break
                    else:
                        if type(list_of_ints) != int:
                            k += int(list_of_ints[j])-1
                        else:
                            k += list_of_ints[j]
            if i + 1 < int_length:
                try:
                    i = j
                except NameError:
                    i = i + 1
            i += 1
            uniq.append(k)
    else:
        for i, elem in enumerate(list_of_ints):
            try:
                int(elem)
            except ValueError:
                list_of_ints.insert(i, 1)
                list_of_ints.pop(i + 1)
        uniq = list_of_ints

    for i in range(elem_length):
        try:
            elem_dict[elem_list[i]] = int(uniq[i])
        except IndexError:
            elem_dict[elem_list[i]] = 1
    # print(elem_dict)
    return elem_dict

# n = input()
# extract_reactants(n)