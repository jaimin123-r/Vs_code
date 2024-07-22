public class Overloading {

    static int area(int w,int l)
    {
        return w*l;
    }
    static double area(double r)
    {
        return 3.14*r*r;
    }
    static int area(int a)
    {
        return a*a;
    }
    public static void main(String arg[])
    {
        System.out.println(area(12,6));
        System.out.println(area(10.10));
        System.out.println(area(70));
       
        
       
    }
    
}
