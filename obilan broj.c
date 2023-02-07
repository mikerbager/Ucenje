#include <stdio.h>

int main() {

    int k,i,s,j;

    scanf("%d",&k);

    for (i=1;i<=k;i++) {
        s=0;

        for (j=1;j<i;j++) {
            if (i%j==0) s=s+j;
        }

        if (i<s) printf("%d\n",i);
    }

    return 0;

}