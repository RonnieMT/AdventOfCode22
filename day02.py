with open("day02text.txt") as f:
    totalScore = 0
    choosingRock = 1
    choosingPaper = 2
    choosingScis = 3
    for line in f.readlines():
        match line[0]:
            # case "A":
            #     if(line[2] == "X"):
            #         totalScore += choosingRock + 3
            #     if(line[2] == "Y"):
            #         totalScore += choosingPaper + 6
            #     if(line[2] == "Z"):
            #         totalScore += choosingScis + 0
            # case "B":
            #     if(line[2] == "X"):
            #         totalScore += choosingRock + 0
            #     if(line[2] == "Y"):
            #         totalScore += choosingPaper + 3
            #     if(line[2] == "Z"):
            #         totalScore += choosingScis + 6
            # case "C":
            #     if(line[2] == "X"):
            #         totalScore += choosingRock + 6
            #     if(line[2] == "Y"):
            #         totalScore += choosingPaper + 0
            #     if(line[2] == "Z"):
            #         totalScore += choosingScis + 3
            case "A":
                if(line[2] == "X"):
                    totalScore += choosingScis + 0
                if(line[2] == "Y"):
                    totalScore += choosingRock + 3
                if(line[2] == "Z"):
                    totalScore += choosingPaper + 6
            case "B":
                if(line[2] == "X"):
                    totalScore += choosingRock + 0
                if(line[2] == "Y"):
                    totalScore += choosingPaper + 3
                if(line[2] == "Z"):
                    totalScore += choosingScis + 6
            case "C":
                if(line[2] == "X"):
                    totalScore += choosingPaper + 0
                if(line[2] == "Y"):
                    totalScore += choosingScis + 3
                if(line[2] == "Z"):
                    totalScore += choosingRock + 6
    print(totalScore)

                    

