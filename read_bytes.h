//
// Created by hkaz0 on 10/6/24.
//

#ifndef SBM_READ_BYTES_H
#define SBM_READ_BYTES_H

#endif //SBM_READ_BYTES_H

#include <iostream>
#include <string>
#include "cstdint"
#include <fstream>
#include <filesystem>

using namespace std;
namespace fs = filesystem;

class ByteReader {
public:
    vector<byte> bytestream;
    int position = 0;
    explicit ByteReader(vector<byte> &bytes) {
        position = 0;
        bytestream = bytes;
    }
    // Use little endian for everything
    int8_t readInt8() {
        auto value = static_cast<int8_t>(bytestream.at(position));
        position += 1;
        return value;
    }
    uint8_t readUInt8() {
        auto value = static_cast<uint8_t>(bytestream.at(position));
        position += 1;
        return value;
    }
    string readHex() {
        string value;
        uint8_t byte = readInt32();
        // convert uint8 to hex
        char hex[3];
        sprintf(hex, "%02X", byte);
        value += hex;
        return value;
    }
    int16_t readInt16() {
        auto value = static_cast<int16_t>(bytestream.at(position) | bytestream.at(position + 1) << 8);
        position += 2;
        return value;
    }
    uint16_t readUInt16() {
        auto value = static_cast<uint16_t>(bytestream.at(position) | bytestream.at(position + 1) << 8);
        position += 2;
        return value;
    }
    int32_t readInt32() {
        auto value = static_cast<int32_t>(bytestream.at(position) | bytestream.at(position + 1) << 8 | bytestream.at(position + 2) << 16 | bytestream.at(position + 3) << 24);
        position += 4;
        return value;
    }
    uint32_t readUInt32() {
        auto value = static_cast<uint32_t>(bytestream.at(position) | bytestream.at(position + 1) << 8 | bytestream.at(position + 2) << 16 | bytestream.at(position + 3) << 24);
        position += 4;
        return value;
    }
    int64_t readInt64() {
        auto value = static_cast<int64_t>(bytestream.at(position) | bytestream.at(position + 1) << 8 | bytestream.at(position + 2) << 16 | bytestream.at(position + 3) << 24 | bytestream.at(position + 4) << 32 | bytestream.at(position + 5) << 40 | bytestream.at(position + 6) << 48 | bytestream.at(position + 7) << 56);
        position += 8;
        return value;
    }
    uint64_t readUInt64() {
        auto value = static_cast<uint64_t>(bytestream.at(position) | bytestream.at(position + 1) << 8 | bytestream.at(position + 2) << 16 | bytestream.at(position + 3) << 24 | bytestream.at(position + 4) << 32 | bytestream.at(position + 5) << 40 | bytestream.at(position + 6) << 48 | bytestream.at(position + 7) << 56);
        position += 8;
        return value;
    }
    string readString() {
        string value;
        int length = readInt32();
        if (length == 0) {
            return "";
        }
        if (length > (bytestream.size() - position)) {
            throw runtime_error("String length exceeds bytestream size");
        }
        for (int i = 0; i < length; i++) {
            char letter = (readInt8());
            if (letter == '\0') {
//                cout << "Null terminator found at position " << i << endl;
//                break;
            } else {
                value += letter;
            }
        }
        return value;
    }

};