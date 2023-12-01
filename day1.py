finalSum = 0
firstNum = 0
secondNum = 0
lineCoordinate = 0
lst = []
wordLst = []
word = ""

def isNumber(wordLst):
    word = "".join(wordLst)
    if "one" in word:
        return(1)
    if "two" in word:
        return(2)
    if "three" in word:
        return(3)
    if "four" in word:
        return(4)
    if "five" in word:
        return(5)
    if "six" in word:
        return(6)
    if "seven" in word:
        return(7)
    if "eight" in word:
        return(8)
    if "nine" in word:
        return(9)
    else:
        return(0)
    
inputFile = open("star1input.txt", "r")
lines = inputFile.readlines()

for line in lines:
    firstNum = 0
    secondNum = 0
    wordLst = []
    for element in line:
        if element.isnumeric():
            firstNum = element
            break
        else:
            if element != "\n":
                wordLst.append(element)
            if len(wordLst) >= 3:
                if isNumber(wordLst) >=1 and isNumber(wordLst) <= 9:
                    firstNum = isNumber(wordLst)
        if int(firstNum) > 0:
            break
            
    wordLst = []
    for element in reversed(line):
        if element.isnumeric():
            secondNum = element
            break
        else:
            if element != "\n":
                wordLst.append(element)
            if len(wordLst) >= 3:
                wordLst.reverse()
                if isNumber(wordLst) >=1 and isNumber(wordLst) <= 9:
                    secondNum = isNumber(wordLst)
                else:
                    wordLst.reverse()
        if int(secondNum) > 0:
            break

    lst = [firstNum, secondNum]
    stringVar = [str(i) for i in lst]
    var = int("".join(stringVar))
    lineCoordinate = int(var)
    finalSum = finalSum + lineCoordinate

print(finalSum)