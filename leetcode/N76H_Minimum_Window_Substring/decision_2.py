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
