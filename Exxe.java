interface bike
{
    int gear(int gear_no);
    void horn();
    void cluch();
}
class ducati implements bike{
    int gear(int gear_no)
    {
        System.out.println("Gear is "+ gear_no);
    }
    void horn()
    {
        System.out.println("horn is blowing");
    }
    void cluch()
    {
        System.out.println("cluch");
    }
}
class penigal_v4 extends ducati
{
    int gear(int gear_no)
    {
        System.out.println("Gear is "+ gear_no);
    }
    void horn()
    {
        System.out.println("horn is blowing");
    }
    void cluch()
    {
        System.out.println("cluch");
    }
    void look()
    {
        System.out.println("kaatil");
    }
}

public class Exxe {
    public static void main(String[] parv)
    {
        System.out.println(parv[0]);

        int[] arr=new int[5];
        int[]={10,20,30,40};

        int p[][]=new int[3][2];

        p[0][0]=1;
        p[0][1]=2;
        p[1][0]=3;
        p[1][1]=4;
        p[2][0]=5;
        p[2][1]=6;

    }
}
