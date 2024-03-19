#include <iostream>
#include <vector>
using namespace std;

int board[9][9];
vector<pair<int,int>> candi;
int lcandi = 0;
bool done = false;

bool check(int x, int y, int val) {
    for (int i = 0; i < 9; i++) {
        if (board[x][i] == val) return false;
    }
    
    for (int i = 0; i < 9; i++) {
        if (board[i][y] == val) return false;
    }
    
    int bx = (x / 3) * 3;
    int by = (y / 3) * 3;
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            if (board[bx+i][by+j] == val) return false;
        }
    }
    
    return true;
}

void backtrack(int depth) {
    if (done) return;
    if (depth == lcandi) {
        done = true;
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                cout << board[i][j] << ' ';
            }
            cout << '\n';
        }
        return;
    }
    
    auto [cx, cy] = candi[depth];
    for (int i = 1; i <= 9; i++) {
        if (check(cx, cy, i)) {
            board[cx][cy] = i;
            backtrack(depth + 1);
            board[cx][cy] = 0;
        }
    }
}

int main(void) {
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    for (int i = 0; i < 9; i++) {
        for (int j = 0; j < 9; j++) {
            cin >> board[i][j];
            if (board[i][j] == 0) {
                candi.push_back({i, j});
                lcandi++;
            }
        }
    }

    backtrack(0);

    return 0;
}