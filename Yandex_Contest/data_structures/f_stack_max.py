# Яндекс Контест Задача F. "Стек - Max."

class StackMax:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.items == []:
            return print('error')
        return self.items.pop()

    def get_max(self):
        if self.items == []:
            return 'None'
        elif len(self.items) == 1:
            return self.items[0]
        else:
            return max(list(map(int, self.items)))


stack = StackMax()
n = int(input())
if n < 10000:
    for _ in range(n):
        cmd = input().split()
        if cmd[0] == 'push':
            stack.push(cmd[1])
        elif cmd[0] == 'pop':
            stack.pop()
        elif cmd[0] == 'get_max':
            print(stack.get_max())
        else:
            print(f'{cmd} - Веведёный оператор не распознан.')
else:
    print('Количество команд не должно превышать 10000')
