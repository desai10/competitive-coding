#include<iostream>
using namespace std;

int main() {
    int t;
    cin>>t;
    while(t--) {
        int a, b, c, r;
        cin>>a>>b>>c>>r;
        if (a > b) {
            int tt = a;
            a = b;
            b = tt;
        }
        int aa = 0;
        if (c - r > a) {
            aa += min((c - r), b) - a;
        }
        if (c + r < b) {
            aa += b - max((c + r), a);
        }
        cout << aa << endl;
    }
    return 0;
}