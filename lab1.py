def traverse_zig_zag(matrix):
    result = []
    row = 0
    column = 0
    m = len(matrix)
    if m == 0:
        return result
    n = len(matrix[0])
    if n == 0:
        return result
    
    # Append first element
    result.append(matrix[row][column])
    while row + 1 < m or column + 1 < n:
        # Try move right
        if column + 1 < n:
            column += 1
            result.append(matrix[row][column])
        # We reached right side, move down
        elif row + 1 < m:
            row += 1
            result.append(matrix[row][column])

        #ZigZag downwards
        while row + 1 < m and column - 1 >= 0:
            if row + 1 < m:
                row += 1
            if column - 1 >= 0:
                column -= 1
            result.append(matrix[row][column])
        # Try move down
        if row + 1 < m:
            row += 1
            result.append(matrix[row][column])
        # We reached bottom side, move right
        elif column + 1 < n:
            column += 1
            result.append(matrix[row][column])

        #ZigZag upwards
        while column + 1 < n and row - 1 >= 0:
            if column + 1 < n:
                column += 1
            if row - 1 >= 0:
                row -= 1
            result.append(matrix[row][column])

    return result