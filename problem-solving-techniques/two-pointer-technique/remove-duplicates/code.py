def remove_duplicates(nums):
    slow = 0

    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]

    return slow + 1


if __name__ == "__main__":
    nums = [1, 2, 2, 3, 4, 4, 4, 5, 5]
    remove_duplicates(nums)
    print(nums)
