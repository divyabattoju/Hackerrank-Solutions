'''Game of Thrones - I
roblem Statement

King Robert has 7 kingdoms under his rule. He finds out from a raven that the Dothraki are soon going to wage a war against him. But, he knows the Dothraki need to cross the Narrow River to enter his realm. There is only one bridge that connects both banks of the river which is sealed by a huge door.
The king wants to lock the door so that the Dothraki can't enter. But, to lock the door he needs a key that is an anagram of a certain palindrome string.

The king has a string composed of lowercase English letters. Help him figure out if any anagram of the string can be a palindrome or not.

Input Format 
A single line which contains the input string
Output Format 
A single line which contains YES or NO in uppercase.'''

text=input()
chararray='abcdefghijklmnopqrstuvwxyz'
indexarray=[0]*26
for i in text:
	indexarray[chararray.index(i)]+=1
odd=0
even=0
for i in indexarray:
	if i!=0 and i%2==0:
		even+=1
	if i!=0 and i%2==1:
		odd+=1

if even>=0 and odd<=1:
	print("YES")
else:
	print("NO")
