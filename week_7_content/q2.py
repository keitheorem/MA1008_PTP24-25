# A matrix can be represented in Python using a list of lists. The elements of the lists would be the row
# values, and the elements of the nested lists would be the column values. Write a program that takes
# the list [[1, 2, 3], [4, 5, 6], [7, 8, 9]] and prints it out as a 3x3 matrix. Also print
# its transpose.

matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]

for row in matrix:
    print(row)

empty_matrix = [[0,0,0],
                [0,0,0],
                [0,0,0]]

no_of_row = 3
no_of_column = 3

for i in range(no_of_row):
    for j in range(no_of_column):
        empty_matrix[i][j] = matrix[j][i]

for row in empty_matrix:
    print(row)