class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        if not self.items:
            return True

    def push_item(self, data):
        self.items.append(data)

    def pop_item(self):
        return self.items.pop()

    def top_item(self):
        return self.items[len(self.items) - 1]

    def length(self):
        return len(self.items)

