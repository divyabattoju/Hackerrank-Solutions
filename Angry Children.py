'''Angry Children
Problem Statement

Bill Gates is on one of his philanthropic journeys to a village in Utopia. He has N packets of candies and would like to distribute one packet to each of the K children in the village (each packet may contain different number of candies). To avoid any fighting among the children, he would like to pick K out of N packets, such that unfairness is minimized.

Suppose the K packets have (x1, x2, x3,....xk) candies in them, where xi denotes the number of candies in the ith packet, then we define unfairness as

max(x1,x2,...xk) - min(x1,x2,...xk)

where max denotes the highest value amongst the elements, and min denotes the least value amongst the elements. Can you figure out the minimum unfairness and print it?

Input Format 
The first line contains an integer N. 
The second line contains an integer K. N lines follow. Each line contains an integer that denotes the candy in the nth (1=n=N) packet.

Output Format 
An integer that denotes the minimum possible value of unfairness.'''

import sys
n=int(input())
k=int(input())
no=n
li=[]
while n>0:
	p=int(input())
	li.append(p)
	n=n-1
li.sort()
i=0
max=sys.maxsize
p=no-k+1
while i<p:
	m=li[i+k-1]-li[i]
	if m<max:
		max=m
	i=i+1
print(max)