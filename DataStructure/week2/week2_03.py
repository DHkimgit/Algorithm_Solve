class Time:
    def __init__(self, h = 0, m = 0, s = 0):
        self.h = h
        self.m = m
        self.s = s
    
    def set(self, h, m, s):
        self.h = h
        self.m = m
        self.s = s
    
    def __str__(self):
        return "%02d:%02d:%02d"%(self.h, self.m, self.s)

    @staticmethod
    def to_time(second):
        h = second // 3600
        second -= h * 60 * 60
        m = second // 60
        s = second - m * 60

        return h, m, s
    
    def to_second(self):
        return self.h * 60 * 60 + self.m * 60 + self.s
    
    def hour(self):
        return self.h
    
    def minute(self):
        return self.m
    
    def second(self):
        return self.s
    
    def isAM(self):
        return self.h < 12
    
    def isSame(self, t2):
        return self.h == t2.h and self.m == t2.m and self.s == t2.s
    
    def add(self, t):        
        self.h, self.m, self.s = Time.to_time(self.to_second() + t.to_second())

    def difference(self, t2):
        new_time_second = abs(self.to_second() - t2.to_second())
        diff_h, diff_m, diff_s = Time.to_time(new_time_second)
        return Time(diff_h, diff_m, diff_s)
    
    def display(self):
        print("time: %02d:%02d:%02d"%(self.h, self.m, self.s))

    def trim(self):
        self.h, self.m, self.s = Time.to_time(self.to_second())


t1 = Time(3, 20, 30) 
t2 = Time(5, 10, 50) 
t3 = t1.difference(t2)
print("t1과 t2의 차이 : ", t3)
t3.display()       

k4 = Time(10, 23, 61)
k4.display()
k4.trim()
k4.display()

k5 = Time(10, -1, 33)
k5.display()
k5.trim()
k5.display()

k6 = Time(1, 0, 10)
k6.add(Time(3, 30, 20))
k6.display()