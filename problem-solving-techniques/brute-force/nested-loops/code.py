def two_sum(nums, k):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == k:
                return True
    return False


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6]
    result = two_sum(nums, 6)
    print(result)
