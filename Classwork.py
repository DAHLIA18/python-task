numbers = [11, 9, 5, 30, 39, 36, 15, 49, 36, 29]


def list_length(numbers):
    result = 1
    for i in numbers:
        result += 1
    return result


def even_positions(numbers):
    result = 0
    for i in numbers:
        if i % 2 == 0:
            result += i
    return result


def odd_positions(numbers):
    result = 0
    for i in numbers:
        if i % 2 == 1:
            result += i
        return result


def multiply_third_position(numbers):
    return


def get_average(numbers):
    return sum(numbers) / len(numbers)


def get_largest(numbers):
    largest = numbers[0]
    for element in numbers:
        if element > largest:
            largest = element
    return largest


def get_smallest(numbers):
    smallest = numbers[0]
    for value in numbers:
        if value < smallest:
            smallest = value
        return smallest


def get_number_of_strings(words):
    result = []
    for string in words:
        length = len(string)
        if len(words) >= 2 and words[0] == words[-1]:
            result.append(words)
        return result

print(even_positions(numbers))
print(odd_positions(numbers))
print(multiply_third_position(numbers))
print(get_average(numbers))
print(get_largest(numbers))
print(get_number_of_strings(numbers))


