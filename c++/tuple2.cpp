//
// Created by 함경재 on 2022/03/18.
//

#include <bits/stdc++.h>

using namespace std;
tuple<int, int, int> tl;
int a, b, c;
int main() {
    tl = make_tuple(1, 2, 3);
    a = get<0>(tl);
    b = get<1>(tl);
    c = get<2>(tl);
    cout << a << " : " << b << " : " << c << "\n";
    return 0;
}