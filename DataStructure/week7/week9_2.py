import time
class LinProbMap:
    def __init__(self, capacity = 17):
        self.capacity = capacity
        self.table = [None] * capacity
    
    def hashFn(self, key):
        return key % self.capacity
    
    def insert(self, key):
        index = self.hashFn(key)
        count = self.capacity
        collision = 0

        while count > 0:
            if self.table[index] == None or self.table[index] == -1:
                break
            collision += 1
            index = (index + 1) % self.capacity
            count -= 1

        if count > 0:
            self.table[index] = key
        
        return collision
    
    def insertQuadraticProbing(self, key):
        index = self.hashFn(key)
        count = self.capacity
        collision = 0
        i = 0
        while count > 0:
            if self.table[index] == None or self.table[index] == -1:
                break
            collision += 1
            index = (index + i*i) % self.capacity
            # print("index : %d, i: %d"%(index, i))
            count -= 1
            i += 1

        if count > 0:
            self.table[index] = key
        return collision
    
    def search(self, key):
        index = self.hashFn(key)
        count = self.capacity

        while count > 0 :
            if self.table[index] == None:
                return None, None
            
            if self.table[index] == key:
                return (index, self.table[index])
            
            index = (index + 1) % self.capacity
            count -= 1

        return None, None
    
    def searchQuadraticProbing(self, key):
        index = self.hashFn(key)
        count = self.capacity
        i = 0
        while count > 0 :
            if self.table[index] == None:
                return None, None
            
            if self.table[index] == key:
                return (index, self.table[index])
            
            index = (index + i*i) % self.capacity
            count -= 1
            i+=1

        return None, None
    
    def delete(self, key):
        index = self.hashFn(key)
        count = self.capacity

        while count > 0 :            
            if self.table[index] == key:
                self.table[index] = -1
                return
            
            if self.table[index] == None :
                return
            index = (index + 1) % self.capacity
            count -= 1
    
    def deleteQuadraticProbing(self, key):
        index = self.hashFn(key)
        count = self.capacity
        i = 0

        while count > 0 :            
            if self.table[index] == key:
                self.table[index] = -1
                return
            
            if self.table[index] == None :
                return
            index = (index + i*i) % self.capacity
            count -= 1
            i+=1
    
    def __str__(self):
        return str(self.table)
            
if __name__ == "__main__":
    linMap = LinProbMap()
    data = [45, 27, 88, 9, 71, 60, 46, 38, 24, 16, 57, 63, 41, 3, 25, 7, 91]

    print("값 삽입")
    for d in data :
        print( "h(%2d)=%2d"%(d, d % len(data)), end=' ')
        collision = linMap.insert(d)
        print("해시충돌횟수= %2d"%(collision), end=' ')
        print("table-->",end='')
        print(linMap)
    
    print("")
    search_result1 = linMap.search(46)
    print("46탐색--> 저장된 위치 : ", search_result1[0], "저장된 값 : ", search_result1[1])
    search_result2 = linMap.search(39)
    print("39탐색--> 저장된 위치 : ", search_result2[0], "저장된 값 : ", search_result2[1])
    search_result3 = linMap.search(71)
    print("71탐색--> 저장된 위치 : ", search_result3[0], "저장된 값 : ", search_result3[1])
    search_result4 = linMap.search(60)
    print("60탐색--> 저장된 위치 : ", search_result4[0], "저장된 값 : ", search_result4[1])

    print("")
    print("60삭제-->", end='')
    linMap.delete(60)
    print(linMap)
    print("46삭제-->", end='')
    linMap.delete(46)
    print(linMap)
    print("71삭제-->", end='')
    linMap.delete(71)
    print(linMap)

    linMapQ = LinProbMap()
    data = [45, 27, 88, 9, 71, 60, 46, 38, 24, 16, 57, 63, 41, 3, 25, 7, 92, 12]

    print("값 삽입")
    for d in data :
        print( "h(%2d)=%2d"%(d, d % len(data)), end=' ')
        collision = linMapQ.insertQuadraticProbing(d)
        print("해시충돌횟수= %2d"%(collision), end=' ')
        print("table-->",end='')
        print(linMapQ)
    
    print("")
    search_result1 = linMapQ.searchQuadraticProbing(46)
    print("46탐색--> 저장된 위치 : ", search_result1[0], "저장된 값 : ", search_result1[1])
    search_result2 = linMapQ.searchQuadraticProbing(39)
    print("39탐색--> 저장된 위치 : ", search_result2[0], "저장된 값 : ", search_result2[1])
    search_result3 = linMapQ.searchQuadraticProbing(71)
    print("71탐색--> 저장된 위치 : ", search_result3[0], "저장된 값 : ", search_result3[1])
    search_result4 = linMapQ.searchQuadraticProbing(60)
    print("60탐색--> 저장된 위치 : ", search_result4[0], "저장된 값 : ", search_result4[1])

    print("")
    print("60삭제-->", end='')
    linMapQ.deleteQuadraticProbing(60)
    print(linMapQ)
    print("46삭제-->", end='')
    linMapQ.deleteQuadraticProbing(46)
    print(linMapQ)
    print("71삭제-->", end='')
    linMapQ.deleteQuadraticProbing(71)
    print(linMapQ)

    k = LinProbMap(6)
    datak = [43, 54, 23, 1, 3, 76]

    print("값 삽입")
    for d in datak :
        print( "h(%2d)=%2d"%(d, d % len(data)), end=' ')
        collision = k.insertQuadraticProbing(d)
        print("해시충돌횟수= %2d"%(collision), end=' ')
        print("table-->",end='')
        print(k)

