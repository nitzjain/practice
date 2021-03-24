class Queue():

    def __init__(self):
        self.items = []

    def enqueue(self,item):
        return self.items.append((item))

    def dequeue(self):
        return self.items.remove(self.items[0])

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def printq(self):
        return self.items


q = Queue()
print(q.isEmpty())
print(q.enqueue(11))
print(q.enqueue(22))
print(q.size())
print(q.dequeue())
print(q.size())
print(q.printq())
print(q.isEmpty())

