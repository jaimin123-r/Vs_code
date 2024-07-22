class My_thread1 extends Thread
{
    public void run()
    {
        int i=0;
        while(i<100)
        {
            System.out.println("Hi");
             i++;
        }
    }
}
class My_thread2 extends Thread
{
    @Override
    public void run()
    {

        int i=0;
        while(i<100)
        {
            System.out.println("I love you");
             i++;
        }
    }
}


public class Threading {
    public static void main(String[] arg)
    {
        My_thread1 t1=new My_thread1();
        My_thread2 t2=new My_thread2();
        t1.start();
        t2.start();
    }
}
