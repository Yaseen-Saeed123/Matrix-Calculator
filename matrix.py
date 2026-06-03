# This is a Calculator Dealing with matrix algebra
import numpy as np
import time as t
def create_matrix(rows,cols, type_mat=None):
    elements = rows * cols
    if type_mat == "zero":
        matrix = np.zeros((rows, cols))
    elif type_mat == "ones":
        matrix = np.ones((rows, cols))
    elif type_mat == "identity":
        if rows != cols:
            return False, "Identity Matrix Must Be Square"
        matrix = np.eye(rows)
    elif type_mat == "constant":
        while True:
            try:
                no= int(input("Enter the constant: ").strip())
                print("-"*30)
                break
            except ValueError:
                print("-"*30)
                print("Not Valid\n"+"-"*30)
        matrix = np.full((rows, cols), no)
    else:
        matrix = [[0 for j in range(cols)] for i in range(rows)]
        print("Let's Add elements for your Matrix")
        print("-"*30)
        for i in range(rows):
            for j in range(cols):
                while True:
                    try:
                        x= int(input("=> ").strip())
                        print("-"*30)
                        matrix[i][j] = x
                        break
                    except ValueError:
                        print("-"*30)
                        print("Not Valid")
                        print("-"*30)
        matrix = np.array(matrix)
    return matrix
def add_and_subtract_matricies(A, B, op="add"):
    if A.shape != B.shape:
        return False, "Addition or Subtraction requires the same shape"
    if op == "sub":
        result_mat = A - B
    else:
        result_mat = A + B
    return result_mat
def multiply_matrices(A, B):
    if A.shape[1] != B.shape[0]:
        return False, "The number of columns of 1st matrix must be equal to 2nd matrix"
    result_mat = A @ B
    return result_mat
def transpose(A):
    transpose_A = A.T
    return transpose_A
def determinant(A):
    if A.shape[0] != A.shape[1]:
        return False, "Error: Matrix should be perfectly square"
    det = round(np.linalg.det(A), 4)
    return det
def multiplicative_inverse(A):
    if A.shape[0] != A.shape[1] or round(determinant(A), 4) == 0:
        return False, "Error: This is a singular Matrix. Inversion require perfectly square matrix and its determinant not equal 0"
    result_mat = np.linalg.inv(A)
    return result_mat
def scalar_multiplication(A, x):
    resulted_mat = A * x
    return resulted_mat
def find_an_element(X, row, col):
    if row <= 0 or col <=0 or row > X.shape[0] or col > X.shape[1]:
        return False, "Element Out of Bounds"
    element = X[row-1, col-1]
    return element
def check(ans):
    if isinstance(ans, tuple):
        return False, f"Math Error: {ans[1]}"
    else:
        return True, ans
# Main Program Logic
my_matrices = {}
my_op = ["Create",
         "View",
        "Delete",
        "Clear",
        "Add", 
        "Subtract", 
        "Multiply", 
        "Scalar", 
        "Find",
        "Multiplicative inverse",
        "Determinant",
        "Transpose",
        "Quit"]
