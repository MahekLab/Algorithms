# data is the actual binary data
# crc is the polynomial from which we will divide our data
# CRC has pure data + redundant bits as finding errors in the pure data is hard.
# CRC uses a (M + r) format. M is the data and R is the redundant bits

# No. of redundant bits is the power of the polynomial(highest power)
# those no. of redundant bits will be appended to the actual data

# eg : data : 10101010 ; polynomial : x4+x2+1
# here, the data will be : 101010100000 (we will append 4 zeros to the end as the highest power in the polynomial is 4)
# This data will be sent to the reciever

# to get the divisor, we have to take the coefficients of the polynomial. the elements present in the original polynomial will have 1 coefficients while those which should come according to the sequence but aren't present originally in the polynomial will have 0 coefficient. 
# eg : x4+x2+1 ; this will be expanded to 1x4+0x3+1x2+0x+1 ; this will have the divisor be: 10101010

# in case the actual divisor is given directly in the question, we have to append only the len(divisor)-1 0s to the actual data

# Now we divide the data and the divisor. using the XOR operator.

#now the remainder we get from this division, will be the codeword which will replace our original added 0s. 

# so this original data with the new found reminder codeword together will be sent to the reeciever as one. the reciever willdivide the entire recieved data with the divisor

# if the data is all 0s then there is no error. if there is any error then atleast 1 bit in the remainder will be 1. and the error is detected.

