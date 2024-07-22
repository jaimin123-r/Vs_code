import Package.A;
import Package.B;

public class Package_ex {
    public static void main(String[] args) {
        A a=new A();
        a.hello_A();
        B b =new B();
        b.hello_A();
        b.hello_B();
    }
}
