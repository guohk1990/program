#include <stdio.h>
#include <stdlib.h>

int test( int a, int b )
{
    a = a - 2;
    b = b - 3;

    return 0;
}

int main( )
{
    int a = 10;
    int b = 20;

    test( a, b );

    printf( "a = %d\n", a );
    printf( "b = %d\n", b );

    return 0;
}
