#include <bits/stdc++.h>
using namespace std;
int camere[11];
int main()
{
    int n;
    string memorie;
    cin>>n>>memorie;
    for(int i=0; i<n; i++)
    {
        if(memorie[i]=='L')
            for(int j=0; j<10; j++)
                if(camere[j]==0)
                {
                    camere[j]++;
                    break;
                }
        if(memorie[i]=='R')
            for(int j=9; j>=0; j--)
                if(camere[j]==0)
                {
                    camere[j]++;
                    break;
                }
        camere[memorie[i]-'0']=0;
    }
    for(int i=0; i<10; i++)
        cout<<camere[i];
}
