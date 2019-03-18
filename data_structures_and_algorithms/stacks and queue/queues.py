class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return self.queue == []

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        data = self.queue[0]
        del self.queue[0]
        return data

    def peek(self):
        return self.queue[0]

    def size_queue(self):
        return len(self.queue)


queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

print("Size of Queue: {}".format(queue.size_queue()))
print("Dequeue: {}".format(queue.dequeue()))
print("Dequeue: {}".format(queue.dequeue()))
print("Size of Queue: {}".format(queue.size_queue()))
