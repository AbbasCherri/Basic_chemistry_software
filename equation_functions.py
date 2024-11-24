from extraction_funcs import extract_reactants
import numpy as np

def extract_equation(equation: str):
    reactant = list()
    product = list()

    equation_list = equation.split(" -> ")
    reactant_side = equation_list[0].split(" + ")
    product_side = equation_list[-1].split(" + ")

    for elem in reactant_side:
        extraction_output = extract_reactants(elem)
        reactant.append(extraction_output)
    extraction_output = dict()

    for elem in product_side:
        extraction_output = extract_reactants(elem)
        product.append(extraction_output)
    
    return reactant, product

def create_matrix(reactants, products):
    unique_elements = set()

    for compound in reactants + products:
        unique_elements.update(compound.keys())
    unique_elements = sorted(unique_elements)  

    num_rows = len(unique_elements)  
    num_cols = len(reactants) + len(products)  
    matrix = [[0] * num_cols for _ in range(num_rows)]
    
    for j, compound in enumerate(reactants + products):
        sign = 1 if j < len(reactants) else -1  
        for element, count in compound.items():
            i = unique_elements.index(element)  
            matrix[i][j] = sign * count
    
    return matrix

