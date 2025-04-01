from operator import *

data = input("Enter 32 bit Binary data : ")
bitSize = int(input("Enter Segment Size : "))

if len(data) > 32:
    print("Data exceedes limit (32).")
    exit() 

def genCheckSum(data, bitSize):
   
    s1 = data[0 : bitSize]
    s2 = data[bitSize : bitSize * 2]
    s3 = data[bitSize * 2 : bitSize * 3]
    s4 = data[bitSize * 3 : bitSize * 4]

    return [s1,s2,s3,s4]

bits = genCheckSum(data, bitSize)


def wrappedAddition(binary_str, bit_size):
    num = int(binary_str, 2)
    while num >= (1 << bit_size):  
        num = (num % (1 << bit_size)) + (num >> bit_size)  
    return f"{num:0{bit_size}b}"

def addBits(bits):
    s1, s2, s3, s4 = bits

    a1 = wrappedAddition(bin(add(int(s1, 2), int(s2, 2)))[2:], bitSize)
    a2 = wrappedAddition(bin(add(int(s3, 2), int(s4, 2)))[2:], bitSize)
    finalSum = wrappedAddition(bin(add(int(a1, 2), int(a2, 2)))[2:], bitSize)

    print("Segment 1 + Segment 2:", a1)
    print("Segment 3 + Segment 4:", a2)
    print("Final Sum (Wrapped to {} bits):".format(bitSize), finalSum)
    
    return finalSum
bitSum = addBits(bits)

def complement(a):
    res = "" 

    for i in a:
        if i == '1':
            res = res + '0'
        else:
            res = res + '1'
        
    return res

checksum = complement(bitSum)
print("Sender side : ", checksum)

def recieverSide(data, bitSize,checksum):

    check = genCheckSum(data,bitSize)
    rAddition = addBits(check)

    finalAddition = bin(add(int(rAddition,2), int(checksum,2)))[2:]

    finalRes = complement(finalAddition)
    print(finalRes)

recieverSide(data, bitSize, checksum)

    
