matrix = [[0, 1, 2],
          [3, 4, 5],
          [6, 7, 8],
          [9, 10, 11]]

rows = len(matrix)  # no of rows is no of sublists i.e. len of list
cols = len(matrix[0])

print("rows",rows)  # no of cols is len of sublist
print("cols",cols)  # no of cols is len of sublist

# printing matrix
print("matrix: ")
for i in range(0, rows):
    print(matrix[i])

# accessing the element on row 2 and column 1 i.e. 3
print("element on row 2 and column 1: ", matrix[1][0])

# accessing the element on row 3 and column 2 i.e. 7
print("element on row 3 and column 2: ", matrix[2][1])

