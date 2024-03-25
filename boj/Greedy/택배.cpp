#include <iostream>
#include <vector>
#include <tuple>
#include <algorithm>

using namespace std;

bool comp(const tuple<int,int,int>& t1, const tuple<int,int,int>& t2) {
    const auto [fr1, to1, am1] = t1;
    const auto [fr2, to2, am2] = t2;

    if (to1 == to2) {
        return fr1 < fr2;
    }
    else
        return to1 < to2;
}

int main(void) {
    iostream::sync_with_stdio(0);
    cin.tie(0);

    int n, m, capacity;
    vector<tuple<int,int,int>> order;
    cin >> n >> capacity >> m;

    for (int i = 0; i < m; i++) {
        int f, t, a;
        cin >> f >> t >> a;
        order.push_back(make_tuple(f, t, a));
    }

    sort(order.begin(), order.end(), comp);
    int buf[25] = {0};
    int ans = 0;

    for (auto [fr, to, am] : order) {
        bool loadable = true;
        for (int i = fr; i < to; i++) {
            am = min(am, capacity - buf[i]);
            if (am == 0) {
                loadable = false;
                break;
            }
        }
        if (!loadable)
            continue;
        for (int i = fr; i < to; i++) {
            buf[i] += am;
        }
        ans += am;
    }

    cout << ans;
    return 0;
}