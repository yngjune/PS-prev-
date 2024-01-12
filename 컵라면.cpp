#include <iostream>
#include <queue>

using namespace std;

int main(void) {
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;
    vector<int> vl[n+1];
    priority_queue<int, vector<int>, less<>> pq;

    for (int i = 1; i <= n; i++) {
        int d, r;
        cin >> d >> r;
        vl[d].push_back(r);
    }

    int ans = 0;
    for (int i = n; i >= 1; i--) {
        for (int r : vl[i]) pq.push(r);
        if (pq.empty()) continue;
        ans += pq.top();
        pq.pop();
    }
    
    cout << ans;
    return 0;
}