def conv_list_of_continuous_bits(ct):
    number = 0
    temp = []
    matrix = []
    flag = False
    for i in ct:
        if number == 79:
            temp.append(i)
            temp.append("0")
            matrix.append(temp)
        if number%9 == 0 and number != 0:
            matrix.append(temp)
            temp = []
            temp.append(i)
            number += 1
        else:
            temp.append(i)
            number += 1  
    return matrix

def level_2_dec(matrix, key):
    Dec = [[], [], [], [], [], [], [], [], []]
    for i in range(0, 9):
        Dec[i].append(int("".join(matrix[i]), base=2))
    last_nine = int(key[27:36], base=2)
    for i in range(0, 9):
        Dec[i] = format(Dec[i][0] ^ last_nine, "09b")
    return Dec   

def conv_matrix_of_individual_bits(Dec):
    pass_matrix = []
    number = 0
    temp = []
    b = ""
    for i in Dec:
        temp = []
        number = 0
        pass_temp = []
        for j in i:
            b += j
            if number == 9:
                break
            if number % 3 == 0 and number != 0:
                pass_temp.append(temp)
                temp = []
                temp.append(j)
                number += 1
            else:
                temp.append(j)
                number += 1
        pass_temp.append(temp)
        pass_matrix.append(pass_temp)
    return pass_matrix   


def level_1_dec(pass_matrix, key):
    Enc = [[], [], [], [], [], [], [], [], []]
    k = 0
    for i in range(0, 9, 3):
        for j in range(0, 3):
            M = [   int("".join(pass_matrix[i][j]), base=2),
                    int("".join(pass_matrix[i+1][j]), base=2),
                    int("".join(pass_matrix[i+2][j]), base=2)
                ]
            first_three = int(key[k:k+3], base=2)
            k += 3
            M[0] = M[0] ^ first_three
            M[1] = M[1] ^ first_three
            M[2] = M[2] ^ first_three
            Enc[i].append(M[0])
            Enc[i+1].append(M[1])
            Enc[i+2].append(M[2])
    return Enc

def conv_ct_to_pt(Enc):
    bit_string = ""
    for i in Enc:
        for j in i:
            bit_string += format(j, "03b")
    pt = ""
    for i in range(0, 80, 8):
        pt += chr(int(bit_string[i:i+8], base=2))
    return pt[:len(pt)-1]

def conv_key_to_bin(key):
    return str(format(key, "036b"))

def decrypt(ct, key):
    matrix = conv_list_of_continuous_bits(ct)
    key = conv_key_to_bin(key)
    Dec = level_2_dec(matrix, key)
    pass_matrix = conv_matrix_of_individual_bits(Dec)
    original_bits = level_1_dec(pass_matrix, key)
    pt = conv_ct_to_pt(original_bits)
    return pt

#ct = "000101101101101010111100100001001111001110101000000001111110010000100011110000000"
#print decrypt(ct, 47930095)
