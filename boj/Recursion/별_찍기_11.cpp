#include <iostream>

using namespace std;

char out[8000][8000] = {0,};
int n;

void fill(int n, int x, int y) {
    if (n == 3) {
        out[x][y+2] = '*';
        out[x+1][y+1] = '*';
        out[x+1][y+3] = '*';
        for (int i = 0; i < 5; i++) out[x+2][y+i] = '*';
        return;
    }

    int m = n / 2;
    fill(m, x, y+m);
    fill(m, x+m, y);
    fill(m, x+m, y+n);
}

int main(void) {
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    cin >> n;
    fill(n, 0, 0);

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n * 2; j++) {
            if (out[i][j] == '*') cout << out[i][j];
            else cout << ' ';
        }
        cout << '\n';
    }

    return 0;
}