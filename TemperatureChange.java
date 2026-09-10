import java.util.Scanner;
public class TemperatureChange {

	static final Integer OFFSET = 32;
	static final Double RATIO_CHANGE = 5.0/9.0; //float division


public static void main(String[] args) {
	Scanner scanner = new Scanner(System.in);

	System.out.print("Enter temperature(F):");
	
	String sFahr = scanner.nextLine();
	Double dFahr = Double.parseDouble(sFahr);

	Double celcius = (dFahr - OFFSET) * RATIO_CHANGE;

	System.out.println("Temperature in Celsius: " + celcius);



	}
}