class Heaps:
    def __init__(self, max_size):
        self.max_size = max_size
        self.data = []
        self.heap_size = 0
    
    def is_full(self):
        return self.heap_size == self.max_size

    def is_empty(self):
        return self.heap_size == 0
    
    def 