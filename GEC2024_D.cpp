#include <iostream>
#include <deque>
#include <vector>
using namespace std;

int N, M;
vector<vector<char>> mountain;
vector<vector<int>> visited;
deque<pair<int, int>> queue;
int dx[2] = {1, -1};
int dy[2] = {1, 1};

int main() {
    cin >> N >> M;
    mountain.assign(N + 1, vector<char>(2 * N + 1, 'O'));
    visited.assign(N + 1, vector<int>(2 * N + 1, 0));

    for (int i = 0; i < M; i++) {
        int a, b;
        cin >> a >> b;
        mountain[b][a] = 'X';
    }

    queue.push_back(make_pair(0, 0));
    visited[0][0] = 1;
    int max_height = 0;

    while (!queue.empty()) {
        int x = queue.front().first;
        int y = queue.front().second;
        queue.pop_front();

        for (int i = 0; i < 2; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (nx >= N + 1 || ny >= 2 * N + 1 || nx < 0 || ny < 0) continue;
            if (ny <= nx - 1 || ny >= 2 * N - nx + 1) continue;
            if (mountain[nx][ny] == 'X') continue;

            queue.push_back(make_pair(nx, ny));
            visited[nx][ny] = 1;
            if (nx > max_height) max_height = nx;
        }
    }

    if (visited[0][2 * N] != 1) {
        cout << -1 << endl;
    } else {
        cout << max_height << endl;
    }

    return 0;
}