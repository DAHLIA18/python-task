def main_class():

    def construct_sequential_list():
        return list(range(1, 16))


def duplicate_elements(lst):
    return [item for item in lst for _ in range(2)]


def eliminate_duplicates(lst):
    return list(set(lst))


def add_every_third(lst):
    return sum(lst[2::3])


def sum_first_middle_last(lst):
    length = len(lst)
    middle_index = length // 2
    if length % 2 == 0:
        middle_sum = (lst[middle_index - 1] + lst[middle_index]) / 2
    else:
        middle_sum = lst[middle_index]
    return lst[0] + middle_sum + lst[-1]


def collect_unique_numbers():
    numbers = set()
    while len(numbers) < 10:
        num = int(input("Enter a number: "))
        numbers.add(num)
    return list(numbers)


def sum_collection(my_set):
    return sum(my_set)


def remove_item(my_set, number):
    if number in my_set:
        my_set.remove(number)
        return number
    else:
        return None


def find_intersection(set1, set2):
    return set1.intersection(set2)