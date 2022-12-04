#include <bits/stdc++.h>

using namespace std;

int score(char x) {
    if('a' <= x && x <= 'z') {
        return x - 'a' + 1;
    } else {
        return 26 + (x - 'A') + 1;
    }
}

int main() {
    ifstream input;
    input.open("input");

    string line;

    int ans = 0;

    while(input) {
        getline(input, line);
        if(line == "") {
            break;
        }

        int half = line.length() / 2;
        auto aa = line.substr(0, half);
        auto bb = line.substr(half);
        set<char> as(aa.begin(), aa.end());
        set<char> bs(bb.begin(), bb.end());

        vector<char> inter = {};
        set_intersection(as.begin(), as.end(), bs.begin(), bs.end(), back_inserter(inter));

        ans += score(inter[0]);
    }
    cout << "Part1 " << ans << endl;

    input.clear();
    input.seekg(0);

    ans = 0;
    vector<vector<string>> batches;
    vector<string> batch;
    int i = 0;
    while(input) {
        getline(input, line);
        if(line == "") {
            break;
        }

        if(i > 0 && i % 3 == 0) {
            // Can't do the intersection here because it would miss the last batch
            batches.push_back(batch);
            batch = {};
        }
        batch.push_back(line);
        i++;
    }
    batches.push_back(batch);

    for(auto batch: batches) {
        bool found = false;
        for(auto x: batch[0]) {
            if(found) break;
            for(auto y: batch[1]) {
                if(found) break;
                for(auto z: batch[2]) {
                    if(found) break;
                    if(x == y && y == z) {
                        ans += score(x);
                        found = true;
                    }
                }
            }
        }
    }

    cout << "Part2 " << ans << endl;

}
