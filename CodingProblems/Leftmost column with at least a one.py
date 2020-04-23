"""
A binary matrix means that all elements are 0 or 1. For each individual row of the matrix, this row is sorted in non-decreasing order.

Given a row-sorted binary matrix binaryMatrix, return leftmost column index(0-indexed) with at least a 1 in it. If such index doesn't exist, return -1.

You can't access the Binary Matrix directly.  You may only access the matrix using a BinaryMatrix interface:

BinaryMatrix.get(row, col) returns the element of the matrix at index (row, col) (0-indexed).
BinaryMatrix.dimensions() returns a list of 2 elements [rows, cols], which means the matrix is rows * cols.
Submissions making more than 1000 calls to BinaryMatrix.get will be judged Wrong Answer.  Also, any solutions that attempt to circumvent the judge will result in disqualification.

For custom testing purposes you're given the binary matrix mat as input in the following four examples. You will not have access the binary matrix directly.
"""


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
