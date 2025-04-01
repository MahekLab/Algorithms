
from operator import *

a = str(input("Enter Binary bits(32) : "))
bitSize = int(input("Enter segment size : "))

def genCheckSum(a, bitSize):
    s1 = a[0:bitSize]
    s2 = a[bitSize:bitSize*2]
    s3 = a[bitSize*2:bitSize*3]
    s4 = a[bitSize*3:bitSize*4]

    return [s1,s2,s3,s4]

checksum = genCheckSum(a,bitSize)


def addBin(bits):
    
    s1 = bits[0]
    s2 = bits[1]
    s3 = bits[2]
    s4 = bits[3]

    a1 = bin(add(int(s1,2),int(s2,2)))
    a2 = bin(add(int(s3,2),int(s4,2)))
    
    print(a1)
    print(a2)

    addition = bin(add(int(a1,2), int(a2,2)))
    
    addition = addition[2:]
    return addition


addition = addBin(checksum)

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

def recieve(a, bitSize, res):
    
    check = genCheckSum(a, bitSize)
    result = addBin(check)

    print("reciever's data : ", result)

    main = bin(add(int(result,2), int(res,2)))


    main = main[2:]
    print("addition : ", main)
    mainRes = compliment(main)
    print("Checked value : ",mainRes)
    
    if mainRes == "0000000000":
        print("no error found")
    else:
        print("error found")


recieve(a,bitSize, addition)

