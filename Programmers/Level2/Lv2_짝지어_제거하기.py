def solution(s):
    idx = 0
    while idx >= 0 and idx < len(s) - 1:
        idx += 1
        if s[idx - 1] == s[idx]:
            s = s[:idx - 1] + s[idx + 1:]
            idx = 0

    return 0 if len(s) else 1