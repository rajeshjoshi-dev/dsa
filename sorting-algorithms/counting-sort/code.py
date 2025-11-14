def counting_sort(array: list[int]) -> list[int]:
    maxx = max(array)
    counts = [0] * (maxx + 1)

    for i in array:
        counts[i] += 1

    i = 0
    for c in range(maxx + 1):
        while counts[c] > 0:
            array[i] = c
            i += 1
            counts[c] -= 1

    return array


if __name__ == "__main__":
    array = [5, 3, 2, 1, 3, 3, 7, 2, 2]
    result = counting_sort(array)
    print(result)
