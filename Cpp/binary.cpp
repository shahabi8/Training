
/*
In memory (little-endian), the 4-byte integer 42 is stored as:

    0x2a 0x00 0x00 0x00
    Which in binary is:
        00101010 00000000 00000000 00000000
    



*/




#include <iostream>
#include <string>
#include <cstring> // Include the appropriate header for memcpy
#include <bitset>

// Function to convert an integer to its binary data representation in a string
std::string intToBinaryData(int num) {
    std::string binaryData;
    binaryData.resize(sizeof(int));
    // Copy the bytes of the integer into the string
    std::memcpy(&binaryData[0], &num, sizeof(int));
    return binaryData;
}

std::string intToBinaryString(int num) {
    // Convert the integer to a 32-bit binary representation
    std::bitset<32> binary(num);
    return binary.to_string();
}

// Function to retrieve the integer from its binary data representation in a string
int binaryDataToInt(const std::string& binaryData) {
    int num = 0;
    if (binaryData.size() >= sizeof(int)) {
        std::memcpy(&num, binaryData.data(), sizeof(int)); // Copy bytes back to integer
    }
    return num;
}

int main() {
    int number = 42; // Example integer
    std::string binaryData = intToBinaryData(number);

    std::cout << "Integer: " << number << std::endl;
    std::cout << "Binary Data in hex:";
    for (unsigned char c : binaryData) {
        std::cout << " " << std::hex << static_cast<int>(c);
    }
    std::cout << std::endl;

    std::string binaryString = intToBinaryString(number);
    std::cout << "Binary Representation: " << binaryString << std::endl;

    // Convert back to integer from binary data
    int retrievedNumber = binaryDataToInt(binaryData);
    std::cout << "Retrieved Integer: " << std::dec << retrievedNumber << std::endl;

    return 0;
}