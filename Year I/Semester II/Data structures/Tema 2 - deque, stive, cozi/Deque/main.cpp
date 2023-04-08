#include <iostream>
#include <fstream>

using namespace std;

ifstream f("deque.in");
ofstream g("deque.out");

int v[5000001], deq[5000001], n, k;
long long suma;

int main()
{
    int i, dr=0, st=1;
    f >> n >> k;
    for(i=1; i<=n; i++)
        f >> v[i];
    for(i=1; i<=n; i++)
    {
        while(st<=dr && v[i]<=v[deq[dr]])
            dr--;
        deq[++dr]=i;
        if(deq[st] == i-k)
            st++;
        if(i>=k)
            suma=suma+v[deq[st]];
    }
    g<<suma;
    return 0;
}
