#include <iostream>
#include <fstream>
#include <deque>
using namespace std;

ifstream f("branza.in");
ofstream g("branza.out");
deque<int> pretminim;

int main(){

    long long n, s, t, p, c[100010], min = 0;

    f >> n >> s >> t;
    t++;
    for(int i = 0; i < n; i++)
    {
        f >> c[i] >> p;
        if(pretminim.size() != 0 && pretminim.front() == i - t)
            pretminim.pop_front();
        while(pretminim.size() != 0 && c[i] <= c[pretminim.back()] + s * (i - pretminim.back()))
            pretminim.pop_back();
        pretminim.push_back(i);
        min += (long long)p * (c[pretminim.front()] + s * (i - pretminim.front()));
    }

    g << min;
}
