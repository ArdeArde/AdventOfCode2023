import re

theAnswer = 0

inputFile = open("star2Input.txt", "r")
lines = inputFile.readlines()

for line in lines:
    handSum = 0
    redAmount = 0
    blueAmount = 0
    greenAmount = 0
    lineLst = line.split(":")
    hands = re.split(", |;", lineLst[1])
    for item in hands:
        handSplit = item.split()
        handNumber = handSplit[0]
        handColor = handSplit[1]
        if handColor == "red":
            if int(handNumber) > int(redAmount):
                redAmount = handNumber
        if handColor == "blue":
            if int(handNumber) > int(blueAmount):
                blueAmount = handNumber
        if handColor == "green":
            if int(handNumber) > int(greenAmount):
                greenAmount = handNumber
    handSum = int(redAmount) * int(blueAmount) * int(greenAmount) 
    theAnswer = theAnswer + handSum

print(theAnswer)