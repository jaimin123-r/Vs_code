class RCB
{
    void play()
    {
        System.out.println("Playing the cricket:");
    }
}
class MI extends RCB{
    void play()
    {
        super.play();
    }
}



public class Super {
    public static void main(String[] arg)
    {
        MI mi=new MI();
        mi.play();
        // final int jaimin=10;
        // jaimin=20;
        // System.out.print(jaimin);
    }
}
