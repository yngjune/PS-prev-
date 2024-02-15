#include <iostream>
#include <algorithm>
using namespace std;

int n, ans = 0;
int arr[2005];

// binary search
// bool isgoodnum (int i) {
//     for (int j = 0; j < n; j++) {
//         if (j == i) continue;
//         int target = arr[i] - arr[j];
//         int tidx = lower_bound(arr, arr+n, target) - arr;
        
//         while (tidx < n && arr[tidx] == target) {
//             if (tidx != i && tidx != j) return true;
//             tidx++;
//         }
//     }

//     return false;
// }

// two pointer
bool isgoodnum (int i) {
    int l = 0, r = n - 1;
    while (l < r) {
        if (l == i) l++;
        if (r == i) r--;
        if (l >= r) break;
        int cur = arr[l] + arr[r];
        if (cur == arr[i]) return true;
        else if (cur < arr[i]) l++;
        else r--;
    }

    return false;
}

int main(void) {
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    cin >> n;
    for (int i = 0; i < n; i++) cin >> arr[i];
    sort(arr, arr+n);

    for (int i = 0; i < n; i++) ans += isgoodnum(i);

    cout << ans;
    return 0;
}