#include <iostream>
using namespace std;

bool primo (int n){
    for (int i = 2; i < n; i++) {
        if(n % i == 0)
            return false;
    }
    return true;
}

int main(){
    int a = 0, b = 0;

    cout << "A: " << endl;
    cin >> a;
    cout << "B: " << endl;
    cin >> b;
    
    cout << "\n";

    for (int i = a; i <= b; i++) {
        /*Mostra todos os números primos entre A e B (A >= i >= B)*/
        if(primo(i))
            cout << i << endl;
    }

    return 0;
}
