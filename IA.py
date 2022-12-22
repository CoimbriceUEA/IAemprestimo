income = int(input("income: "))
age = int(input("age: "))
civil_state = str(input("civil state(s, c): "))
loan = int(input("loan: "))
score = int(input("score: "))
dependents = int(input("dependents: "))
answear = 0

print("")

def incomeCalc(inc, xinc):
    dif = abs(inc - xinc)
    if dif >= 0 and dif < 2000:
           return 1
    elif dif >= 2000 and dif < 5000:
           return 0.7
    elif dif >= 5000 and dif <= 8000:
           return 0.4
    elif dif > 8000:
           return 0

def ageCalc(age, xage):
    dif = abs(age - xage)
    if dif >= 0 and dif < 5:
           return 1
    elif dif >= 5 and dif < 8:
        return 0.7
    elif dif >= 8 and dif <= 12:
        return 0.4
    elif dif > 12:
        return 0

def civCalc(civ, xciv):
    if civ != xciv:
        return 0
    else:
        return 1

def loanCalc(loa, xloa):
    dif = abs(loa - xloa)
    if dif < 2_000:
        return 1
    elif dif >= 2_000 and dif < 5_000:
        return 0.7
    elif dif >= 5_000 and dif < 10_000:
        return 0.4
    elif dif >= 10_000 and dif < 20_000:
        return 0.2
    elif dif >= 20_000:
        return 0

def scoreCalc(sco, xsco):
    dif = abs(sco - xsco)
    if dif <= 200:
        return 1
    elif dif > 200 and dif < 400:
        return 0.7
    elif dif >= 400 and dif < 800:
        return 0.4
    elif dif >= 800:
        return 0

def depenCalc(dep, xdep):
    if dep != xdep:
        return 0
    else:
        return 1

with open('data.txt', "r+") as d:
    case = 0
    compatibility = 0
    while True:
        line = d.readline()
        case += 1
        if not line:
            break

        Xincome, Xage, Xcivil_state, Xloan, Xscore, Xdependents, Xanswear = line.split(", ")

        incomeCompat = incomeCalc(income, int(Xincome))
        ageCompat = ageCalc(age, int(Xage))
        civCompat = civCalc(civil_state, Xcivil_state)
        loanCompat = loanCalc(loan, int(Xloan))
        scoreCompat = scoreCalc(score, int(Xscore))
        depenCompat = depenCalc(dependents, int(Xdependents))

        caseCompatibility = (((5*incomeCompat) + (3*ageCompat) + (1*civCompat) + (4*loanCompat) + (5*scoreCompat) + (3*depenCompat)) / 21)

        if caseCompatibility > compatibility:
            mostCompatible = case
            compatibility = caseCompatibility
            answear = Xanswear

        print("case %d" %(case))
        print("income compatibility: ", incomeCompat)
        print("age compatibility: ", ageCompat)
        print("civil state compatibility: ", civCompat)
        print("loan compatibility: ", loanCompat)
        print("score compatibility: ", scoreCompat)
        print("dependents compatibility: ", depenCompat)
        print("avarage: %f" %(caseCompatibility))
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