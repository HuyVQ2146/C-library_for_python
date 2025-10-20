#include <iostream>
using namespace std;

void hello_world() {
    cout << "Hello world." << endl;
}

extern "C" {
    int add_num(int a, int b) {
        int x = a + b;
        return x;
    }

    void hello() {
        hello_world();
    }

}
