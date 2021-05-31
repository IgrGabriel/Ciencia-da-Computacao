#include <iostream>
#include <iomanip>

using namespace std;

double fatorial(int n);
double euler(int n);

int main() {
    int n;

    cin >> n;
    std::cout <<fixed << setprecision(6)<< euler(n) << std::endl; 

    return 0;
}

double fatorial(int n){    
    double fat;
    
    for(fat = 1; n > 1; n--)
        fat *= n;
        
    return fat;
}

double euler(int n){
    double euler_var = 1.0;

    for (int i = 1; i <= n; i++)
       euler_var += 1/fatorial(i);

    return euler_var; 
}