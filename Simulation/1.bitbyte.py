# Bit Stuffing
def bit_stuffing(data):
    count = 0
    stuffed = ""
    for bit in data:
        if bit == '1':
            count += 1
            stuffed += bit
        else:
            count = 0
            stuffed += bit
        if count == 5:
            stuffed += '0'  # Insert 0 after five consecutive 1s
            count = 0
    return stuffed

def bit_unstuffing(stuffed):
    count = 0
    unstuffed = ""
    for bit in stuffed:
        if bit == '1':
            count += 1
            unstuffed += bit
        else:
            if count == 5 and bit == '0':
                count = 0  # Remove stuffed 0
            else:
                unstuffed += bit
            count = 0
    return unstuffed

# Byte Stuffing
def byte_stuffing(data, flag='01111110', escape='11100000'):
    stuffed = ''
    for i in range(0, len(data), 8):
        byte = data[i:i+8]
        if byte == flag or byte == escape:
            stuffed += escape + byte
        else:
            stuffed += byte
    return stuffed

def byte_unstuffing(stuffed, escape='11100000'):
    unstuffed = ''
    i = 0
    while i < len(stuffed):
        if stuffed[i:i+8] == escape:
            i += 8
            unstuffed += stuffed[i:i+8]
        else:
            unstuffed += stuffed[i:i+8]
        i += 8
    return unstuffed

# Example
data = "01111110111111011111"
print("Original Data:        ", data)
bs = bit_stuffing(data)
print("Bit Stuffed Data:     ", bs)
bu = bit_unstuffing(bs)
print("Bit Unstuffed Data:   ", bu)

byte_data = "0111111001111110"  # Two flags to stuff
bst = byte_stuffing(byte_data)
print("Byte Stuffed Data:    ", bst)
but = byte_unstuffing(bst)
print("Byte Unstuffed Data:  ", but)
