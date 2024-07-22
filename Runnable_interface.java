class Runnable_thread1 implements Runnable
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
class Runnable_thread2 implements Runnable
{
    public void run()
    {
        int i=0;
        while(i<100)
        {
            System.out.println("i love gg");
             i++;
        }
    }
}

public class Runnable_interface {
    public static void main(String[] e)
    {
        Runnable_thread1 t1=new Runnable_thread1();
        Thread th1=new Thread(t1);

        Runnable_thread2 t2=new Runnable_thread2();
        Thread th2=new Thread(t2);

        th1.start();
        th2.start();
    }
}
