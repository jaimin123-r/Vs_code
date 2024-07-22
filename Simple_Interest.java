import java.util.*;
import java.io.*;

public class Simple_Interest
{
    public static void main(String[] arg)
    {
        Scanner sc =new Scanner(System.in);
        double rate,year,principle;

        System.out.print("Enter The Amount:");
        principle=sc.nextDouble();

        System.out.print("Enter The Interest Rate:");
        rate=sc.nextDouble();

        System.out.print("Enter The Time(In year):");
        year=sc.nextDouble();

        double total=(rate*year*principle)/100;
        System.out.println("Simple Interest is "+ total);

        double total2=principle * (Math.pow((1 + rate / 100), year));

        System.out.println("Compound interest is "+ total2);

    }
}