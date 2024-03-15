#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int n, m, st, en;
vector<pair<int,int>> edge[1005];
int dist[1005];
priority_queue<pair<int,int>, vector<pair<int,int>>, greater<>> pq;

void dijkstra() {
    while (!pq.empty()) {
        auto [ccost, cnode] = pq.top(); pq.pop();
        if (dist[cnode] != -1 && dist[cnode] < ccost) continue;

        for (auto [nnode, ncost] : edge[cnode]) {
            if (dist[nnode] == -1 || ccost + ncost < dist[nnode]) {
                dist[nnode] = ccost + ncost;
                pq.push({dist[nnode], nnode});
            }
        }
    }
}


int main(void) {
    cin >> n >> m;
    for (int i = 0; i < m; i++) {
        int f, t, c;
        cin >> f >> t >> c;
        edge[f].push_back({t, c});
    }

    cin >> st >> en;
    fill(dist, dist+n+1, -1);
    dist[st] = 0;
    pq.push({0, st});

    dijkstra();
    cout << dist[en];

    return 0;
}