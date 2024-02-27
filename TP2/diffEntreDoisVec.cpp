#include <iostream>
#include <iomanip>
#include <vector>

using namespace std;

int main() {
    vector<double> noDown;
    vector<double> vecDown;

    double tx = 0;

    for (int i = 0; i < 15; i++) {
        cin >> tx;
        noDown.push_back(tx);
    }
    for (int i = 0; i < 15; i++) {
        cin >> tx;
        vecDown.push_back(tx);
    }
    for (int i = 0; i < 15; i++) {
        cout << noDown[i] - vecDown[i] << " ";
    }
    return 0;
}