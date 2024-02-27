#include <iostream>
#include <cstdlib>
#include <iomanip>
#include <ctime>

using namespace std;

int main() {
    int n;
    int playerA;//ganha com cara (0)
    int playerB;//ganha com coroa (1)
    int jogosGanhosA = 0;
    int jogosGanhosB = 0;
    cout << "Insira a quantidade de testes a serem feitos" << endl;
    cin >> n;
    cout << "Insira o dinheiro disponivel para o player A" << endl;
    cin >> playerA;
    cout << "Insira o dinheiro disponivel para o player B" << endl;
    cin >> playerB;

    const int auxPA = playerA;
    const int auxPB = playerB;

    unsigned int seed = time(0);
    srand(seed);

    for (int i = 0; i < n; i++) {
        int contLances = 0;
        
        while (playerA && playerB) {   
            int moeda = rand()%2;
            //cout << moeda << endl;
            if (moeda == 0) {
                playerB--;
                playerA++;
            }
            if (moeda== 1) {
                playerA--;
                playerB++;
            }
            //cout << "O jogador A tem " << playerA << " moedas" << endl;
            //cout << "O jogador B tem " << playerB << " moedas" << endl;
            contLances++;
        }
        //cout << "Nesse jogo foram necessarios " << contLances << " lances de moeda para que tivesse um ganhador" << endl;
        if (playerA) {
            //cout << "A ganhou" << endl;
            jogosGanhosA++;
        }
        if (playerB) {
            //cout << "B ganhou" << endl;
            jogosGanhosB++;
        }
        playerA = auxPA;
        playerB = auxPB;
    }

    cout << "A ganhou " << jogosGanhosA << " em " << n << " jogos" << endl;
    cout << "B ganhou " << jogosGanhosB << " em " << n << " jogos" << endl;
    
    return 0;
}