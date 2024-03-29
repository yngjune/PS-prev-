#include <iostream>
#include <queue>

using namespace std;

int v, e;
long long ans = 0;
vector<vector<pair<int,int>>> edge(10005);

void prim(int start) {
    priority_queue<pair<int,int>, vector<pair<int,int>>, greater<>> pq;
    vector<bool> visit(v+1, false);
    pq.push({0, start});

    while (!pq.empty()) {
        auto [cw, cx] = pq.top();
        pq.pop();
        if (!visit[cx]) {
            visit[cx] = true;
            for (auto [nx, nw] : edge[cx]) {
                pq.push({nw, nx});
            }
            ans += cw;
        }
    }
}

int main(void) {
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    cin >> v >> e;
    for (int i = 0; i < e; i++) {
        int a, b, c;
        cin >> a >> b >> c;
        edge[a].push_back({b, c});
        edge[b].push_back({a, c});
    }

    prim(1);
    cout << ans;

    return 0;
}