#include <iostream>
#include <iomanip>
#include <vector>
#include <algorithm>
#include <math.h>
using namespace std;

int main() {
    vector<double> vecOrd1;
    vector<double> vecOrd2;
    double num;
    double sum1 = 0;
    double sum2 = 0;
    double var1 = 0;
    double var2 = 0;
    
    for (int i = 0; i < 10; i++) {
        cin >> num;
        vecOrd1.push_back(num);
    }
    for (int i = 0; i < 7; i++) {
        cin >> num;
        vecOrd2.push_back(num);
    }
    //sort(vecOrd.begin(), vecOrd.end());

    for (int i = 0; i < vecOrd1.size(); i++) {
        sum1 += vecOrd1[i];
        var1 += pow(vecOrd1[i],2);
        cout << pow(vecOrd1[i],2) << " ";
    }
    cout << endl;
    cout << sum1/10 << endl;
    cout << var1 << " ";
    cout << endl;

    for (int i = 0; i < vecOrd2.size(); i++) {
        sum2 += vecOrd2[i];
        var2 += pow(vecOrd2[i],2);
        cout << pow(vecOrd2[i],2) << " ";
    }
    cout << endl;
    cout << sum2/7 << endl;
    cout << var2 << " ";


    
    return 0;
}