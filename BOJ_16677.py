s = str(input())
N = int(input())

def check_possible(orignal: str, weird: str, cost: int):
    length = len(orignal)
    val = 0

    for c in weird:
        if c == orignal[val]:
            val += 1
        if val >= length:
            break
    
    if val == length:
        return True, float(cost / (len(weird) - length))
    else:
        return False, -1

result_cost = 0
result_value = "No Jam"

for i in range(N):
    weird, cost = map(str, input().split())

    is_possible, val = check_possible(s, weird, int(cost))

    if is_possible and val > result_cost:
        result_cost = val
        result_value = weird

print(result_value)
