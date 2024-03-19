#include <iostream>
using namespace std;

int main(void) {
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int n, s;
    int arr[100000];
    int ans = 0x7fffffff;

    cin >> n >> s;
    for (int i = 0; i < n; i++) cin >> arr[i];

    int l = 0, r = 0, acc = arr[0];
    while (l <= r && r < n) {
        if (acc < s) {
            r++;
            if (r >= n) break;
            acc += arr[r];
        }
        else {
            ans = min(ans, r - l + 1);
            acc -= arr[l++];
        }
    }

    if (ans == 0x7fffffff)
        cout << 0;
    else
        cout << ans;
    return 0;
}