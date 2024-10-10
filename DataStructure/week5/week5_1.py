import os
import time
import copy
import math

class ArrayStack :
    def __init__(self, capacity):
        self.capacity = capacity
        self.array = [None] * self.capacity	
        self.top = -1

    def isEmpty(self) :
       return self.top == -1

    def isFull(self) :
       return self.top == self.capacity - 1

    def push(self, item):
        if not self.isFull() :
            self.top += 1
            self.array[self.top] = item
        else: pass

    def pop(self):
        if not self.isEmpty():
            self.top -= 1
            return self.array[self.top + 1]
        else: pass

    def peek(self):
        if not self.isEmpty():
            return self.array[self.top]
        else: pass

    def __str__(self):
        return str(self.array[0:self.top+1][::-1])

    def size(self): 
        return self.top+1
    
class CircularQueue:
    def __init__(self, capacity = 100):
        self.capacity = capacity
        self.array = [None] * capacity
        self.front = 0
        self.rear = 0

    def isFull(self):
        return self.front == (self.rear + 1) % self.capacity
    
    def isEmpty(self):
        return self.front == self.rear

    def enqueue(self, e):
        if not self.isFull():
            self.rear = (self.rear + 1) % self.capacity
            self.array[self.rear] = e
        else:
            pass
    
    def dequeue( self ):
        if not self.isEmpty():
            self.front = (self.front + 1) % self.capacity
            return self.array[self.front]
    
    def peek( self ):
        if not self.isEmpty():
            return self.array[(self.front + 1) % self.capacity]
    
    def size( self ) :
       return (self.rear - self.front + self.capacity) % self.capacity

class PriorityQueue :
    def __init__( self, capacity = 100 ) :
        self.capacity = capacity
        self.array = [None] * capacity
        self.size = 0

    def isEmpty( self ) :
       return self.size == 0

    def isFull( self ) :
       return self.size == self.capacity

    def enqueue( self, e ):
        if not self.isFull():
            self.array[self.size] = e
            self.size += 1

    def findMaxIndex( self ):
        if self.isEmpty(): return -1
        highest = 0
        for i in range(1, self.size) :
            if self.array[i][2] > self.array[highest][2] :
                highest = i
        return highest

    def dequeue( self ):
        highest = self.findMaxIndex()
        if highest != -1 :
            self.size -= 1 
            self.array[highest], self.array[self.size] = \
                self.array[self.size], self.array[highest]
            return self.array[self.size]

    def peek( self ):
        highest = self.findMaxIndex()
        if highest != -1 :
            return self.array[highest]


n, m = map(int, input().split())

maze = []
start_x, start_y, end_x, end_y = (0, 0, 0, 0)

for i in range(n):
    maze.append(list(map(int, input().split())))

maze_init = copy.deepcopy(maze)

for i in range(n):
    for j in range(m):
        if(maze[i][j] == 0):
            maze[i][j] = "■"
        elif(maze[i][j] == 1):
            maze[i][j] = " "
        elif(maze[i][j] == 2):
            maze[i][j] = "→"
            start_y = i
            start_x = j
        elif(maze[i][j] == 3):
            maze[i][j] = "→"
            end_y = i
            end_x = j
        else:
            pass

def printMaze(current_x, current_y, end_x, end_y):
    os.system('cls' if os.name == 'nt' else 'clear')
    for i in range(n):
        for j in range(m):
            print(maze[i][j], end=" ")
        print()
    print(f"현재 위치 : ({current_x}, {current_y})")
    if current_x == end_x and current_y == end_y:
        print(" --> 미로 탐색 성공")
    time.sleep(0.5)

def dist(x, y):
    (dx, dy) = (end_x - x, end_y - y)
    return math.sqrt(dx*dx + dy*dy)

print(f"현재 위치 : ({start_x}, {start_y})")

order = input("탐색 방법 1=DFS, 2=BFS, 3=Pqueue, q = 종료 ==> ")

visited = [[0]*m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 0 = 벽, 1 = 통로, 2 = 시작지점, 3 = 출구

def BFS(maze:list):
    
    queue = CircularQueue()
    
    queue.enqueue((start_x, start_y))
    visited[start_y][start_x] = 1

    while not queue.isEmpty():
        here = queue.dequeue()
        x, y = here

        if (maze_init[y][x] == 3):
            maze[y][x] = "★"
            printMaze(x, y, end_x, end_y)
            return True

        maze[y][x] = "√"

        printMaze(x, y, end_x, end_y)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= m or ny >= n:
                continue
            
            if maze_init[ny][nx] == 0 or visited[ny][nx] == 1:
                continue
            
            if maze_init[ny][nx] == 1 or maze_init[ny][nx] == 3:
                queue.enqueue((nx, ny))
                visited[ny][nx] = 1

    return False

def DFS(maze:list):
    
    stack = ArrayStack(100)
    
    stack.push((start_x, start_y))
    visited[start_y][start_x] = 1

    while not stack.isEmpty():
        here = stack.pop()
        x, y = here

        if (maze_init[y][x] == 3):
            maze[y][x] = "★"
            printMaze(x, y, end_x, end_y)
            return True

        maze[y][x] = "√"

        printMaze(x, y, end_x, end_y)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= m or ny >= n:
                continue
            
            if maze_init[ny][nx] == 0 or visited[ny][nx] == 1:
                continue
            
            if maze_init[ny][nx] == 1 or maze_init[ny][nx] == 3:
                stack.push((nx, ny))
                visited[ny][nx] = 1

    return False

def Priority(maze:list):
    
    queue = PriorityQueue()
    
    queue.enqueue((start_x, start_y, -dist(start_x, start_y)))
    visited[start_y][start_x] = 1

    while not queue.isEmpty():
        here = queue.dequeue()
        x, y, _ = here

        if (maze_init[y][x] == 3):
            maze[y][x] = "★"
            printMaze(x, y, end_x, end_y)
            return True

        maze[y][x] = "√"

        printMaze(x, y, end_x, end_y)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= m or ny >= n:
                continue
            
            if maze_init[ny][nx] == 0 or visited[ny][nx] == 1:
                continue
            
            if maze_init[ny][nx] == 1 or maze_init[ny][nx] == 3:
                queue.enqueue((nx, ny, -dist(nx, ny)))
                visited[ny][nx] = 1
            
    return False

if order == "1":
    if not DFS(maze):
        print("미로 탈출 실패")

elif order == "2":
    if not BFS(maze):
        print("미로 탈출 실패")

elif order == "3":
    if not Priority(maze):
        print("미로 탈출 실패")
else:
    pass

