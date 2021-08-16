#include <iostream>
using namespace std;

int main(){
    int qtd_produtos = 0, contJ1 = 0, contJ2 = 0;

    cin >> qtd_produtos;

    float valor_produtos[qtd_produtos], jogador_1[qtd_produtos], valor = 0;
    char jogador_2[qtd_produtos];

    for(int i = 0; i < qtd_produtos; i++){
        cin >> valor;
        valor_produtos[i] = valor;
    }
        
    for(int i = 0; i < qtd_produtos; i++){
        cin >> valor;
        jogador_1[i] = valor;
    }

    for(int i = 0; i < qtd_produtos; i++){
        cin >> jogador_2[i];
    }

    for(int i = 0; i < qtd_produtos; i++){
        if(jogador_1[i] == valor_produtos[i])
            contJ1++;
        else if(valor_produtos[i] < jogador_1[i] && jogador_2[i] == 'm')
            contJ2++;
        else if(valor_produtos[i] > jogador_1[i] && jogador_2[i] == 'M')
            contJ2++;
        else
            contJ1++;    
    }

    if(contJ1 > contJ2)
        cout << "primeiro";
    else if (contJ1 < contJ2)
        cout << "segundo";
    else
        cout << "empate";

}