#include <iostream>
#include <queue>

using namespace std;

int main(void) {
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int n, x;
    priority_queue<int, vector<int>, less<>> left;
    priority_queue<int, vector<int>, greater<>> right;

    cin >> n;
    while (n--) {
        cin >> x;
        right.push(x);

        if (right.size() > left.size()) {
            left.push(right.top());
            right.pop();
        }

        if (int lt = left.top(), rt = right.top(); lt > rt) {
            left.pop();
            right.pop();
            left.push(rt);
            right.push(lt);
        }

        cout << left.top() << '\n';
    }
    
    return 0;
}