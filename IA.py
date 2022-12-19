income = int(input("income: "))
age = int(input("age: "))
civil_state = str(input("civil state(s, c, d): "))
loan = int(input("loan: "))
score = int(input("score: "))
dependents = int(input("dependents: "))
answear = 0

print("")

def incomeCalc(a):
    if a >= 0 and a < 2000:
           return 1
    elif a >= 2000 and a < 5000:
           return 0.7
    elif a >= 5000 and a <= 8000:
           return 0.4
    elif a > 8000:
           return 0

def ageCalc(b):
    if b >= 0 and b < 5:
           b = 1
    elif b >= 5 and b < 8:
        b = 0.7
    elif b >= 8 and b <= 12:
        b = 0.4
    elif b > 12:
        b = 0

def loanCalc(inc, loa):
    if loa <= inc:
        return 1
    elif loa > inc and loa <= 2*(inc):
        return 0.4
    elif loa > 2*(inc) and loa <= 3*(inc):
        return 0.7
    elif loa >= 3*(inc):
        return 0

def scoreCalc(c):
    if c <= 200:
        return 0
    elif c > 200 and c < 400:
        return 0.4
    elif c >= 400 and c < 700:
        return 0.7
    elif c >= 700:
        return 1

def depenCalc(d):
    if d == 0:
        return 1
    elif d > 0 and d <= 2:
        return 0.7
    elif d == 3:
        return 0.4
    elif d >= 4:
        return 0

with open('data.txt', "r+") as d:
    case = 0
    compatibility = 0
    while True:
        line = d.readline()
        case += 1
        if not line:
            break

        Xincome, Xage, Xcivil_state, Xloan, Xscore, Xdependents, Xanswear = line.split(", ")

        incomeNum = incomeCalc(income)
        Xincome = incomeCalc(int(Xincome))
        simIncome = (1 - (abs(int(Xincome) - incomeNum)/(1-0)))

        ageNum = incomeCalc(age)
        Xage = incomeCalc(int(Xage))
        simAge = (1 - (abs(int(Xage) - ageNum)/(1-0)))

        if civil_state == Xcivil_state:
            simCivil_state = 1
        else:
            simCivil_state = 0

        loanNum = loanCalc(income, loan)
        Xloan = loanCalc(int(Xincome), int(Xloan))
        simLoan = (1 - (abs(int(Xloan) - loanNum)/(1-0)))

        scoreNum = scoreCalc(score)
        Xscore = scoreCalc(int(Xscore))
        simScore = (1 - (abs(int(Xscore) - scoreNum)/(1-0)))

        dependentsNum = depenCalc(dependents)
        Xdependents = depenCalc(int(Xdependents))
        simDepen = (1 - (abs(int(Xdependents) - dependentsNum)/(1-0)))

        Xcompatibility = (((5*simIncome) + (3*simAge) + (1*simCivil_state) + (4*simLoan) + (5*simScore) + (3*simDepen)) / 21)

        if Xcompatibility > compatibility:
            mostCompatible = case
            compatibility = Xcompatibility
            answear = Xanswear

        print("case %d" %(case))
        print("income compatibility: ", simIncome)
        print("age compatibility: ", simAge)
        print("civil state compatibility: ", simCivil_state)
        print("loan compatibility: ", simLoan)
        print("score compatibility: ", simScore)
        print("dependents compatibility: ", simDepen)
        print("avarage: %f" %(Xcompatibility))
        print("")
    d.close()
    pass

with open('data.txt', "a") as e:
    e.write("%s, %s, %s, %s, %s, %s, %s" %(income, age, civil_state, loan, score, dependents, answear))
    e.close()
    pass

print("Most compatible case:", mostCompatible)
if int(answear) == 1:
    print("loan approved")
elif int(answear) == 0:
    print("loan rejected")  