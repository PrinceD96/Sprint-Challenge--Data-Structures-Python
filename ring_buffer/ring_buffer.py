class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []
        self.oldest = 0

    def append(self, item):
        # if buffer is full,
        # overwrite the oldest item with the new one
        if len(self.data) == self.capacity:
            self.data[self.oldest] = item
        else:
            self.data.append(item)
        self.update_oldest()

    def get(self):
        return self.data

    def update_oldest(self):
        if self.oldest + 1 < self.capacity:
            self.oldest += 1
        else:
            self.oldest = 0
