package yep;

public class ReversedArray {

	public static void main(String[] args) {
		int arr[] = new int[16];
		for (int i = 1; i < arr.length; i++) {
			arr[i] += i;
		}
		int index = arr.length;
		while(index > 1) {
			index -= 1;
			System.out.println(arr[index]);
		}
	}
}