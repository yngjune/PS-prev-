#include <iostream>
#include <queue>

using namespace std;

int n, l, r;
int board[55][55];
bool edge[55][55][4];
int edge_cnt, total_country, total_popularity;

int idx;
int visit[55][55];
int ncountry[2505];
int npopularity[2505];

int dx[] = {-1, 0, 1, 0};
int dy[] = {0, 1, 0, -1};
int rev[] = {2, 3, 0, 1};

void connect(int x, int y) {
    for (int k = 0; k < 4; k++) {
        int nx = x + dx[k];
        int ny = y + dy[k];
        if (nx < 0 || ny < 0 || nx >= n || ny >= n) continue;
        int diff = abs(board[nx][ny] - board[x][y]);
        if (diff >= l && diff <= r) {
            edge[x][y][k] = true;
            edge[nx][ny][rev[k]] = true;
            edge_cnt++;
        }
    }
}


pair<int,int> bfs(int x, int y) {
    queue<pair<int,int>> q;
    q.push({x, y});
    visit[x][y] = idx;

    int nc = 0;
    int np = 0;
    
    while (!q.empty()) {
        auto [cx, cy] = q.front();  q.pop();
        nc++;
        np += board[cx][cy];

        for (int k = 0; k < 4; k++) {
            if (edge[cx][cy][k]) {
                int nx = cx + dx[k];
                int ny = cy + dy[k];
                if (visit[nx][ny] != -1) continue;
                visit[nx][ny] = idx;
                q.push({nx, ny});
            }
        }
    }

    return {nc, np};
}


int main(void) {
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    cin >> n >> l >> r;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> board[i][j];
        }
    }

    int ans = 0;

    do {
        edge_cnt = 0;
        fill(&edge[0][0][0], &edge[54][54][4], false);
        for (int x = 0; x < n; x++) {
            for (int y = 0; y < n; y++) {
                connect(x, y);
            }
        }

        if (edge_cnt) ans++;

        idx = 0;
        fill(ncountry, ncountry+2505, 0);
        fill(npopularity, npopularity+2505, 0);
        fill(&visit[0][0], &visit[54][55], -1);

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (visit[i][j] != -1) continue;
                auto [c, p] = bfs(i, j);
                ncountry[idx] = c;
                npopularity[idx++] = p;
            }
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                board[i][j] = npopularity[visit[i][j]] / ncountry[visit[i][j]];
            }
        }

    } while (edge_cnt);

    cout << ans;
    return 0;
}