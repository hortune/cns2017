#include <iostream>
#include <unordered_map>
using namespace std;
int main() {
    unordered_map<int, int> ht;
    int n;
    cin >> n;
    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;
        ht[x] = i;
    }
    return 0;
}
