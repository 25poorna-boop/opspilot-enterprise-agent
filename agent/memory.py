class SimpleMemory:
    def __init__(self):
        self.store = []

    def save(self, item):
        self.store.append(item)

    def all(self):
        return self.store
