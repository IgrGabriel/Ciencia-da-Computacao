#include <iostream>

using namespace std;

struct Aluno
{
    char nome[100];
    int matricula;
    char disciplina[120];
    double nota;
};

int main(){

    Aluno a1;

    cin.get(a1.nome, 50);

    cin >> a1.matricula;
    cin.ignore();

    cin.get(a1.disciplina, 120);

    cin >> a1.nota;
    cin.ignore();
    
    
    if(a1.nota >= 7)
        cout << a1.nome << " aprovado(a) em " << a1.disciplina << endl;
    else
        cout << a1.nome << " reprovado(a) em " << a1.disciplina << endl;

    return 0;
}