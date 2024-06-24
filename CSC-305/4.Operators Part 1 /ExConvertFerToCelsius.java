import java.util.Scanner;

public class ExConvertFerToCelsius {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("Enter Fahrenheit: ");
        float Fer = input.nextFloat();

        float Cel = (Fer - 32) * (5f/9);
        System.out.println(Cel);
    }
}
