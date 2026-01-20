def permute(nums):
    result = []

    def backtrack(path, used):
        if len(path) == len(nums):
            result.append(path[:])
            return

        for i in range(len(nums)):
            if used[i]:
                continue
            used[i] = True
            backtrack(path + [nums[i]], used)
            used[i] = False

    backtrack([], [False] * len(nums))
    return result


if __name__ == "__main__":
    nums = [1, 2, 3]
    result = permute(nums)
    print(result)
