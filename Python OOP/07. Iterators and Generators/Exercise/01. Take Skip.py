class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.current_number = 0
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < self.count:
            temp = self.current_number
            self.counter += 1
            self.current_number += self.step
            return temp
        raise StopIteration()


numbers = take_skip(2, 6)
for number in numbers:
    print(number)

numbers = take_skip(10, 5)
for number in numbers:
    print(number)
