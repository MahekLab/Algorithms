data = input("Enter the binary data to be sent : ")
divisor = input("Enter the divisor : ")


def xor(divisor, crcRes):
    res = []

    for i in range(len(divisor)) :

        # print(crcRes[i], divisor[i]) 
        res.append('0' if crcRes[i] == divisor[i] else '1')

    return ''.join(res)

def crc(data, divisor):

    n = len(divisor)
    padded_data = data + "0" * (n-1)
    print(padded_data)
   
    check = list(padded_data)
    
    for i in range(len(data)):
        if check[i] == '1':
            check[i : i+n] = xor(check[i : i+n], divisor)


    return ''.join(check[-(n-1):])

# crcRes = crc(data, divisor)
# xorRes = xor(divisor, crcRes)
# print(xorRes)


def recieverSide(data, divisor):
    print("recieved data : ",data)
    crcValue = crc(data, divisor)

    if "1" in crcValue : 
        print("Error Detected")
    else:
        print("No error detected")


crcvalue = crc(data, divisor)  # Compute CRC
final_data = data + crcvalue  # Append CRC to original data
    
print("CRC value is:", crcvalue)
print("Final data to be sent:", final_data)
    
recieverSide(final_data, divisor) 


