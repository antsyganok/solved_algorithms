from typing import List, Tuple, Optional


def two_sum(arr: List[int], target_sum: int, n: int) -> Optional[Tuple[int, int]]:
    result = []
    for i in range(0, n):
        for j in range(i+1, n):
            if arr[i]+arr[j] == target_sum:
                result.append(arr[i])
                result.append(arr[j])
                return result
    return None


def read_input() -> Tuple[List[int], int]:
    n = int(input())
    arr = list(map(int, input().strip().split()))
    target_sum = int(input())
    return arr, target_sum, n


def print_result(result: Optional[Tuple[int, int]]) -> None:
    if result is None:
        print(None)
    else:
        print(" ".join(map(str, result)))


arr, target_sum, n = read_input()
print_result(two_sum(arr, target_sum, n))
