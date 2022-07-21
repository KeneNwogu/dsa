def binary_search(numbers: list, search_key: int):
    numbers.sort()
    low = 0
    high = len(numbers) - 1

    while low <= high:
        mid = (low + high) // 2
        if numbers[mid] == search_key:
            return mid
        elif numbers[mid] < search_key:
            low = mid + 1
        else:
            high = mid - 1
    return None


assert binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 1) == 0
assert binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 2) == 1
assert binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 3) == 2
assert binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 4) == 3
assert binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 5) == 4
assert binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 6) == 5
assert binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 7) == 6
assert binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 8) == 7
assert binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 9) == 8
assert binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 10) is None


print('all test cases passed')
