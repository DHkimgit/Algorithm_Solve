import time
class SortedArraySet:
    def __init__(self, capacity=100):
        self.capacity = capacity
        self.array = [None]*capacity
        self.size = 0

    def isEmpty( self ):
       return self.size == 0

    def isFull( self ):
       return self.size == self.capacity

    def __str__( self ) :
        return str(self.array[0:self.size])

    def contains(self, e):
        low = 0
        high = self.size - 1
        
        while low <= high:
            middle = (low + high) // 2
            element = self.array[middle]

            if element == e:
                return True
            elif element < e:
                low = middle + 1
            else:
                high = middle - 1
                
        return False

    def insert(self, e):
        if self.contains(e) or self.isFull():
            return

        self.array[self.size] = e
        self.size += 1

        for i in range(self.size-1, 0, -1):
            if self.array[i-1] <= self.array[i]: 
                break
            self.array[i-1], self.array[i] = self.array[i], self.array[i-1]

    def delete(self, e):
        if not self.contains(e):
           return
        
        index = 0
        for i in range(0, self.size):
            if self.array[i] == e:
                index = i
                break

        for i in range(index, self.size - 1):
            self.array[i] = self.array[i + 1]
        
        self.array[self.size - 1] = None
        self.size -= 1


    def __eq__(self, setB):
        if self.size != setB.size:
            return False

        for i in range(self.size):
            if self.array[i] != setB.array[i]:
                return False
        return True

    def union(self, setB):
        result = SortedArraySet()
        
        i = 0
        j = 0

        while i < self.size and j < setB.size:
            a = self.array[i]
            b = setB.array[j]

            if a == b:
                result.append(a)
                i += 1
                j += 1

            elif a < b: 
                result.append(a)
                i += 1

            else:
                result.append(b)
                j += 1

        while i < self.size:
            result.append(self.array[i])
            i += 1

        while j < setB.size:
            result.append(setB.array[j])
            j += 1

        return result


    def intersect(self, setB):
        result = SortedArraySet()
        i = 0
        j = 0

        while i < self.size and j < setB.size:
            a = self.array[i]
            b = setB.array[j]

            if a == b :
                result.append(a)
                i += 1
                j += 1
            elif a < b: 
                i += 1
            else :
                j += 1

        return result

    def difference(self, setB):
        result = SortedArraySet()
        i = 0
        j = 0

        while i < self.size and j < setB.size:
            a = self.array[i]
            b = setB.array[j]

            if a == b:
                i += 1
                j += 1

            elif a < b:
                result.append(a)
                i += 1

            else:
                j += 1

        return result 
    
    def display(self, msg):
        print(msg, self.items)

    def append(self, e) :
        self.array[self.size] = e
        self.size += 1
    

class ArraySet:
    def __init__(self, capacity=100):
        self.capacity = capacity
        self.array = [None]*capacity
        self.size = 0

    def isEmpty( self ):
       return self.size == 0

    def isFull( self ):
       return self.size == self.capacity

    def __str__( self ) :
        return str(self.array[0:self.size])

    def contains(self, e) :
        for i in range(self.size) :
            if self.array[i] == e :
                return True
        return False

    def insert(self, e) :
        if not self.contains(e) and not self.isFull() :
           self.array[self.size] = e
           self.size += 1
        else : pass

    def delete(self, e) :
        for i in range(self.size) :
            if self.array[i] == e :
                self.array[i] = self.array[self.size-1]
                self.size -= 1

    def union( self, setB ):
        setC = ArraySet()
        for i in range(self.size) :
            setC.insert(self.array[i])

        for i in range(setB.size) :
            if not setC.contains(setB.array[i]) :
                setC.insert(setB.array[i])

        return setC

    def intersect( self, setB ):            
        setC = ArraySet()
        for i in range(setB.size) :
            if self.contains(setB.array[i]) :
                setC.insert(setB.array[i])
        return setC

    def difference( self, setB ):            
        setC = ArraySet()
        for i in range(self.size) :
            if not setB.contains(self.array[i]) :
                setC.insert(self.array[i])
        return setC

    def __eq__( self, setB ):
        if self.size != setB.size :
            return False

        for i in range(self.size) :
            if not setB.contains(self.array[i]) :
                return False
        return True
    
