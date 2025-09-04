#include <iostream>
int main() {
    int a;
    int b;
    std::cin >> a >> b;
    if (b % a) {
        std::cout << "True";
    } else {
        std::cout << "False";
    }
}
