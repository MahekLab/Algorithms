
# XOR function compares two strings bit by bit and returns the result
def xor(check, polynomial):
    result = []
    for i in range(len(polynomial)):
        # If bits are the same, add '0', if not, add '1'
        if check[i] == polynomial[i]:
            result.append('0')
        else:
            result.append('1')
    return ''.join(result)

# CRC function adds padding and performs the division (like long division)
def crc(data, polynomial):
    n = len(polynomial)  # Length of the polynomial
    padded_data = data + '0' * (n - 1)  # Add zeros to data to prepare for division
    check = list(padded_data)  # Convert the padded data into a list to manipulate

    # Perform the division for each bit in the data
    for i in range(len(data)):
        # If the current bit is '1', perform XOR with the polynomial
        if check[i] == '1':
            check[i:i + n] = xor(check[i:i + n], polynomial)  # Perform XOR

    # Return the remainder (the last n-1 bits after division)
    return ''.join(check[-(n - 1):])

# Receiver function checks if the received data has no error
def receiver(data, polynomial):
    print("Data received:", data)
    # Get the CRC value from the received data (remove the CRC part before checking)
    crcvalue = crc(data[:-len(polynomial) + 1], polynomial)
    
    # If there are any '1's in the CRC value, an error occurred
    if '1' in crcvalue:
        print("Error detected\n")
    else:
        print("No error detected\n")

# Main function to run the CRC process
def main():
    data = input("Enter data: ")  # Get the data to send
    polynomial = input("Enter the polynomial: ")  # Get the CRC polynomial

    # Generate the CRC value and append it to the data
    crcvalue = crc(data, polynomial)
    final_data = data + crcvalue
    
    # Show the results
    print("CRC value:", crcvalue)
    print("Final data to be sent:", final_data)
    
    # Simulate receiver checking the received data
    receiver(final_data, polynomial)

# Run the program
if __name__ == "__main__":
    main()
