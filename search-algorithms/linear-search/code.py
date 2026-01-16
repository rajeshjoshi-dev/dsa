def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # element found
    return -1  # element not found


if __name__ == "__main__":

    numbers = [10, 25, 30, 45, 50]
    key = 30

    result = linear_search(numbers, key)
    print(result)
