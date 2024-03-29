#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int n, m, x;
vector<pair<int,int>> edge[1005];
vector<pair<int,int>> rev_edge[1005];
int dist[1005];
int rev_dist[1005];
const int INF = 1000000;

void dijkstra(vector<pair<int,int>>* const edge, int* const dist) {
    fill(dist, dist+n+1, INF);
    dist[x] = 0;
    priority_queue<pair<int,int>, vector<pair<int,int>>, greater<>> pq;
    pq.push({0, x});

    while (!pq.empty()) {
        auto [ct, cx] = pq.top();
        pq.pop();

        if (dist[cx] < ct)
            continue;
        for (auto [nx, nt] : edge[cx]) {
            if (ct + nt < dist[nx]) {
                dist[nx] = ct + nt;
                pq.push({ct + nt, nx});
            }
        }
    }
}

int main(void) {
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    cin >> n >> m >> x;
    for (int i = 0; i < m; i++) {
        int u, v, t;
        cin >> u >> v >> t;
        edge[u].push_back(make_pair(v, t));
        rev_edge[v].push_back(make_pair(u, t));
    }

    dijkstra(edge, dist);
    dijkstra(rev_edge, rev_dist);

    int maxt = 0;
    for (int i = 1; i <= n; i++) {
        int curt = dist[i] + rev_dist[i];
        if (curt > maxt)
            maxt = curt;
    }

    cout << maxt;
    return 0;
}