#include <iostream>
#include <string>
using namespace std;

int main() {
    int a = 10;
    int* ptr = &a;

    cout << a << endl;
    cout << &a << endl;
    cout << *ptr << endl;
    cout << ptr << endl;

    *ptr = 20;
    cout << a << endl;
    cout << &a << endl;
    cout << *ptr << endl;
    cout << ptr << endl;
    return 0;
}