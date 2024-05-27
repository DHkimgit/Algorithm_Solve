#include<iostream>
#include<string>
#include<unordered_set>
#include<queue>
#include<vector>
using namespace std;

int main() {
	int N, M;
	cin >> N >> M;
	unordered_set<string> unSeen;
	priority_queue<string, vector<string>, greater<string>> unLook;
	int k = 0;
	for (int i = 0; i < N; i++) {
		string tmp;
		cin >> tmp;
		unSeen.insert(tmp);
	}
	for (int i = 0; i < M; i++) {
		string tmp;
		cin >> tmp;
		if (unSeen.find(tmp) != unSeen.end()) {
			k += 1;
			unLook.push(tmp);
		}
	}
	cout << k << '\n';
	while (!unLook.empty()) {
		cout << unLook.top() << '\n';
		unLook.pop();
	}

    return 0;

}