# Яндекс Контест Задача L. "Два велосипеда."

def bicycle(money, price, left, right):
    if right <= left:
        return -1
    mid = (left + right) // 2
    if money[mid] >= price and (money[mid - 1] < price or mid == 0):
        return mid + 1
    elif price <= money[mid]:
        return bicycle(money, price, left, mid)
    else:
        return bicycle(money, price, mid+1, right)


right = int(input())
left = 0
money = list(map(int, input().split()))
price = int(input())

print(bicycle(money, price, left, right), end=' ')
print(bicycle(money, price*2, left, right))
