#include <iostream>

using namespace std;

// Recebe tempo em 'segundos', converte para horas, minutos e seguntos, e 
// retorna o resultado através dos parâmetros 'hor', 'min' e 'seg'.
void converte_tempo(int segundos, int *hor, int *min, int *seg)
{
    *hor = 0, *min = 0, *seg = 0;

    for(int i = 0; i < segundos; i++){
        *seg += 1;

        if(*seg == 60) {
            
            *min += 1;
            *seg = 0;
            
                if(*min == 60){
                    *hor += 1;
                    *min = 0;  
            }
        }
    }


}

int main()
{
   int tempo, h, m, s;
   std::cin >> tempo;
   
   // Chame a função 'converte_tempo' para converter o valor de 'tempo' em horas
   // minutos e segundos, gravando o resultado nas variáveis 'h', 'm' e 's'.
   converte_tempo(tempo, &h, &m, &s);

   std::cout << h << ":" << m << ":" << s;
   
   return 0;
}