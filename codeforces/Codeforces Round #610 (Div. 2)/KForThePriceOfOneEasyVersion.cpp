#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int n, p;
vector<int> v;
// int arr[200005][200005][4];

// int doit(int i, int added, int curC) {
//     if (i >= n) {
//         return 0;
//     }
//     int ans = 0;
//     if (added == 1) {
//         if (curC + v[i] <= p) {
//             ans = 2 + doit(i + 1, 0, curC + v[i]);
//         }
//     } else {
//         ans = max(ans, doit(i + 1, 1, curC));
//         if (v[i] + curC <= p) {
//             ans = max(ans, 1 + doit(i + 1, 0, curC + v[i]));
//         }
//     }
//     return ans;
// }

int main() {
    int t;
    cin>>t;
    while(t--) {
        int k;
        cin>>n>>p>>k;
        v.clear();
        for (int i=0;i<n;i++) {
            int tt;
            cin>>tt;
            v.push_back(tt);
        }
        sort(v.begin(), v.end());
        int a = 0, cur = 0, i = 1;
        for (i=1;i<n;i+=2) {
            if (cur + v[i] <= p) {
                a += 2;
                cur += v[i];
                continue;
            }
            if (cur + v[i - 1] <= p) {
                a++;
                cur += v[i - 1];
                continue;
            }
            if (i == n - 2) {
                if (cur + v[i + 1] <= p) {
                    a++;
                    cur += v[i + 1];
                }
            }
        }
        int b = 0;
        cur = 0;
        i = 2;
        if (v[0] <= p) {
            b = 1;
            cur += v[0];
        }
        for(i=2;i<n;i+=2) {
            if (cur + v[i] <= p) {
                b += 2;
                cur += v[i];
                continue;
            }
            if (cur + v[i - 1] <= p) {
                b++;
                cur += v[i - 1];
                continue;
            }
            if (i == n - 2) {
                if (cur + v[i + 1] <= p) {
                    b++;
                    cur += v[i + 1];
                }
            }
        }
        cout<<max(a, b)<<endl;
        // cout<<doit(0, 0, 0)<<endl;
    }
    return 0;
}