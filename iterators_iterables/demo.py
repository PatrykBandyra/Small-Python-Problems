def for_loop_as_while_loop():
    nums = [1, 2, 3]
    for num in nums:
        print(num)

    i_nums = iter(nums)
    while True:
        try:
            item = next(i_nums)
            print(item)
        except StopIteration:
            break


# Both iterable and iterator
class MyRange:
    def __init__(self, start, end):
        self.value = start
        self.end = end

    def __iter__(self):
        return self  # Returns iterator

    def __next__(self):
        if self.value >= self.end:
            raise StopIteration
        current = self.value
        self.value += 1
        return current


def test_my_range_class():
    nums = MyRange(1, 5)
    for num in nums:
        print(num)

    nums2 = MyRange(5, 10)
    print(next(nums2))
    print(next(nums2))
    print(next(nums2))
    print(next(nums2))


# Generator
def my_range_generator(start, end):
    current = start
    while current < end:
        yield current  # Returns generator
        current += 1


def test_my_range_generator():
    nums = my_range_generator(1, 5)
    for num in nums:
        print(num)

    nums2 = my_range_generator(5, 10)
    print(next(nums2))
    print(next(nums2))
    print(next(nums2))
    print(next(nums2))


if __name__ == '__main__':
    # for_loop_as_while_loop()
    # test_my_range_class()
    test_my_range_generator()
