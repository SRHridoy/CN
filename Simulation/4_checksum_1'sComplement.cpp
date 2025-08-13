#include<bits/stdc++.h>
using namespace std;

uint8_t onesComplementAdd(uint8_t a, uint8_t b) {
    uint16_t sum = a + b; // might overflow
    if (sum > 0xFF) sum = (sum & 0xFF) + 1; // wrap carry
    return static_cast<uint8_t>(sum);
}

uint8_t computeChecksum(const vector<uint8_t>& data) {
    uint8_t sum = 0;
    for (uint8_t word : data) {
        sum = onesComplementAdd(sum, word);
    }
    return ~sum; // 1's complement
}

bool verifyData(const vector<uint8_t>& data) {
    uint8_t sum = 0;
    for (uint8_t word : data) {
        sum = onesComplementAdd(sum, word);
    }
    return sum == 0xFF; // If sum = all 1's, data OK
}

int main() {
    int n;
    cout << "Enter number of 8-bit words: ";
    cin >> n;

    vector<uint8_t> data(n);
    cout << "Enter data words in binary (8 bits each):\n";
    for (int i = 0; i < n; i++) {
        string bits;
        cin >> bits;
        data[i] = bitset<8>(bits).to_ulong();
    }

    uint8_t checksum = computeChecksum(data);
    cout << "Computed Checksum: " << bitset<8>(checksum) << "\n";

    // Encoding (append checksum)
    data.push_back(checksum);

    // Verification
    if (verifyData(data))
        cout << "No Error Detected.\n";
    else
        cout << "Error Detected!\n";

    return 0;
}
