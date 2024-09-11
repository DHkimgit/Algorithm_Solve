print("연봉을 입력하세요 ==> ", end='')
origin_income = int(input())
tax = 0
income = origin_income

if income > 15000:
    tax += (income - 15000) * 0.38
    income = 15000

if income > 8800:
    tax += (income - 8800) * 0.35
    income = 8800

if income > 4600:
    tax += (income - 4600) * 0.24
    income = 4600

if income > 1200:
    tax += (income - 1200) * 0.15
    income = 1200

tax += income * 0.06
print(" 전체 세금 = ", tax)
print(" 순수 소득 = ",  origin_income - tax)
