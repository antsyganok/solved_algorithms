# Яндекс Контест Задача C. "Соседи."

from typing import List, Tuple


def get_neighbours(
        n: int, m: int, matrix: List[List[int]], row: int, col: int
        ) -> List[int]:
    lst = []
    if col < m-1:
        lst.append(matrix[row][col+1])  # top

    if col > 0:
        lst.append(matrix[row][col-1])  # bottom

    if row > 0:
        lst.append(matrix[row-1][col])  # right

    if row < n-1:
        lst.append(matrix[row+1][col])  # left

    return sorted(lst)


def read_input() -> Tuple[int, int, List[List[int]], int, int]:
    n = int(input())
    m = int(input())
    matrix = []
    for i in range(n):
        matrix.append(list(map(int, input().strip().split())))
    row = int(input())
    col = int(input())
    return n, m, matrix, row, col


n, m, matrix, row, col = read_input()
print(" ".join(map(str, get_neighbours(n, m, matrix, row, col))))
