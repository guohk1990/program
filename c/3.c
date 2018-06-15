#include <stdio.h>

int main( )
{
    struct s1{
        int a;
        char b;
        double c;
        char d;
    }s1;

    struct s2{
        char a;
        char b;
        int c;
        double d;
    }s2;

    struct s3{
        char a;
        char b;
        int c;
        double d;
        struct s1 e;
    }s3;

    printf( "sizeof( char ) = %d\n", sizeof( char ) );
    printf( "sizeof( int ) = %d\n", sizeof( int ) );
    printf( "sizeof( double ) = %d\n", sizeof( double ) );
    printf( "sizeof( s1 ) = %d\n", sizeof( s1 ) );
    printf( "sizeof( s2 ) = %d\n", sizeof( s2 ) );
    printf( "sizeof( s3 ) = %d\n", sizeof( s3 ) );

    return 0;
}
