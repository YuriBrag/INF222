#include<bits/stdc++.h>  
using namespace std;  
  
void DNFS(std::vector<float>& vetor) {
    int baixo = 0;
    int alto = vetor.size() - 1;
    int i = 0;

    while (i <= alto) {
        if (vetor[i] < 0) {
            std::swap(vetor[i], vetor[baixo]);
            baixo++;
            i++;
        } else if (vetor[i] > 0) {
            std::swap(vetor[i], vetor[alto]);
            alto--;
        } else {
            i++;
        }
    }
}
  

void printArray(std::vector<float>& arr, int arr_size)  
{  
    for (int i = 0; i < arr_size; i++) 
        cout << arr[i] << " ";  
  
}  
    
int main() {  
    vector<float> arr = {0,0,1,-14,2,0,1,2, 2.4, -783.98, 28.5};  
    int n = arr.size();

    cout << "Array before running the algorithm: ";  
      
    printArray(arr, n);
    
    DNFS(arr);  
  
    cout << "\nArray after DNFS algorithm: ";  
      
    printArray(arr, n);  
  
    return 0;  
}  