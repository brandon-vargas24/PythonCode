#Homework Assignment 8, Magic Square
#VARGAS, BRANDON
#April 3, 2017

import random

def square(n):
    row = 0
    col = (n/2)
    Magic_Square[row][col] = 1
    for position in range(2, (n**2)+1):
        row = row - 1
        col = col + 1
        if Magic_Square[(row)%n][(col)%n] == 0:
            Magic_Square[(row)%n][(col)%n] = position
        elif Magic_Square[(row)%n][(col)%n] != 0:
            row = row + 2
            col = col - 1
            Magic_Square[(row)%n][(col)%n] = position

    #Prints the square
    for row1 in range(0, n):
        print ""
        for col1 in range(0, n):
            print "%4i"%Magic_Square[row1][col1],
    print ("\n")

    #Calculates sum of diagonal numbers
    diagonal_down = 0
    for i in range(n):
        diagonal_down = diagonal_down + Magic_Square[i][i]

    diagonal_up = -1
    for r in range(n,-1,-1):
        diagonal_up = diagonal_up + Magic_Square[i][n-1-i]

    diagonal = 0
    if diagonal_up == diagonal_down:
        diagonal = diagonal_down

    #Calculates sum of numbers in each column
    for col2 in range(n):
        col_sum = 0
        for row2 in range(n):
            col_sum = col_sum + Magic_Square[row2][col2]

    #Calculates sum of numbers in each row
    for row3 in range(n):
        row_sum = 0
        for col3 in range(n):
            row_sum = row_sum + Magic_Square[row3][col3]

    if row_sum == diagonal and col_sum:
        print "The sum of each row, column, and diagonal is:", row_sum
    



print "This program creates an odd-sided Magic Square,"
print "where the sum of each rown, column, and diagonal"
print "add up to the same number."
print
n = int(raw_input("Enter an Odd integer between 3 and 15 for the Magic Square:"))  
Magic_Square = [[0 for row_size in range(n)] for col_size in range(n)]
square(n)
