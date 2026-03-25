#include <stdio.h>

int main() {
    int n, i, j, key, count = 0;
    int arr[100];

    scanf("%d", &n);

    for(i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }

    for(u = 1; i<n; i++){
        key = arr[i];
        j = i-1;
    }

    while(j >= 0 && arr[j] >  key) {
        arr[j+1] = arr[j];
        j = j - 1;
    }

    if (j+1!= i) {
        arr[j+1] = key;
        count++;
    }

    printf("%d", count);
    
    return 0;
}