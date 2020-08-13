def solution(x,y):
    M = int(x)
    F = int(y)

    generations = 0
    previousGen = []
    stop = [1,1]
    while not (M==1 and F==1):
        if (M == F or F<=0 or M<=0):
            return "impossible"
        if (F>M):
            F = F-M
            previousGen.append([M,F])
            generations+=1
            if (stop in previousGen):
                return str(generations)
            continue          
        if (M>F):
            M = M-F
            previousGen.append([M,F])
            generations+=1
            if (stop in previousGen):
                return str(generations)
    

M = '4'
F = '7'
print(solution(M,F))