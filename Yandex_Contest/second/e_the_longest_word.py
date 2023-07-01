# Яндекс Контест Задача E. "Самое длинное слово."

num = int(input())
words = input()


words = words.split(' ')
maximum = ''
for word in words:
    if len(word) > len(maximum):
        maximum = word
print(maximum)
print(len(maximum))
