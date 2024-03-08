#include <bits/stdc++.h>
using namespace std;

int ans = 1;
bool a_visit[26] = {0};
int r, c;
string board[25];

int dx[] = {-1, 0, 1, 0};
int dy[] = {0, 1, 0, -1};

void dfs(int x, int y, int depth) {
    ans = max(ans, depth);
    for (int i = 0; i < 4; i++) {
        int nx = x + dx[i];
        int ny = y + dy[i];

        if (nx < 0 || ny < 0 || nx >= r || ny >= c) 
            continue;
        if (!a_visit[board[nx][ny] - 'A']) {
            a_visit[board[nx][ny] - 'A'] = true;
            dfs(nx, ny, depth + 1);
            a_visit[board[nx][ny] - 'A'] = false;
        }
    }
}

int main(void) {
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    cin >> r >> c;
    for (int i = 0; i < r; i++) {
        cin >> board[i];
    }

    a_visit[board[0][0] - 'A'] = true;
    dfs(0, 0, 1);
    cout << ans;

    return 0;
}