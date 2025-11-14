def bubble_sort(array: list[int]) -> list[int]:
    n = len(array)
    flag = True
    while flag:
        flag = False
        for i in range(1, n):
            if array[i - 1] > array[i]:
                flag = True
                array[i - 1], array[i] = array[i], array[i - 1]

    return array


if __name__ == "__main__":
    array = [-5, 3, 2, 1, -3, -3, 7, 2, 2]
    result = bubble_sort(array)
    print(result)
