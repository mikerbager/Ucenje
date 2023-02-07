#include <stdio.h>

int main() {

    int m,n,i,j,k,s1,s2;

    scanf("%d %d",&m,&n);

    for (i=m;i<=n;i++) {

        s1=0;
        for (j=1;j<i;j++) {
            if (i%j==0) s1=s1+j;
        }

        for (j=i+1;j<=n;j++) {

            s2=0;
            for (k=1;k<j;k++) {
                if (j%k==0) s2=s2+k;
            }

            if ((s1==j)&(s2==i)) printf("%d,%d\n",i,j);
        }



    }

    return 0;

}