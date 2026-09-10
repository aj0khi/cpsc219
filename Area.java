import java.util.Scanner;
public class Area {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter the radius of the circle (float): ");
        double dRadius = scanner.nextDouble();
        double dArea = Math.PI * Math.pow(dRadius, 2);
        System.out.println("Area of the circle: " + dArea);
        scanner.close();
    }

}
