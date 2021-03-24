class Queue2stacks(object):
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self,element):
        self.stack1.append(element)
        return self.stack1

    def dequeue(self):
        if len(self.stack1) == len(self.stack2) == 0:
            return "Queue is empty"
        else:
            for x in self.stack1:
                if self.stack1.index(x) == 0:
                    self.stack1.pop(0)
                    for y in range(1,len(self.stack2)):
                        self.stack1.append(self.stack2[len(self.stack2)-y])
                    self.stack2 = []
                else:
                        self.stack2.append(x)
        return self.stack1


q = Queue2stacks()
print(q.enqueue(1))
print(q.enqueue(2))
print(q.enqueue(3))
print(q.dequeue())
print(q.dequeue())

