#include <bits/stdc++.h>

using namespace std;


// Helper function for parsing that works similar to python's .split()
void split_string(
    string const &input,
    char delim,
    vector<string> &out
) {
    stringstream s(input);
    string s2;

    while(getline(s, s2, delim)) {
        out.push_back(s2);
    }
}



int main() {
    ifstream input;
    input.open("input");

    string line;

    int ans1 = 0;
    int ans2 = 0;

    while(input) {
        getline(input, line);
        if(line == "") break;

        // Parsing
        vector<string> parts;
        split_string(line, ',', parts);

        vector<string> lhs;
        split_string(parts[0], '-', lhs);

        vector<string> rhs;
        split_string(parts[1], '-', rhs);

        int a = stoi(lhs[0]);
        int b = stoi(lhs[1]);
        int c = stoi(rhs[0]);
        int d = stoi(rhs[1]);


        // Solving
        if (a <= c && b >= d) {
            ans1++;
        }
        else if (c <= a && d >= b) {
            ans1++;
        }

        bool found = false;
        vector<int> rangeA(b-a+1);
        iota(rangeA.begin(), rangeA.end(), a);
        vector<int> rangeB(d-c+1);
        iota(rangeB.begin(), rangeB.end(), c);

        for(auto a: rangeA) {
            for(auto b: rangeB) {
                if(a == b) {
                    found = true;
                    break;
                }
            }
            if(found) break;
        }
        if(found) ans2++;


    }
    cout << "Part1 " << ans1 << endl;
    cout << "Part2 " << ans2 << endl;

}
