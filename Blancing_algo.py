import numpy as np
from scipy.linalg import null_space
from equation_functions import create_matrix, extract_equation


def equation_balancer(equation):

    a, b = extract_equation(equation)

    A = np.array(create_matrix(a, b))

    ns = null_space(A)

    coefficients = ns[:, 0] / np.min(np.abs(ns[:, 0]))
    coefficients = np.round(coefficients).astype(int)

    L = equation.split(" -> ")
    left = L[0].split(" + ")
    right = L[1].split(" + ")
    L = left + ["->"] + right

    i = 0
    s = ""
    while i < len(coefficients):
        if L[i] == "->":
            s += "-> "
            L.pop(i)

        if i+1 == len(coefficients):
            s += str(abs(coefficients[i])) + " " + str(L[i]) 
        else:
            s += str(abs(coefficients[i])) + " " + str(L[i]) + " + "
        i += 1
    # print(s)
    return s

n = input()
print(equation_balancer(n))