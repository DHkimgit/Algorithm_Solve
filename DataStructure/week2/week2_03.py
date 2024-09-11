class Time:
    def __init__(self, h = 0, m = 0, s = 0):
        self.h = h
        self.m = m
        self.s = s
    
    def set(self, h, m, s):
        self.h = h
        self.m = m
        self.s = s
    
    def hour(self):
        return self.h
    
    def minute(self):
        return self.m
    
    def second(self):
        return self.s
    
    def isAM(self):
        if 0 <= self.h <= 12:
            return True
        else:
            return False
    
    def isSame(self, t2):
        return self.h == t2.h and self.m == t2.m and self.s == t2.s
    
    def add(self, t):
        time_to_second = self.h * 60 * 60 + self.m * 60 + self.s
        time_to_second_t = t.h * 60 * 60 + t.m * 60 + t.s
        new_time_second = time_to_second + time_to_second_t
        new_time_h = new_time_second // 3600
        new_time_second -= new_time_h * 60 * 60
        new_time_m = new_time_second // 60
        new_time_second -= new_time_m * 60
        self.h = new_time_h
        self.m = new_time_m
        self.s = new_time_second

    
    def difference(self, t2):
        time_to_second = self.h * 60 * 60 + self.m * 60 + self.s
        time_to_second_t2 = t2.h * 60 * 60 + t2.m * 60 + t2.s
        new_time_second = abs(time_to_second - time_to_second_t2)
        new_time_h = new_time_second // 3600
        new_time_second -= new_time_h * 60 * 60
        new_time_m = new_time_second // 60
        new_time_second -= new_time_m * 60
        return Time(new_time_h, new_time_m, new_time_second)
    
    def display(self):
        print("time: %02d:%02d:%02d"%(self.h, self.m, self.s))

    def trim(self):
        new_time_s = self.h * 60 * 60 + self.m * 60 + self.s
        new_time_h = new_time_s // 3600
        new_time_s -= new_time_h * 60 * 60
        new_time_m = new_time_s // 60
        new_time_s -= new_time_m * 60

        self.h = new_time_h
        self.m = new_time_m
        self.s = new_time_s

k1 = Time(3, 20, 30)
k2 = Time(5, 10, 50)
# 2시간 10초

k3 = k1.difference(k2)
k3.display()
        

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