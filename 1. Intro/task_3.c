#include <iostream>
int main() {
    int a;
    std::cin >> a;
    for (int i = 0; i <= 9; i++) {
        std::cout << a << "*" << i << "=" << a*i << "\n";  
    }
}