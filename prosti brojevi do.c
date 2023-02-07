#include <stdio.h>

int main() {

    int n,i,j,brojac,b=0;

    scanf("%d",&n);

    for (i=2;i<=n;i++) {
        brojac=0;
        for (j=1;j<=i;j++) {
            if (i%j==0) brojac=brojac+1;
        }

        if (brojac==2) b=b+1;
    }

    printf("%d\n",b);


    return 0;

}