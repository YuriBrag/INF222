#include <iostream>
#include <cmath>
#include <vector>
#include <algorithm>
#include <iomanip>
#include <chrono>

using namespace std;

void imprime(vector<double>& vetor){
    for (int i =0; i< vetor.size(); i++ ){
        cout << vetor[i] << " ";
    }
}

void merge(vector<double>&vetor, int i, int r, int l){
    int p1 = i;
    int p2 = r;
    int k = 0;

    vector<double> novo (l - i + 1);
    while (p1 < r && p2 < l){
        if (vetor[p1] <= vetor[p2]){
            novo[k] = vetor[p1];
            k++;
            p1++;
        } else {
            novo[k] = vetor[p2];
            k++;
            p2++;
        }
    }

    while (p1 < r) {
        novo[k] = vetor[p1];
        p1++;
        k++;
    }
    while (p2 < l) {
        novo[k] = vetor[p2];
        p2++;
        k++;
    }

    for (int j = 0; j < k; j++) {
        vetor[i + j] = novo[j];
    }
}

void mergeSort(vector<double>&vetor, int i, int f){
    if ( f <= i) return;
   // imprime(vetor);
    int mid = (f+ i) / 2;
    mergeSort(vetor, i, mid);
    mergeSort(vetor, mid+1, f);

    merge(vetor, i, mid, f);
}

double randomdouble()
{
    return (double)(rand()) / (double)(rand());
}

void aloca(vector<double>& vetor, int semi_ordenado, int tamanho, int uniformidade){
    vetor.resize(tamanho);
    if (uniformidade && semi_ordenado) {
        // Uniforme e quase ordenado
        // 1/3 para cada tipo (- 0 +)
        int ini = tamanho/3;
        for (int i = 0; i <ini; i++){
            vetor[i] = -ini - i;
            vetor[i + ini] = 0;
            vetor[i + 2*ini] = ini + i;
        }
        return;
    } 

    if (uniformidade && !semi_ordenado){
        int ini = tamanho/3;
        for (int i = 0; i <ini; i++){
            vetor[i] = -randomdouble();
            vetor[i + ini] = 0;
            vetor[i + 2*ini] = randomdouble();
        }

        return;
    }

    if (semi_ordenado){
        for (int i = 0; i< tamanho; i++){
            vetor[i] = i;
        }

        int perturbacao = tamanho / (rand() % 1000);
        for (int i = 0; i < perturbacao; ++i) {
        int indice1 = rand() % tamanho;
        int indice2 = rand() % tamanho;
        swap(vetor[indice1], vetor[indice2]);
    }
    return;
    }

    if (!semi_ordenado){
        for (int i = 0; i <tamanho; i++){
            vetor[i] = randomdouble();
        }
        for(int i = 0; i < tamanho / 2; i++){
            int mudar = rand() % tamanho;
            vetor[mudar] = -vetor[mudar];
        }
    }
    
}

void DNFS(vector<double>& vetor) {
    int baixo = 0;
    int alto = vetor.size() - 1;
    int i = 0;

    while (i <= alto) {
        if (vetor[i] < 0) {
            swap(vetor[i], vetor[baixo]);
            baixo++;
            i++;
        } else if (vetor[i] > 0) {
            swap(vetor[i], vetor[alto]);
            alto--;
        } else {
            i++;
        }
    }
}

double mai_method(int M, int T, int E, int Q) {
    srand(time(NULL));
    vector<double> vetor;
    M = M < 0? 0 : 1;
    T = T < 0 ? 500000 : 1000000;
    E = E < 0 ? 0 : 1;
    Q =  Q < 0 ? 0 : 1;
    aloca(vetor, E, T, Q);
    auto start = chrono::high_resolution_clock::now();
    if (M == 0){
        DNFS(vetor);
    }
    else{
        mergeSort(vetor, 0, vetor.size());
    }
    auto end = chrono::high_resolution_clock::now();

    double time_taken = chrono::duration_cast<chrono::nanoseconds>(end - start).count();
    time_taken *= 1e-9;
    return time_taken;
}


int main() {
    int M, T, E, Q;
    cout << "Entre com M T E Q \n";
    cin >> M >> T >> E >> Q;
    cout << mai_method(M,T,E,Q) << endl;
    return 0;
}