sortedSetA = SortedArraySet()
sortedSetB = SortedArraySet()

normalSetA = ArraySet()
normalSetB = ArraySet()

start = time.time()
sortedSetA.insert(9)
sortedSetA.insert(8)
sortedSetA.insert(7)
sortedSetA.insert(6)
sortedSetA.insert(5)
sortedSetA.insert(4)
sortedSetA.insert(3)
sortedSetA.insert(2)
sortedSetA.insert(1)
sortedSetA.insert(20)
sortedSetA.insert(13)
sortedSetA.insert(15)
sortedSetA.insert(48)
sortedSetA.insert(96)
sortedSetA.insert(54)
sortedSetA.insert(22)
sortedSetA.insert(26)
sortedSetA.insert(14)

print(f"정렬된 배열 집합 원소 삽입 시간 : {time.time()-start} sec")

start = time.time()
normalSetA.insert(9)
normalSetA.insert(8)
normalSetA.insert(7)
normalSetA.insert(6)
normalSetA.insert(5)
normalSetA.insert(4)
normalSetA.insert(3)
normalSetA.insert(2)
normalSetA.insert(1)
normalSetA.insert(20)
normalSetA.insert(13)
normalSetA.insert(15)
normalSetA.insert(48)
normalSetA.insert(96)
normalSetA.insert(54)
normalSetA.insert(22)
normalSetA.insert(26)
normalSetA.insert(14)
print(f"정렬되지 않은 배열 집합 원소 삽입 시간 : {time.time()-start} sec")

start = time.time()
sortedSetA.contains(25)
sortedSetA.contains(50)
sortedSetA.contains(75)
sortedSetA.contains(100)
print(f"정렬된 배열 집합 원소 탐색 시간 : {time.time()-start} sec")

start = time.time()
normalSetA.contains(25)
normalSetA.contains(50)
normalSetA.contains(75)
normalSetA.contains(100)
print(f"정렬되지 않은 배열 집합 원소 탐색 시간 : {time.time()-start} sec")

sortedSetB.insert(119)
sortedSetB.insert(218)
sortedSetB.insert(27)
sortedSetB.insert(246)
sortedSetB.insert(554)
sortedSetB.insert(5)
sortedSetB.insert(6)
sortedSetB.insert(7)
sortedSetB.insert(15)
sortedSetB.insert(48)
sortedSetB.insert(96)

normalSetB.insert(119)
normalSetB.insert(218)
normalSetB.insert(27)
normalSetB.insert(246)
normalSetB.insert(554)
normalSetB.insert(5)
normalSetB.insert(6)
normalSetB.insert(7)
normalSetB.insert(15)
normalSetB.insert(48)
normalSetB.insert(96)

start = time.time()
result_sorted = sortedSetA.union(sortedSetB)
print(result_sorted)
print(f"정렬된 배열 집합 원소 합집합 연산 시간 : {time.time()-start} sec")

start = time.time()
result_normal = normalSetA.union(normalSetB)
print(result_normal)
print(f"정렬되지 않은 배열 집합 원소 합집합 연산 시간 : {time.time()-start} sec")

start = time.time()
result_sorted = sortedSetA.intersect(sortedSetB)
print(result_sorted)
print(f"정렬된 배열 집합 원소 교집합 연산 시간 : {time.time()-start} sec")

start = time.time()
result_normal = normalSetA.intersect(normalSetB)
print(result_normal)
print(f"정렬되지 않은 배열 집합 원소 교집합 연산 시간 : {time.time()-start} sec")
print(sortedSetA)
print(sortedSetB)
start = time.time()
result_sorted = sortedSetA.difference(sortedSetB)
print(result_sorted)
print(f"정렬된 배열 집합 원소 차집합 연산 시간 : {time.time()-start} sec")

start = time.time()
result_normal = normalSetA.difference(normalSetB)
print(result_normal)
print(f"정렬되지 않은 배열 집합 원소 차집합 연산 시간 : {time.time()-start} sec")