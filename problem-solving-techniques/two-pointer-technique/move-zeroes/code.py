def move_zeroes(nums):
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1


if __name__ == "__main__":
    nums = [1, 0, 2, 5, 0, 0, 6]
    move_zeroes(nums)
    print(nums)
