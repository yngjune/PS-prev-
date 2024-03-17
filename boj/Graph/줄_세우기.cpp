#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int main(void) {
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int n, m;
    cin >> n >> m;

    vector<int> edge[32005];
    int in_degree[32005];
    
    fill(in_degree, in_degree+n, 0);
    for (int i = 0; i < m; i++) {
        int u, v;
        cin >> u >> v;
        edge[u].push_back(v);
        in_degree[v]++;
    }

    queue<int> q;
    for (int i = 1; i <= n; i++) {
        if (in_degree[i] == 0) q.push(i);
    }

    while (!q.empty()) {
        auto cur = q.front();
        cout << cur << ' ';
        q.pop();

        for (auto nxt : edge[cur]) {
            in_degree[nxt]--;
            if (in_degree[nxt] == 0) q.push(nxt);
        }
    }

    return 0;
}