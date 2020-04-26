#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

int main() {
    int n;
    cin>>n;
    vector<pair<int, int> > v;
    for(int i=0;i<n;i++) {
        int a, b;
        cin>>a>>b;
        v.push_back(make_pair(a, b));
    }
    int draws = 0;
    int s1 = 0, s2 = 0;
    for (int i=0;i<n;i++) {
        int a = min(v[i].first, v[i].second) - max(s1, s2);
        if (a >= 0) {
            draws += (a + 1);
        }
        s1 = v[i].first;
        s2 = v[i].second;
        if (s1 == s2) {
            s1++;
            s2++;
        }
    }
    cout<<draws;
    return 0;
}