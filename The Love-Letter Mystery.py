'''The Love-Letter Mystery
Problem Statement

James found a love letter his friend Harry has written for his girlfriend. James is a prankster, so he decides to meddle with the letter. He changes all the words in the letter into palindromes.

To do this, he follows 2 rules:

(a) He can reduce the value of a letter, e.g. he can change 'd' to 'c', but he cannot change 'c' to 'd'. 
(b) In order to form a palindrome, if he has to repeatedly reduce the value of a letter, he can do it until the letter becomes 'a'. Once a letter has been changed to 'a', it can no longer be changed.

Each reduction in the value of any letter is counted as a single operation. Find the minimum number of operations required to convert a given string into a palindrome. 


Input Format 
The first line contains an integer T, i.e., the number of test cases. 
The next T lines will contain a string each. The strings do not contain any spaces.

Output Format 
A single line containing the number of minimum operations corresponding to each test case.'''
def MinOp(s):
	i=0
	j=len(s)-1
	c=0
	while i<j:
		if(s[i]!=s[j]):
			c=c+abs(ord(s[j])-ord(s[i]))
		i=i+1
		j=j-1
	return c
t=int(input())
while t>0:
	t=t-1
	s=input()
	print(MinOp(s))

