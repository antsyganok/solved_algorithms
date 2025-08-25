"""
Ещё одно интересное решение задачи с линейным поиском.
"""

nums = enumerate(input().split(), 1)
lost = input()

for idx, num in nums:
    if num == lost:
        print(idx)
        break
else:
    print('ErrorValue')
