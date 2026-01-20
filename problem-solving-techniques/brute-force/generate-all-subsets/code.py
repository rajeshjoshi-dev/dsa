def subsets(nums):
    n = len(nums)
    result = []

    for mask in range(1 << n):  # 2^n
        subset = []
        for i in range(n):
            if mask & (1 << i):
                subset.append(nums[i])
        result.append(subset)

    return result


if __name__ == "__main__":
    nums = [1, 2, 3]
    result = subsets(nums)
    print(result)
