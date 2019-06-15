#include<stdio.h>
#include<stdlib.h>
#include<string.h>
int main()
{
char name;
scanf("%c",&name);
if(name>='a'&&name<='z'||name>='A'&&name<='Z')
printf("Alphabet");
else
printf("No");
return 0;
}
