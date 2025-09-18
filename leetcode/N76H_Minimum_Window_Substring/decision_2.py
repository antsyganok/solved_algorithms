"""
76. Minimum Window Substring
Hard

Given two strings s and t of lengths m and n respectively,
return the minimum window substring of s such that every character in
t (including duplicates) is included in the window.
If there is no such substring, return the empty string "".
The testcases will be generated such that the answer is unique.

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B',
and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
"""


def minWindow(s: str, t: str) -> str:
    need = {}
    window = {}
    left, right = 0, 0
    missing = len(t)
    result = ""

    for char in t:
        need[char] = need.get(char, 0) + 1

    while right < len(s):
        right_char = s[right]
        if right_char in need:
            window[right_char] = window.get(right_char, 0) + 1

            if window[right_char] <= need[right_char]:
                missing -= 1

        while missing == 0:
            curr_len = right - left + 1
            if not result or curr_len < len(result):
                result = s[left:right + 1]

            left_char = s[left]
            if left_char in need:
                window[left_char] -= 1
                if window[left_char] < need[left_char]:
                    missing += 1
            left += 1

        right += 1

    return "" if not s or not t else result


print(minWindow("ADOBECODEBANC", "ABC"))  # → "BANC"
print(minWindow("a", "a"))               # → "a"
print(minWindow("a", "aa"))              # → ""
