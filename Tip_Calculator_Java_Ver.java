/*
 * @author Cowen Hames January 2021
 * The Java version of my Tip Calculator program originally created in Python.
 */
package tip_calculator;

import java.util.InputMismatchException;
import java.util.Scanner;

public class Tip_Calculator_Java_Ver {

	public static void main(String[] args) throws InputMismatchException {

		System.out.println("###################################################");
		System.out.println("########     Tip Calculator Program     ########");
		System.out.println("###################################################");

		Scanner console = new Scanner(System.in);
		double bill = 0;
		boolean continueProgram = true;

		while (continueProgram) {
			try {
				System.out.println("Hello! Please enter your pre-tax bill amount: ");
				bill = console.nextDouble();
				System.out.println(
						"Great. Next enter your feeling of the service. Bad, Average, Good or Excellent. Enter 'Quit' to close.");
				String input = console.next();

				if (input.equalsIgnoreCase("Bad")) {
					System.out.println("Your total pre-tax bill including tip is: " + badService(bill));

				}

				else if (input.equalsIgnoreCase("Average")) {
					System.out.println("Your total pre-tax bill including tip is: " + averageService(bill));
				}

				else if (input.equalsIgnoreCase("Good")) {
					System.out.println("Your total pre-tax bill including tip is: " + goodService(bill));
				}

				else if (input.equalsIgnoreCase("Excellent")) {
					System.out.println("Your total pre-tax bill including tip is: " + excellentService(bill));
				} else if (input.equalsIgnoreCase("Quit")) {
					continueProgram = false;
					console.close();
				}
			} catch (InputMismatchException e) {
				System.out.println("Invalid response, try again");
				continueProgram = false;
			}
		}
	}

	public static double badService(double x) {
		return (x * .10) + x;
	}

	public static double averageService(double x) {
		return (x * .15) + x;
	}

	public static double goodService(double x) {
		return (x * .20) + x;
	}

	public static double excellentService(double x) {
		return (x * .25) + x;
	}

}