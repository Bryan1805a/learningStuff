package java_learning;

import java.util.Scanner;

public class learning {
    private static final Scanner SCANNER = new Scanner(System.in);

    public static int int_input() {
        return SCANNER.nextInt();
    }

    public static int[][] array_input() {
        System.out.print("Input rows = ");
        int rows = int_input();

        System.out.print("Input columns = ");
        int columns = int_input();

        int[][] array = new int[rows][columns];

        System.out.println("Input elements:");
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < columns; j++) {
                System.out.printf("array[%d][%d] = ", i, j);
                array[i][j] = int_input();
            }
        }

        return array;
    }

    public static void array_output(int[][] array) {
        System.out.println("2D array: ");
        for (int i = 0; i < array.length; i++) {
            for (int j = 0; j < array[i].length; j++) {
                System.out.print(array[i][j] + " ");
            }
            System.out.println();
        }
    }

    // Bài 2. Tính tổng các phần tử trong mảng 2 chiều
    public static void sum_of_elements(int[][] array) {
        int sum = 0;

        for (int i = 0; i < array.length; i++) {
            for (int j = 0; j < array[i].length; j++) {
                sum += array[i][j];
            }
        }

        System.out.println("Sum of elements = " + sum);
        System.out.println();
    }

    // Bài 3. Tính tổng từng hàng, từng cột
    public static void sum_of_each_col_row(int[][] array) {
        int rows = array.length;
        int cols = array[0].length;

        for (int i = 0; i < rows; i++) {
            int sum_of_rows = 0;
            for (int j = 0; j < cols; j++) {
                sum_of_rows += array[i][j];
            }
            System.out.println("Sum of row " + (i + 1) + " = " + sum_of_rows);
        }

        for (int j = 0; j < cols; j++) {
            int sum_of_cols = 0;
            for (int i = 0; i < rows; i++) {
                sum_of_cols += array[i][j];
            }
            System.out.println("Sum of cols " + (j + 1) + " = " + sum_of_cols);
        }
        System.out.println();
    }

    public static void main(String[] args) {
        System.out.println("----- Bai 1 -----");
        int[][] two_D_array = array_input();
        array_output(two_D_array);

        System.out.println("----- Bai 2 -----");
        sum_of_elements(two_D_array);

        System.out.println("----- Bai 3 -----");
        sum_of_each_col_row(two_D_array);
    }
}