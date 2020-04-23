class BinaryMatrix(object):
    def __init__(self, matrix):
        self.matrix = matrix

    def get(self, x: int, y: int) -> int:
        return self.matrix[x][y]

    def dimensions(self) -> list:
        return [len(self.matrix), len(self.matrix[0])]


# O(n log(m))
def solution_1(binary_matrix: BinaryMatrix) -> int:
    d = binary_matrix.dimensions()
    n = d[0]
    one = m = d[1]

    for i in range(n):
        left = 0
        right = one - 1

        while left <= right:
            mid = (left + right) // 2

            if binary_matrix.get(i, mid) == 0:
                left = mid + 1
            else:
                one = mid
                right = mid - 1

    if one == m:
        return -1
    return one


# O(n + m)
def solution_2(binaryMatrix: BinaryMatrix) -> int:
    d = binaryMatrix.dimensions()
    n = d[0]
    m = d[1]

    i = 0
    j = m - 1

    while i < n and j >= 0:
        if binaryMatrix.get(i, j) == 0:
            i += 1
        else:
            j -= 1

    if j == m - 1:
        return -1
    return j + 1
