# Яндекс Контест Задача G. "Стек - MaxEffective."

class StackMaxEffective:
    def __init__(self):
        self.items = []
        self.max = []

    def push(self, item):
        if self.items == []:
            self.max.append(item)
        elif item > self.max[len(self.items)-1]:
            self.max.append(item)
        else:
            self.max.append(self.max[len(self.items)-1])
        self.items.append(item)

    def pop(self):
        if self.items == []:
            return print('error')
        self.max.pop()
        return self.items.pop()

    def get_max(self):
        if self.items == []:
            return 'None'
        else:
            return self.max[len(self.items)-1]


stack = StackMaxEffective()
n = int(input())
if n < 100000:
    for _ in range(n):
        cmd = input().split()
        if cmd[0] == 'push':
            stack.push(int(cmd[1]))
        elif cmd[0] == 'pop':
            stack.pop()
        elif cmd[0] == 'get_max':
            print(stack.get_max())
        else:
            break
