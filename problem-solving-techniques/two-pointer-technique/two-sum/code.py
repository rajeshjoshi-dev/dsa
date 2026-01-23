def two_sum(nums, target):
    left, right = 0, len(nums) - 1

    while left < right:
        sum = nums[left] + nums[right]

        if sum == target:
            return True

        elif sum > target:
            right -= 1
        else:
            left += 1


if __name__ == "__main__":
    nums = [2, 3, 4]  # sorted array
    print(two_sum(nums, 6))
