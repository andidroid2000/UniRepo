#include <iostream>
#include <fstream>
#include <unordered_map>

using namespace std;

unordered_map <int,int>valori;

int main()
{
    int n, i, m, j, t, s;
    ifstream f("pariuri.in");
    f >> n;
    for(i = 1; i <= n; i++)
    {
        f >> m;
        for(j = 1; j <= m; j++)
        {
            f >> t >> s;
            valori[t] += s;
        }
    }
    f.close();

    ofstream o("pariuri.out");
    o << valori.size() << '\n';
    for(unordered_map<int, int> ::iterator i = valori.begin(); i != valori.end(); ++i)
    o << i -> first << " " << i -> second << " ";
    o.close();
}
