# https: // leetcode.com/problems/set-matrix-zeroes/
# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

# You must do it in place.

# Example 1:
# Input: matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
# Output: [[1, 0, 1], [0, 0, 0], [1, 0, 1]]

# Example 2:
# Input: matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
# Output: [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]

def setZeroes(arr):
    col_count = len(arr[0])
    row_count = len(arr)
    col_0 = 0
    for i in range(row_count):
            if arr[i][0] == 0:
                col_0 = 1
            for j in range(1, col_count):
                if arr[i][j] == 0:
                    arr[i][0] = 0
                    arr[0][j] = 0
    for i in range(row_count-1, -1, -1):
            for j in range(col_count-1, 0, -1):
                if (arr[i][0] == 0 or arr[0][j] == 0):
                    arr[i][j] = 0
    if col_0:
            for i in range(row_count):
                arr[i][0] = 0
