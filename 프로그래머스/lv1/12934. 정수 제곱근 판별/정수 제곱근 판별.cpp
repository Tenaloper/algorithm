#include <string>
#include <vector>
#include <bits/stdc++.h>

using namespace std;

long long solution(long long n) {
    long long answer = 0;
    long long a = sqrt(n);
    if (a*a == n) {
        answer=pow(a+1,2);
    }
    else {
        answer=-1;
    }
    return answer;
}