N = int(input())
cm = 0
kg = 0
people_cm = []
people_kg = []
people_BMI = []
for i in range(N):
    cm, kg = map(int, input().split())
    people_cm.append(cm)
    people_kg.append(kg)
    people_BMI.append(kg/(cm/100))

                      
for i in range(N):
    if(people_cm[i] < 140.1):
        print(6)
    elif(140.1 <= people_cm[i] < 146):
        print(5)
    elif(146 <= people_cm[i] < 159):
        print(4)
    elif(159 <= people_cm[i] < 161):
        if(16 <= people_BMI[i] < 35):
            print(3)
        else:
            print(4)
    elif(161 <= people_cm[i] < 204):
        if(20 <= people_BMI[i] < 25):
            print(1)
        elif(18.5 <= people_BMI[i] < 20 or 25 <= people_BMI[i] < 30):
            print(2)
        elif(16 <= people_BMI[i] <18.5 or 30 <= people_BMI[i] < 35):
            print(3)
        elif(people_BMI[i] < 16 or people_BMI[i] >= 35):
            print(4)
        else:
            print(4)
    