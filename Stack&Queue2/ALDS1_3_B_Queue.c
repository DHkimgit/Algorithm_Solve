#include<stdio.h>
#include<string.h>
#define LEN 100005

// 프로세스를 나타내는 구조체
typedef struct pp {
    char name[100];
    int t;
} P;

P Q[LEN];
int head, tail, n;

void enqueue (P x) {
    Q[tail] = x;
    head = (tail + 1) % LEN;
}

P dequeue () {
    P x = Q[head];
    head = (head + 1) % LEN;
    return x;
}

int min(int a, int b) {return a < b ? a : b;} //최솟값 리턴

int main() {
    int elaps = 0, c;
    int i, q;
    P u;
    scanf("%d %d", &n, &q);

    //모든 프로세스를 큐에 차례대로 추가
    for (i = 1; i <= n; i++) {
        scanf("%s", Q[i].name);
        scanf("%d", &Q[i].t);
    }
    head = 1;
    tail = n + 1;

    // 시뮬레이션
    while (head != tail) {
        u = dequeue();
        c = min(q, u.t);
        u.t -= c;
        elaps += c;
        if(u.t > 0) enqueue(u);
        else {
            printf("%s %d\n", u.name, elaps);
        }
    }
    return 0;
}

