#include <iostream>
#include <tuple>

using namespace std;

int opposite[] = {0, 6, 5, 4, 3, 2, 1};
int dx[] = {0, 0, -1, 1};
int dy[] = {1, -1, 0, 0};

int bot, top, front, back, left_, right_;
int dice[7] = {0};

void move_east() {
    tie(bot, right_, top, left_) = make_tuple(right_, top, left_, bot);
}

void move_west() {
    tie(bot, right_, top, left_) = make_tuple(left_, bot, right_, top);
}

void move_north() {
    tie(bot, front, top, back) = make_tuple(back, bot, front, top);
}

void move_south() {
    tie(bot, front, top, back) = make_tuple(front, top, back, bot);
}

int main(void) {
    iostream::sync_with_stdio(0);
    cin.tie(0);

    int n, m, x, y, k;
    int board[25][25];
    bot = 6, top = 1, front = 5, back = 2, left_ = 4, right_ = 3;

    cin >> n >> m >> x >> y >> k;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> board[i][j];
        }
    }

    for (int i = 0; i < k; i++) {
        int dir;    cin >> dir;
        
        int nx = x + dx[dir-1];
        int ny = y + dy[dir-1];
        if (nx < 0 || ny < 0 || nx >= n | ny >= m) continue;
        
        switch (dir)
        {
        case 1:
            move_east();
            break;
        case 2:
            move_west();
            break;
        case 3:
            move_north();
            break;
        default:
            move_south();
            break;
        }

        if (board[nx][ny] == 0) {
            board[nx][ny] = dice[bot];
        }
        else {
            dice[bot] = board[nx][ny];
            board[nx][ny] = 0;
        }
        x = nx; y = ny;
        cout << dice[top] << '\n';
    }

    return 0;
}