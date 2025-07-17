#include <iostream>
#include <string>
using namespace std;

int main() {
    string my_name;
    getline (cin, my_name);

    cout << "Hello" << " " << my_name;
    return 0;
}