print("-"*30 + "\nWelcome to our Matrix Algebra Calculator\n" + "-"*30)
while True:
    for op in my_op:
        print(op+" "+"| " , end="")
    print("\n"+"-"*30)
    while True:
        operation = input("=> ").strip().capitalize()
        print("-"*30)
        if operation not in my_op:
            print("Not a Valid input\n" + "-"*30)
            continue
        if operation not in my_op[:3] and len(list(my_matrices.keys())) == 0 and operation != "Quit":
            print(f"You have no matrices to start {operation}\n" + "-"*30)
            continue
        if operation in ["Add", "Subtract", "Multiply"] and len(list(my_matrices.keys())) < 2:
            print(f"You must have at least two matrices to start {operation}\n" + "-"*30)
            continue
        break
    if operation in ['Create', "View", "Delete", "Clear","Quit"]:
        match operation:
            case "Create":
                # Get name
                while True:
                    name = input("Enter the name of your matrix: ").strip().upper()
                    print("-"*30)
                    if len(name) != 1:
                        print("Not a Valid Matrix name\n"+"-"*30)
                        continue
                    if name in list(my_matrices.keys()):
                        print("Already existing\n"+"-"*30)
                        continue
                    break
                # Get shape
                while True:
                    shape = input("Enter the shape of your matrix:(rxc) ").strip().lower()
                    print("-"*30)
                    parts = shape.split('x')
                    if parts[0].isdigit() and parts[1].isdigit() and len(parts) == 2:
                        rows = int(parts[0])
                        cols = int(parts[1])
                        if rows < 1 or cols < 1:
                            print("Not a valid Matrix Shape\n"+"-"*30)
                            continue
                        break
                    else:
                        print("Not a Valid Matrix shape\n"+"-"*30)
                        continue
                # Get Certain matrix type
                while True:
                    types = ['zero', 'ones', 'identity', 'constant', 'custom']
                    for my_type in types:
                        print(my_type + " "+ "| ", end="")
                    print("\n"+"-"*30)
                    type_mat = input("=> ").strip().lower()
                    print("-"*30)
                    if type_mat not in types:
                        print("Not a Valid Matrix Type\n"+"-"*30)
                        continue
                    else:
                        if type_mat == "zero":
                            my_mat = create_matrix(rows, cols, "zero")
                        elif type_mat == "ones":
                            my_mat = create_matrix(rows, cols, "ones")
                        elif type_mat == "identity":
                            my_mat = create_matrix(rows, cols, "identity")
                        elif type_mat == "constant":
                            my_mat = create_matrix(rows, cols, "constant")
                        else:
                            my_mat = create_matrix(rows, cols)
                    is_true, result = check(my_mat)
                    if not is_true:
                        print(result+"\n" + "-"*30)
                        break
                    else:
                        print("Matrix Created successfully\n"+"-"*30)
                        break
                # Store the result in my matrices
                my_matrices[name] = result
            case "View":
                while True:
                    if len(list(my_matrices.keys())) == 0:
                        print("You haven't got any matrices in memory\n"+"-"*30)
                        break
                    else:
                        mat = input("Type the name of the matrix you want to view:- ").strip().upper()
                        print("-"*30)
                        if mat not in list(my_matrices.keys()):
                            print("Not an Existing Matrix\n"+"-"*30)
                            continue
                        else:
                            result = my_matrices[mat]
                            print(f"""{mat} =\n{result}""")
                            print("-"*30)
                            break
            case "Delete":
                while True:
                    mat = input("Type the name of the matrix you want to delete:- ").strip().upper()
                    print("-"*30)
                    if mat not in list(my_matrices.keys()):
                        print("Not an Existing Matrix\n"+"-"*30)
                        continue
                    break
                del my_matrices[mat]
                print(f"Matrix {mat} was successfully deleted\n"+"-"*30)
            case "Clear":
                my_matrices.clear()
                print("You haven't got any matrices in memory\n"+"-"*30)
            case "Quit":
                print("Shutting down ...\n"+"-"*30)
                t.sleep(1)
                break
    elif operation in ["Scalar", "Find","Multiplicative inverse","Determinant","Transpose"]:
        while True:
            mat = input("Enter the matrix name: ").strip().upper()
            print("-"*30)
            if mat not in list(my_matrices.keys()):
                print("Not an Existing Matrix\n"+"-"*30)
                continue
            break
        match operation:
            case "Multiplicative inverse":
                ans = multiplicative_inverse(my_matrices[mat])
                expr = f"{mat}\u207b\u00b9 =\n{ans}"
            case "Find":
                position = []
                corr = ["row", "column"]
                for i in range(2):
                    while True:
                        try:
                            const = int(input(f"Enter the {corr[i]} of the element: ").strip())
                            print("-"*30)
                            position.append(const)
                            break
                        except ValueError:
                            print("-"*30 + "\nNot A Valid Number\n"+"-"*30)
                ans = find_an_element(my_matrices[mat], position[0], position[1])
                expr = f"Element in matrix {mat} in {position[0]}th row and {position[1]}th column =\n{ans}"
            case "Scalar":
                while True:
                    try:
                        const = int(input("Enter the constant: ").strip())
                        print("-"*30)
                        break
                    except ValueError:
                        print("-"*30 + "\nNot A Valid Number\n"+"-"*30)
                ans = scalar_multiplication(my_matrices[mat], const)
                expr = f"{const}{mat} =\n{ans}"
            case "Determinant":
                ans = determinant(my_matrices[mat])
                expr = f"|{mat}| =\n{ans}"
            case "Transpose":
                ans = transpose(my_matrices[mat])
                expr = f"{mat}ᵀ =\n{ans}"
        is_true, result = check(ans)
        if is_true:
            print(expr+"\n"+"-"*30)
        else:
            print(result+"\n"+"-"*30)
    
    elif operation in ["Add", "Subtract", "Multiply"]:
        mats = []
        for i in range(2):
            while True:
                mat = input(f"Enter Mat #{i+1} for {operation}: ").strip().upper()
                print("-"*30)
                if mat not in list(my_matrices.keys()):
                    print("Not an Existing Matrix\n"+"-"*30)
                    continue
                mats.append(mat)
                break
        match operation:
            case "Add":
                ans = add_and_subtract_matricies(my_matrices[mats[0]],my_matrices[mats[1]])
                expr = f"{mats[0]} + {mats[1]} =\n{ans}"
            case "Subtract":
                ans = add_and_subtract_matricies(my_matrices[mats[0]],my_matrices[mats[1]], op="sub")
                expr = f"{mats[0]} - {mats[1]} =\n{ans}"
            case "Multiply":
                ans = multiply_matrices(my_matrices[mats[0]],my_matrices[mats[1]])
                expr = f"{mats[0]}{mats[1]} =\n{ans}"
        is_true, result = check(ans)
        if is_true:
            print(expr+"\n"+"-"*30)
        else:
            print(result+"\n"+"-"*30)