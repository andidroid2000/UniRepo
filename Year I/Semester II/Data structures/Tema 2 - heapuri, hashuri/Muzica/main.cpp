#include <iostream>
#include <fstream>
#include <unordered_map>

using namespace std;

unordered_map<int, bool> dj(100001);

int main()
{
    int n, m, mel, sol = 0, i;
    long long a, b, c, d, e;

    ifstream f("muzica.in");
    f >> n >> m >> a >> b >> c >> d >> e;
    for(i = 0; i < n; i++)
    {
        f >> mel;
        dj[mel] = 1;
    }
    f.close();

    for (int i = 0; i < m; i++)
    {
        if (dj.count(a))
        {
            sol++;
            dj.erase(a);
        }
        mel = (c * b + d * a) % e;
        a = b;
        b = mel;
    }

    ofstream g("muzica.out");
    g << sol;
    g.close();
}
