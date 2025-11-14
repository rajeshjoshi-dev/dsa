def quick_sort(array: list[int]) -> list[int]:
    n = len(array)

    if n <= 1:
        return array

    p = array[-1]

    L = [x for x in array[:-1] if x <= p]
    R = [x for x in array[:-1] if x > p]

    L = quick_sort(L)
    R = quick_sort(R)

    return L + [p] + R


if __name__ == "__main__":
    array = [-5, 3, 2, 1, -3, -3, 7, 2, 2]
    result = quick_sort(array)
    print(result)
