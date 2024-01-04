#include <bits/stdc++.h>
using namespace std;

int main(void) {
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int N, L, x;
    vector<int> a;
    vector<int> d;
    deque<pair<int, int>> window;

    cin >> N >> L;
    for (int i=0; i<N; i++) {
        cin >> x;
        a.push_back(x);
    }

    for (int i=0; i<N; i++) {
        while (!window.empty() && window.front().second <= i - L)
            window.pop_front();
        while (!window.empty() && window.back().first >= a[i])
            window.pop_back();
        window.push_back({a[i], i});
        d.push_back(window[0].first);
    }

    for (auto dd : d) cout << dd << ' ';
    return 0;
}