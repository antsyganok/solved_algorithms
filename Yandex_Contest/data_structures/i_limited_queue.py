# Яндекс Контест Задача I. "Ограниченная очередь."

class MyQueueSized:
    def __init__(self, n, max_size):
        self.queue = [None] * n
        self.max_n = max_size
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def push(self, x):
        if self.size != self.max_n:
            self.queue[self.tail] = x
            self.tail = (self.tail + 1) % self.max_n
            self.size += 1
        else:
            return print('error')

    def peek(self):
        if self.is_empty():
            return None
        return self.queue[self.head]

    def pop(self):
        if self.is_empty():
            return None
        x = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_n
        self.size -= 1
        return x


if __name__ == '__main__':
    n = int(input())
    max_size = int(input())
    q = MyQueueSized(n, max_size)
    if n < 5000:
        for _ in range(n):
            cmd = input().split()
            if cmd[0] == 'push':
                q.push(int(cmd[1]))
            elif cmd[0] == 'pop':
                print(q.pop())
            elif cmd[0] == 'size':
                print(q.size)
            elif cmd[0] == 'peek':
                print(q.peek())
            else:
                break
