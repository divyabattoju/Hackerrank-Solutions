'''Alternating Characters
Problem Statement

Shashank likes strings in which consecutive characters are different. For example, he likes ABABA, while he doesn't like ABAA. Given a string containing characters A and B only, he wants to change it into a string he likes. To do this, he is allowed to delete the characters in the string.

Your task is to find the minimum number of required deletions.

Input Format 
The first line contains an integer T i.e. the number of test cases. 
Next T lines contain a string each.

Output Format 
Print minimum number of required steps for each test case.'''
def Cosecutivechar(a):
	alt=0
	for i in range(0,len(a)-1):
		if(a[i]==a[i+1]):
			alt=alt+1
	return alt
t=int(input())
while t>0:
	t=t-1
	s=input()
	print(Cosecutivechar(s))