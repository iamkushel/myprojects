#include <stdio.h>
#include <stdlib.h>

int main(){
	
	int a[3];
	int i;
	
	for(i =0;i<3;i++)
	{
		scanf("\n%d", a +i); /*a itself will be pointing to memory location of 1 */
	}                         //so a + i will will jump to next mem location 
	for(i =0;i<3;i++)
	{
		printf("%d\n", a[i]);
		
	}
	printf("%p \t %p \t %p \t %p", a[0], *a, a, &a[0]); //&a[0] == a here a[0] == *a
	
}