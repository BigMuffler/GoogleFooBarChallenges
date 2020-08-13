from itertools import combinations

def solution(l):

    l.sort()
    l.reverse()

    combList = []
    integerList = []
    if (sum(l) % 3 == 0): ##if reversed list at its largest is divisble by 3 then stop the program and return
        strings = [str(l) for l in l]
        temp = "".join(strings)
        integer = int(temp)
        return integer
    else:   
        length = range(1,len(l))
        for i in length:
            comb = list(combinations(l,i))
            for j in range(len(comb)):
                if (sum(comb[j]) % 3 == 0):
                    combList.append(comb[j])

    for i in range(len(combList)):
        temp = sorted(combList[i])
        if len(temp) == 1:
            combList[i] = temp
            strings = [str(combList[i]) for combList[i] in combList[i]]
            joined = "".join(strings)
            integerList.append(int(joined))
        else:
            temp.reverse()
            combList[i] = temp
            strings = [str(combList[i]) for combList[i] in combList[i]]
            joined = "".join(strings)
            integerList.append(int(joined))

    if not integerList:
        return 0
    else:
        return max(integerList)
    

listofDigits  = [3,1,4,1,5,9]
print(solution(listofDigits))