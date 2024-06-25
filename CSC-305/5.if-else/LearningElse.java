public class LearningElse {
    public static void main(String[] args) {
        boolean isMale = false;
        String name = "Jyoti";

        System.out.println("Before If");

        if (isMale) {
            System.out.println("Mr " + name);
        }
        else{
            System.out.println("Ms "+ name);
        }
        System.out.println("After If");
    }
}
// curly bracks can be skiped if statements are written in one line (if - else block)