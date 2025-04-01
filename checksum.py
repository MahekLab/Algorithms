from operator import *

# a = str(10101000110111010)
# bitSize = int(4)
a = str(input("Enter Binary bits(32) : "))
bitSize = int(input("Enter segment size : "))
# a = str(10101100110000000001111111110101)
# bitSize = int(8)
def genCheckSum(a, bitSize):
    s1 = a[0:bitSize]
    s2 = a[bitSize:bitSize*2]
    s3 = a[bitSize*2:bitSize*3]
    s4 = a[bitSize*3:bitSize*4]

    # print("segment 1",s1)
    # print(s2)
    # print(s3)
    # print(s4)
    return [s1,s2,s3,s4]

checksum = genCheckSum(a,bitSize)


def addBin(bits):
    
    s1 = bits[0]
    s2 = bits[1]
    s3 = bits[2]
    s4 = bits[3]

    a1 = bin(add(int(s1,2),int(s2,2)))
    a2 = bin(add(int(s3,2),int(s4,2)))
 
    addition = bin(add(int(a1,2), int(a2,2)))
    
    # print("a1 :",  a1[2:], "a2 :", a2[2:]) 
    # print("addition : ", addition[2:])
    # print("main : ", main[2:])
    
    # main = main[2:]
    addition = addition[2:]
    return addition



# addBin(checksum)

addition = addBin(checksum)
#  do ones compliment
# complemented = bin(add(int(addition,2), int(1)))

def compliment(num):
    tst = "";
    for i in num:
        if i == '1':
            tst = tst + "0"
        else:
           tst = tst + "1"
    return tst

addition = compliment(addition)
print("sender data : ", addition)
# compliment(addition)

    # print(complemented)
def recieve(a, bitSize, res):

    check = genCheckSum(a, bitSize)
    result = addBin(check)

    print("reciever's data : ", result)

    main = bin(add(int(result,2), int(res,2)))

    # print(check)
    # print(result)

    # print(main)
    main = main[2:]
    print("addition : ", main)
    mainRes = compliment(main)
    # mainres = int(mainRes)
    print("Checked value : ",mainRes)
    
    # checkstring = 0 *bitSize
    if mainRes == "0000000000":
        print("no error found")
    else:
        print("error found")


recieve(a,bitSize, addition)


# reciever side : 
# i/p : bits, segmentsize, previous o/p (complimented with 1)
# todo : take bits, divide them acc to segmentsize, add segmentsize
# take previous checksum and add it with current one
# take 1's compliment
