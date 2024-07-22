import java.util.*;
import java.io.*;

public class Interest
{
    public static final String ANSI_RESET = "\u001B[0m"; 
    public static final String ANSI_YELLOW = "\u001B[33m";
    public static final String ANSI_RED_BACKGROUND = "\u001B[41m"; 

    public static void main(String[] arg)
    {
        Scanner sc =new Scanner(System.in);
        double rate,year,principle;
        int ch;
        System.out.print("Enter The Amount:");
        principle=sc.nextDouble();

        System.out.print("Enter The Interest Rate:");
        rate=sc.nextDouble();

        System.out.print("Enter The Time(In year):");
        year=sc.nextDouble();

        System.out.println(ANSI_RED_BACKGROUND+"1)Simple Interest\n 2)Compound Interest"+ANSI_RESET);
        do
        {
            System.out.println(ANSI_YELLOW+"Enter The Choice:"+ANSI_RESET);
            ch = sc.nextInt();

            switch(ch)
        {
            case 1:
            double total=(rate*year*principle)/100;
            System.out.println("Simple Interest is "+ total);
            break;
            case 2:
            double total2=principle * (Math.pow((1 + rate / 100), year));
            System.out.println("Compound interest is "+ total2);
            break;
            default:
                System.out.println("Not Valid Choice!");
        }
        }while(ch!=3);

       
        

    }
}