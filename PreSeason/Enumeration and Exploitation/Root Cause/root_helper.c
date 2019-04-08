#include <stdio.h>

/* calculate the value being used in the xor decryption */

int main()
{
    char a1[] = "58dbc163b9b55b162220ce14ae9a2dfe";
    int v2 = 0;
    for (int i = 0; strlen(a1) > i; ++i )
        v2 += a1[i];
    int v3 = v2 % 10;
    printf("%d\n", v3);
}
