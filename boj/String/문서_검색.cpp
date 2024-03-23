#include <iostream>
#include <string>

using namespace std;

int find(string buf, string word, int sidx) {
    int bl = buf.length();
    int wl = word.length();

    if (sidx >= bl) return -1;
    for (int i = sidx; i < bl; i++) {
        bool done = true;
        for (int j = 0; j < wl; j++) {
            if (buf[i+j] != word[j]) {
                done = false;
                break;
            }
        }
        if (done) return i + wl;
    }

    return -1;
}

int main(void) {
    // ios_base::sync_with_stdio(0);
    // cin.tie(0);

    string doc, word;
    getline(cin, doc);
    getline(cin, word);

    int cidx = 0;
    int ans = 0;
    while (cidx != -1) {
        cidx = find(doc, word, cidx);
        if (cidx != -1) ans++;
    }

    cout << ans;
    return 0;
}