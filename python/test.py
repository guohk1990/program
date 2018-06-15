#! /usr/bin/env python3

print( "Hello World!" );
print( "你好，世界!" );

str = 'Runoob'

print( str )
print( str[ 0 : -1 ] )
print( str[ 0 ] )
print( str[ 2 : 5 ] )
print( str[ 2: ] )
print( str * 2 )
print( str + '你好' )

print( '-----------------------------' )

print( 'hello\nrunoob' )
print( r'hello\nrunoob' )

x = "a"
y = "b"

print( x )
print( y )

print( '----------' )

print( x, end = ' ' )
print( y, end = ' ' )
print( )

import sys
print( '==========Python import mode==========' )
print( '命令行参数为:' )
for i in sys.argv:
    print( i )
print( '\n python 路径为', sys.path )

print( '\n' )
from sys import argv, path
print( '===========python from import==========' )
print( 'path:', path )

print( '\n' )
list = [ 'abcd', 786, 2.23, 'runoob',70.2 ]
tinylist = [ 123, 'runoob' ]

print( list )
print( list[ 0 ] )
print( list[ 1 : 3 ] )
print( list[ 2 : ] )
print( tinylist * 2 )
print( list + tinylist )

print( '\n' )
tuple = ('abcd', 786, 2.23, 'runoob', 70.2 )
tinytuple = ( 123, 'runoob' )

print( tuple)
print( tuple[ 0 ] )
print( tuple[ 1:3 ] )
print( tuple[ 2: ] )
print( tinytuple * 2 )
print( tuple + tinytuple )

print( '\n' )
student = { 'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose' }
print( student )

if( 'Rose' in student ) :
    print( 'Rose 在集合中' )
else :
    print( 'Rose 不在集合中' )

a = set( 'abracadabra' )
b = set( 'alacazam' )

print( a )
print( a - b )
print( a | b )
print( a & b )
print( a ^ b )

print( '\n' )
dict = {}
dict[ 'one' ] = "1 - 菜鸟教程"
dict[ 2 ] = "2 - 菜鸟工具"

tinydict = { 'name': 'runoob', 'code':1, 'site':'www.runoob.com'}

print( dict[ 'one' ] )
print( dict[ 2 ] )
print( tinydict )
print( tinydict.keys())
print( tinydict.values())

list1 = [ 'Google', 'Runoob', 1997, 2000 ];
list2 = [ 1, 2, 3, 4, 5, 6, 7 ];

print( '\n' );
print( "lsit1[0]:", list1[ 0 ] );
print( "list2[ 1:5 ]:", list2[ 1:5 ] );
del list1[ 2 ];
print( list1 );

print('\n')
tup1 = ( 'Google', 'Runoob', 1997, 2000 )
tup2 = ( 1, 2, 3, 4, 5, 6, 7 )
print( "tup1[ 0 ]:", tup1[ 0 ] )
print( "tup2[ 1:5 ]:", tup2[ 1:5 ] )
tup3 = tup1 + tup2;
print( tup3 )
del tup3;

print( '\n' )
dict = { 'Name':'Runoob', 'Age':7, 'Class':'Firt' }
print( "dict[ name ]:", dict[ 'Name' ] )
print( "dict[ 'Age' ]:", dict[ 'Age' ] )

print( '\n' )
var1 = 100
if var1:
    print( "1 - if 表达式条件为 true" )
    print( var1 )

var2 = 0
if var2:
    print( "2 - if 表达式条件为 true" )
    print( var2 )
print( 'Good bye!' )

print( '\n' )
age = int( input( "请输入你家狗的年龄: " ) )
print( "" )
if age <= 0:
    print( "你是在逗我吧！" )
elif age == 1:
    print( "相当于14岁的人。" )
elif age == 2:
    print( "相当于22岁的人。" )
elif age > 2:
    human = 22 + ( age - 2 ) * 5
    print( "对应人类年龄：", human )

print( 5 == 6 )
x = 5
y = 8
print( x == y )

print( '\n' )
for letter in 'Runoob':
    if letter == 'b':
        break
    print( '当前字母为：', letter )

var = 10
while var > 0:
    print( '当前变量值为：', var )
    var = var - 1
    if var == 5:
        break
print( "Good Bye!" )

print( '\n' )
for n in range( 2, 10 ):
    for x in range( 2, n ):
        if n % x == 0:
            print( n, '等于', x, '*', n//x )
            break
    else:
        print( n, ' 是质数' )

print( '\n' )
def printinfo( arg1, *vartuple ):
    print( "输出：" )
    print( arg1 )
    for var in vartuple:
        print( var )
    return

printinfo( 10 )
printinfo( 70, 60, 50 )

print( '\n' )
sum = lambda arg1, arg2: arg1 + arg2

print( "相加后的值为：", sum( 10, 20 ) )
print( "相加后的值为; ", sum( 20, 20 ) )

print( '\n' )
def sum( arg1, arg2 ):
    total = arg1 + arg2
    print( "函数内: ", total )
    return total

total = sum( 10, 20 )
print( "函数外：", total )


input ( "\n\n按下 enter 键退出。" )
