#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <bits/stdc++.h>

using namespace std;

int main() {
    ifstream input_file;
    input_file.open("input");

    string line;

    vector<int> ans;

    int temp = 0;
    while(input_file) {
        getline(input_file, line);
        if(line == "") {
            ans.push_back(temp);
            temp = 0;
        } else {
            temp += stoi(line);
        }
    }

    sort(ans.begin(), ans.end(), greater<int>());
    cout << "Part1: " << ans[0] << endl;

    cout << "Part2: " << ans[0] + ans[1] + ans[2] << endl;
    return 0;
}
