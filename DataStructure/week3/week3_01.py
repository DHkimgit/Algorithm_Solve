class Polynomial:
    def __init__(self, coef:list):
        self.coef = coef

    def __add__(self, rhs):
        index_self = self.degree() + 1
        index_rhs = rhs.degree() + 1
        result_coef = []

        if(index_self == index_rhs):
            for i in range(index_self):
                result_coef.append(self.coef[i] + rhs.coef[i])

        elif index_self > index_rhs:
            result_coef = self.coef[:]
            for i in range(index_rhs):
                result_coef[i] += rhs.coef[i]

        else:
            result_coef = rhs.coef[:]
            for i in range(index_self):
                result_coef[i] += self.coef[i]
        
        return Polynomial(result_coef)
    
    def __sub__(self, rhs):
        index_self = self.degree() + 1
        index_rhs = rhs.degree() + 1
        result_coef = []

        if(index_self == index_rhs):
            for i in range(index_self):
                result_coef.append(self.coef[i] - rhs.coef[i])
        
        elif index_self > index_rhs:
            result_coef = self.coef[:]
            for i in range(index_rhs):
                result_coef[i] -= rhs.coef[i]

        else:
            result_coef = [-coef for coef in rhs.coef[:]]
            for i in range(index_self):
                result_coef[i] += self.coef[i]
        
        return Polynomial(result_coef)
    
    def __mul__(self, rhs):
        index_self = self.degree() + 1
        index_rhs = rhs.degree() + 1
        result_coef = []

        if(index_self == index_rhs):
            for i in range(index_self):
                result_coef.append(self.coef[i] * rhs.coef[i])
        
        elif index_self > index_rhs:
            result_coef = self.coef[:]
            for i in range(index_rhs):
                result_coef[i] *= rhs.coef[i]

        else:
            result_coef = rhs.coef[:]
            for i in range(index_self):
                result_coef[i] *= self.coef[i]
        
        return Polynomial(result_coef)
    
    def degree(self):
        return len(self.coef) - 1
    
    def evaluate(self, scalar):
        result = 0
        for i in range(self.degree() + 1):
            result += self.coef[i] * (scalar ** i)
        return result
    
    def display(self, message = ""):
        result = []
        first_flag = True
        
        for i in range(self.degree(), -1, -1):
            coef = float(self.coef[i])

            if first_flag:
                result.append(f"{coef} x^{i}")
                first_flag = False
            
            else:
                if coef < 0:
                    if i == 0:
                        result.append(f" - {-coef}")
                    else:
                        result.append(f" - {-coef} x^{i}")
                elif coef > 0:
                    if i == 0:
                        result.append(f" + {coef}")
                    else:
                        result.append(f" + {coef} x^{i}")
                else:
                    pass

        print(message + ''.join(result))

    @staticmethod
    def read():
        coef_list = list(map(int, input("최고차항부터 차수를 순서대로 입력하세요: ").split()))
        
        return Polynomial(coef_list[::-1])
    
a = Polynomial.read()
b = Polynomial.read()
c = a + b
d = a - b
d2 = b - a
e = a * b

a.display("A(x) = ")
b.display("B(x) = ")
c.display("A(x) + B(x) = ")
d.display("A(x) - B(x) = ")
d2.display("B(x) - A(x) = ")
e.display("A(x) * B(x) = ")
print("A(2) + B(2) = ", c.evaluate(2))
