#include <iostream>
#include <iomanip>

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
    Aluno a2;

    /*Aluno 1*/
    cin.get(a1.nome, 50);

    cin >> a1.matricula;
    cin.ignore();

    cin.get(a1.disciplina, 120);
  
    cin >> a1.nota;
    cin.ignore();

    /*Aluno 2*/
    cin.get(a2.nome, 50);

    cin >> a2.matricula;
    cin.ignore();

    cin.get(a2.disciplina, 120);

    cin >> a2.nota;
    cin.ignore();
    
    cout << fixed << setprecision(1);
    
    if(a1.nota > a2.nota)
        cout << a1.nome << " , " << a1.nota << endl;
    else if (a1.nota < a2.nota)
        cout << a2.nome << " , " << a2.nota << endl;
    else if (a1.nota == a2.nota)
        cout << a1.nome << " e " << a2.nome << " , " << a1.nota << endl;

    return 0;
}