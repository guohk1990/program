import java.io.*;

public class Employee{
    String name;
    int age;
    String decision;
    double salary;

    public Employee( String emname ){
        this.name = emname;
    }

    public void setAge( int emage ){
        age = emage;
    }

    public void emDecision( String emDec ){
        decision = emDec;
    }

    public void setSalary( double emSalary ){
        salary = emSalary;
    }

    public void printEmployee( ){
        System.out.println( "姓名：" + name );
        System.out.println( "年龄：" + age );
        System.out.println( "职务：" + decision );
        System.out.println( "薪水：" + salary );
    }
}
