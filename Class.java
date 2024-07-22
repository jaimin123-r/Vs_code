class A
{
    A()
    {
        System.out.println("I am Constructor in class A");
    }
    A(int t)
    {
        System.out.println("I am parameterize Constructor "+ t);
    }
}
class B extends A
{
    B()
    {
        super(10);
        System.out.println("I am Consructor in class B ");
    }
}

public class Class {
    public static void main(String arg[])
    {
        A objA = new A();
        B objB = new B();

    }
}
