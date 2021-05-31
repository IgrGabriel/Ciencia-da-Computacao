#include <iostream>
using namespace std;

    int main(){

        int nLinha = 3, nColuna= 3, antecessor = 0, contador = 0, matriz[3][3];

        for(int i = 0; i < nLinha; i++){
            for(int j = 0; j < nColuna; j++)
                cin >> matriz[i][j];
        }

        for(int j = 0; j < nColuna; j++){
            for(int i = 0; i < nLinha ;i++){
                if(matriz[i][j] <antecessor)
                    contador++;
                antecessor = matriz[i][j];
            }
            antecessor=0;
        }

       cout << contador << endl;
}