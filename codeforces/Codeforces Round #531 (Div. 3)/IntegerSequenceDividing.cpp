#include<iostream>
#include<vector>

using namespace std;

int main() {
    int n;
    cin>>n;
    long long int aa = 1, mod = 1000000009;
    for(int i=1;i<=n;i++) {
        aa = (aa * i) % mod;
    }
    cout<<aa;
}