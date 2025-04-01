from operator import *

data = input("Enter 32 bit Binary data : ")
bitSize = int(input("Enter segment size : "))

def genCheckSum(data, bitSize):
    s1 = data[0:bitSize]
    s2 = data[bitSize:bitSize*2]
    s3 = data[bitSize*2:bitSize*3]
    s4 = data[bitSize*3:bitSize*4]


    # print("Segment 1 : ",s1)
    # print("Segment 2 : ",s2)
    # print("Segment 3 : ",s3)
    # print("Segment 4 : ",s4)

    return [s1,s2,s3,s4]
bits = genCheckSum(data,bitSize)
print(bits)
def addBin(bits):
    s1,s2,s3,s4 = bits

    a1 = bin(add(int(s1,2),int(s2,2)))
    a2 = bin(add(int(s3,2),int(s4,2)))
    
    addition = bin(add(int(a1,2),int(a2,2)))

    addition = addition[2:]
    return addition

    

print(addBin(bits))
