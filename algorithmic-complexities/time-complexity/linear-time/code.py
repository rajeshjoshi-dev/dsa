def sum_array(arr):
    total = 0
    for num in arr:
        total += num
    return total


if __name__ == "__main__":
    arr = [100, 101, 103, 104]
    result = sum_array(arr)
    print(result)
