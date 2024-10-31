import java.util.Scanner;

public class ExSwap2Nums {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int num1,num2,container;
        System.out.print("Enter 1st Number: ");
        num1 = input.nextInt();
        System.out.print("Enter 2nd Number: ");
        num2 = input.nextInt();

        System.out.println("Before: "+ num1 + " " + num2);
        //swap operation
        container = num1;
        num1 = num2;
        num2 = container;
        System.out.println("After: "+ num1 + " " + num2);

    }
}
