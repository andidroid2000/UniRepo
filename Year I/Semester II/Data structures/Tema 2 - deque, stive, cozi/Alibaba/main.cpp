#include <iostream>
#include <fstream>
#include <vector>
#include <stack>
#include <string.h>
using namespace std;

int main()
{

    int n, k;
    string cifre;
    stack<char> s;
    vector<char> rezultat;
    ifstream f("alibaba.in");

    f >> n >> k;
    f >> cifre;
    f.close();

    for(int i = 0; i < cifre.size(); i++){
        if(s.empty()){
            s.push(cifre[i]);
        }
        else{
            while(!s.empty() && s.top() < cifre[i] && k != 0){
                k--;
                s.pop();
            }
            s.push(cifre[i]);
        }
    }
    while(k != 0 && !s.empty()){
        s.pop();
        k--;
    }
    while(!s.empty()){
        rezultat.push_back(s.top());
        s.pop();
    }

    ofstream g("alibaba.out");
    for(int i = rezultat.size() - 1; i >= 0; i--){
       g << rezultat[i];
    }
    g.close();
    return 0;
}
