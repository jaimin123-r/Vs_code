import java.lang.Exception;

public class Exceptions {
    public static void main(String[] arg)
    {
        try
        {
            // String sr="jaimin";
            // System.out.println(sr[0]);
            int arr[] = new int[5];
            arr[0]=10;
            arr[1]=90;
            System.out.println(arr[6]);
        }
        catch(Exception e)
        {
            System.out.println(e+"  <-- This Custom Error");
        }
    }
}
