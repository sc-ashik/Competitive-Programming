#include <bits/stdc++.h>
using namespace std;

long long gcd(long long a, long long b){
    if(a==0 || b==0)return a+b;
    return gcd(b, a % b);
}

int main(){
    int n,m=0,c;
    cin>>n;
    c=n;
    while(n--){
        int t;
        cin>>t;
        m=gcd(m,t);
    }
    cout<<m*c<<endl;
}
