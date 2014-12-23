'''Maximizing XOR
Problem Statement

Given two integers: L and R,

find the maximal values of A xor B given, L = A = B = R

Input Format 
The input contains two lines, L is present in the first line. 
R in the second line.

Constraints 
1 = L = R = 103

Output Format 
The maximal value as mentioned in the problem statement.'''
def LogicalXOR(a,b):
	max=0
	for x in range(a,b+1):
		for y in range(x,b+1):
			z=(x|y)&~(x&y)
			if(max<z):
				max=z
	return max
l=int(input())
r=int(input())
print(LogicalXOR(l,r))