import numpy


def gauss_method(equation_system):
    zero_control_sum = finding_first_sum(equation_system)
    zero_matrix = adding_control_sum(equation_system, zero_control_sum)
    zero_step = adding_control_sum(zero_matrix, zero_control_sum)

    first_matrix = calculating_first_matrix(zero_matrix)
    first_sum = finding_next_sum(first_matrix)

    first_step = adding_control_sum(first_matrix, first_sum)
    first_step = inserting_empty_column(first_step)

    matrix_viewing(zero_step)
    print("{:-^101s}".format(""))
    matrix_viewing(first_step)
    print("{:-^101s}".format(""))

    previous_matrix = first_matrix.copy()
    first_row = [previous_matrix[0][:-2]]
    free_member = [previous_matrix[0][-2]]

    for i in range(len(previous_matrix) - 1):
        next_matrix = calculating_next_matrix(previous_matrix)
        next_control_sum = finding_next_sum(next_matrix)
        next_step = adding_control_sum(next_matrix, next_control_sum)

        for j in range(i + 2):
            if j == 0:
                next_step = inserting_empty_column(next_step)
            else:
                next_step = inserting_zero_column(next_step)

        matrix_viewing(next_step)
        print("{:-^101s}".format(""))

        previous_matrix = next_matrix.copy()
        first_row.append(previous_matrix[0][:-2])
        free_member.append(previous_matrix[0][-2])

    first_rows = numpy.array(matrix_for_solving(first_row))
    free_members = numpy.array(free_member)
    res = numpy.linalg.solve(first_rows, free_members)

    result = res.tolist()

    for n in range(len(result)):
        print("x{:.0f} ={:10.5f}".format(n + 1, round(result[n], 5)))


def finding_first_sum(matrix):
    control_sum = []
    for i in range(len(matrix)):
        control_sum.append(round(sum(matrix[i]), 5))
    return control_sum


def finding_next_sum(matrix):
    control_sum = []
    for i in range(len(matrix)):
        if i == 0:
            control_sum.append(round(sum(matrix[i][:-1]), 5) + 1)
        else:
            control_sum.append(round(sum(matrix[i][:-1]), 5))
    return control_sum


def calculating_first_matrix(matrix):
    new_matrix = []
    for i in range(len(matrix)):
        temp = []
        for j in range(1, len(matrix[i])):
            if i == 0:
                new_element = matrix[0][j] / matrix[0][0]
                temp.append(round(new_element, 5))
            else:
                new_element = matrix[i][j] - new_matrix[0][j-1] * matrix[i][0]
                temp.append(round(new_element, 5))
        new_matrix.append(temp)
    return new_matrix


def calculating_next_matrix(matrix):
    new_matrix = []
    for i in range(1, len(matrix)):
        temp = []
        for j in range(1, len(matrix[i])):
            if i == 1:
                new_element = matrix[i][j] / matrix[i][0]
                temp.append(round(new_element, 5))
            else:
                new_element = matrix[i][j] - new_matrix[0][j-1] * matrix[i][0]
                temp.append(round(new_element, 5))
        new_matrix.append(temp)
    return new_matrix


def matrix_viewing(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if j == len(matrix[i]) - 1:
                print("{:12.5f}".format(matrix[i][j]))
            else:
                print("{:12.5f}".format(matrix[i][j]), end='')


def adding_control_sum(matrix, control_sum):
    new_matrix = []
    for i in matrix:
        new_matrix.append(i[:])

    for j in range(len(new_matrix)):
        new_matrix[j].append(control_sum[j])
    return new_matrix


def inserting_empty_column(matrix):
    new_matrix = []
    for i in matrix:
        new_matrix.append(i[:])

    for j in range(len(new_matrix)):
        if j == 0:
            new_matrix[j].insert(0, 1)
        else:
            new_matrix[j].insert(0, 0)
    return new_matrix


def inserting_zero_column(matrix):
    new_matrix = []
    for i in matrix:
        new_matrix.append(i[:])

    for j in range(len(new_matrix)):
        new_matrix[j].insert(0, 0)
    return new_matrix


def matrix_for_solving(matrix):
    new_matrix = []
    for i in matrix:
        new_matrix.append(i[:])

    for k in range(len(new_matrix)):
        new_matrix[k].insert(0, 1)

    for j in range(len(new_matrix)):
        while len(new_matrix[j]) != len(new_matrix):
            new_matrix[j].insert(0, 0)
    return new_matrix


gauss_method([  [17, -5.6, 4, -8.3, 3.2, 64],
                [4, -12.2, -6.5, 7, 1.4, 12.45],
                [-5, 9.6, -15.3, 2.3, 1.1, 16.9],
                [3.9, 5.6, 2.4, -13, 2.4, 21.4],
                [4.3, 2.7, -6.3, 3.5, 10, 9.7]])