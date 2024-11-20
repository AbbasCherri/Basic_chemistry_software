def extract_reactants(reaction):
    elem_dict = dict()
    elem_list = []
    list_of_ints = []

    for i in range(len(reaction)):

        try:
            int(reaction[i])
            list_of_ints.append(reaction[i])
        except ValueError:
            if reaction[i].isupper():
                if reaction[i+1].islower():
                    elem_list.append(reaction[i] + reaction[i+1])
                else:
                    elem_list.append(reaction[i])
                if list_of_ints != []:
                    list_of_ints.append("")

    print(elem_list)
    print(list_of_ints)
    uniq = []

    int_length = len(list_of_ints)
    elem_length = len(elem_list)

    if int_length != elem_length:
        i = 0
        while i < int_length:
            if list_of_ints[i] != "":
                k = list_of_ints[i]
            if i+1 < int_length and list_of_ints[i+1] != "":
                for j in range(i+1, int_length):
                    if list_of_ints[j] == "":
                        break
                    else:
                        k += list_of_ints[j]
            if i + 1 < int_length:
                try:
                    i = j  
                except NameError:
                    i = i + 1
            i += 1
            uniq.append(k)
    print(uniq)

    for i in range(elem_length):
        try:
            elem_dict[elem_list[i]] = int(uniq[i])
        except IndexError:
            elem_dict[elem_list[i]] = 1

    print(elem_dict)