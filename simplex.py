#Projeto de Otimização 1 - PPL(Python)
#Letícia Vitória Merss Moreira
#GES
#56

import numpy as np

pivot_vector = []

def matrix_scaling(matrix, pivot_row, pivot_col):

    pivot = float(matrix[pivot_row][pivot_col])

    for i in range(len(matrix)):

        if matrix[i][pivot_col] == 0:
            continue

        if i != pivot_row:

            first_calculation = pivot * matrix[i]
            second_calculation = matrix[i][pivot_col] * matrix[pivot_row]
            result = first_calculation - second_calculation
            matrix[i] = result

    return matrix, pivot

def change_base_column(matrix, index_new_column):
    column_B = matrix[:, -1][:-1]
    new_column_base = matrix[:, index_new_column][:-1]

    if len(np.where(new_column_base <= 0)) == 0:
        column_B = np.where(new_column_base <= 0, 0, column_B)
        new_column_base = np.where(column_B <= 0, 1, new_column_base)

    division = column_B / new_column_base
    lowest = max(division)
    lowest_index = 0
    for index, i in enumerate(division):
        if i > 0:
            if i < lowest:
                lowest = i
                lowest_index = index

    pivot_row = lowest_index
    pivot_col = index_new_column

    matrix, pivot = matrix_scaling(matrix, pivot_row, pivot_col)
    return matrix, pivot


def identity_matrix(matrix, matrix_restrictions, vetor_b, vetor_c):
    num_restrictions = len(matrix) - 1
    matrix_identify = np.identity(num_restrictions, dtype=float)
    matrix_normalizeted_aux = []

    for i in range(num_restrictions):
        row_normalized = np.append(matrix_restrictions[i], matrix_identify[i])
        row_normalized = np.append(row_normalized, vetor_b[i])
        matrix_normalizeted_aux.append(row_normalized)

    aux_vector_zeros = np.zeros(num_restrictions)
    row_normalized = np.append(vetor_c, aux_vector_zeros)
    matrix_normalizeted_aux.append(row_normalized)

    final_matrix = []
    cont = 0
    aux = []
    for i in range(len(matrix_normalizeted_aux)):
        for j in range(len(matrix_normalizeted_aux[0])):
            if cont == len(matrix_normalizeted_aux[0]) - 1:
                aux.append(matrix_normalizeted_aux[i][j])
                final_matrix.append(aux)
                cont = 0
                aux = []
            else:
                aux.append(matrix_normalizeted_aux[i][j])
                cont += 1
    return final_matrix


def search_var_values(matrix, is_max):
    variables = 'abcdefghijklmnopqrstuvwxyz'
    aux = int(len(matrix[0]) - 1)
    variables = variables[:aux]
    result = ''
    for i in range(len(matrix[0]) - 1):
        if matrix[-1][i] == 0:

            pivot = np.where(matrix[:, i] > 0)
            pivot_index = pivot[0][0]
            if matrix[pivot_index][i] < 1:
                aux = 1 - matrix[pivot_index][i]

                num_inteiro = matrix[pivot_index][i] + aux
                (1 / aux) * matrix[pivot_index][-1]

                result += str(num_inteiro) + variables[i] + ' = ' + str(
                    (1 / matrix[pivot_index][i]) * matrix[pivot_index][-1]) + '\n'
            else:
                result += str(matrix[pivot_index][i]) + variables[i] + ' = ' + str(matrix[pivot_index][-1]) + '\n'

        else:
            result += str(variables[i] + ' = 0\n')
    if is_max:
        print(matrix)
        func_z = matrix[-1][-1] * -1
        result += '\n'
        result += 'A melhor solução de Z: ' + str(func_z) + '\n\n'
        #Exemplo Ex Chapas metalicas
        '''
        result += 'Preço sombra de x: ' + str((matrix[2][3]) * -1) + '\n'
        result += 'Preço sombra de y: ' + str((matrix[2][4]) * -1) + '\n'
        '''
        #Exemplo Empresa Venix
        '''
        result += 'Preço sombra de w: ' + str((matrix[3][2]) * -1) + '\n'
        result += 'Preço sombra de x: ' + str((matrix[3][3]) * -1) + '\n'
        result += 'Preço sombra de y: ' + str((matrix[3][4]) * -1) + '\n'
        '''
    else:
        result += 'A melhor solução de Z: ' + str(matrix[-1][-1])

    result += '\n\nOBS: Caso queira executar outro problema, feche está aba e execute novamente o programa.'

    return result


def search_better(matrix, is_max, start=True):
    global pivot_vector

    if start == True:

        matrix = np.array(matrix)
        matrix = matrix.astype('float')

        matrix = np.array(identity_matrix(matrix, matrix[:-1][:, :-1], matrix[:-1][:, -1], matrix[-1]))
        if is_max == False:
            aux = matrix[-1:] *-1
            matrix[-1:] = aux

    bigger_value = max(matrix[-1][:])
    if bigger_value >= 1:
        index_highest_value = np.argmax(matrix[-1][:-1])
        matrix, pivot = change_base_column(matrix, index_highest_value)
        pivot_vector.append(pivot)
        return search_better(matrix, is_max, start=False)

    else:
        for i in pivot_vector:
            matrix = matrix / i

        aux3 = search_var_values(matrix, is_max)

    return aux3