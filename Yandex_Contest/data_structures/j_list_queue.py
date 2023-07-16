# Яндекс Контест Задача J. "Списочная очередь."

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def get(self):
        if self.head is None:
            return 'error'
        tmp = self.head
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        self.count -= 1
        return tmp.value

    def put(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.count += 1

    def size(self):
        return self.count


if __name__ == '__main__':
    n = int(input())
    ll = LinkedList()
    if n < 1000:
        for _ in range(n):
            cmd = input().split()
            if cmd[0] == 'put':
                ll.put(int(cmd[1]))
            elif cmd[0] == 'get':
                print(ll.get())
            elif cmd[0] == 'size':
                print(ll.size())
            else:
                break
