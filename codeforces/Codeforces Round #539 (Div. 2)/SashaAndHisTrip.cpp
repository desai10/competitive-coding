#include<iostream>
using namespace std;

int main() {
    int n, v;
    cin>>n>>v;
    int tot = 0, curf = 0;
    for(int i=1;i<=n;i++, curf--) {
        int req = (n - i) - curf, pos = v - curf;
        if (pos > req) {
            curf += req;
            tot += i * req;
        } else {
            curf += pos;
            tot += i * pos;
        }
    }
    cout<<tot;
    return 0;
}