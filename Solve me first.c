/*This is an introductory challenge. The purpose of this challenge is to give you a working I/O template in your preferred language. It includes scanning 2 integers from STDIN, calling a function, returning a value, and printing it to STDOUT.

The task is to scan two numbers from STDIN, and print the sum A+B on STDOUT. The code has already been provided for most of the popular languages. This is primarily for you to read and inspect how the IO is handled.

Note: The code has been saved in a template, which you can submit if you want. Or, you may try rewriting it and building it up from scratch.

Input Format 
This section specifies the Input Format. 
Given A and B on two different lines.

Output Format 
This section specifies the Output Format. 
An integer that denotes Sum (A + B)

Constraints 
This section tells what input you can expect. You can freely assume that the input will remain within the boundaries specified. As an example here given below, A and B will never be below 1 or above 1000. 
1 = A, B = 1000*/

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>


int solveMeFirst(int a, int b) {
  return a+b;
}
int main() {
  int num1,num2;
  scanf("%d %d",&num1,&num2);
  int sum; 
  sum = solveMeFirst(num1,num2);
  printf("%d",sum);
  return 0;
}


