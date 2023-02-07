#include <stdio.h>

int main() {

    int n,i,j,istina=0;

    scanf("%d",&n);

    for (i=1;i<n;i++) {
        for (j=i+1;j<n;j++) {
            if (i+j>n) {
                if (i*i+j*j==n*n) {
                    printf("%d,%d,%d",i,j,n);
                    istina=1;
                }
            }
        }
    }

    if (istina==0) printf("nema takvih trokuta.");

    return 0;

}