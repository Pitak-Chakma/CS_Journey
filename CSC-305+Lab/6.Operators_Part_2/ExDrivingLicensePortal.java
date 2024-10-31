import java.util.Scanner;

public class ExDrivingLicensePortal {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Enter Your Age: ");
        int age = input.nextInt();

        if (age<0){
            System.out.println("Enter A valid Age.");
        }
        else{
            if(age>=18){
                System.out.println("You are Eligible for Driving Licence");
            }
            else{
                System.out.println("You are not Eligible for Driving Licence");
            }
        }

    }
}

