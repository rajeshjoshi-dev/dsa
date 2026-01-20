def max_subarray(nums):
    n = len(nums)
    best = float("-inf")

    for i in range(n):
        for j in range(i, n):
            current_sum = sum(nums[i : j + 1])
            best = max(best, current_sum)

    return best


if __name__ == "__main__":
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    result = max_subarray(nums)
    print(result)
