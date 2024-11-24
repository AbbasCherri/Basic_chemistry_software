import numpy as np
from scipy.linalg import null_space
from equation_functions import create_matrix, extract_equation


def equation_balancer():

    equation = input()

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
    while i < len(coefficients):
        if L[i] == "->":
            print("->", end=" ")
            L.pop(i)

        if i+1 == len(coefficients):
            print(abs(coefficients[i]), L[i]) 
        else:
            print(abs(coefficients[i]), L[i], " + ", end="")
        i += 1

