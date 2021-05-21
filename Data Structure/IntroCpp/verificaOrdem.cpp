#include <iostream>
using namespace std;

 /*protótipo da função que verifica se o vetor está em ordem crescente*/
bool verifica_Ordem(int n, int *vet);

int main(){
    int n;
    
    cout << "Digite o tamanho do vetor: " << endl;
    cin >> n;
    int VetOrdem[n];

    cout << "Digite o(s) valor(es) para o popular o vetor" << endl;
    for(int i = 0; i < n; i++)     
        cin >> VetOrdem[i];

    if(verifica_Ordem(n, VetOrdem))
        cout << "ok";
    else
        cout << "precisa de ajuste";
        
    return 0;
}

bool verifica_Ordem(int n, int *vet){
    for (int i = 0; i < n; i++){
        if (vet[i+1] < vet[i])
            return false;
    }
    return true;   
}
