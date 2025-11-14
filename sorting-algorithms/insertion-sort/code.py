def insertion_sort(array: list[int]) -> list[int]:
    n = len(array)

    for i in range(1, n):
        for j in range(i, 0, -1):
            if array[j - 1] > array[j]:
                array[j - 1], array[j] = array[j], array[j - 1]
            else:
                break

    return array


if __name__ == "__main__":
    array = [-5, 3, 2, 1, -3, -3, 7, 2, 2]
    result = insertion_sort(array)
    print(result)
