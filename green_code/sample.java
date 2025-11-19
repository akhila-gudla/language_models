public class HighTimeComplexityExample {

    // Function to calculate all permutations of a given array
    public static void generatePermutations(int[] arr, int k) {
        if (k == arr.length - 1) {
            // Base case: print the current permutation
            for (int i = 0; i < arr.length; i++) {
                System.out.print(arr[i] + " ");
            }
            System.out.println();
        } else {
            for (int i = k; i < arr.length; i++) {
                // Swap elements to generate new permutations
                swap(arr, k, i);
                generatePermutations(arr, k + 1);
                // Backtrack: swap back to restore original order for next iteration
                swap(arr, k, i);
            }
        }
    }

    private static void swap(int[] arr, int i, int j) {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

    public static void main(String[] args) {
        int[] numbers = {1, 2, 3}; // For a small input size
        System.out.println("Permutations of {1, 2, 3}:");
        generatePermutations(numbers, 0);

        // Uncommenting the following line with a larger array will demonstrate the high time complexity.
        // For example, an array of 10 elements would result in 10! (3,628,800) permutations.
        // int[] largeNumbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
        // System.out.println("\nPermutations of {1, 2, 3, ..., 10}:");
        // generatePermutations(largeNumbers, 0);
    }
}
