with open("day01text.txt") as f:
 
    elfNum = 1
    finalElfNum = 1
    maxCals = 0
    tempCals = 0
    elfList = []
    i = 0
    for line in f.readlines():
        #print(line)
        if(line == "\n"):
            if(maxCals < tempCals):
                maxCals = tempCals
                finalElfNum = elfNum
            elfList.append(tempCals)
            i += 1
            tempCals = 0
            elfNum += 1
            continue
        #print(tempCals)
        tempCals += int(line)
    print(maxCals)

    maxElfCals = sorted(elfList)
    print(maxElfCals[len(maxElfCals)-1] + maxElfCals[len(maxElfCals)-2] + maxElfCals[len(maxElfCals)-3])
