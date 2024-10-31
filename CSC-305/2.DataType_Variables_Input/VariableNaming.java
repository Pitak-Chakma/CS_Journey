import java.sql.SQLOutput;

public class VariableNaming {
    public static void main(String[] args) {
        System.out.println("Camel Case - myAge,isEmployee");

        // keep it short and simple
        // should be descriptive


        String Rules = "all alphanumeric characters _ $\n"
                + "no keywords allowed\n"
                + "cant start with digit\n"
                + "case sensitive\n";

        System.out.println(Rules);
    }
}
