import math


def confirm(no):
    while True:
        try:
            no = float(no)
            return no
        except ValueError:
            no = input(f"Invalid input ... replace {no} with a digit or decimal: ")


def get_numbers():
    numbers = input("Enter numbers seperated by a space: ").split()
    while True:
        if numbers:
            for i in range(len(numbers)):
                numbers[i] = confirm(numbers[i])
            break
        else:
            print("---------- You must enter a set of numbers! ----------")
            numbers = input("Enter numbers seperated by a space: ").split()

    return numbers


def find_min(numbers):
    minimum = numbers[0]
    for i in range(1, len(numbers)):
        if numbers[i] < minimum:
            minimum = numbers[i]
    return minimum


def find_max(numbers):
    maximum = numbers[0]
    for i in range(1, len(numbers)):
        if numbers[i] > maximum:
            maximum = numbers[i]
    return maximum


def find_mean(numbers):
    total = 0
    for number in numbers:
        total += number
    return total / len(numbers)


def find_mode(numbers):

    hash_table = dict()
    mode = None
    flag = False

    for number in numbers:
        if hash_table.get(
            number
        ):  # if number exists in dict add its number of occurences
            hash_table[number] += 1

            if flag:
                if hash_table[number] > hash_table[mode]:
                    mode = number

            else:
                mode = number
                flag = True

        else:  # add it to dict
            hash_table[number] = 1

    if flag:
        # check for multiple modes
        modes = []
        for number, freq in hash_table.items():
            if freq == hash_table[mode]:
                modes.append(number)

        if len(modes) == len(
            hash_table
        ):  # if all numbers occured an equal amount of times
            return None

        else:
            return modes

    else:
        return None


def find_median(numbers):
    numbers.sort()
    length = len(numbers)
    middle = length // 2

    if length == 1:
        return numbers[0]

    if length % 2:  # if odd
        return numbers[middle]
    else:
        return (numbers[middle] + numbers[middle - 1]) / 2


def find_range(numbers):
    maximum = numbers[0]
    minimum = numbers[0]

    for number in numbers:
        if number > maximum:
            maximum = number
        if number < minimum:
            minimum = number

    return maximum - minimum


def find_variance(numbers):
    mean = find_mean(numbers)
    total = 0

    for number in numbers:
        total += (number - mean) ** 2

    if not total:
        return 0
    return total / (len(numbers) - 1)


def find_STD(numbers):
    variance = find_variance(numbers)
    return math.sqrt(variance)


def find_Quartiles(numbers):
    length = len(numbers)
    middle = length // 2
    Q2 = find_median(numbers)

    if length < 4:
        return [None, Q2, None]

    if length % 2:  # if odd
        Q1 = find_median(numbers[:middle])
        Q3 = find_median(numbers[middle + 1 :])
        return [Q1, Q2, Q3]

    Q1 = find_median(numbers[:middle])
    Q3 = find_median(numbers[middle:])
    return [Q1, Q2, Q3]


def find_IQR(numbers):
    length = len(numbers)
    middle = length // 2

    if length < 4:
        return None

    if length % 2:  # if odd
        Q1 = find_median(numbers[:middle])
        Q3 = find_median(numbers[middle + 1 :])
        return Q3 - Q1

    Q1 = find_median(numbers[:middle])
    Q3 = find_median(numbers[middle:])
    return Q3 - Q1
