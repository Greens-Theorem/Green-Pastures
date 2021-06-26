package maxandmin;

/**
 * CMH June 2021
 */

import java.util.ArrayList;
import java.util.Scanner;

public class MaxandMinJava {

	public static void main(String[] args) {
		ArrayList<Integer> arr = new ArrayList<Integer>();
		ArrayList<Integer> arr2 = new ArrayList<Integer>();
		Scanner in = new Scanner(System.in);
		System.out.println("Enter a number to add to the max list");
		int val1 = in.nextInt();
		arr.add(val1);
		System.out.println("Enter a final number to add to the max list");
		int val2 = in.nextInt();
		arr.add(val2);
		System.out.println("Enter a number to add to the min list");
		int val3 = in.nextInt();
		arr2.add(val3);
		System.out.println("Enter a final number to add to the min list");
		int val4 = in.nextInt();
		arr2.add(val4);
		getMax(arr);
		getMin(arr2);
		in.close();

	}

	public static void getMax(ArrayList<Integer> arr) {
		int max = arr.get(0);
		for (int i : arr) {
			if (i > max) {
				max = i;
			}
		}
		System.out.println("The max is: " + " " + max);

	}

	public static void getMin(ArrayList<Integer> arr2) {
		int min = arr2.get(0);
		for (int i : arr2) {
			if (i < min) {
				min = i;
			}
		}
		System.out.println("The min is: " + " " + min);

	}

}