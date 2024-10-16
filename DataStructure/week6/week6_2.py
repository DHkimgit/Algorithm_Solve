import os
import time
import copy
import math

class Node:
    def __init__ (self, data, link = None):
        self.data = data 
        self.link = link

class LinkedQueue:
    def __init__(self):
        self.tail = None

    def isEmpty(self): 
        return self.tail == None
    
    def isFull(self): 
        return False

    def enqueue(self, item):
        node = Node(item, None)
        if self.isEmpty() :
           self.tail = node
           node.link = node
        else :
            node.link = self.tail.link
            self.tail.link = node
            self.tail = node

    def dequeue(self):
        if not self.isEmpty():
            data = self.tail.link.data
            if self.tail.link == self.tail: 
                self.tail = None
            else:
                self.tail.link = self.tail.link.link
            return data

    def peek(self):
        if not self.isEmpty():
            return self.tail.link.data

    def size( self ):
        if self.isEmpty(): 
            return 0
        else:
            count = 1
            node = self.tail.link
            while not node == self.tail :
                node = node.link
                count += 1
            return count

    def __str__( self ):
        arr = []
        if not self.isEmpty() :
            node = self.tail.link
            while not node == self.tail :
                arr.append(node.data)
                node = node.link
            arr.append(node.data)
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

# 0 = 벽, 1 = 통로, 2 = 시작지점, 3 = 출구

def BFS(maze:list):
    
    queue = LinkedQueue()
    
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

if not BFS(maze):
    print("미로 탈출 실패")
