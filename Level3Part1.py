import numpy as np
from fractions import Fraction 
    
def solution(m):
    newMatrix = []
    I = []
    Q = []
    qAndR = []
    for i in range(len(m)):
        temp = m[i]
        totalSumRow = sum(temp)
        if (totalSumRow != 0 and totalSumRow != 1) :           
            newRow = [Fraction(number,totalSumRow) for number in temp]
            qAndR.append(newRow)
        else:
        ## Need at 1's in appropriate empty rows to make a true Absorbing Markov Matrix
            temp[i] = 1
            newRow = temp
            I.append(newRow)
        newMatrix.append(newRow)
    
    I.reverse()
    indices = []
    for i in range(len(I)):
        I[i].reverse()
        indices.append(I[i].index(1))
        size = list(range(len(I[i])))

    ## Extracting 0 columns for matrix
    for i in size[:]:
      if i in indices:
          size.remove(i) ##size will now store indices of zero columns
    
    sizeOfIndentity = len(I[0]) - len(size)
    
    ## Create Q and R Matrix
    indicesToReverse = list(reversed(range(sizeOfIndentity , len(I[0]))))
    for i in range(len(qAndR)):
        qAndR[i].reverse()
        temp = []
        for j in indicesToReverse:
            temp.append(qAndR[i][j])
            qAndR[i].pop(j) ##qandR become just R at this point 
        Q.append(temp)

    ## Calculations 
    sol = Calculations(Q,qAndR)
    newSol = []
    for i in range(len(sol)):
        fracValue = Fraction(sol[i]).limit_denominator(1000000)
        newSol.append(fracValue)
    
    ## Extract numerators and Denominators
    denominators = []
    numerators = []
    for i in range(len(newSol)):
        denominators.append(newSol[i].denominator)

    maxDenom = max(denominators)
    for i in range(len(newSol)):
        if(newSol[i].denominator != maxDenom):
            ratio = maxDenom / newSol[i].denominator
            newNumerator = newSol[i].numerator * ratio
            numerators.append(newNumerator)
        else:
            numerators.append(newSol[i].numerator)

    numerators.reverse()
    numerators.append(maxDenom)
    solution = [int(i) for i in numerators]

    return solution

def Calculations(Q,R):
    ##Create Appropriate Identity
    sizeOfIndentity = len(Q)
    I = np.eye(sizeOfIndentity)
    arrQ = np.array(Q,dtype= float)
    fPrime = I - arrQ
    F = np.linalg.inv(fPrime)
    sol = F@R

    return sol[0]

defineInputState = [
                    [0,2,1,0,0],
                    [0,0,0,3,4],
                    [0,0,0,0,0],
                    [0,0,0,0,0],
                    [0,0,0,0,0],
                    ]

print(solution(defineInputState))