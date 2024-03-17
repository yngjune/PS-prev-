#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int n, e, u, v;
vector<pair<int,int>> edge[805];
int dist_1[805], dist_u[805], dist_v[805];

void dijkstra (int st, int* const dist) {
    dist[st] = 0;
    priority_queue<pair<int,int>, vector<pair<int,int>>, greater<>> pq;
    pq.push({0, st});

    while (!pq.empty()) {
        auto [cd, cx] = pq.top();   pq.pop();
        if (cd > dist[cx]) continue;

        for (auto [nx, nd] : edge[cx]) {
            if (dist[nx] == -1 || dist[nx] > cd + nd) {
                dist[nx] = cd + nd;
                pq.push({dist[nx], nx});
            }
        }
    }
}

int main(void) {
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    cin >> n >> e;
    for (int i = 0; i < e; i++) {
        int a, b, c;
        cin >> a >> b >> c;
        edge[a].push_back({b, c});
        edge[b].push_back({a, c});
    }

    cin >> u >> v;
    fill(dist_1, dist_1+n+1, -1);
    fill(dist_u, dist_u+n+1, -1);
    fill(dist_v, dist_v+n+1, -1);

    dijkstra(1, dist_1);
    dijkstra(u, dist_u);
    dijkstra(v, dist_v);

    int ans = -1;
    // case 1 : 1 -> u -> v -> n
    if (dist_1[u] != -1 && dist_u[v] != -1 && dist_v[n] != -1)
        ans = dist_1[u] + dist_u[v] + dist_v[n];

    // case 2 : 1 -> v -> u -> n
    if (dist_1[v] != -1 && dist_v[u] != -1 && dist_u[n] != -1)
        if (ans == -1)
            ans = dist_1[v] + dist_v[u] + dist_u[n];
        else
            ans = min(ans, dist_1[v] + dist_v[u] + dist_u[n]);

    cout << ans;

    return 0;
}