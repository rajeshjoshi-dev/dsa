def selection_sort(array: list[int]) -> list[int]:
    n = len(array)

    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if array[j] < array[min_index]:
                min_index = j

        array[i], array[min_index] = array[min_index], array[i]

    return array


if __name__ == "__main__":
    array = [-3, 3, 2, 1, -5, -3, 7, 2, 2]
    result = selection_sort(array)
    print(result)
