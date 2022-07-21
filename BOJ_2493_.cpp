#include <iostream>
#include <stack>

using namespace std;

int N, K;
stack<pair<int, int>> st;
//stack ( { index, value } )

int main() {
    ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
    cin >> N; //탑의 수

    for(int i=1;i<=N;i++) {
        cin >> K; //비교할 값

        if(st.empty()) { //비어있다면 push 후 0 출력
            st.push({i,K});
            cout << "0 ";
        }
        else {
            while(!st.empty()) {
                if(st.top().second > K) { //신호 수신 가능 시
                    cout << st.top().first<< " "; //index 출력
                    break;
                } else {
                    st.pop(); // 신호 수신 불가 시 pop
                }
            }
        if(st.empty()) cout << "0 "; //스택이 비면 0 출력

        st.push({i,K}); //스택에 push
        }

    }
}
