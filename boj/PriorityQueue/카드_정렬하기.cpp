#include <iostream>
#include <queue>

using namespace std;

int main(void) {
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int n;
    long long ans = 0;
    priority_queue<int, vector<int>, greater<>> pq;

    cin >> n;
    for (int i = 0; i < n; i++) {
        int tmp;    cin>> tmp;
        pq.push(tmp);
    }

    while (pq.size() > 1) {
        int t1 = pq.top();  pq.pop();
        int t2 = pq.top();  pq.pop();
        ans += t1 + t2;
        pq.push(t1 + t2);
    }
    
    cout << ans;
    return 0;
}