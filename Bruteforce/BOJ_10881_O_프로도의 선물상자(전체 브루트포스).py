T = int(input())
box_a = []
box_b = []

for i in range(T):
    tmp_a = [0, 0, 0, 0, 0, 0]
    tmp_b = [0, 0, 0, 0, 0, 0]
    x1, y1 = map(int, input().split())
    tmp_a[0] = x1
    tmp_b[3] = x1
    tmp_b[0] = y1
    tmp_a[3] = y1
    x2, y2 = map(int, input().split())
    tmp_a[1] = x2
    tmp_b[4] = x2
    tmp_b[1] = y2
    tmp_a[4] = y2
    x3, y3 = map(int, input().split())
    tmp_a[2] = x3
    tmp_b[5] = x3
    tmp_b[2] = y3
    tmp_a[5] = y3
    box_a.append(tmp_a)
    box_b.append(tmp_b)

def lineThree(i, x, y, z):
    return (box_a[i][x] + box_a[i][y] + box_a[i][z]) * max(box_b[i][x], box_b[i][y], box_b[i][z])

def lineTwo(i, x, y, z):
    return max(box_a[i][x] + box_a[i][y], box_a[i][z]) * (max(box_b[i][x], box_b[i][y]) + box_b[i][z])

def findBox(Testcase: int):
    minarea = 999999
    for i in range(0, 6):
        for j in range(0, 6):
            for k in range(0, 6):
                if (i % 3) == (j % 3) or (i % 3) == (k % 3) or (k % 3) == (j % 3):
                    continue
                else:
                    minarea = min(minarea, lineThree(Testcase, i, j, k))
                    minarea = min(minarea, lineTwo(Testcase, i, j, k))
    
    return minarea

for i in range(T):
    print(findBox(i))
