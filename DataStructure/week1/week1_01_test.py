class Bag:
    def __init__(self):
        self.bag = []

    def contains(self, e):
        return e in self.bag

    def insert(self, e):
        self.bag.append(e)

    def remove(self, e):
        if e in self.bag:
            self.bag.remove(e)

    def count(self):
        return len(self.bag)
    
    def numOf(self, e):
        result = 0
        for i in self.bag:
            if i == e:
                result += 1
        return result
    
    def __str__(self):
        return str(self.bag)

myBag = Bag()
myBag.insert('휴대폰')
myBag.insert('지갑')
myBag.insert('손수건')
myBag.insert('빗')
myBag.insert('자료구조')
myBag.insert('야구공')
print('가방 속의 물건 : ', myBag)

myBag.insert('빗')
myBag.remove('손수건')

print('가방 속의 물건 : ', myBag)

myBag2 = Bag()
myBag2.insert('휴대폰')
myBag2.insert('휴대폰')
myBag2.insert('휴대폰')
myBag2.insert('휴대폰')
myBag2.insert('지갑')
myBag2.insert('손수건')
myBag2.insert('빗')
myBag2.insert('자료구조')
myBag2.insert('야구공')

print('numOf(\'휴대폰\') : ', myBag2.numOf('휴대폰'))
print('numOf(\'손수건\') : ', myBag2.numOf('손수건'))
print('numOf(\'게임기\') : ', myBag2.numOf('게임기'))