def xor(a, b):
    result = ''
    for i in range(len(b)):
        result += '0' if a[i] == b[i] else '1'
    return result

def crc(data, key):
    key_length = len(key)
    appended_data = data + '0'*(key_length-1)
    remainder = appended_data[:key_length]

    for i in range(len(data)):
        if remainder[0] == '1':
            remainder = xor(remainder, key) + (appended_data[key_length + i] if key_length + i < len(appended_data) else '')
        else:
            remainder = xor('0'*key_length, remainder) + (appended_data[key_length + i] if key_length + i < len(appended_data) else '')
        remainder = remainder[1:]  # Shift left by one bit
    return remainder

# Example
data = "1101011011"
key = "10011"
remainder = crc(data, key)
encoded = data + remainder
print("Original Data:", data)
print("CRC Remainder:", remainder)
print("Encoded Data with CRC:", encoded)
