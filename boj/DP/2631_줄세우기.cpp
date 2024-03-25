#include <iostream>

using namespace std;

int main(void) {
    iostream::sync_with_stdio(0);
    cin.tie(0);

    int n, max_lis = 1;
    int arr[205];
    int lis[205];

    cin >> n;
    for (int i = 0; i < n; i++) cin >> arr[i];
    for (int i = 0; i < n; i++) {
        lis[i] = 1;
        for (int j = 0; j < i; j++) {
            if (arr[j] < arr[i]) {
                lis[i] = max(lis[i], lis[j] + 1);
            }
        }
        max_lis = max(max_lis, lis[i]);
    }

    cout << n - max_lis;
    return 0;
}