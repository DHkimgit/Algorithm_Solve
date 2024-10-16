import os
import time
import copy
import math

class DNode:
    def __init__ (self, data, prev, next):
        self.data = data 
        self.prev = prev
        self.next = next

class DoublyLinkedDeque:
    def __init__(self):
        self.front = None
        self.rear = None

    def isEmpty(self): 
        return self.front == None
    def isFull(self): 
        return False

    def addFront(self, item):
        node = DNode(item, None, self.front)
        if self.isEmpty():
            self.front = self.rear = node
        else :
            self.front.prev = node
            self.front = node

    def addRear(self, item):
        node = DNode(item, self.rear, None)
        if( self.isEmpty()):
            self.front = self.rear = node
        else :
            self.rear.next = node
            self.rear = node

    def deleteFront(self):
        if not self.isEmpty():
            data = self.front.data
            self.front = self.front.next
            if self.front == None :
                self.rear = None
            else:
                self.front.prev = None
            return data

    def deleteRear(self):
        if not self.isEmpty():
            data = self.rear.data
            self.rear = self.rear.prev
            if self.rear == None :
                self.front = None
            else:
                self.rear.next = None
            return data

    def __str__( self ) :
        arr = []
        node = self.front
        while not node == None :
            arr.append(node.data)
            node = node.next
        return str(arr)

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

visited = [[0]*m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def DFS(maze:list):
    
    stack = DoublyLinkedDeque()
    
    stack.addRear((start_x, start_y))
    visited[start_y][start_x] = 1

    while not stack.isEmpty():
        here = stack.deleteRear()
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
                stack.addRear((nx, ny))
                visited[ny][nx] = 1

    return False

if not DFS(maze):
    print("미로 탈출 실패")