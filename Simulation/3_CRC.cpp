#include <bits/stdc++.h>
using namespace std;

uint64_t computeCRC(uint64_t data, int dataLen, uint64_t generator, int genLen) {
    // Align generator with the highest bit of the data
    uint64_t mask = 1ULL << (dataLen - 1);
    uint64_t genMask = generator << (dataLen - genLen);

    while (mask >= (1ULL << (genLen - 1))) {
        if (data & mask) { // If MSB is 1, XOR with generator
            data ^= genMask;
        }
        mask >>= 1;
        genMask >>= 1;
    }
    return data; // Remainder is in lower (genLen - 1) bits
}

int main() {
    cout << "=== Bitwise CRC Calculator ===\n";
    string dataStr, genStr;
    cout << "Enter binary data: ";
    cin >> dataStr;
    cout << "Enter generator polynomial (binary): ";
    cin >> genStr;

    int dataLen = dataStr.size();
    int genLen = genStr.size();

    // Convert binary strings to integers
    uint64_t data = 0, generator = 0;
    for (char c : dataStr) data = (data << 1) | (c - '0');
    for (char c : genStr) generator = (generator << 1) | (c - '0');

    // Append zeros to data for CRC calculation
    uint64_t dataPadded = data << (genLen - 1);
    uint64_t remainder = computeCRC(dataPadded, dataLen + genLen - 1, generator, genLen);

    // Encode: Append remainder to data
    uint64_t encoded = dataPadded | remainder;

    cout << "\nRemainder: ";
    for (int i = genLen - 2; i >= 0; i--) cout << ((remainder >> i) & 1);
    cout << "\nEncoded data: ";
    for (int i = dataLen + genLen - 2; i >= 0; i--) cout << ((encoded >> i) & 1);

    // Decoding check (no error case)
    uint64_t checkRem = computeCRC(encoded, dataLen + genLen - 1, generator, genLen);
    cout << "\nDecoding check: " << (checkRem == 0 ? "No error detected." : "Error detected!") << "\n";

    // Error detection test — flip one bit
    uint64_t corrupted = encoded ^ (1ULL << (dataLen + 1)); // Flip 3rd MSB
    cout << "\nCorrupted data: ";
    for (int i = dataLen + genLen - 2; i >= 0; i--) cout << ((corrupted >> i) & 1);

    uint64_t corruptRem = computeCRC(corrupted, dataLen + genLen - 1, generator, genLen);
    cout << "\nError check after corruption: " << (corruptRem == 0 ? "No error detected!" : "Error detected!") << "\n";
}
