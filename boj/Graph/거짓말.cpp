#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int main(void) {
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int n, m, t;
    vector<int> party[55];
    vector<int> edge[55];
    bool truth[55] = {false};

    cin >> n >> m >> t;
    while (t--) {
        int x; cin >> x;
        truth[x] = true;
    }

    for (int i = 0; i < m; i++) {
        int np; cin >> np;
        int prv = 0, nxt;
        
        while (np--) {
            cin >> nxt;
            party[i].push_back(nxt);
            if (prv) {
                edge[prv].push_back(nxt);
                edge[nxt].push_back(prv);
            }
            prv = nxt;
        }
    }
    
    queue<int> q;
    for (int i = 1; i <= n; i++)
        if (truth[i]) q.push(i);
    
    while (!q.empty()) {
        int cur = q.front(); q.pop();

        for (int nxt : edge[cur]) {
            if (truth[nxt]) continue;
            truth[nxt] = true;
            q.push(nxt);
        }
    }

    int ans = 0;
    for (int i = 0; i < m; i++) {
        bool add = true;
        for (int x : party[i])
            if (truth[x]) {
                add = false;
                break;
            }
        if (add) ans++;
    }
    
    cout << ans;
    return 0;
}