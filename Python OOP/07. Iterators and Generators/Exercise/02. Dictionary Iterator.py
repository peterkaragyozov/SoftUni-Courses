class dictionary_iter:
    def __init__(self, dictionary):
        self.dictionary = dictionary
        self.length = len(self.dictionary)
        self.keys = list(self.dictionary.keys())
        self.current_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index < self.length:
            key = self.keys[self.current_index]
            value = self.dictionary[key]
            self.current_index += 1
            return key, value
        raise StopIteration()


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
