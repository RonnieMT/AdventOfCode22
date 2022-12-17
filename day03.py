with open("day03input.txt") as f:
    points = 0
    #for line in f.readlines():
    #    if(line == "\n") : continue
    #    # sol to first part
    #    firstString, secondString = line[:len(line)//2], line[len(line)//2:]
    #    common = ''.join(set(firstString).intersection(secondString))
    #    #print(common)
    #    if(ord(common) < 97):
    #        # add 27 because thats the points that capital letters start at, and subtract 65 to 
    #        # figure out what char it is
    #        points += 27 + ord(common) - 65
    #    else:
    #        points += 1 + ord(common) - 97

    #print(len(f.readlines()))
    
    inputFile = f.read().splitlines()
    for i in range(0, len(inputFile)-1, 3):
        string1 = inputFile[i]
        string2 = inputFile[i+1]
        string3 = inputFile[i+2]
        common = set(string1).intersection(string2)
        common = set(common).intersection(string3)
        common = list(common)
        if(ord(common[0]) < 97):
           # add 27 because thats the points that capital letters start at, and subtract 65 to 
           # figure out what char it is
            points += 27 + ord(common[0]) - 65
        else:
            points += 1 + ord(common[0]) - 97

    print(points)

