#!/usr/bin/env python3
#
# Created by: Rodas Nega
# Created on: Oct 2021
# This program finds the mean of elements in a 2D array


import random


def matrix_mean(random_grid, rowNumber, columnNumber):
    # this function calculates the mean of all the elements in a 2D array

    sum_of_matrix_elements = 0
    for row_value in random_grid:
        for array_element in row_value:
            sum_of_matrix_elements += array_element

    sum_of_matrix_elements = sum_of_matrix_elements / (rowNumber * columnNumber)

    return sum_of_matrix_elements


def main():
    # this function creates a 2D array

    matrix = []

    # input
    rows = input("Enter in the number of rows: ")
    columns = input("Enter in the number of columns: ")
    print("")

    try:
        rows_int = int(rows)
        columns_int = int(columns)

        if rows_int < 0:
            print("That is an invalid integer.")
        elif columns_int < 0:
            print("That is an invalid integer.")

        else:
            for loop_counter_rows in range(0, rows_int):
                temp_column = []
                for loop_counter_columns in range(0, columns_int):
                    random_number = random.randint(0, 50)
                    temp_column.append(random_number)
                    print("{0} ".format(random_number), end="")
                matrix.append(temp_column)
                print("")

            rounded_matrix_mean = matrix_mean(matrix, rows_int, columns_int)
            print("")
            print("The mean of the matrix is: {0} ".format(rounded_matrix_mean))

    except Exception:
        print("That is an invalid input.")

    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
