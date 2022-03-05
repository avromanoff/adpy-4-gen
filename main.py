# Написать генератор, который принимает список списков,
# и возвращает их плоское представление.

nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    [1, 2, None],
]


def flat_generator(some_list):
    for x in some_list:
        if type(x) == list:
            for y in x:
                yield y
        else:
            yield x


if __name__ == '__main__':
    for item in flat_generator(nested_list):
        print(item)
