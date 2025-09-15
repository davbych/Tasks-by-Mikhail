#include <iostream>
#include <string>
int main() {
    std::cout << "Please write your username: \n";
    std::string username;
    std::getline(std::cin, username);
    std::cout << "Hello " << username;
}