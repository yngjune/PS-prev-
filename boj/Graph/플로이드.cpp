#include <iostream>

#define MAXDIST 10000000

using namespace std;

int main(void) {
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int n, m;
    int dist[105][105];

    cin >> n >> m;

    for (int i = 1; i <= n; i++) {
        fill(dist[i], dist[i]+n+1, MAXDIST);
        dist[i][i] = 0;
    }

    for (int i = 0; i < m; i++) {
        int a, b, c;
        cin >> a >> b >> c;
        dist[a][b] = min(dist[a][b], c);
    }

    for (int k = 1; k <= n; k++) {
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                if (dist[i][k] + dist[k][j] < dist[i][j])
                    dist[i][j] = dist[i][k] + dist[k][j];
            }
        }
    }

    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            if (dist[i][j] == MAXDIST)
                cout << 0;
            else
                cout << dist[i][j];
            cout << ' ';
        }
        cout << '\n';
    }
    return 0;
}