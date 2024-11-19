#include <iostream>
#include <vector>

using namespace std;

string findStringAtRank(int rank, int length) {
    string result;
    vector<char> alphabets;

    for (int i = 0; i < 26; ++i) {
        alphabets.push_back('a' + i);
    }

    for (int i = length - 1; i >= 0; --i) {
        int index = rank % (26 - i);
        result.push_back(alphabets[index]);
        alphabets.erase(alphabets.begin() + index);
        rank /= (26 - i);
    }

    return result;
}

int main() {
    int rank, length;
    cin >> rank >> length;

    cout << findStringAtRank(rank, length) << endl;

    return 0;
}