class FK extends Thread
{
    public void run()
    {
    for(int i=0;i<=50;i++)
    {
        System.out.println("Jay Shree Ram");
        sleep(10);
    }
}
}
class PK implements Runnable
{
    public void run()
    {
         for(int i=0;i<=50;i++)
        {
            System.out.println("Krishna");
        }
    }
}

public class THRead_exa {
    public static void main(String[] agr)
    {
        FK fk=new FK();
        PK pk=new PK();
        Thread ttt=new Thread(pk);
        fk.start();
        ttt.start();
    } 
}
