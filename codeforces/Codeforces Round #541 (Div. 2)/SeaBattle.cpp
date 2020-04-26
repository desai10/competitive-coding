#include<iostream>
using namespace std;

int main() {
    long long int h1, w1, h2, w2;
    cin>>w1>>h1>>w2>>h2;
    cout<<((2 * (h1 + h2)) + (2 * w1)) + 4;
    return 0;
}