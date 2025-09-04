#include <iostream>
int main() {
    int meters;
    int kilom;
    std::cin >> meters >> kilom;
    kilom *= 1000;
    if (kilom < meters) {
        std::cout << "kilom";
    } else if (kilom == meters) {
        std::cout << "Equals";
    } else if (kilom > meters) {
        std::cout << "meters";
    }
}
