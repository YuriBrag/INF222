#include <iostream>
#include <iomanip>
#include <vector>
#include <algorithm>
#include <math.h>
using namespace std;

int main() {
    vector<int> vecOrd;
    int sum = 0;
    int num;
    double media;
    long double sumVariancia = 0;
    
    while (cin >> num) {
        vecOrd.push_back(num);
        sum += num;
    }
    sort(vecOrd.begin(), vecOrd.end());
    cout << "Soma: " << sum << endl;
    cout << "Numero de elementos: " << vecOrd.size() << endl;
    media = (double)sum/(double)vecOrd.size();
    cout << "Media: " << media << endl;
    cout << "Mediana: ";

    if (vecOrd.size()%2 == 0) {
        int soma2 = vecOrd[vecOrd.size()/2] + vecOrd[(vecOrd.size()/2) - 1];
        cout << (double)soma2/2 << endl;
    }
    else {
        cout << vecOrd[(vecOrd.size()/2) + 1] << endl;
    }
    cout << "Amplitude: " << vecOrd[vecOrd.size() - 1] - vecOrd[0] << endl;
    cout << "Ponto Medio: " << (double)(vecOrd[0] + vecOrd[vecOrd.size() - 1])/2 << endl;
    
    for (int i = 0; i < vecOrd.size(); i++) {
        sumVariancia += (vecOrd[i] - media) * (vecOrd[i] - media);
    }
    //cout << setprecision(10) <<  sumVariancia << endl;
    //cout << vecOrd.size() << endl;
    cout << "Variancia: " << sumVariancia/(double)vecOrd.size() << endl;
    cout << "Desvio Padrao: " << sqrt(sumVariancia/vecOrd.size()) << endl;
    cout << "Coeficiente de Variacao: " << (sqrt(sumVariancia/vecOrd.size())/(double)media)*100 << '%' << endl;
    // for (int i = 0; i < vecOrd.size(); i++) {
    //     cout << vecOrd[i] << " ";
    // }

    return 0;
}