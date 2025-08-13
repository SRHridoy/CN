def ones_complement_sum(data):
    n = 8  # 8-bit chunks
    sum_bin = 0
    for i in range(0, len(data), n):
        byte = int(data[i:i+n], 2)
        sum_bin += byte
        # Carry-around addition
        sum_bin = (sum_bin & 0xFF) + (sum_bin >> 8)
    checksum = (~sum_bin) & 0xFF
    return format(checksum, '08b')

def verify_checksum(data, checksum):
    total = int(data, 2) + int(checksum, 2)
    total = (total & 0xFF) + (total >> 8)
    return total == 0xFF

# Example
data = "11010011101100"  # pad to 16 bits
data = data.zfill(16)
checksum = ones_complement_sum(data)
print("Data:", data)
print("Checksum:", checksum)
print("Verification:", verify_checksum(data, checksum))
