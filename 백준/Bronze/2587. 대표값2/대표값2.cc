#include <bits/stdc++.h>
using namespace std;
#define fi cin.tie(0)->sync_with_stdio(0)

int main() {
    fi;
    
    vector<int> v(5);
    
    for (int i = 0; i < 5; i++) {
        cin>>v[i];
    }
    
    sort(v.begin(), v.end());
    
    cout << accumulate(v.begin(), v.end(), 0) / 5 << "\n";
    cout << v[2];
  
    return 0;
}