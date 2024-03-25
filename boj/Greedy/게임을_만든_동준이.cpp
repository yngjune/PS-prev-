#include <iostream>

using namespace std;

int main(void) {
    iostream::sync_with_stdio(0);
    cin.tie(0);

    int n, ans = 0;
    int score[105];
    cin >> n;
    for (int i = 0; i < n; i++) cin >> score[i];

    int prev = score[n - 1];
    for (int i = n - 2; i >= 0; i--) {
        if (score[i] >= prev) {
            ans += (score[i] - prev + 1);
            prev--;
        }
        else {
            prev = score[i];
        }
    }

    cout << ans;
    return 0;
}