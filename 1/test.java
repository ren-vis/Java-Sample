
class test {

  public static void main(String[] args) {
    
    int first = 10;
    int second = 20;

    // add two numbers
    int sum = first + second;
    System.out.println(first + " + " + second + " = "  + sum);
    
    for (int i = 0; i < 5; i++) {
         System.out.println(i);
        try {
            Thread.sleep(20000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
  }
}