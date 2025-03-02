s1 = str(input())
s2 = str(input())

def equals(s1: str, s2: str) -> str:
    if s1 == "null":
        return "NullPointerException"
    if s2 == "null":
        return "false"

    if s1 != s2:
        return "false"

    return "true"

def equals_ignore_case(s1: str, s2: str) -> str:
    if s1 == "null":
        return "NullPointerException"
    if s2 == "null":
        return "false"
    
    if s1.lower() != s2.lower():
        return "false"
    return "true"

print(equals(s1, s2))
print(equals_ignore_case(s1, s2))
