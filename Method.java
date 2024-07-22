public class Method {

    void hello()
    {
        System.out.println("hello i am conda reddy");
    }
    public static void main(String[] arg)
    {
        Method obj = new Method(); // if you want to call non-static method you do like this
        obj.hello();// make a object and throgh object you can call non-static methods
    }
}
