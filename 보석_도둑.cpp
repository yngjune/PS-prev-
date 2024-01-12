#include <iostream>
#include <algorithm>
#include <vector>
#include <set>

using namespace std;

int main(void) {
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int ngem, nbag, ans = 0;
    cin >> ngem >> nbag;
    vector<pair<int,int>> gem;

    for (int i = 0; i < ngem; i++) {
        int w, v;
        cin >> w >> v;
        gem.push_back({v, w});
    }

    multiset<int> ms;
    for (int i = 0; i < nbag; i++) {
        int x;
        cin >> x;
        ms.insert(x);
    }

    sort(gem.begin(), gem.end());
    for (int i = ngem - 1; i >= 0; i--) {
        auto it = ms.lower_bound(gem[i].second);
        if (it == ms.end()) continue;
        ans += gem[i].first;
        ms.erase(it);
    }

    cout << ans;
    return 0;
}