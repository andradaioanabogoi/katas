class QueueTwoStacks(object):
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def enqueue(self, item):
        self.in_stack.append(item)

    def dequeue(self):
        if len(self.out_stack) == 0:

            while len(self.in_stack) > 0:
                newest_in_stack_item = self.in_stack.pop()
                self.out_stack.append(newest_in_stack_item)

            if(len(self.out_stack) == 0):
                raise("Empty queue")

        return self.out_stack.pop()


queue = QueueTwoStacks()
queue.enqueue(1)
queue.enqueue(2)
queue.dequeue()
# queue.enqueue(1)

print(queue.in_stack)
