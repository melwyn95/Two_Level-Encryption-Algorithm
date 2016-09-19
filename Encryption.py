def conv_bit_string(pt):
    pt += "x"
    bit_string = ""
    for i in pt:
        bit_string += format(ord(i), "08b")
    return bit_string

def conv_list_of_continuous_bits(bit_string):
    matrix = []
    temp = []
    number = 0
    flag = False
    for i in bit_string:
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
        if number == 81:
            matrix.append(temp)
    return matrix

def conv_matrix_of_individual_bits(list_cont_bits):
    pass_matrix = []
    number = 0
    temp = []
    b = ""
    for i in list_cont_bits:
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

def conv_key_to_bin(key):
    return str(format(key, "036b"))


def level_1_enc(pass_matrix, key):
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

def level_2_enc(Enc, key):
    new_a = ""
    temp_list = []
    for i in range(0, 9):
        new_a = ""
        for j in range(0, 3):
            new_a += format(Enc[i][j], "03b")
        temp_list.append([new_a])
    last_nine = int(key[27:36], base=2)
    for i in range(0, 9):
        Enc[i] = format(int("".join(temp_list[i]), base=2) ^ last_nine, "09b")
    new_a_wolast = ""
    for i in range(0, 9):
        new_a_wolast += Enc[i]
    return new_a_wolast

def encrypt(pt_block, key):
    bit_string = conv_bit_string(pt_block)
    list_bit_list = conv_list_of_continuous_bits(bit_string)
    matrix = conv_matrix_of_individual_bits(list_bit_list)
    key = conv_key_to_bin(key)
    Enc = level_1_enc(matrix, key)
    ct = level_2_enc(Enc, key)
    return ct

#print encrypt("aaaaaaaaa", 47930095)
