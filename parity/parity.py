data = input("Enter the binary data : ")
parity = str(input("Enter the parity you want (even/odd) : "))

if parity != "even" and parity != "odd":
    print("invalid value for parity. exiting")
    exit()

print("Original data : ", data)
print("Parity : ", parity)

def checkParity(data):

    oneCounter = 0

    for i in data:
        if i == "1" :
            oneCounter += 1
         
    return oneCounter

ones = checkParity(data)
print("No. of 1s in data are : ", ones)

def parityMatcher(data, ones,parity):
    if (ones %2 == 0 and parity == "odd") or (ones %2 != 0 and parity == "even"):
        data = data + "1"
        print("After modification : ", data)

    return data

sRes = parityMatcher(data, ones, parity)


def recieverSide(data, parity):

    rOnes = checkParity(data)
    
    print("Data on Reciever side : ", data)
    print("Parity : ", parity)
    print("No. of parity bits : ", rOnes)

    if (rOnes % 2 == 0 and parity == "even") or (rOnes % 2!=0 and parity == "odd"):
        print("no error found")
    
    if (rOnes % 2 == 0 and parity == "odd") or (rOnes % 2!=0 and parity == "even"):
        print("error found")
    

recieverSide(sRes, parity)


        
