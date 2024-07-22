interface Add{
    void add();
    void print();
}

interface Sub{
    void sub();
    //void print();
}

class calculate implements Add,Sub{
    public void add()
    {
        System.out.println("100+10= "+(100+10));
    }
    public void sub()
    {
        System.out.println("90-9= "+(90-9));
    }
    public void print()
    {
        System.out.println("Print");
    }
}

public class Interface {
    public static void main(String[] arg)
    {
        calculate c = new calculate();
        c.add();
        c.sub();
        c.print();
    }
}
