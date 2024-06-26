import java.util.Scanner;

public class ExPositiveNegZero {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Emter Number: ");
        float num = input.nextFloat();

        if (num<0){
            System.out.println("Negative");
        }
        else if (num == 0){
            System.out.println("Zero");
        }
        else {
            System.out.println("Positive");
        }
    }
}
