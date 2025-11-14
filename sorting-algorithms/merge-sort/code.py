def merge_sort(array: list[int]) -> list[int]:
    n = len(array)

    if n == 1:
        return array

    m = n // 2
    L = array[:m]
    R = array[m:]

    L = merge_sort(L)
    R = merge_sort(R)

    L_len = len(L)
    R_len = len(R)

    sorted_arr = [0] * n
    r = l = i = 0

    while l < L_len and r < R_len:
        if L[l] < R[r]:
            sorted_arr[i] = L[l]
            l += 1
        else:
            sorted_arr[i] = R[r]
            r += 1

        i += 1

    while l < L_len:
        sorted_arr[i] = L[l]
        l += 1
        i += 1

    while r < R_len:
        sorted_arr[i] = R[r]
        r += 1
        i += 1

    return sorted_arr


if __name__ == "__main__":
    array = [-5, 3, 2, 1, -3, -3, 7, 2, 2]
    result = merge_sort(array)
    print(result)
