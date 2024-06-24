import java.util.Scanner;

public class ExParameterOfARectangle {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        double a,b,c,d;
        System.out.println("Enter All Sides of a Rectangle One By one: ");
        a = input.nextDouble();
        b = input.nextDouble();
        c = input.nextDouble();
        d = input.nextDouble();
        System.out.println("Parameter : " + (a+b+c+d) + "unit");

    }
}
