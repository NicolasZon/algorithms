"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3
"""


def dfs(grid, i, j):
    if grid[i][j] == '1':
        grid[i][j] = '2'
        if j + 1 < len(grid[0]): dfs(grid, i, j + 1)
        if i + 1 < len(grid): dfs(grid, i + 1, j)
        if j > 0: dfs(grid, i, j - 1)
        if i > 0: dfs(grid, i - 1, j)
        return True
    return False


def num_islands(grid):
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            count += 1 if dfs(grid, i, j) else 0
    return count


grid = [
    ['1', '1', '1', '1', '0'],
    ['1', '1', '0', '1', '0'],
    ['1', '1', '0', '0', '0'],
    ['0', '0', '0', '0', '0'],
]

print(num_islands(grid))

grid = [
    ['1', '1', '0', '0', '0'],
    ['1', '1', '0', '0', '0'],
    ['0', '0', '1', '0', '0'],
    ['0', '0', '0', '1', '1'],
]

print(num_islands(grid))



qww