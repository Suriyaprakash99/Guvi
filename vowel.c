#include<stdio.h>
#include<stdlib.h>
#include<string.h>
int main()
{
char name;
scanf("%c",&name);
if(name=='a'||name=='e'||name=='i'||name=='o'||name=='u'||name=='A'||name=='E'||name=='I'||name=='O'||name=='U')
printf("Vowel");
else
printf("Consonant");
return 0;
}
