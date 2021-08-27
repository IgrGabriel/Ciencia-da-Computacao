#include <iostream>

using namespace std;

int main() {
    int var1;
    int* pont;

    var1 = 5;
    pont = &var1; // pont = 5

    cout << "Valor da variavel, atraves do seu nome: " << var << endl; // 5
    cout << "Endereço armazenado no ponteiro: " << pont << endl; // endereço da variavel
    
    cout << "Valor da variavel atraves do ponteiro: " << *pont << endl; // 5

    int var2;

    /* var2 recebe o valor de var1*/
    var2 = var1; // 5
    var2 = *pont; // 5
    cout << var2; // 5
    
    /*Mudar o valor de var 1*/
    var1 = 30;
    *pont = 30;
    cout << var1; // 30

    /*Fazer o pont apontar para a var2  (Mudou o endereço)*/
    var2 = 50;
    pont = &var2;
    cout << *pont1; // 50
    cout << var1;
    
    /*Ponteiro apontando para o vazio*/
    #include <cstddef>
    int* pont2;
    pont2 = NULL;
    cout << *pont2; // nada
    cout << pont2; // 0

    /*Pegar um pedaço da mémoria que ele vai apontar*/
    //Só pode acessar a variavel pelo ponteiro
    int* pont3 = new int; // o valor pode ser perdido se não tiver cuidado
    *pont3 = 35;
    cout << pont3; //Imprime o endereço
    cout << *pont3; //35

    *pont3 = *pont1; // Valor (Dois espaços de mémoria diferente)
    
    delete pont3; // Para não haver vazamento de memória
    pont3 = pont1; // Endereço (A memória de pont3 é perdida)

    cout << *pont3; // 5
    
    return 0;
}