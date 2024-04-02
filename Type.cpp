#include <iostream>
#include <typeinfo>
using namespace std;

int main(){

    const char* a = "dkdk";

    cout << typeid(a).name() << "\n";
}
