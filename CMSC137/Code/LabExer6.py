# 10/22/23
# LabExer6

# >>>>>>>>>>>>>>>>>>>>>>>>>> helper functions <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
def checksum_binary_add(bin1, bin2, max_len):
    carry = ""
    str_bin = str(bin(int(bin1,2) + int(bin2,2)))[2:]
    if len(str_bin) > max_len:
        carry = str_bin[0]
        str_bin = str_bin[1:]
    if carry != "":
        str_bin = bin(int(str_bin, 2) + int(carry,2))[2:].zfill(max_len)

    return str(str_bin)

# >>>>>>>>>>>>>>>>>>>>>>>>>> user functions <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
def parity_check():
    dataword: str = input()
    codeword: str = input()

    dword_count: int = dataword.count("1")

    gen_codeword = str(dataword)
    if dword_count % 2 == 0:
        gen_codeword += "0"
    elif dword_count % 2 != 0:
        gen_codeword += "1"
        
    print(f"Codeword:{gen_codeword}")
    if codeword == gen_codeword:
        print("Data word: Accepted")
    else:
        print("Data word: Discarded")

def twod_parity_check():
    input_str = input()
    bytewords = [input_str[i:i+9] for i in range(0, len(input_str), 9)]
    col_count = [0] * len(bytewords[0])
    row_count = []
    error_count = 0

    for i in range(0,len(bytewords) - 1):
        rc = 0
        for j in range(0,8):
            if bytewords[i][j] == "1":
                col_count[j] += 1
                rc += 1
        row_count.append(rc)

    lc_bits = ""
    lr_bits = ""
    for i in range(0,8):
        curr = bytewords[4][i]
        lr_bits += curr
        if (curr == "1" and col_count[i] % 2 == 0) or (curr == "0" and col_count[i] % 2 != 0):
            error_count += 1

    for i in range(0,4):
        curr = bytewords[i][8]
        lc_bits += curr
        if (curr == "1" and row_count[i] % 2 == 0) or (curr == "0" and row_count[i] % 2 != 0):
            error_count += 1

    if (lc_bits.count("1") % 2 == 0 and bytewords[4][8] == "1") or (lc_bits.count("1") % 2 != 0 and bytewords[4][8] == "0"):
        error_count += 1

    if (lr_bits.count("1") % 2 == 0 and bytewords[4][8] == "1") or (lr_bits.count("1") % 2 != 0 and bytewords[4][8] == "0"):
        error_count += 1
    print(f"Error count: {error_count}")


def checksum():
    input_str: str = input()

    bytewords = [input_str[i:i+7] for i in range(0, len(input_str), 7)]
    sum = bytewords[0] 
    for b in bytewords[1:]:
        sum = checksum_binary_add(sum, b, 7)

    print(sum)
    # if "0" not in sum:
    #     print("Accept data")
    # else:
    #     print("Reject data")

def crc():
    data: str = input()
    keyword: str = input()

    rem = bin(int(data,2) // int(keyword,2))
    if keyword == str(bin(int(data,2) // int(rem,2)))[2:].zfill(len(keyword)):
        print("Accept data")
    else:
        print("CRC error detected")


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> main <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
def main():
    input_num: str = input()
    if input_num == "1":
        parity_check()
    elif input_num == "2":
        twod_parity_check()
    elif input_num == "3":
        checksum()
    elif input_num == "4":
        crc()

if __name__ == "__main__":
    main()
