#include <stdio.h>

int main() {

    int n,i,j,s,brojac=0;

    scanf("%d",&n);

    for (i=1;i<=n;i++) {
        s=0;

        for (j=i;1;j++) {
            s=s+j;
            if (s==n) {
                brojac=brojac+1;
                break;
            }
            if (s>n) break;
        }
    }

    printf("%d\n",brojac);


    return 0;

}