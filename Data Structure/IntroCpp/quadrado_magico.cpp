#include <iostream>
using namespace std;

int main(){
    int matriz[3][3], lin[3], col[3], DP, DS, ln = 1, cl = 1;

    for (int i = 0; i < 3; i++){
        for(int j = 0; j < 3; j++)
            cin >> matriz[i][j];
    }

    for (int i = 0; i < 3; i++)
        DS += matriz[i][i];

    for (int i = 0; i < 3; i++)
        DS += matriz[i][3-i-1];
    
    for (int i = 0; i < 3; i++){
        for (int j = 0; j < 3; j++)
            lin[3] = matriz[i][j];
    }
        
    for (int i = 0; i < 3; i++){
        for (int j = 0; j < 3; j++)
            col[3] = matriz[i][j];
    }    

    for (int i = 1; i <  3; i++) {
        if (lin[i-1] != lin[i]) { 
            ln = 0;
            break;
        } else if (col[i-1] != col[i]){
            cl = 0;
            break;
        }     
    }  

    if (DP == DS && ln && cl && DP == lin[0]) {
        printf("sim");
    } else {
        printf("nao");
    }
    
    return 0;
}