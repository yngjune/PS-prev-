#include <iostream>

using namespace std;

int main(void) {
    iostream::sync_with_stdio(0);
    cin.tie(0);

    int n, maxlis = 1;
    int arr[1000005];
    int idx_of_num[1000005];
    int lis[1000005];

    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
        idx_of_num[arr[i]] = i;
    }

    fill(lis, lis+n, 1);
    for (int i = 0; i < n; i++) {
        int prev = arr[i] - 1;
        if (prev == 0)
            continue;
        int idx_prev = idx_of_num[prev];
        if (idx_prev < i) {
            lis[i] = lis[idx_prev] + 1;
        }
        maxlis = max(maxlis, lis[i]);
    }

    cout << n - maxlis;
    return 0;
}