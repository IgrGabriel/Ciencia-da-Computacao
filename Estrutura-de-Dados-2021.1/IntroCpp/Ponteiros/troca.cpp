/* Troca de valores de variáveis */
#include <iostream>

// Implemente a função 'troca'.
void troca(int *a, int *b)
{
    int* aux;
    int var;
    
    aux = &var;
    *aux = *a;
    
    *a = *b;
    *b = *aux;
}

int main()
{
    int x, y;
    std::cout << "x: ";
    std::cin >> x;
    std::cout << "y: ";
    std::cin >> y;
    
    // Chame a função 'troca' para trocar os valores de x e y.
    troca(&x, &y);

    std::cout << "x: " << x << " y: " << y << std::endl;
    return 0;
}