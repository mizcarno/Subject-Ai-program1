def readScore():
    score=int(input("INPUT SCORE : "))
    return score

def printGrade(G):
    print(str(G))

def computGrade(score):
    if(score>=80 and score<=100):
        Gard=str("Your Score is A")
    elif(score>=75 and score<=79):
        Gard=str("Your Score is B+")
    elif(score>=70 and score<=74):
        Gard=str("Your Score is B")
    elif(score>=65 and score<=69):
        Gard=str("Your Score is C+")
    elif(score>=60 and score<=64):
        Gard=str("Your Score is C")
    elif(score>=55 and score<=59):
        Gard=str("Your Score is D+")
    elif(score>=50 and score<=54):
        Gard=str("Your Score is D")
    elif(score>=0 and score<=49):
        Gard=str("Your Score is F")
    else:
        Gard=str("In Put Number 1-100")
    return Gard

sr=int(readScore())
gard=str(computGrade(sr))  
printGrade(gard)
