public class TypeConversion {
    public static void main(String[] args) {
        // implicit - automatic - smaller to larger = int > float
        // explicit - manual - larger to smaller = float > int

        float num1 = 5; // int into float
        System.out.println(num1);

        int num2 = (int) 5.0;
        System.out.println(num2);
    }
}
