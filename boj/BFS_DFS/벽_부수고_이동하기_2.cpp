#include <bits/stdc++.h>
using namespace std;

int dx[] = {-1, 1, 0, 0};
int dy[] = {0, 0, 1, -1};

int main(void) {
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int n, m, k;
    string board[1001];
    int dist[1001][1001][11] = {0};

    cin >> n >> m >> k;
    for (int i = 0; i < n; i++) cin >> board[i];

    queue<tuple<int,int,int>> q;
    q.push({0, 0, 0});
    dist[0][0][0] = 1;
    while (!q.empty()) {
        auto [x, y, z] = q.front(); q.pop();
        if (x == n - 1 && y == m - 1) {
            cout << dist[x][y][z];
            return 0;
        }

        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            if (nx < 0 || nx >= n || ny < 0 || ny >= m) continue;
            if (z < k && board[nx][ny] == '1' && dist[nx][ny][z+1] == 0) {
                dist[nx][ny][z+1] = dist[x][y][z] + 1;
                q.push({nx, ny, z+1});
            }
            if (board[nx][ny] == '0' && dist[nx][ny][z] == 0) {
                dist[nx][ny][z] = dist[x][y][z] + 1;
                q.push({nx, ny, z});
            }
        }
    }
    
    cout << -1;
    return 0;
}