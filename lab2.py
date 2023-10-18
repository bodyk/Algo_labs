def max_hamsters(S, C, hamsters):
    hamsters.sort(key=lambda x: (x[0] + (C-1)*x[1])/x[0])

    count = 0
    for H, G in hamsters:
        required_food = H + count * G
        if S >= required_food:
            count += 1
            S -= required_food
        else:
            break

    return count

S = 7
C = 3
hamsters = [[1, 2], [2, 2], [3, 1]]
print(max_hamsters(S, C, hamsters))