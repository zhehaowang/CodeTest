#include <stdio.h>
#include <stdlib.h>

#define MAXLENGTH 100

int main()
{
	FILE * fp = fopen("teminput.txt", "r");
	if (fp==NULL)
	{
		printf("File not exist");
		return 0;
	}
	else
	{
		char str[MAXLENGTH] = "";
		while (fgets(str, MAXLENGTH, fp) != NULL)
		{
			if (str[strlen(str) - 1] = '\n')
			{
				str[strlen(str) - 1] = 0;
			}
			printf("%s\\n", str);
		}
		printf("\n");
		return 1;
	}
	return 1;
}