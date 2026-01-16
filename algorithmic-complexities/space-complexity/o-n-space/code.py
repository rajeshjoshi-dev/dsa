def copy_array(arr):
    new_arr = []
    for item in arr:
        new_arr.append(item)
    return new_arr

def recursive_sum(n):
    if n == 0:
        return 0
    return n + recursive_sum(n - 1)

if __name__ == "__main__":
    arr = [100, 101, 103, 104]
    result = copy_array(arr)
    print(result)

    result = recursive_sum(120)
    print(result)
