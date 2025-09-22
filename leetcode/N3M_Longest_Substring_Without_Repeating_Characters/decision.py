"""

"""


def lengthOfLongestSubstring(s: str) -> int:
    if not s:
        return 0

    char_map = {}
    max_length = 0
    left = 0

    for right, char in enumerate(s):
        if char in char_map and char_map[char] >= left:
            left = char_map[char] + 1
        char_map[char] = right
        max_length = max(max_length, right - left + 1)

    return max_length
