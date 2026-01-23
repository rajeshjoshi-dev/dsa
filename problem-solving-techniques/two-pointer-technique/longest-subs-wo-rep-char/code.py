def longest_unique_substring(s):
    seen = set()
    left = 0
    best = 0

    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1

        seen.add(s[right])
        best = max(best, right - left + 1)

    return best


if __name__ == "__main__":
    print(longest_unique_substring("abbananapple"))
