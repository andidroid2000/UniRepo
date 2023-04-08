#include <iostream>
#include <fstream>
#include <deque>
using namespace std;

ifstream f("vila2.in");
ofstream g("vila2.out");

deque<int> varste;
deque<int> minim;
deque<int> maxim;
int main()
{
    int n, k, a, max = 0;
    f >> n >> k;
    for(int i=0; i<n; i++)
    {
        f>>a;
        varste.push_back(a);

    }

    for (int i=0; i<varste.size(); i++)
    {
        minim.push_back(varste[i]);
        maxim.push_back(varste[i]);
        while(minim.back() < minim.front())
            minim.pop_front();
        while(maxim.back() > maxim.front())
            maxim.pop_front();
        if(i>k && minim.front()==varste[i-k-1])
            minim.pop_front();
        if(i>k && maxim.front()==varste[i-k-1])
            maxim.pop_front();
        if(max < maxim.front()-minim.front())
            max=maxim.front()-minim.front();
    }
    g<<max;
}
