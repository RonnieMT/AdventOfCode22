with open("day04input.txt") as f:
    fully_contained_pairs = 0
    for line in f.readlines():
        split_comma = line.split(",")
        # print(split_comma)
        # print(split_comma[0])
        # print(split_comma[1])
        first_split = split_comma[0].split("-")
        second_split = split_comma[1].split("-")
        # Had to get rid of the end line
        # print(split_comma)
        # print(first_split[0])
        # print(second_split[0])
        # print(first_split[1])

        # if(int(first_split[0]) <= int(second_split[0]) and int(first_split[1]) >= int(second_split[1])):
        #     fully_contained_pairs += 1
        #     # print("in if")
        # elif(int(second_split[0]) <= int(first_split[0]) and int(second_split[1]) >= int(first_split[1])):
        #     fully_contained_pairs += 1
        #     # print("in elif")

        if(int(second_split[1]) >= int(first_split[0]) >= int(second_split[0])):
            fully_contained_pairs += 1 
        elif(int(first_split[1]) >= int(second_split[0]) >= int(first_split[0])):
            fully_contained_pairs += 1
       
    print(fully_contained_pairs)
