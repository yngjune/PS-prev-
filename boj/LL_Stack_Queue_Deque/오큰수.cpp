#include <iostream>
#include <stack>
#include <vector>

using namespace std;

int main(void) {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    vector<int> seq;
    stack<int> stk;
    int n, x;

    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> x;
        seq.push_back(x);
    }
    vector<int> nge(n, -1);
    for (int i = n - 1; i >= 0; i--) {
        while (!stk.empty() && stk.top() <= seq[i])
            stk.pop();
        if (!stk.empty()) {
            nge[i] = stk.top();
        }
        stk.push(seq[i]);
    }

    for (auto i : nge) cout << i << " ";
    return 0;
}