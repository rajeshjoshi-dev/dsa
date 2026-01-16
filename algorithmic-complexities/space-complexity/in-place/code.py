def reverse_in_place(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr


if __name__ == "__main__":
    arr = [100, 101, 103, 104]
    result = reverse_in_place(arr)
    print(result)
