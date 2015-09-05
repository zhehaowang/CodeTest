#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int stringCompCaseInsensitive(char * str1, char * str2, int length1, int length2)
{
	if (length1 != length2)
	{
		//printf("%d\t%d\n", length1, length2);
		return 0;
	}
	else
	{
		int i = 0;
		char temp1 = 0;
		char temp2 = 0;
		for (i = 0; i < length1; i++)
		{
			if (str1[i] > 0x60)
			{
				temp1 = str1[i] - 0x20;
			}
			else
			{
				temp1 = str1[i];
			}
			
			if (str2[i] > 0x60)
			{
				temp2 = str2[i] - 0x20;
			}
			else
			{
				temp2 = str2[i];
			}
			
			if (temp1 != temp2)
			{
				//printf("%d\n", i);
				return 0;
			}
		}
		return 1;
	}
}

int main()
{
	char str1[20] = "Good is bad";
	char str2[20] = "gOOddsis BAD";
	int equal = stringCompCaseInsensitive(str1, str2, strlen(str1), strlen(str2));
	printf("%d\n", equal);
	return 0;
}