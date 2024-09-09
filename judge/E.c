#include <stdio.h>

int main(){
    int t;
    scanf("%d", &t);

    for(int i = 0; i < t; i++){
        int boy, girl;
        scanf("%d, %d", &boy, &girl);
        int maxteam = 0;

        for(int j = 1; j < boy + 1 ; j++) {
            int boy_tmp = boy;
            int girl_tmp = girl;
            boy_tmp -= j;
            girl_tmp -= 2*j;
            if (girl_tmp <= 0) continue;
            int result = j;

            while(boy_tmp >= 2){
                boy_tmp -= 2;
                girl_tmp -= 1;
                result += 1;
                if (girl_tmp == 0) break;
            }
        
            if(result < maxteam) break;
            if(result >= maxteam) maxteam = result;
        }
        printf("%d", maxteam);
    }
}
