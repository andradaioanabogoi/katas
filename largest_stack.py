class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.items:
            return None
        else:
            return self.items.pop()

    def peek(self):
        if not self.items:
            return None
        else:
            return self.items[-1]


class MaxStack:
    def __init__(self):
        self.stack = Stack()
        self.maxes = Stack()

    def push(self, item):
        self.stack.push(item)

        if self.maxes.peek() is None or item >= self.maxes.peek():
            self.maxes.push(item)

    def pop(self):
        item = self.stack.pop()

        if item == self.maxes.peek():
            self.maxes.pop()
        return item

    def get_max(self):
        return self.maxes.peek()


stack = MaxStack()
stack.push(1)
stack.push(2)
# stack.push(1)
# stack.push(1)

print(stack.get_max())
print(stack.maxes)
