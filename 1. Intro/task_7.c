#include <iostream>
int main() {
// 1 zadanie
    int r;
    std::cin >> r;
    std::cout << "diameter: " << r * 2;

// 2 zadanie
    for (int i = 100; i <= 500; i++) {
        std::cout << i + i;
    }

//3 zadanie
    int a;
    std::cin >> a;
    for (a; a<500; a++) {
        std::cout << a + a;
    }
}