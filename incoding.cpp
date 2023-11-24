#include <iostream>
#include <string>
using namespace std;

// Function to compress the string
string compress(const string& str) {
    string compressed;
    int count = 1;
    for (int i = 1; i <= str.length(); ++i) {
        if (i == str.length() || str[i] != str[i-1]) {
            compressed += str[i-1] + to_string(count);
            count = 1;
        } else {
            ++count;
        }
    }
    return compressed;
}

// Function to further compress the string
string compress2(const string& str) {
    string compressed2;
    for (int i = 0; i < str.length(); i += 2) {
        if (str[i+1] == '1') {
            compressed2 += str[i];
        } else {
            compressed2 += str[i] + str[i+1];
        }
    }
    return compressed2;
}

// Function to decompress the string
string decompress2(const string& str) {
    string decompressed;
    for (int i = 0; i < str.length(); i += 2) {
        decompressed += string(str[i+1]-'0', str[i]);
    }
    return decompressed;
}

int main(){
    string str ;
    cout << "Enter the string: ";
    cin >> str;
    string compressed = compress(str);
    cout << "Compressed: " << compressed << std::endl;

    string compressed2 = compress2(compressed);
    cout << "Further Compressed: " << compressed2 << std::endl;

    string decompressed = decompress2(compressed2);
    cout << "Decompressed: " << decompressed << std::endl;

    return 0;
}