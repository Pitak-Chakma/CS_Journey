import java.util.Scanner;

public class ExAreaOfTriangle {
    public static void main(String[] args) {
        int height,base;
        Scanner input = new Scanner(System.in);

        System.out.print("Enter Height of a Triangle: ");
        height = input.nextInt();

        System.out.print("Enter Base of a Triangle: ");
        base = input.nextInt();

        float area = ((1f/2) * base * height);
        System.out.println("Area of a Triangle:" + area);
    }
}
