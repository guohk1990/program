import java.io.*;

public class EmployeeTest{
    public static void main( String []args ){
        Employee emOne = new Employee( "小可爱" );
        Employee emTwo = new Employee( "大可爱" );

        emOne.setAge( 27 );
        emOne.emDecision( "助理" );
        emOne.setSalary( 10000.0 );
        emOne.printEmployee( );

        System.out.println( "\n" );

        emTwo.setAge( 24 );
        emTwo.emDecision( "前台" );
        emTwo.setSalary( 12000.0 );
        emTwo.printEmployee( );
    }
}
