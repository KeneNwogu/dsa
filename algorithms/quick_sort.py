def quick_sort(arr: list):
    def partition(sub_arr: list, pivot: int, pivot_index=0):
        lower_values = []
        higher_values = []
        for i in range(len(sub_arr)):
            if sub_arr[i] < pivot:
                lower_values.append(sub_arr[i])
            elif sub_arr[i] > pivot:
                higher_values.append(sub_arr[i])
            elif sub_arr[i] == pivot and i != pivot_index:
                lower_values.append(sub_arr[i])
        return lower_values, higher_values

    if len(arr) < 2:
        return arr

    p = arr[0]
    lower_boundaries, higher_boundaries = partition(arr, p)
    return quick_sort(lower_boundaries) + [p] + quick_sort(higher_boundaries)


assert quick_sort([7, 3, 9, 4, 6, 5, 2, 8, 1]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
print('all test cases passed')
