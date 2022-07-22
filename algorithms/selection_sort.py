def selection_sort(numbers: list):
    if len(numbers) <= 1:
        return numbers

    sorted_list = []
    for i in range(len(numbers)):
        smallest = numbers[0]
        smallest_index = 0
        for j in range(1, len(numbers)):
            if numbers[j] < smallest:
                smallest = numbers[j]
                smallest_index = j
        sorted_list.append(numbers.pop(smallest_index))
    return sorted_list


assert selection_sort([7, 3, 9, 4, 6, 5, 2, 8, 1]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
print('all test cases passed')