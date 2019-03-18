class Stack(object):
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return self.stack == []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        data = self.stack[-1]
        del self.stack[-1]
        return data

    def peek(self):
        return self.stack[-1]

    def size_stack(self):
        return len(self.stack)

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print("Size: {}".format(stack.size_stack()))
print("Popped: {}".format(stack.pop()))
print("Popped: {}".format(stack.pop()))
print("Size: {}".format(stack.size_stack()))
print("Peek: {}".format(stack.peek()))
print("Size: {}".format(stack.size_stack()))
