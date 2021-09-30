class Sentence:
    def __init__(self, sentence: str):
        self.sentence = sentence.split(sep=' ')
        self.index = 0

    @property
    def get_sentence(self):
        return ' '.join(self.sentence)

    def __iter__(self):
        return self

    def __next__(self):
        current = self.index
        if current >= len(self.sentence):
            self.index = 0  # Resetting index - multiple iterations possible
            raise StopIteration
        self.index += 1
        return self.sentence[current]


def sentence(sentence: str):
    for word in sentence.split(sep=' '):
        yield word


if __name__ == '__main__':
    print('Class solution: ')

    my_sentence = Sentence('This is a test')

    for word in my_sentence:
        print(word)

    print('Second iteration of the same object: ')

    for word in my_sentence:
        print(word)

    print(my_sentence.get_sentence, end='\n\n')

    print('Generator solution: ')

    my_sentence2 = sentence('This is a test')

    for word in my_sentence2:
        print(word)


