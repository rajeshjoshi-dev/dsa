def longest_unique_substring(s):
    n = len(s)
    best = 0

    for i in range(n):
        for j in range(i, n):
            substring = s[i : j + 1]
            if len(set(substring)) == len(substring):
                best = max(best, len(substring))

    return best


if __name__ == "__main__":
    nums = "ababcabba"
    result = longest_unique_substring(nums)
    print(result)
