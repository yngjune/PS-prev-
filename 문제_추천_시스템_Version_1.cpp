#include <iostream>
#include <set>

using namespace std;

int main(void) {
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int n, m;
    cin >> n;
    set<int> prob[101];

    while (n--) {
        int p, l;
        cin >> p >> l;
        prob[l].insert(p);
    }

    cin >> m;
    while (m--) {
        string op;
        cin >> op;
        if (op == "add") {
            int p, l;
            cin >> p >> l;
            prob[l].insert(p);
        }
        else if (op == "solved") {
            int p;
            cin >> p;
            for (int l = 1; l <= 100; l++) {
                prob[l].erase(p);
            }
        }
        else if (op == "recommend") {
            int x;
            cin >> x;
            if (x == 1) {
                for (int l = 100; l >= 1; l--) {
                    if (!prob[l].empty()) {
                        cout << *prev(prob[l].end()) << '\n';
                        break;
                    }
                }
            }
            else {
                for (int l = 1; l <= 100; l++) {
                    if (!prob[l].empty()) {
                        cout << *prob[l].begin() << '\n';
                        break;
                    }
                }
            }
        }
    }

    return 0;
}