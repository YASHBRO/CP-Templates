#include <bits/stdc++.h>
using namespace std;
typedef long long int ll;

int main()
{
       ll t;
       cin >> t;
       while (t--)
       {
              ll n;
              cin >> n;
              double a[n];
              double max = (-1e9) - 1;
              double sum = 0.0;
              for (ll i = 0; i < n; i++)
              {
                     cin >> a[i];
                     sum += a[i];
                     if (a[i] > max)
                     {
                            max = a[i];
                     }
                     cout << fixed << setprecision(9) << max << ' ' << a[i] << endl;
              }
              sum = sum - max;
              double val = sum / ((double)n - 1);
              double k = sum + max;
              // cout << fixed << setprecision(9) << k << endl;
       }
       return 0;
}