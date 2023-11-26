# String Compression and Decompression

## Overview
This C++ program demonstrates string compression and decompression techniques. The compression function takes a string as input and compresses it by counting consecutive occurrences of characters. The decompression functions reverse the compression process, allowing the original string to be recovered.

## Functions
### 1. `compress`
```cpp
string compress(const string& str)
```
- Compresses the input string by counting consecutive occurrences of characters.
- Returns the compressed string.

### 2. `compress2`
```cpp
string compress2(const string& str)
```
- Further compresses the string by removing counts for characters with only one occurrence.
- Returns the further compressed string.

### 3. `decompress2`
```cpp
string decompress2(const string& str)
```
- Decompresses the string by expanding characters based on the counts provided.
- Returns the decompressed string.

## Usage
1. Enter a string when prompted by the program.
2. The program will compress the string using the `compress` function and display the result.
3. It will then further compress the string using the `compress2` function and display the result.
4. Finally, it will decompress the further compressed string using the `decompress2` function and display the result.

## Example
```cpp
Enter the string: aaabbbccc
Compressed: a3b3c3
Further Compressed: a3b3c3
Decompressed: aaabbbccc
```

## Note
- The further compression (`compress2`) assumes that characters with a count of 1 are not repeated in the compressed string.

## Credits
This program was created to illustrate string compression and decompression in C++. Feel free to modify and use the code for your projects. If you have any questions or suggestions, please feel free to reach out. Happy coding! 🚀