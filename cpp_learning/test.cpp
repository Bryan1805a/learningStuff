#include <iostream>
#include <string>
using namespace std;

void hello_world(string a) {
    cout << "Hello" << " " << a << endl;
};

int main() {
    string name;
    getline (cin, name);
    hello_world(name);
    return 0;
}
