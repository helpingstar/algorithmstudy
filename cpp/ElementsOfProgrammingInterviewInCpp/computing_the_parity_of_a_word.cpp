#include <iostream>

short Parity(unsigned long long x) {
    short result = 0;
    while (x) {
        result ^= (x & 1);
        x >>= 1;
    }
    return result;
}

int main() {
    std::cout << Parity(234234234) << std::endl;
}