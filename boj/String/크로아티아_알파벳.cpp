#include <iostream>
#include <string>

using namespace std;

int main(void) {
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    string word[] = {"c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="};
    const int WLEN = 8;
    int ans = 0;

    string sentence;
    cin >> sentence;

    for (int i = 0; i < sentence.length(); i++) {
        for (auto cword : word) {
            bool found = true;
            int j = 0;
            for (; j < cword.length() && i + j < sentence.length(); j++) {
                if (sentence[i+j] != cword[j]) {
                    found = false;
                    break;
                }
            }
            if (found && j == cword.length()) {
                i += cword.length() - 1;
                break;
            }
        }
        ans++;
    }

    cout << ans;
    return 0;
}