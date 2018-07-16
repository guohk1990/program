class Animal{
    public void eat( ){
        System.out.println( "animal : eat" );
    }
}

class Dog extends Animal{
    public void eat( ){
        System.out.println( "dog : eat" );
    }

    public void eatTest( ){
        this.eat( );
        super.eat( );
    }
 }

public class AnimalTest{
    public static void main( String []args ){
        Animal a = new Animal( );
        a.eat( );
        Dog d = new Dog( );
        d.eat( );
        d.eatTest( );
    }
}
