#include <iostream>
using namespace std;

int main(void) {
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int n;
    int arr[1005], lis[1005], lds[1005];

    cin >> n;
    for (int i = 0; i < n; i++) cin >> arr[i];

    lis[0] = 1;
    for (int i = 1; i < n; i++) {
        lis[i] = 1;
        for (int j = 0; j < i; j++) {
            if (arr[j] < arr[i])
                lis[i] = max(lis[i], lis[j] + 1);
        }
    }

    lds[n-1] = 1;
    for (int i = n-2; i >= 0; i--) {
        lds[i] = 1;
        for (int j = n - 1; j > i; j--) {
            if (arr[j] < arr[i])
                lds[i] = max(lds[i], lds[j] + 1);
        }
    }
    
    int ans = 1;
    for (int i = 0; i < n; i++) {
        ans = max(ans, lis[i] + lds[i] - 1);
    }

    cout << ans;
    return 0;
}