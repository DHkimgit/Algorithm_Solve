"""
민겸이는 영어 소문자와 대문자로 이루어진 문자열을 타이핑하기로 했다. 민겸이가 사용할 수 있는 버튼은 26개의 영어 알파벳 버튼과 마름모(◆) 버튼, 별(★) 버튼이다. 각 버튼은 아래와 같이 작동한다.

알파벳 버튼을 누르면 소문자 또는 대문자 중 하나가 입력된다. 이때, 마름모 버튼이 활성화되어있다면 대문자, 아니라면 소문자가 입력된다. 마름모 버튼은 처음에 비활성화되어있다.
마름모 버튼은 한번 누를 때마다 활성화 및 비활성화 여부가 바뀐다.
별 버튼을 누르면 마지막으로 입력한 알파벳의 대소문자 여부가 바뀐다. 예를 들어 대문자가 마지막으로 입력되었을 경우 소문자로 바뀌고, 소문자가 마지막으로 입력되었을 경우 대문자로 바뀐다. 만약 마지막으로 입력한 알파벳이 없다면 작동하지 않는다.
민겸이는 사용할 수 있는 28개의 버튼을 이용해 어떤 문자열을 입력하려고 한다. 이때, 가능한 한 적은 횟수만큼 버튼을 누르고 싶다. 민겸이가 해당 문자열을 입력하기 위해 버튼을 최소 몇 번 눌러야 하는지 알려주자.

입력
입력은 한 줄로 주어진다.

첫 번째 줄에 민겸이가 타이핑할 문자열이 주어진다.

출력
민겸이가 해당 문자열을 입력하기 위해 버튼을 최소 몇 번 눌러야 하는지 출력한다.

제한
1 ≤ 문자열의 길이 ≤ 3,000
주어지는 문자열은 알파벳 대소문자로만 이루어져 있다.


"""
import sys
sys.setrecursionlimit(10**7)

s = input()

s_len = len(s)

t = [0]*3000

star = 0

rhombus = 0

n = 0

def d_star():
    global star
    star = star + 1

def d_rhombus():
    global rhombus
    rhombus = rhombus + 1
    
def config(s, s_len, t):
    n = 0
    while 1:
        if n == s_len:
            return
        elif s[n].isupper() == True:
            t[n] = 1
            n = n + 1
        elif s[n].islower() == True:
            t[n] = 0
            n = n + 1
        else:
            return 0
            
def del_t(t, s_len):
    global l
    l = t[0:s_len+1]
    l[s_len] = 2

def check_A(l, s_len, n): 
    if n == s_len:
        return
    
    if l[n] == l[n + 1]:
        n = n + 1
        check_A(l, s_len, n)
        
    elif l[n+1] == 2:
        return
    
    elif l[n + 1] - l[n] == 1 or l[n + 1] - l[n] == -1:
        if l[n+2] == 2:
            if l[n+1] != l[n+2]:
                d_star()
                return
            else:    
                return
            
        elif l[n+1] == l[n+2]:
            n = n + 2
            d_rhombus()
            
        elif l[n+1] != l[n+2]:
            n = n + 2
            d_star()
        
        check_A(l, s_len, n)
        
    return

def check_a(l, s_len, n): 
    if n == s_len:
        return
    
    if l[n] == l[n + 1]:
        n = n + 1
        check_a(l, s_len, n)
    
    elif l[n+1] == 2:
        return
    
    elif l[n + 1] - l[n] == 1 or l[n + 1] - l[n] == -1:
        if l[n+2] == 2:
            if l[n+1] != l[n+2]:
                d_star()
                return
            else:    
                return
        elif l[n+1] == l[n+2]:
            n = n + 2
            d_rhombus()
            
        elif l[n+1] != l[n+2]:
            n = n + 2
            d_star()
        
        check_a(l, s_len, n)
    
    return
    
config(s, s_len, t)
del_t(t, s_len)

if l[0] == 1 and l[1] == 1:
    check_A(l, s_len, 0)
    print(s_len + star + rhombus + 1)
    
elif l[0] == 1:
    check_A(l, s_len, 0)
    print(s_len + star + rhombus)

else:
    check_a(l, s_len, 0)
    print(s_len + star + rhombus)