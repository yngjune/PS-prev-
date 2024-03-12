#include <iostream>
#include <queue>
using namespace std;

enum block {EMPTY=0, APPLE=1, BODY=2};
pair<int,int> dir[4] = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
int ldir[4] = {3, 0, 1, 2};
int rdir[4] = {1, 2, 3, 0};

int n, k, l;
int board[105][105] = {EMPTY};
int tail_dir[105][105] = {0};
deque<pair<int, char>> rotate;

bool over = false;
int sec = 0;
int cur_dir = 0;
int headX = 1, headY = 1;
int tailX = 1, tailY = 1;


void move() {
    auto [movX, movY] = dir[cur_dir];
    int nx = headX + movX;
    int ny = headY + movY;

    if (nx < 1 || ny < 1 || nx > n || ny > n) {
        over = true;
        return;
    }

    if (board[nx][ny] == BODY) {
        over = true;
        return;
    }

    else if (board[nx][ny] == APPLE) {
        tail_dir[headX][headY] = cur_dir;
        headX = nx;
        headY = ny;
        board[headX][headY] = BODY;
    }

    else {
        tail_dir[headX][headY] = cur_dir;
        board[tailX][tailY] = EMPTY;
        board[nx][ny] = BODY;
        headX = nx;
        headY = ny;
        
        int td = tail_dir[tailX][tailY];
        tailX += dir[td].first;
        tailY += dir[td].second;
    }
}


int main(void) {
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    cin >> n >> k;
    for (int i = 0; i < k; i++) {
        int r, c;
        cin >> r >> c;
        board[r][c] = APPLE;
    }

    cin >> l;
    for (int i = 0; i < l; i++) {
        int sec;     char op;
        cin >> sec >> op;
        
        rotate.push_back({sec, op});
    }

    board[1][1] = BODY;
    while (!over) {
        sec++;
        move();
        if (sec != rotate[0].first) continue;
        if (rotate[0].second == 'L') {
            cur_dir = ldir[cur_dir];
        }
        else {
            cur_dir = rdir[cur_dir];
        }
        rotate.pop_front();
    }

    cout << sec;
    return 0;
}