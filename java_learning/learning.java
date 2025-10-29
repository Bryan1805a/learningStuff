package java_learning;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
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

    // Bài 4. Tìm phần tử lớn nhất và nhỏ nhất trong mảng
    public static void largest_and_smallest_element(int[][] array) {
        int smallest_element = array[0][0];
        int largest_element = array[0][0];

        for (int i = 0; i < array.length; i++) {
            for (int j = 0; j < array[i].length; j++) {
                if (array[i][j] > largest_element) {
                    largest_element = array[i][j];
                }
                else if (array[i][j] < smallest_element) {
                    smallest_element = array[i][j];
                }
            }
        }

        System.out.println("Smallest element = " + smallest_element);
        System.out.println("Largest element = " + largest_element);
        System.out.println();
    }

    // Bài 5. Đếm số chẵn và số lẻ trong mảng
    public static void odd_and_event_elements(int[][] array) {
        int odd_elements = 0;
        int even_elements = 0;

        for (int i = 0; i < array.length; i++) {
            for (int j = 0; j < array[i].length; j++) {
                if (array[i][j] % 2 == 0) {
                    even_elements += 1;
                }
                else {
                    odd_elements += 1;
                }
            }
        }
        System.out.println("Odd Elements = " + odd_elements);
        System.out.println("Even Elements = " + even_elements);
        System.out.println();
    }

    // Bài 6. Tính tổng đường chéo chính và phụ (chỉ áp dụng cho ma trận vuông)
    public static void sum_of_dianogal(int[][] array) {
        int rows = array.length;
        int cols = array[0].length;

        int sum_of_main_dianogal = 0;
        int sum_of_sub_dianogal = 0;

        if (rows != cols) {
            System.out.println("Only for Square Matrix");
            System.out.println();
            return;
        }

        for (int i = 0; i < rows; i++) {
            sum_of_main_dianogal += array[i][i];
            sum_of_sub_dianogal += array[i][rows - 1 - i];
        }

        System.out.println("Sum of main dianogal = " + sum_of_main_dianogal);
        System.out.println("Sum of sub_dianogal = " + sum_of_sub_dianogal);
        System.out.println();
    }

    // Bài 9. Sắp xếp các phần tử trong mảng 2 chiều tăng dần
    public static int[] flatting_array(int[][] array) {
        // Calculate total size needed for the flattened array
        int totalSize = 0;
        for (int i = 0; i < array.length; i++) {
            totalSize += array[i].length;
        }
        
        // Create the flattened array with the correct size
        int[] flatten_array = new int[totalSize];
        
        // Copy all elements to the flattened array
        int index = 0;
        for (int i = 0; i < array.length; i++) {
            for (int j = 0; j < array[i].length; j++) {
                flatten_array[index] = array[i][j];
                index++;
            }
        }
        
        // Sort the array in ascending order
        Arrays.sort(flatten_array);
        
        return flatten_array;
    }

    public static void main(String[] args) {
        System.out.println("----- Bai 1 -----");
        int[][] two_D_array = array_input();
        array_output(two_D_array);

        System.out.println("----- Bai 2 -----");
        sum_of_elements(two_D_array);

        System.out.println("----- Bai 3 -----");
        sum_of_each_col_row(two_D_array);

        System.out.println("----- Bai 4 -----");
        largest_and_smallest_element(two_D_array);

        System.out.println("----- Bai 5 -----");
        odd_and_event_elements(two_D_array);

        System.out.println("----- Bai 6 -----");
        sum_of_dianogal(two_D_array);

        System.out.println("----- Bai 9 -----");
        int[] a = flatting_array(two_D_array);
        System.out.println("Sorted flattened array: " + Arrays.toString(a));
    }
}