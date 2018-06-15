#! /usr/bin/python3

def area( width, height ) :
    return width * height

def print_welcome( name ) :
    print( "Welcome", name )

print_welcome( "Runoob" )

w = 4
h = 5

print( "width = ", w, " height = ", h, " area = ", area( w, h ) )

def printme( str ) :
    print( str )
    return

printme( "我要调用用户自定义函数" )
printme( "再次调用同一函数" )

print( '\n' )
def ChangeInt( a ) :
    a = 10

b = 2
ChangeInt( b )
print( b )

print( '\n' )
def changeme( mylist ):
    "修改传入的列表"
    mylist.append( [ 1, 2, 3, 4 ] )
    print( "函数内取值: ", mylist )
    return

mylist = [ 10, 20, 30 ]
changeme( mylist )
print( "函数外取值: ", mylist )

print( '\n' )
def printinfo( name, age ):
    print( "名字: ", name )
    print( "年龄: ", age )
    return

printinfo( age = 50, name = "runoob" )

print( '\n' )
def printinfo( name , age = 35 ):
    print( "名字：", name )
    print( "年龄: ", age )
    return

printinfo( age = 50, name = "runoob" )
print( "--------------------" )
printinfo( name = "runoob" )

