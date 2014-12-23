/*The Utopian tree goes through 2 cycles of growth every year. The first growth cycle occurs during the spring, when it doubles in height. The second growth cycle occurs during the summer, when its height increases by 1 meter. 
Now, a new Utopian tree sapling is planted at the onset of the spring. Its height is 1 meter. Can you find the height of the tree after N growth cycles?

Input Format 
The first line contains an integer, T, the number of test cases. 
T lines follow. Each line contains an integer, N, that denotes the number of cycles for that test case.

Constraints 
1 <= T <= 10 
0 <= N <= 60

Output Format 
For each test case, print the height of the Utopian tree after N cycles.*/
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

    /* Enter your code here. Read input from STDIN. Print output to STDOUT */  
    int testcases;
    scanf("%d",&testcases);
    if(testcases<=10&&testcases>=1)
        {
        while(testcases--)
            {
            int num;
            int height=1;
            scanf("%d",&num);
           
            if(num>=0 && num<=60)
                {
                int i;
                for(i=1;i<=num;i++)
                    {
                    if((i%2)==0)
                        {
                        height=height+1;
                    }
                    if(i%2==1)
                        {
                        height=height*2;
                    }
                }
            }
            printf("%d \n",height);
             
            
        }
    }
    return 0;
}


