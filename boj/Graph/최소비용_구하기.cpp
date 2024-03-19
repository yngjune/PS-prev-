// #include <iostream>
// #include <vector>
// #include <queue>

// using namespace std;

// int n, m, st, en;
// vector<pair<int,int>> edge[1005];
// int dist[1005];
// priority_queue<pair<int,int>, vector<pair<int,int>>, greater<>> pq;

// void dijkstra() {
//     while (!pq.empty()) {
//         auto [ccost, cnode] = pq.top(); pq.pop();
//         if (dist[cnode] != -1 && dist[cnode] < ccost) continue;

//         for (auto [nnode, ncost] : edge[cnode]) {
//             if (dist[nnode] == -1 || ccost + ncost < dist[nnode]) {
//                 dist[nnode] = ccost + ncost;
//                 pq.push({dist[nnode], nnode});
//             }
//         }
//     }
// }


// int main(void) {
//     cin >> n >> m;
//     for (int i = 0; i < m; i++) {
//         int f, t, c;
//         cin >> f >> t >> c;
//         edge[f].push_back({t, c});
//     }

//     cin >> st >> en;
//     fill(dist, dist+n+1, -1);
//     dist[st] = 0;
//     pq.push({0, st});

//     dijkstra();
//     cout << dist[en];

//     return 0;
// }

#include <iostream>
#include <vector>
#include <tuple>

using namespace std;

const int MAXDIST = 100000000;
int n, m, u, v;
vector<tuple<int,int,int>> edge;
int dist[1005];

void bellman_ford(int start) {
    fill(dist, dist+n+1, MAXDIST);
    dist[start] = 0;

    for (int i = 0; i < n - 1; i++) {
        for (auto [cx, nx, cost] : edge) {
            if (dist[nx] > dist[cx] + cost) {
                dist[nx] = dist[cx] + cost;
            }
        }
    }
}

int main(void) {
    iostream::sync_with_stdio(0);
    cin.tie(0);

    cin >> n >> m;
    for (int i = 0; i < m; i++) {
        int a, b, c;
        cin >> a >> b >> c;
        edge.push_back(make_tuple(a, b, c));
    }
    cin >> u >> v;
    bellman_ford(u);
    cout << dist[v];

    return 0;
}