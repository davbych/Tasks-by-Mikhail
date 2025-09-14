#include <iostream>
int main() {
    int m;
    int n;
    std::cin >> m >> n;
    if (m > n) {
        std::cout << "Number m > n";
    } else if (m < n) {
        std::cout << "Number m < n";
    } else {
        std::cout << "The numbers are equal";
    }
}