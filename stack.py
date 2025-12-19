class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0


if __name__ == "__main__":
    stack = Stack()
    stack.push(10)
    stack.push(20)
    print(stack.pop())
