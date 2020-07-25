class countdown_iterator:
    def __init__(self, count):
        self.count = count
        self.end_count = 0

    def __iter__(self):
        return self

    def __next__(self):
        current_num = self.count
        if self.count >= self.end_count:
            self.count -= 1
            return current_num
        raise StopIteration()


iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")
