"""
Construct a square matrix with a size N × N containing integers from 1 to N * N in a spiral order,
starting from top-left and in clockwise direction.

Example

For n = 3, the output should be
spiralNumbers(n) = [[1, 2, 3],
                    [8, 9, 4],
                    [7, 6, 5]]
"""
def spiralNumbers(n):
    m = [[0 for _ in range(n)] for _ in range(n)]
    maxn = n * n
    i, j = 0, 0
    mini, minj = 0, 0
    maxi, maxj = n - 1, n - 1
    n = 0
    d = 'R'

    while n < maxn:
        n += 1
        m[i][j] = n

        if d == 'R':
            if j + 1 > maxj:
                mini += 1
                i += 1
                d = 'D'
            else:
                j += 1

        elif d == 'D':
            if i + 1 > maxi:
                maxj -= 1
                j -= 1
                d = 'L'
            else:
                i += 1

        elif d == 'L':
            if j - 1 < minj:
                maxi -= 1
                i -= 1
                d = 'U'
            else:
                j -= 1

        elif d == 'U':
            if i - 1 < mini:
                minj += 1
                j += 1
                d = 'R'

            else:
                i -= 1
    return m

print(spiralNumbers(3))