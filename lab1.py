def traverse_zig_zag(matrix):
    result = []
    row = 0
    column = 0
    m = len(matrix)
    n = len(matrix[0])
    result.append(matrix[row][column])
    while row + 1 < m or column + 1 < n:
        if column + 1 < n:
            column += 1
            result.append(matrix[row][column])
        elif row + 1 < m:
            row += 1
            result.append(matrix[row][column])
        while row + 1 < m and column - 1 >= 0:
            if row + 1 < m:
                row += 1
            if column - 1 >= 0:
                column -= 1
            result.append(matrix[row][column])
        if row + 1 < m:
            row += 1
            result.append(matrix[row][column])
        elif column + 1 < n:
            column += 1
            result.append(matrix[row][column])
        while column + 1 < n and row - 1 >= 0:
            if column + 1 < n:
                column += 1
            if row - 1 >= 0:
                row -= 1
            result.append(matrix[row][column])

    return result

matrix = [
    [1, 2, 6],
    [3, 5, 7],
    [4, 8, 9],
]

matrix = [
    [1, 2, 6, 7, 12],
    [3, 5, 8, 11, 13],
    [4, 9, 10, 14, 15],
]

result = traverse_zig_zag(matrix)
for element in result:
    print(element)