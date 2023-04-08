#include <iostream>
#include <fstream>
#include <vector>
#include <unordered_map>

using namespace std;

int main()
{
    int n, s, i, j, k, suma;
    vector<int> valori;
    unordered_map<int,vector<int> > numere;

    ifstream f("loto.in");
    f >> n >> s;
    for(i=0;i<n;i++)
    {
        f>>j;
        valori.push_back(j);
    }
    f.close();

    ofstream g("loto.out");
    for(i=0;i<valori.size();i++)
    {
        for(j=i;j<valori.size();j++)
        {
            for(k=j;k<valori.size();k++)
            {
                suma=valori[i]+valori[j]+valori[k];
                numere[suma]={valori[i],valori[j],valori[k]};
                if(numere.find(s-suma)!=numere.end())
                {
                    g<<valori[i]<<" "<<valori[j]<<" "<<valori[k]<<" "<<numere[s-suma][0]<<" "<<numere[s-suma][1]<<" "<<numere[s-suma][2];
                    return 0;
                }
            }
        }
    }
    g<<-1;
    g.close();
}
