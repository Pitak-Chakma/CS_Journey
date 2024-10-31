import java.util.Scanner;

public class ExTicketDiscountCalculator {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Enter Your Age: ");
        int age = input.nextInt();
        System.out.println("Are You Female: (true or false) ");
        boolean isFemale = input.hasNextBoolean();

        if (age<5){
            System.out.println("75% Discount");
        }
        else if (isFemale){
            System.out.println("50% Discount");
        }
        else if (age>60 && !isFemale){
            System.out.println("30% Discount");
        }
        else{
            System.out.println("10% discount");
        }
    }
}
