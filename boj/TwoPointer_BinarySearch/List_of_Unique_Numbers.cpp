#include <iostream>

using namespace std;

int main(void) {
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int n;
    int arr[100005];
    int cnt[100005] = {0};
    
    cin >> n;
    for (int i = 0; i < n; i++) cin >> arr[i];
    
    long long ans = 0;
    int en = 0;
    cnt[arr[0]] = 1;
    for (int st = 0; st < n; st++) {
        while (en < n - 1 && !cnt[arr[en + 1]]) {
            en++;
            cnt[arr[en]] = 1;
        }
        ans += (en - st + 1);
        cnt[arr[st]] = 0;
    }
    
    cout << ans;
    return 0;
}