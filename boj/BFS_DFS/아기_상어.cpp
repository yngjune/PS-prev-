#include <iostream>
#include <queue>
#include <algorithm>

using namespace std;

int n;
int board[25][25];
int dx[] = {-1, 0, 0, 1};
int dy[] = {0, -1, 1, 0};

int ssize = 2;
int sstk = 0;
int sx, sy;
int sec = 0;


int main(void) {
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    cin >> n;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> board[i][j];
            if (board[i][j] == 9) {
                sx = i;
                sy = j;
            }
        }
    }

    while (true) {
        queue<pair<int,int>> q;
        vector<pair<int,int>> candi;
        int dist[25][25];
        fill(&dist[0][0], &dist[n][n-1], -1);
        int found = -1;
        
        q.push({sx, sy});
        dist[sx][sy] = 0;
        while (!q.empty()) {
            auto [cx, cy] = q.front();
            q.pop();
            if (found != -1 && dist[cx][cy] >= found)
                continue;

            for (int i = 0; i < 4; i++) {
                int nx = cx + dx[i];
                int ny = cy + dy[i];
                if (nx < 0 || ny < 0 || nx >= n || ny >= n)
                    continue;
                if (dist[nx][ny] != -1)
                    continue;
                if (board[nx][ny] == 0 || board[nx][ny] == ssize) {
                    q.push({nx, ny});
                    dist[nx][ny] = dist[cx][cy] + 1;
                }
                else if (board[nx][ny] < ssize) {
                    candi.push_back({nx, ny});
                    dist[nx][ny] = dist[cx][cy] + 1;
                    found = dist[nx][ny];
                }
            }
        }

        if (candi.size() == 0)
            break;
        if (candi.size() > 1)
            sort(candi.begin(), candi.end());
        auto [nx, ny] = candi[0];
        board[nx][ny] = 9;
        board[sx][sy] = 0;
        sec += dist[nx][ny];
        sx = nx;    sy = ny;
        sstk++;
        if (sstk == ssize) {
            ssize++;
            sstk = 0;
        }
    }

    cout << sec;
    return 0;
}