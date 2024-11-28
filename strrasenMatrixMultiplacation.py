#Strassen's Matrix Multiplication Implementation

def strassen_matrix_multiply(first_matrix, second_matrix):
    length = len(first_matrix)
    
    #Pad matrix
    def pad_matrix(matrix):
        next_power_of_2 = 1
        while next_power_of_2 < length:
            next_power_of_2 *= 2
        
        padded = [[0 for _ in range(next_power_of_2)] for _ in range(next_power_of_2)]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                padded[i][j] = matrix[i][j]
        return padded
    
    # Pad matrices if they are not already powers of 2
    if length & (length - 1): 
        first_matrix = pad_matrix(first_matrix)
        second_matrix = pad_matrix(second_matrix)
        length = len(first_matrix)
    
    # Base case
    if length <= 1:
        return [[first_matrix[0][0] * second_matrix[0][0]]]
    
    # Split matrices
    mid = length // 2
    A11 = [row[:mid] for row in first_matrix[:mid]]
    A12 = [row[mid:] for row in first_matrix[:mid]]
    A21 = [row[:mid] for row in first_matrix[mid:]]
    A22 = [row[mid:] for row in first_matrix[mid:]]
    
    B11 = [row[:mid] for row in second_matrix[:mid]]
    B12 = [row[mid:] for row in second_matrix[:mid]]
    B21 = [row[:mid] for row in second_matrix[mid:]]
    B22 = [row[mid:] for row in second_matrix[mid:]]
    
    # Recursively compute products
    P1 = strassen_matrix_multiply(matrix_add(A11, A22), matrix_add(B11, B22))
    P2 = strassen_matrix_multiply(matrix_add(A21, A22), B11)
    P3 = strassen_matrix_multiply(A11, matrix_subtract(B12, B22))
    P4 = strassen_matrix_multiply(A22, matrix_subtract(B21, B11))
    P5 = strassen_matrix_multiply(matrix_add(A11, A12), B22)
    P6 = strassen_matrix_multiply(matrix_subtract(A21, A11), matrix_add(B11, B12))
    P7 = strassen_matrix_multiply(matrix_subtract(A12, A22), matrix_add(B21, B22))
    
    # Compute matric quadrants from above products
    C11 = matrix_add(matrix_subtract(matrix_add(P1, P4), P5), P7)
    C12 = matrix_add(P3, P5)
    C21 = matrix_add(P2, P4)
    C22 = matrix_add(matrix_subtract(matrix_add(P1, P3), P2), P6)
    
    # Combine quadrants
    C = [[0 for _ in range(length)] for _ in range(length)]
    for i in range(mid):
        for j in range(mid):
            C[i][j] = C11[i][j]
            C[i][j + mid] = C12[i][j]
            C[i + mid][j] = C21[i][j]
            C[i + mid][j + mid] = C22[i][j]
    
    # Combibe result for final product (also matrices that were padded will be trimmed to match produce appropriate matrix length and structure)
    return [row[:len(first_matrix) if len(first_matrix) < length else length][:len(second_matrix[0]) if len(second_matrix[0]) < length else length]
            for row in C[:len(first_matrix) if len(first_matrix) < length else length]]

def matrix_subtract(first_matrix, second_matrix):
    return [[first_matrix[i][j] - second_matrix[i][j] for j in range(len(first_matrix[0]))] for i in range(len(first_matrix))]


def matrix_add(first_matrix, second_matrix):
    return [[first_matrix[i][j] + second_matrix[i][j] for j in range(len(first_matrix[0]))] for i in range(len(first_matrix))]

#Standard Matrix multiplication
def standard_matrix_multiplication(first_matrix, second_matrix):
    product = [[0 for _ in range(len(second_matrix[0]))] for _ in range(len(first_matrix))]
    for i in range(len(first_matrix)):
        for j in range(len(second_matrix[0])):
            for k in range(len(second_matrix)):
                product[i][j] += first_matrix[i][k] * second_matrix[k][j]
    return product
  

if __name__ == "__main__":
    a = [
        [25, 2],
        [23, 78]]
    
    b = [
        [100, 56],
        [15, 92]]
    
    #Strassen's multiplication
    strassen_multiplication_result = strassen_matrix_multiply(a, b)
    print("First Matrix:", a)
    print("Second Matrix:", b)
    print("Strassen's Matrix Multiplication Result:", strassen_multiplication_result)
    
    #Standard multiplication
    standard_result = standard_matrix_multiplication(a, b)
    print("Standard Matrix Multiplication Result:", standard_result)
    print("Results Match:", strassen_multiplication_result == standard_result)