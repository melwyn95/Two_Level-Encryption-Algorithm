def divide_in_blocks(UserInput):
    blocks = []
    number = 0
    temp = []
    for i in UserInput:
        if number % 9 == 0 and number != 0:
            blocks.append(temp)
            temp = []
            temp.append(i)
            number += 1
        else:
            temp.append(i)
            number += 1
    while len(temp) < 9:
        temp.append(" ")
    blocks.append(temp)
    return blocks
